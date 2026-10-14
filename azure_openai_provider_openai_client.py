import json
import logging
import time

from openai import OpenAI
from .base import LLMProvider
from .openrouter_provider import CLASSIFY_SCHEMA, MERGE_SCHEMA

log = logging.getLogger(__name__)


class AzureOpenAIProvider(LLMProvider):
    """Azure OpenAI v1 provider implemented with the standard OpenAI Python client."""

    def __init__(self, config):
        self.config = config
        endpoint = config.azure_openai_endpoint.rstrip("/")
        if not endpoint.endswith("/openai/v1"):
            endpoint = f"{endpoint}/openai/v1"
        endpoint += "/"

        self.client = OpenAI(
            api_key=config.azure_openai_api_key,
            base_url=endpoint,
            timeout=config.llm_timeout_seconds,
            max_retries=0,
        )

    def _json_call(self, system, payload, schema, name):
        last = None
        for attempt in range(self.config.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.config.azure_openai_deployment,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": json.dumps(payload, ensure_ascii=False, default=str)},
                    ],
                    response_format={
                        "type": "json_schema",
                        "json_schema": {
                            "name": name,
                            "strict": True,
                            "schema": schema,
                        },
                    },
                )
                content = response.choices[0].message.content
                if not content:
                    raise ValueError("Azure OpenAI returned an empty response.")
                result = json.loads(content)
                if not isinstance(result, dict):
                    raise ValueError("LLM response was not a JSON object.")
                return result
            except Exception as exc:
                last = exc
                # Do not log credentials, prompts, or financial payloads.
                log.warning(
                    "Azure OpenAI request failed (attempt %s/%s): %s",
                    attempt + 1,
                    self.config.max_retries,
                    type(exc).__name__,
                )
                if attempt + 1 < self.config.max_retries:
                    time.sleep(min(2 ** attempt, 4))
        raise RuntimeError(
            f"Azure OpenAI request failed after retries: {type(last).__name__}"
        ) from last

    def classify_table(self, table_context):
        return self._json_call(
            "Classify financial extracted tables by actual row-level meaning. "
            "Include individual transactions and individual portfolio holdings only. "
            "Exclude summaries and unrelated tables. Be conservative and flag uncertainty.",
            table_context,
            CLASSIFY_SCHEMA,
            "table_classification",
        )

    def decide_table_continuation(self, previous_table, candidate_table):
        return self._json_call(
            "Decide whether a candidate table continues the prior logical table. "
            "Matching headers alone is insufficient. Use source, page order, schema, "
            "title, rows and context. Do not change source values. Use uncertain when "
            "evidence is insufficient.",
            {"previous_table": previous_table, "candidate_table": candidate_table},
            MERGE_SCHEMA,
            "table_continuation",
        )
