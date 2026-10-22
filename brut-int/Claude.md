# Resume Deep-Dive: Adversarial Technical Interview Prep
### Shivam Shrivastava — AI/ML Engineer, 3+ YOE

This document treats every bullet on your resume as a claim that must be defended, not a fact to be taken at face value. It is organized company-by-company, bullet-by-bullet, and ends with cross-cutting attack surfaces, cross-company questions, a "bluff-detection" round, a difficulty-tagged master bank, and a final readiness report.

**Difficulty legend** (used throughout):
🟢 Basic · 🟡 Intermediate · 🔴 Advanced · ☠️ Brutal · 💀 Fundamental/first-principles

As a rough (not strict) mapping: Level 1–2 questions tend to be 🟢, Level 3–4 are 🟡, Level 5–6 are 🔴, Level 7 is 🔴/☠️, and Level 8 (adversarial cross-questioning) is ☠️/💀.

---

# COMPANY 1 — EY, Data Scientist I, AIQRM (Agent Operations & Evaluation), Sept 2025–Present

## Bullet 1.1
> "Deployed Langfuse observability across 10+ LLM agents, unifying tracing for prompts, tool calls, tokens, and costs; cut agent-debugging time by 35% and enabled real-time monitoring."

### Claim inventory
Technologies/claims embedded here: **Langfuse**, **10+ LLM agents**, tracing of **prompts, tool calls, tokens, costs**, "**unifying**" (implies prior fragmentation), "**deployed**" (implies infra ownership, not just SDK usage), **35% debugging-time reduction**, "**real-time monitoring**."

### Vague/exaggerated flags
- "Deployed" — self-hosted (Docker/K8s + Postgres/ClickHouse) or Langfuse Cloud? Very different amounts of "your work."
- "10+ agents" — undefined unit. Are these 10 distinct LangGraph/agentic pipelines, or 10 prompt templates within one agent?
- "Unifying" implies there were previously N different logging approaches — what were they?
- "35%" — reduction relative to what baseline, measured by whom, over what time window?
- "Real-time" is a specific technical claim (sub-second, streaming) vs. "near-real-time" dashboards refreshed periodically — these are different systems.

### Question Tree

**Level 1 — Direct** 🟢
- What is Langfuse, in your own words — what problem does it solve that logging to a file doesn't?
- Why did observability become necessary — what was breaking or slow before it existed?
- What exactly did *you* set up vs. what came out-of-the-box?

**Level 2 — Implementation** 🟡
- Self-hosted or Langfuse Cloud? If self-hosted: what's the storage backend, how is it deployed, who manages upgrades?
- How did you instrument 10+ agents — a shared SDK wrapper/decorator, or per-agent manual instrumentation?
- How are tool calls captured — do you wrap every tool function, or does your orchestration framework (LangChain/LangGraph/custom) emit callback events that Langfuse hooks into?
- How is cost calculated per call — token counts × a pricing table you maintain, or does Langfuse infer pricing from model name automatically? What happens when a new model isn't in that table?
- What alternatives did you evaluate (LangSmith, Arize Phoenix, Helicone, W&B Weave, raw OpenTelemetry) and why Langfuse specifically?

**Level 3 — Internal Mechanics** 🟡/🔴
- Explain Langfuse's data model: trace → observation (span/generation/event) → score. How do nested spans get correlated to one trace (trace ID propagation across async calls)?
- How does the SDK avoid blocking your application's request path — is ingestion synchronous or batched/async in a background thread?
- For streaming LLM responses, how does Langfuse capture token-by-token output and still compute total latency and token counts correctly?
- What exactly gets stored for a "tool call" — arguments, return value, latency, success/failure — and how is that structured (JSON schema)?

**Level 4 — Design Decisions** 🔴
- Why not just structured logs shipped to Grafana/Loki plus a cost-calculation Lambda? What did Langfuse give you that a bespoke system wouldn't have, and what did you give up (vendor dependency, less control over retention/schema)?
- Do you trace 100% of requests or sample? If sampling, how did you choose the rate, and how do you avoid missing rare failure traces?
- How do you keep PII out of traces (prompts/tool args often contain user data) — redaction at the SDK layer, or do you accept the risk?

**Level 5 — Scale & Performance** 🔴
- Roughly how many traces/day across the 10+ agents? What's the added latency per LLM call from the tracing SDK (p50/p95)?
- Did the self-hosted (or cloud) instance ever become a bottleneck — ingestion queue backing up, UI slow to load traces?
- How would this look at 100 agents and 100x traffic — does the current instrumentation pattern (per-agent wrapper) scale, or would you need a shared middleware/proxy layer?

**Level 6 — Failure Scenarios** ☠️
- What happens to the LLM call itself if the Langfuse backend is unreachable — does the agent request fail, hang, or silently drop the trace?
- Duplicate traces on retries — how do you avoid double-counting cost/tokens when a request is retried after a timeout?
- What happens if a tool call throws an exception mid-span — is the span still closed and marked failed, or does it leak as "open forever"?
- Malformed or huge payloads (e.g., an agent that dumps a 50k-token tool result) — does that ever break trace ingestion or blow up storage costs?

**Level 7 — Production Reality** ☠️
- How do you get alerted vs. just having a dashboard someone has to remember to check? Concretely: is there a threshold-based alert (e.g., cost spike, failure rate) wired to Slack/PagerDuty?
- Walk through one real debugging session: a specific bug found via a trace, and the exact sequence of clicks/queries that found it.
- Who has access to trace data across teams — is there any access control given traces may contain sensitive tool-call arguments (AWS/Jira/Slack payloads)?
- What's the retention/rollback policy — how far back can you go, and what happens when storage gets expensive?

**Level 8 — Adversarial** 💀
- "You said 'unifying tracing' — unifying implies there were multiple separate systems before. Name them. What exactly was fragmented?"
- "Did you write the instrumentation code yourself, or is this Langfuse's built-in LangChain/LlamaIndex callback integration that auto-instruments with near-zero code? Be specific about what required custom code."
- "35% — 35% of what number, measured how? Was there a stopwatch, a ticket-resolution-time metric, a developer survey? If I asked your teammate the same question, would they give me the same number?"
- "If Langfuse went down for a day, would anyone notice via an alert, or would you just… not have traces for that day? What does that tell you about how load-bearing this system actually is?"
- "What's the actual COGS/cost overhead of running this — self-hosted infra cost, or Langfuse Cloud pricing tier — and did that factor into your evaluation vs. alternatives, or did you not own that decision?"

### Metric deep-dive: "cut agent-debugging time by 35%"
1. What is "agent-debugging time" precisely — mean time to root-cause a reported issue? Mean time to resolve?
2. How was it measured before Langfuse existed — was there any timestamped record, or is the "before" number a recollection/estimate?
3. What's the sample size — how many debugging incidents pre- vs. post-Langfuse is 35% computed over?
4. What's the baseline population — same set of agents, same team, same time-of-year workload?
5. Could confounds explain it instead — team members simply getting more experienced with the agents over the same period, other tooling introduced concurrently (better error messages, more tests)?
6. Is 35% an average, a median, or a single anecdote generalized? Outliers (one incident that used to take a week and now takes an hour) can massively skew an average.
7. Was this self-reported/estimated by you, or independently tracked in a ticketing system (Jira cycle time)?
8. What would you say if I told you 35% sounds like a round, estimated number rather than a computed statistic — defend it or concede the precision.

---

## Bullet 1.2
> "Built LLM-judge evaluation frameworks scoring decision quality, correctness, and guardrail coverage; automated regression suites caught 32% more reasoning defects pre-release vs. manual review."

### Claim inventory
**LLM-as-judge**, three scoring dimensions (**decision quality, correctness, guardrail coverage**), **automated regression suites**, **32% more reasoning defects caught pre-release vs. manual review**.

### Vague/exaggerated flags
- "Decision quality" and "guardrail coverage" are not standard, well-defined metrics — how are they operationalized into a numeric or categorical score?
- "32% more reasoning defects" requires a well-defined notion of "defect" and a way to count them consistently for both the automated and manual process — that's non-trivial.
- "vs. manual review" implies a clean A/B or before/after comparison — was it actually run that cleanly, or estimated?

### Question Tree

**Level 1 — Direct** 🟢
- What does "LLM-judge" mean here — a separate LLM call that scores another LLM's output? Which model did you use as judge, and why?
- Why not just use human review for everything — what specifically motivated automating this?

**Level 2 — Implementation** 🟡
- How is the judge prompted — pointwise (score this response 1–5 against a rubric) or pairwise (which of two responses is better)?
- How did you build the rubric for "decision quality" and "guardrail coverage" — did you write it, or was it derived from existing risk/compliance policies at EY?
- What's the output format from the judge — free text, a JSON schema, a numeric score? How do you parse/validate it reliably?
- What did the "regression suite" consist of — a fixed golden dataset of prompts/expected behaviors run on every release?

**Level 3 — Internal Mechanics** 🟡/🔴
- What are the known failure modes of LLM-as-judge (position bias, verbosity bias, self-preference bias when judge and generator are the same model family)? Which of these did you actively mitigate, and how?
- How did you validate the judge itself — did you measure agreement between the LLM judge and human raters (e.g., Cohen's kappa, percent agreement)? What was that agreement rate?
- If the judge disagrees with a human on a sampled case, what's your process — do you refine the rubric, few-shot examples, or the base prompt?

**Level 4 — Design Decisions** 🔴
- Why an LLM judge instead of a smaller fine-tuned classifier trained on labeled examples of "good" vs. "bad" agent decisions? What are the cost/latency/consistency trade-offs?
- Pointwise vs. pairwise scoring — which did you choose, and what does that choice cost you (pairwise is more robust to score-scale drift but doesn't give you an absolute number for a dashboard)?
- How do you prevent the judge from being gamed — e.g., an agent whose outputs are just longer/more confident-sounding scoring higher regardless of correctness?

**Level 5 — Scale & Performance** 🔴
- How large is the regression suite (number of test cases)? How often does it run — every PR, nightly, pre-release only?
- What's the cost and latency of running the full suite (judge calls aren't free or instant) — did that ever become a bottleneck blocking releases?

**Level 6 — Failure Scenarios** ☠️
- What happens when the judge model itself is updated/deprecated by the provider — does your whole scoring baseline silently shift, invalidating historical comparisons?
- What about non-determinism — the same agent output judged twice by the same judge prompt gives different scores. How do you handle that (temperature=0, multiple samples + majority vote)?
- A "reasoning defect" that's actually a defect in the *rubric* (i.e., you're scoring the wrong thing) — how would you even detect that?

**Level 7 — Production Reality** ☠️
- Is a low score from the regression suite a hard release gate, or advisory? Who can override it and under what process?
- How do you monitor drift in judge behavior over time in production, not just at release time?
- Concrete example: describe one specific "reasoning defect" the automated suite caught that manual review had missed in the past.

**Level 8 — Adversarial** 💀
- "32% more — more than what baseline number of defects caught by manual review? Give me the raw counts, not just the percentage."
- "How do you know the 32% 'extra' defects the automated suite found are real defects and not false positives from an overly strict judge rubric? Did anyone manually verify those specific 32%?"
- "If your judge is itself an LLM, and LLMs make mistakes, what's your judge's own false-positive/false-negative rate — and how would that number bias your headline 32% either up or down?"
- "You said this catches defects 'pre-release' — what's your actual definition of a release boundary here, and could some of those 32% have been marginal calls that a human reviewer would have caught anyway if given the same time budget?"

### Metric deep-dive: "32% more reasoning defects pre-release vs. manual review"
1. Define "reasoning defect" precisely — what category of failure counts?
2. What's the denominator — total defects found by *either* method, total test cases run, total releases?
3. Was this measured on the same set of releases/agents for both methods (paired comparison) or different time periods (confounded by agents changing)?
4. Who verified a caught "defect" was actually a defect and not a judge false positive?
5. What's the raw N — is 32% "found 33 vs 25" or "found 3300 vs 2500"? Small-N percentages are fragile.
6. Could the automated suite simply be running *more test cases* than a human ever would in the same time, making the comparison apples-to-oranges (of course automation finds "more" if it checks 10x more scenarios)?
7. How would you reproduce this number if asked to redo the analysis today?

---

## Bullet 1.3
> "Standardized eval gates and risk-based release criteria across agent teams; reduced production defects by 40% compared to the pre-evaluation-framework baseline."

### Claim inventory
**Standardization across teams** (org-level influence, not just one agent), **risk-based release criteria** (implies a tiering/scoring system for risk), **40% production defect reduction vs. pre-framework baseline**.

### Vague/exaggerated flags
- "Standardized... across agent teams" is an organizational claim — how many teams, and what was your actual authority/role in getting other teams to adopt this (mandate vs. influence)?
- "Risk-based" — what determines an agent's risk tier? Is this your framework or an existing EY risk taxonomy you plugged into?
- "40% reduction... vs. pre-evaluation-framework baseline" — pre/post comparison across an org is hard to attribute cleanly to one initiative.

### Question Tree

**Level 1 — Direct** 🟢
- What's an "eval gate" concretely — a CI check that blocks a merge/deploy if a score is below threshold?
- What made an agent "high risk" vs. "low risk" in your criteria?

**Level 2 — Implementation** 🟡
- Where do these gates live technically — a CI/CD pipeline step, a manual sign-off checklist, both?
- How did you get buy-in from other agent teams to adopt a shared standard rather than their own bar?
- What thresholds did you set, and how were they chosen — arbitrary, based on historical defect rates, negotiated with each team?

**Level 3 — Internal Mechanics** 🟡
- Walk through the full path from a code/prompt change to a release decision: what runs, in what order, what blocks what?
- How is "risk" scored — a checklist, a weighted formula, human judgment?

**Level 4 — Design Decisions** 🔴
- Why a uniform gate across teams rather than letting each team set its own bar for its own risk profile? What tension did that create?
- What happens when a team disagrees that a gate should block their release — is there an override path, and who owns that decision?

**Level 5 — Scale & Performance** 🔴
- How many teams/agents were actually brought under this standard? Was adoption complete, or partial?

**Level 6 — Failure Scenarios** ☠️
- What happens if a gate has a bug and blocks all releases across every team — what's the kill-switch/rollback for the gating system itself?
- False negatives: a release passes all gates and still causes a production incident — how do you feed that back into the criteria?

**Level 7 — Production Reality** ☠️
- What's the actual "production defect" being counted — customer-reported bugs, internal QA tickets, incident reports?
- Give a concrete example of a defect that *would* have shipped before this framework and was caught after.

**Level 8 — Adversarial** 💀
- "This is your third bullet claiming a big percentage improvement (35%, 32%, 40%) in the same few months at EY, all somewhat overlapping systems. Are these three independent measurements, or three ways of describing the impact of the same underlying work?"
- "'Compared to the pre-evaluation-framework baseline' — that baseline period presumably has fewer data points than the post period, since you've only been there since Sept 2025. How many production defects total are we talking about — is 40% a reduction from 10 to 6, or from 1000 to 600?"
- "What was YOUR specific contribution to 'standardizing across agent teams' vs. what a manager or a cross-team working group drove?"

### Metric deep-dive: "40% production defect reduction"
1. Define "production defect" exactly (severity threshold? customer-facing only? any incident?).
2. What's the before/after window length — is it long enough to be statistically meaningful given how recently you joined (Sept 2025)?
3. What else changed in that window besides the eval framework (headcount, model upgrades, other process changes)?
4. Raw counts behind the 40%?
5. Is this reduction rate-normalized (defects per release, per agent, per API call) or absolute count (which could just reflect fewer releases shipped)?

---

# COMPANY 2 — Sekyurity AI, Software R&D Engineer, Niki Virtual Assistant, Sept 2023–Aug 2025

## Bullet 2.1 — The centerpiece claim
> "Architected a Continual Learning (CL) + RAG system for the virtual assistant across 300+ enterprise APIs (AWS, GCP, Jira, Slack), mitigating catastrophic forgetting and improving multi-turn context retention by 84%."

This is the single highest-scrutiny bullet on the resume: it combines two distinct, non-trivial ML subfields (continual learning and RAG), a large claimed API surface (300+), a specific ML failure mode by name (catastrophic forgetting), a strong ownership verb ("architected"), and an unusually high metric (84%).

### Claim inventory
**Continual Learning (CL)**, **RAG**, **300+ enterprise APIs** spanning **AWS, GCP, Jira, Slack**, **catastrophic forgetting mitigation**, **84% improvement in multi-turn context retention**, "**architected**" (system-design-level ownership claim).

### Vague/exaggerated flags
- "Architected" is the strongest ownership word on the resume — an interviewer will assume you can defend every design decision, not just describe what the system did.
- CL and RAG solve *different* problems (RAG = external knowledge grounding at inference time; CL = a model incrementally learning new tasks/data without forgetting old ones via parameter updates). Combining them into one bullet invites the question: what exactly was learned continually, if RAG is already handling knowledge freshness?
- "Catastrophic forgetting" is a specific, well-studied phenomenon (McCloskey & Cohen, 1989) with known mitigation families (regularization: EWC/SI; replay: rehearsal buffers/generative replay; architectural: progressive networks/adapters/LoRA-per-domain). Naming it without naming *which* mitigation technique you used is the first thing a strong interviewer will probe.
- "84%" is a very large jump for a UX/quality metric — the exact definition of "multi-turn context retention" will be interrogated hard.
- "300+ enterprise APIs" — is this the number of API *endpoints*, *services* (AWS/GCP/Jira/Slack = only 4 named services, implying the 300+ is endpoints/actions within them), or documented tool definitions the agent can call?

### Question Tree

**Level 1 — Direct** 🟢
- In plain terms, what problem was this system solving for Niki's users?
- What specifically did you personally architect vs. what did teammates own?
- Define "multi-turn context retention" in your own words — retention of what, across how many turns?

**Level 2 — Implementation** 🟡
- What was the actual continual learning technique — regularization-based (EWC, Synaptic Intelligence), replay-based (rehearsal buffer of past examples, generative replay), or architecture-based (adapters/LoRA modules added per new API domain)?
- What model was being continually updated — an intent classifier, a slot-filling model, the base LLM itself, an embedding model, a dialogue policy?
- How does RAG fit alongside CL — is RAG retrieving API documentation/schemas at inference time while CL updates something else (e.g., which tools to prefer, or a retrieval ranking model) over time?
- How is a new enterprise API (of the 300+) onboarded into the system — do you write the tool schema by hand, auto-generate it from OpenAPI specs, or fine-tune on new examples?

**Level 3 — Internal Mechanics** 🔴
- Explain how catastrophic forgetting actually happens mechanically — why does gradient descent on new data overwrite weights important for old tasks?
- If you used EWC: explain the Fisher information matrix and how it's used to penalize changes to "important" weights. If you used replay: how large was the buffer, how was it sampled (random, reservoir sampling, importance-weighted)?
- Walk through the RAG retrieval path end-to-end for a single user query: what gets embedded, what vector store is queried, how many chunks are retrieved, how are they inserted into the prompt?
- How is "multi-turn context" represented internally — a running conversation buffer, a summarized state, a knowledge-graph of slots/entities extracted so far?

**Level 4 — Design Decisions** 🔴
- If RAG can fetch the latest information about any of the 300+ APIs at query time, what does continual learning actually buy you that a well-tuned RAG system alone wouldn't? Be precise — what's the thing that must be *learned* rather than *retrieved*?
- Why not simply fine-tune a fresh model periodically (batch retraining) instead of true continual/online learning, which is operationally much harder and riskier (forgetting, instability)?
- What's the trade-off of adding a rehearsal buffer (memory cost, privacy of stored past interactions) vs. a regularization approach (no stored data, but weaker forgetting protection)?
- Why per-domain adapters (if used) instead of one shared model — what does that cost in terms of routing complexity (how do you decide which adapter/domain to activate for an ambiguous query)?

**Level 5 — Scale & Performance** 🔴
- 300+ APIs — how many tool definitions are actually in the model's context/tool registry at once? Do you face a context-window/tool-selection scaling problem, and if so, how is that solved (tool retrieval before generation, hierarchical routing)?
- What was the latency added by retrieval + a potential continual-learning inference-time component, end-to-end?
- How does training/update time scale as more APIs are added — does each new domain require a full retraining pass, or an incremental update?

**Level 6 — Failure Scenarios** ☠️
- What happens when an enterprise API the assistant relies on is down or returns malformed data mid-conversation?
- What happens when RAG retrieves an outdated or contradictory chunk about an API's parameters — does the system have any way to detect the contradiction, or does it just act on stale info?
- Concurrent updates: two new API integrations being learned continually at the same time — any risk of interference between them?
- What happens on catastrophic forgetting *despite* your mitigation — how would you detect that regression before a user does?

**Level 7 — Production Reality** ☠️
- How did you *measure* forgetting in production/eval — a fixed regression set of old-API tasks re-run after each new domain is added, tracking accuracy drop?
- How was this deployed — is CL happening online in production, or is it a periodic offline retraining+eval+deploy cycle (which is a much more common and defensible real-world pattern)?
- What's the rollback plan if a continual update degrades quality on old tasks?

**Level 8 — Adversarial** 💀
- "You used the words 'continual learning' — walk me through the actual training loop. What loss function, what regularization term, what triggers a new learning episode? If you can't name the mechanism, this was likely RAG-with-frequent-reindexing, not CL in the ML-research sense — which is fine, but say so precisely."
- "'84% improvement in multi-turn context retention' — retention measured how? Was there a benchmark of multi-turn conversations with ground-truth expected context carryover, scored automatically or by humans?"
- "If I gave you a fresh multi-turn conversation right now involving 3 of your 300 APIs, could you trace exactly how context flows from turn 1 to turn 5 in your architecture?"
- "'Architected' — did you make the CL-vs-RAG-vs-fine-tuning decision yourself, or was that decided above you and you implemented a component of it?"
- "What's the single hardest bug you personally debugged in this system, and what was actually wrong?"

### Metric deep-dive: "improving multi-turn context retention by 84%"
1. What exact metric is "multi-turn context retention" — task success rate across turns, slot-carryover accuracy, a human-rated coherence score?
2. What was the baseline system (no RAG? no CL? an earlier, simpler dialogue manager)?
3. What benchmark/dataset was this measured on — internal conversation logs, a synthetic multi-turn test suite you built?
4. 84% improvement — relative (0.45 → 0.83) or absolute (45% → 84%)? These are wildly different claims and get conflated constantly — be ready to state which.
5. Sample size of evaluated conversations?
6. Could the improvement be explained by something other than CL+RAG (e.g., a better base LLM being swapped in during the same period, a longer context window)?
7. How would you defend this number if an interviewer said "84% sounds implausibly high for this kind of improvement"?

---

## Bullet 2.2
> "Led the Data & Automation team, automating 20+ vendor integrations/day and cutting new-integration deployment time from 7 days to 1 day."

### Claim inventory
**Team leadership** claim, "**20+ vendor integrations/day**" (throughput claim — ambiguous unit), **7 days → 1 day** deployment time reduction (86% reduction, note this isn't stated as a percentage but is implicitly a huge one).

### Vague/exaggerated flags
- "Led the team" — how many people, and were you the manager, or a technical/individual lead among peers? These are very different claims.
- "20+ vendor integrations/day" is ambiguous: does the *automation system* process/sync 20+ integrations per day on an ongoing basis (throughput of a running pipeline), or did your team *build* 20+ new integrations per day during a burst (which would be an extraordinary, and slightly implausible, build rate)? This phrasing needs to be nailed down precisely before an interview.
- 7→1 days is a huge (~86%) reduction — what was actually automated to get there?

### Question Tree

**Level 1 — Direct** 🟢
- What is a "vendor integration" in this context — a new third-party API being wired into Niki's tool registry?
- What was the manual 7-day process, step by step, before automation?
- How many people were on the "Data & Automation team," and what was your role — technical lead, people manager, or senior IC?

**Level 2 — Implementation** 🟡
- What did you actually build to compress 7 days into 1 — a code-generation tool from OpenAPI specs, a templated integration scaffold, an internal CLI, a CI/CD pipeline for onboarding new APIs?
- Was "20+/day" describing new integrations being *built*, or existing integrations being *synced/refreshed* on a schedule? Which is it, precisely?
- What still required a human in the loop after automation (auth/credential setup, legal/security review, schema validation)?

**Level 3 — Internal Mechanics** 🟡
- Walk through the automated pipeline: input (vendor API spec) → output (working tool integration) — what are the concrete stages?
- How does the system handle vendors with non-standard or missing OpenAPI specs?

**Level 4 — Design Decisions** 🔴
- Why build custom tooling rather than using an existing integration platform (e.g., an iPaaS like Workato/Zapier-style approach) if one was available?
- What was sacrificed for speed — did the 7→1 day process trade off validation/testing rigor?

**Level 5 — Scale & Performance** 🔴
- At "20+/day" sustained, what breaks first if that doubled to 40+/day — team bandwidth, review bottleneck, API rate limits, something else?

**Level 6 — Failure Scenarios** ☠️
- What happens when an automated integration is deployed with a subtly wrong schema and starts returning bad data to the assistant in production?
- How do you catch a broken/regressed vendor integration before it affects users — automated contract tests against the vendor API?

**Level 7 — Production Reality** ☠️
- How were these integrations monitored post-deployment (uptime, schema drift when a vendor changes their API)?
- Concrete example: what's the worst integration-related production incident you dealt with?

**Level 8 — Adversarial** 💀
- "Say the number again, precisely: is it 20 integrations built per day, or 20 integration *jobs/syncs* running per day? Those are a 100x-different claim in terms of engineering difficulty."
- "'Led the team' — whose performance review did you write, or is 'led' here meaning 'technically drove the roadmap' without formal management authority? Be exact."
- "If this pipeline is so automated, what exactly was YOUR ongoing job once it was built — were you still hand-holding integrations, or fully hands-off?"

### Metric deep-dive: "20+ vendor integrations/day" and "7 days → 1 day"
1. Precisely define the unit being counted as "an integration."
2. Is 20+/day an average over a sustained period, or a peak/best-case number?
3. For the 7→1 day number: what was included in "7 days" (waiting on approvals? actual engineering time? vendor back-and-forth?) — if a chunk of the 7 days was waiting on other people/processes, automating engineering steps might not have caused the whole reduction.
4. What's the current re-measured baseline — has anyone validated the 1-day number is still accurate today vs. when first implemented?
5. Could parallelization (more people/integrations running at once) explain part of the speedup rather than automation alone?

---

## Bullet 2.3
> "Tuned RAG retrieval (chunking, re-ranking, embedding strategy) across the API surface, reducing hallucination rate by 25%, improving overall response reliability for enterprise API queries."

### Claim inventory
**Chunking strategy**, **re-ranking**, **embedding strategy**, **25% hallucination rate reduction**, "response reliability."

### Vague/exaggerated flags
- "Hallucination rate" needs a precise, measurable definition — this term is thrown around loosely industry-wide.
- Three separate RAG levers (chunking, re-ranking, embeddings) are bundled into one metric — which lever contributed how much?

### Question Tree

**Level 1 — Direct** 🟢
- What does "hallucination" mean specifically in the context of API queries — the assistant inventing a parameter name that doesn't exist? Fabricating a response value? Calling the wrong API confidently?
- What was the retrieval pipeline before your tuning, and what exactly did you change?

**Level 2 — Implementation** 🟡
- What chunking strategy did you use — fixed-size token windows, recursive character splitting, semantic chunking (splitting on embedding-similarity boundaries), or document-structure-aware chunking (e.g., per API endpoint)?
- What embedding model, and why that one (open-source like BGE/E5 vs. API-based like OpenAI's text-embedding-3)?
- What re-ranker did you use — a cross-encoder (e.g., a BGE-reranker, Cohere Rerank), and how many candidates does it re-rank (retrieve top-k, re-rank to top-n)?
- What vector database, and how is it indexed (HNSW, IVF)?

**Level 3 — Internal Mechanics** 🟡/🔴
- Explain the difference mechanically between a bi-encoder (used for initial retrieval) and a cross-encoder (used for re-ranking) — why is re-ranking more accurate but too slow to run on the whole corpus?
- How does chunk size trade off against retrieval precision/recall — what happens with chunks that are too large (dilutes relevance signal) vs. too small (loses context, e.g., splits a parameter definition from its description)?
- How do you handle API documentation structure specifically — tables of parameters, nested JSON schemas — during chunking, since naive text splitting can break structured content badly?

**Level 4 — Design Decisions** 🔴
- Of chunking, re-ranking, and embedding strategy, which change had the biggest individual impact, and how do you know (did you ablate them independently)?
- Why re-ranking instead of just retrieving more candidates (higher k) directly into the prompt?
- What are the trade-offs of your chunk size choice, concretely, for this API-documentation use case?

**Level 5 — Scale & Performance** 🔴
- How large was the corpus (number of chunks) across 300+ APIs? What's retrieval latency with re-ranking added (cross-encoders are slower per-candidate)?
- How does index build/update time scale as new APIs are onboarded (ties to bullet 2.2)?

**Level 6 — Failure Scenarios** ☠️
- What happens when no relevant chunk exists for a query (out-of-scope API request) — does the system know to say "I don't know," or does it hallucinate anyway?
- What happens with near-duplicate or conflicting documentation chunks (e.g., two versions of an API doc)?
- Embedding model or vector index corruption/staleness — how would you detect that a chunk of the index has gone stale after a vendor changes their API?

**Level 7 — Production Reality** ☠️
- How is hallucination measured continuously in production, not just in a one-time eval?
- What's the fallback UX when the system can't confidently answer — silent failure, a clarifying question, an explicit "I don't know"?

**Level 8 — Adversarial** 💀
- "25% reduction in hallucination rate — from what baseline rate to what new rate? Give me the two numbers, not just the delta."
- "How did you measure 'hallucination' — human-labeled, LLM-judge labeled, or some automatic factuality-check heuristic? What's the measurement's own error rate?"
- "You listed three changes at once (chunking, re-ranking, embeddings). If I asked you to remove exactly one of the three and re-measure, which do you predict would hurt the most, and why?"

### Metric deep-dive: "reducing hallucination rate by 25%"
1. Precise definition of a "hallucination" event for scoring purposes.
2. Baseline hallucination rate (absolute number) before tuning, and after.
3. Evaluation set: size, source (real user queries vs. synthetic test set), how labeled.
4. Relative vs. absolute reduction — 25% relative (e.g., 20%→15%) is very different from 25 percentage points (e.g., 40%→15%).
5. Was this measured once, or tracked over time to confirm it wasn't a one-off eval-set artifact?
6. Could the reduction be explained by something else changing concurrently (e.g., the base LLM version, prompt template changes)?

---

# COMPANY 3 — Globussoft Technologies, Machine Learning Intern, Sept 2022–Aug 2023

## Bullet 3.1
> "Developed ML model for email intent classification achieving 0.88 F1 score using Random Forest and Weak Supervision on the Enron Dataset."

### Claim inventory
**Random Forest**, **Weak Supervision**, **Enron Dataset**, **0.88 F1 score**, "email intent classification."

### Vague/exaggerated flags
- F1 score requires specifying **which averaging** (macro/micro/weighted) for anything beyond binary classification — intent classification is almost always multi-class.
- "Weak supervision" is a specific methodology (e.g., Snorkel-style labeling functions + a generative label model) — was it actually that, or just "a small amount of manual labeling," which is a very different (and much weaker) claim?
- The Enron dataset is a fixed, well-known public corpus — an interviewer may know its quirks (skewed sender distribution, no ground-truth "intent" labels natively) and ask how you got intent labels for it at all.

### Question Tree

**Level 1 — Direct** 🟢
- What are "email intents" here — categories like meeting-request, complaint, FYI, action-required? How many classes?
- Why Random Forest specifically for this task?

**Level 2 — Implementation** 🟡
- What features fed the Random Forest — TF-IDF, bag-of-words, hand-engineered features (sender, subject-line patterns, time), or embeddings?
- Enron has no native "intent" labels — how did you get ground truth? Manual labeling of a subset, or heuristic rules?
- What exactly did "weak supervision" look like — labeling functions (heuristics/regex/keyword rules) combined via a generative model (à la Snorkel), or something simpler like keyword-based pseudo-labeling?

**Level 3 — Internal Mechanics** 🟡
- Explain how Random Forest works: bootstrap aggregation (bagging), random feature subsetting at each split, how predictions are aggregated (majority vote/averaging) across trees.
- How does weak supervision combine multiple noisy labeling functions into a single training label — majority vote, or a learned generative label model that weighs each labeling function's reliability?
- What's the exact F1 formula, and which averaging scheme did you report (macro treats all classes equally; micro/weighted are dominated by frequent classes)?

**Level 4 — Design Decisions** 🔴
- Why Random Forest over a gradient-boosted model (XGBoost, which is also on your skills list) or a simple linear classifier (logistic regression on TF-IDF, often a strong baseline for text) or a BERT-based classifier?
- Why weak supervision instead of just manually labeling a few hundred emails — what made manual labeling infeasible or undesirable here?
- How did you handle class imbalance if some intents are rare?

**Level 5 — Scale & Performance** 🔴
- How large was the dataset (rows used), train/test split methodology (random split? time-based split, which matters for email data)?
- How long did training take, and did you tune hyperparameters (number of trees, max depth) — how, grid search/random search/manual?

**Level 6 — Failure Scenarios** ☠️
- What kinds of emails did the model get wrong most often, and why (ambiguous intent, sarcasm, forwarded threads)?
- Weak supervision labeling functions conflicting with each other on the same email — how was that resolved?

**Level 7 — Production Reality** ☠️
- Was this deployed anywhere, or purely an offline research/prototype result? Be precise — this changes the nature of the claim significantly.

**Level 8 — Adversarial** 💀
- "0.88 F1 — macro, micro, or weighted? If you don't know the difference, that's the actual answer to how deeply you understand the metric you put on your resume."
- "Walk me through exactly one labeling function you wrote for weak supervision, and how the label model combined it with others."
- "What was the class distribution, and could a trivial always-predict-majority-class baseline have gotten close to 0.88 if the classes were skewed?"
- "Enron email dataset is from the early 2000s and highly domain-specific (energy-trading company). How would this model perform on a modern, different company's email — did you test generalization at all, or is 0.88 purely an in-distribution number?"

### Metric deep-dive: "0.88 F1 score"
1. Binary or multi-class? If multi-class, which averaging (macro/micro/weighted)?
2. What's the train/test split, and is there any data leakage risk (same email thread appearing in both train and test)?
3. What's the class distribution — is 0.88 impressive or close to what a naive baseline gets?
4. How were "true" intent labels obtained/validated for the test set specifically (weak supervision labels test data too, or was test set manually verified for higher-quality ground truth)?
5. Precision/recall breakdown — is 0.88 balanced, or hiding a precision/recall trade-off (e.g., high recall, mediocre precision)?

---

## Bullet 3.2
> "Built ad context categorization model with 85% accuracy, integrating DeepPavlov's BERT for Named Entity Recognition (NER)."

### Claim inventory
**Ad context categorization**, **85% accuracy**, **DeepPavlov**, **BERT-based NER**.

### Vague/exaggerated flags
- **Accuracy** as the headline metric for a categorization task is itself an attack surface — if categories are imbalanced, accuracy can be misleadingly high (or unimpressive) compared to F1/precision-recall.
- "Integrating DeepPavlov's BERT for NER" — this sounds like using a pre-built library/pretrained model rather than training a model yourself. Be ready to be precise about what you built vs. what you called.

### Question Tree

**Level 1 — Direct** 🟢
- What is "ad context categorization" — classifying a webpage/content into categories for ad targeting (like "sports," "finance," "travel")?
- How does NER feed into categorization — are extracted entities used as classifier features, or as a rule-based signal directly?

**Level 2 — Implementation** 🟡
- Did you fine-tune DeepPavlov's BERT NER model on custom entities, or use it purely off-the-shelf (pretrained, zero fine-tuning)? This is the single most important distinction here.
- What did the categorization model itself look like — a separate classifier taking NER output as features, or an end-to-end model?
- How many ad categories, and how was the training/label data for categorization obtained?

**Level 3 — Internal Mechanics** 🟡/🔴
- Explain how BERT-based NER works at a high level — token classification with BIO tagging scheme, contextual embeddings distinguishing entity types by surrounding context.
- Why DeepPavlov specifically (a Russian-origin conversational AI library) rather than spaCy or HuggingFace's own NER pipelines — what did DeepPavlov offer that was better suited?

**Level 4 — Design Decisions** 🔴
- Why NER-based features rather than a straightforward text classifier (TF-IDF/embeddings → classifier) for categorization — what does entity extraction add that raw text features don't?
- What are the failure modes of NER-derived features — e.g., missed entities, wrong entity type, out-of-vocabulary named entities in ad content?

**Level 5/6/7 — Scale, Failure, Production** 🔴/☠️
- How much content was categorized, and at what latency (NER + classification per document)?
- What happens with content with no detectable named entities at all?
- Was this deployed in any real ad-serving pipeline, or evaluated offline only?

**Level 8 — Adversarial** 💀
- "85% accuracy — accuracy on a categorization task can hide a lot. What's the class distribution across ad categories, and would a majority-class baseline get close to 85%?"
- "Did you fine-tune the BERT NER model, or did you literally call a pretrained DeepPavlov pipeline function and use its output as-is? Be exact — 'integrating' is doing a lot of work in that sentence."

### Metric deep-dive: "85% accuracy"
1. Accuracy over how many classes, and what's the class balance?
2. What would a naive majority-class baseline score?
3. Precision/recall per class — is 85% hiding poor performance on rare-but-important categories?
4. Test set size and how it was constructed/labeled.

---

# COMPANY 4 — FloData Analytics, Data Science Intern, Jul 2021–Oct 2021

## Bullet 4.1
> "Built an automated OCR pipeline for US (Ohio) accident data extraction – PyMuPDF for vector images (95% accuracy) and OpenCV + Pytesseract for raster images (85% accuracy), ingesting results into AWS S3."

### Claim inventory
**PyMuPDF** (vector-content extraction), **OpenCV** (image preprocessing), **Pytesseract**/Tesseract (OCR engine), a **routing logic** deciding vector vs. raster handling, **95% vs. 85% accuracy** for the two paths, **AWS S3** ingestion.

### Vague/exaggerated flags
- "Vector images" is slightly imprecise terminology — PDFs contain vector-drawn text/graphics (which PyMuPDF can extract as actual text, not an "image" at all) vs. raster/scanned images (which need OCR). Clarify this distinction precisely — it's a great opportunity to show genuine understanding vs. surface-level buzzword use.
- 95%/85% "accuracy" — accuracy of *what unit* (characters? fields? whole documents extracted correctly)?
- How does the pipeline *decide* whether a given page/document is vector or raster? This routing logic is actually the most interesting engineering part and is easy to gloss over.

### Question Tree

**Level 1 — Direct** 🟢
- What was the actual source data — scanned Ohio accident report PDFs from a government portal?
- What's the difference between a "vector" and a "raster" page in a PDF, in your own words?

**Level 2 — Implementation** 🟡
- How did the pipeline decide which extraction path (PyMuPDF vs. OpenCV+Tesseract) to use for a given page — checking for an embedded text layer, image-only page detection, file metadata?
- What OpenCV preprocessing steps did you apply before Tesseract (grayscale conversion, thresholding/binarization, deskewing, noise removal, contour detection for cropping to relevant regions)?
- What fields were being extracted specifically (date, location, vehicle count, injury severity)? Free text or a structured template with fixed field positions?
- What format did you write to S3 (raw text, structured JSON/CSV, partitioned by date)?

**Level 3 — Internal Mechanics** 🟡/🔴
- Explain how Tesseract's OCR engine works at a high level (LSTM-based line recognition in modern Tesseract versions) — and why preprocessing (binarization, deskew) improves its accuracy so much.
- How does PyMuPDF extract "vector" text — is it reading the PDF's content stream directly (text-showing operators with embedded font/glyph mappings) rather than doing any visual recognition at all? This is a fundamentally different (and much more reliable) mechanism than OCR — do you understand *why* it's more accurate?

**Level 4 — Design Decisions** 🔴
- Why not just run everything through Tesseract uniformly, skipping the vector/raster branching logic? What would you lose in accuracy/speed by doing that?
- What are the trade-offs of your specific OpenCV preprocessing choices — could over-aggressive thresholding have hurt accuracy on lower-quality scans?

**Level 5 — Scale & Performance** 🔴
- How many documents/pages did this pipeline process? What was per-document processing latency, and did that matter (batch job vs. any time-sensitivity)?

**Level 6 — Failure Scenarios** ☠️
- What happens with a rotated/skewed scan that OpenCV's deskew logic gets wrong?
- What happens with a hybrid page (partly vector text, partly a scanned stamp/signature image)?
- Corrupted or password-protected PDFs — did the pipeline handle those, or just fail/skip?
- Duplicate documents ingested twice into S3 — any deduplication logic?

**Level 7 — Production Reality** ☠️
- How did you validate the 95%/85% accuracy numbers — manual spot-checking against a sample, or a full ground-truth-labeled test set?
- Was there any human-in-the-loop review step for low-confidence extractions, or fully unattended?
- What monitoring existed for pipeline failures (a page that silently extracts garbage vs. an explicit error)?

**Level 8 — Adversarial** 💀
- "You call it 'vector images' — vector content in a PDF is text-with-fonts, not an image at all. If PyMuPDF got 95% 'accuracy,' what exactly could still go wrong with pure text-stream extraction that isn't already 100%? Give me a real failure case."
- "85% accuracy for the OCR path — accuracy measured per character, per field, or per whole document? These are very different bars, and 85% character-level accuracy is actually mediocre for a production OCR pipeline (~15% character error rate) versus 85% whole-document-correct, which is a much higher bar."
- "How did you decide the routing between vector and raster pages programmatically — show me the actual logic, not just 'PyMuPDF for one, OpenCV for the other.'"
- "This was a 4-month internship. Realistically, how much of this pipeline did you build solo versus following an existing team pattern/codebase?"

### Metric deep-dive: "95% accuracy" (vector) and "85% accuracy" (raster)
1. Accuracy unit: character-level, field-level (e.g., correctly extracted "accident date"), or document-level (whole record fully correct)?
2. Ground truth source: manually verified subset, or another automated system used as a check?
3. Sample size for each accuracy figure.
4. Is 95% for the vector path suspiciously *not* ~99-100%, given vector text extraction is close to deterministic — what's causing the remaining 5% error (malformed PDFs, mixed content, encoding issues)?
5. Is 85% for OCR calculated the same way as the 95% for vector, so the two numbers are actually comparable?

---

# PART 5 — SKILLS-SECTION CONSISTENCY AUDIT (bonus attack surface)

A sharp interviewer cross-references your **Technical Skills** list against your **Work Experience** narrative and flags anything listed but never evidenced. On this resume:

| Skill listed | Evidenced in a bullet? | Likely question |
|---|---|---|
| TypeScript | ❌ Not mentioned anywhere in Work Experience | "Where have you used TypeScript professionally? Frontend, backend, tooling?" |
| Azure | ❌ Only AWS/GCP appear in bullets | "You list Azure — what did you actually build or deploy on Azure specifically?" |
| Feature Stores | ❌ Not mentioned in any bullet | "Which feature store (Feast, Tecton, SageMaker Feature Store)? What did you use it for?" |
| Vector Databases | ⚠️ Implied by RAG bullets but never named | "Which vector DB — Pinecone, Weaviate, Milvus, pgvector, FAISS? Why that one?" |
| Microservices | ❌ Not evidenced | "Describe one microservice you built — its boundary, its API contract, how it talked to other services." |
| Flask | ❌ Only implied generically under "Backend & Infra" | "Flask vs. FastAPI — where did you actually use Flask specifically?" |
| Feature Stores / ETL Pipelines / PySpark | ❌ No bullet mentions large-scale data engineering | "Walk me through one PySpark job you personally wrote — what was the data volume?" |
| XGBoost | ❌ Bullets mention Random Forest, not XGBoost | "You list XGBoost as a skill but your resume's only classical-ML bullet uses Random Forest — where did you use XGBoost?" |
| MLflow | ❌ No bullet mentions experiment tracking | "How did you track experiments/model versions in your projects — was it MLflow, or ad hoc?" |

**Strong-candidate move:** be ready to either (a) give a real, specific example for each skill you claim, or (b) honestly say "that's foundational knowledge I have but haven't used in a flagship project yet" — the second answer, said confidently, is far better than fumbling to retrofit a fake example.

---

# PART 6 — CROSS-COMPANY QUESTIONS

- You used **Random Forest** at Globussoft and **LLM-based systems** at Sekyurity/EY — why the shift? Was it because the problems changed, the field moved, or your own skill focus evolved?
- At FloData you built a **classical rules+OCR pipeline** with clearly measurable per-path accuracy; at Sekyurity you claim an **84% improvement** on a fuzzier metric. Which of your two measurement approaches is actually more rigorous, and why?
- Compare "catastrophic forgetting mitigation" (Sekyurity) conceptually to "weak supervision" (Globussoft) — both are ways of dealing with imperfect/limited labeled data or model drift. What's the common thread in how you think about data quality problems?
- At EY you evaluate *other people's/teams'* agents (an evaluation/QA-adjacent role); at Sekyurity you *built* the agent being evaluated. Which vantage point taught you more about what actually causes agent failures, and why?
- Across EY (LLM-judge evaluation) and Sekyurity (RAG hallucination reduction), you're solving similar sub-problems (is the model's output trustworthy?) with different tools (a judge model vs. retrieval tuning). If you had EY's evaluation infrastructure available *while* building Sekyurity's RAG system, what would you have done differently?
- Which of your four roles had the **least well-defined success metric**, and how did you personally decide the work was "done" or "good"?
- If you had to **redesign the Sekyurity CL+RAG system today** with everything you now know from your EY evaluation work, what would you change first?
- What did you **personally own end-to-end** at Sekyurity vs. what the "Data & Automation team" you led collectively owned? Draw the line explicitly.
- Which project was **technically hardest**, and why — not "most impactful," but hardest to get working correctly?
- Your metrics get progressively bigger/rounder as you move up your career (0.88 F1 → 85% → 25%/84% → 32%/35%/40%). Is that because the systems genuinely improved more at each stage, or because later metrics are measured more loosely? Defend the trend.

---

# PART 7 — "QUESTIONS THAT COULD EXPOSE RESUME BLUFFING"

These are deliberately pointed. Being asked them isn't an accusation — it's standard due diligence for anyone claiming system-architecture-level ownership at 3 YOE. The goal is to know, cold, which side of each line you're on.

1. "For the CL+RAG system: did you personally choose and implement the continual-learning algorithm, or was CL a term used loosely for 'the RAG index gets updated regularly'? There's no shame in the second answer — but say which it actually was."
2. "For Langfuse: did you write custom instrumentation code, or mostly configure an existing auto-instrumentation integration (e.g., LangChain callback handler)? Both are legitimate, real work — but they're different work."
3. "For the LLM-judge framework: did you design the rubric and prompt from scratch, or adapt an existing open-source eval framework (RAGAS, DeepEval, OpenAI evals)? If the latter, what did *you* customize?"
4. "For DeepPavlov BERT NER: fine-tuned by you, or used out-of-the-box?"
5. "For weak supervision on Enron: did you build actual labeling functions and a label-aggregation model, or hand-label a small set and call it 'weak supervision' loosely?"
6. "For 'led the Data & Automation team': formal manager, tech lead, or 'most senior/vocal person on a small team'? What decisions could you make unilaterally vs. needed sign-off?"
7. "Every single bullet on this resume has a specific percentage in it. Pick the one you're least confident defending under a skeptical audit, right now, and tell me why."
8. "If I called your Sekyurity manager today, what would they say your single biggest individual technical contribution was — in one sentence?"
9. "What's something on this resume that, if I dug deep enough, turned out to be more 'the team did this and I was part of it' than 'I personally built this'? I'd rather hear that honestly now than catch an inconsistency later."
10. "What's the one bullet on this entire resume you're proudest of because you can defend every layer of it, top to bottom, right now, unprompted?"

---

# PART 8 — DIFFICULTY-TAGGED MASTER BANK: BRUTAL (☠️) & FUNDAMENTAL (💀) DEEP CHAINS

These are the "no escape" chains — if a partial answer is given, the interviewer keeps pulling the thread.

### Chain A — Catastrophic forgetting (💀 first-principles)
1. 💀 "What is catastrophic forgetting, mechanically, in terms of what happens to neural network weights?"
   → *If answered:* ☠️ "Why does this happen more in neural nets than in, say, a Random Forest being incrementally updated with new trees?"
   → ☠️ "Name two families of mitigation. Explain one in enough mathematical/algorithmic detail that I could reimplement it."
   → ☠️ "Which one did you use? Why not the other?"
   → 💀 "If you didn't use a named CL technique at all, and this was really 'we re-ran RAG indexing periodically,' is 'catastrophic forgetting' even the right term for what you were mitigating? What actually would forget, mechanically, in a pure RAG system with no model fine-tuning at all?"

### Chain B — LLM-as-judge validity (☠️)
1. ☠️ "How do you know your judge is measuring the thing you think it's measuring, and not just rewarding confident-sounding, longer answers?"
   → ☠️ "What's your judge's agreement rate with human raters, on how many samples?"
   → 💀 "If the judge and the agent being judged are the same underlying model family, what bias does that introduce, and how would you even detect it?"
   → ☠️ "Convince me a 32% improvement in defects-caught isn't just the judge being stricter/noisier, catching things that aren't real defects."

### Chain C — RAG hallucination reduction (☠️)
1. ☠️ "Define hallucination measurably, right now, in one sentence."
   → ☠️ "Of chunking, re-ranking, and embeddings — if you could only ship one of the three changes, which moves the number most, and how do you know?"
   → 💀 "Explain, from first principles, why a cross-encoder re-ranker is more accurate than the bi-encoder used for initial retrieval, and why you can't just use the cross-encoder for the whole corpus."

### Chain D — Vector vs. raster OCR routing (☠️)
1. ☠️ "Show me the actual decision logic for vector-vs-raster routing."
   → 💀 "Explain why PyMuPDF's vector extraction is fundamentally not OCR at all — what's actually happening at the PDF-content-stream level?"
   → ☠️ "Given that, why is the 'vector' path only 95% and not ~100%, if it's just reading text objects directly?"

### Chain E — The "architected" verb (☠️)
1. ☠️ "Give me the actual design doc/decision — CL vs. fine-tuning vs. RAG-only. What were the options on the table, and who made the final call?"
   → ☠️ "What was your reasoning artifact — a written proposal, a whiteboard session, a Slack thread? Walk me through it."
   → 💀 "If you were removed from the team the day after this launched, what would have broken that only you understood?"

---

# FINAL INTERVIEW READINESS REPORT

## 1. Top 20 areas you must prepare
1. Precise definition of "multi-turn context retention" and how 84% was computed.
2. The exact continual-learning technique used (name it, and its mechanics) — or an honest reframe if "CL" was used loosely.
3. How RAG and CL functionally divide labor in the Sekyurity system.
4. Langfuse: self-hosted vs. cloud, and what you personally instrumented vs. auto-instrumentation.
5. LLM-judge design: pointwise vs. pairwise, rubric design, judge-vs-human agreement rate.
6. Known LLM-judge biases (position, verbosity, self-preference) and mitigations.
7. Precise chunking strategy and why it was chosen for API documentation specifically.
8. Bi-encoder vs. cross-encoder mechanics for re-ranking.
9. Definition of "hallucination" used for the 25% metric, with baseline/after numbers.
10. What exactly "20+ vendor integrations/day" measures (build rate vs. sync throughput).
11. Your actual scope of "leading" the Data & Automation team.
12. F1 averaging scheme (macro/micro/weighted) for the 0.88 score, and class distribution.
13. What "weak supervision" concretely consisted of (labeling functions + aggregation, or informal).
14. Whether DeepPavlov's BERT NER was fine-tuned or used off-the-shelf.
15. Class distribution and majority-baseline comparison for the 85% ad-categorization accuracy.
16. Precise definition of "accuracy" (character/field/document-level) for both OCR paths.
17. The vector-vs-raster routing logic in the OCR pipeline, and why vector extraction isn't ~100%.
18. Raw numerator/denominator behind every headline percentage (35%, 32%, 40%, 84%, 25%, 88%, 85%, 95%, 85%).
19. What specifically you'd say is YOUR contribution vs. team/framework/library at each company.
20. A ready, honest answer for any skill on your list (TypeScript, Azure, Feature Stores, Microservices, XGBoost, MLflow) you can't back with a real example.

## 2. Top 20 questions most likely to expose weaknesses
1. "Walk me through the actual continual-learning training loop, mechanically."
2. "84% — relative or absolute? Baseline number vs. new number?"
3. "Did you write the Langfuse instrumentation, or is this the framework's built-in callback integration?"
4. "What's your LLM judge's agreement rate with human raters?"
5. "Is 20+ integrations/day a build rate or a sync/throughput rate?"
6. "0.88 F1 — macro, micro, or weighted, and what's the class distribution?"
7. "Fine-tuned DeepPavlov BERT, or used it pretrained, unmodified?"
8. "What exactly does 'hallucination' mean in your 25% metric, with before/after numbers?"
9. "'Led the team' — manager, tech lead, or senior IC on a small team?"
10. "Why does the 'vector' OCR path score 95% and not ~100% if it's direct text extraction, not OCR?"
11. "If RAG can fetch fresh API info at query time, what does continual learning add?"
12. "What's the raw defect count behind the 40% production-defect reduction?"
13. "Give one concrete debugging session where Langfuse traces saved real time — what broke, how did you find it?"
14. "What would break in the CL+RAG system if you were gone tomorrow?"
15. "Between chunking, re-ranking, and embeddings — which single change moved the hallucination number most?"
16. "How do you know the 32% 'extra' defects are real defects, not judge false positives?"
17. "What's a specific example of a reasoning defect the automated suite caught?"
18. "Which skill on your list (TypeScript, Azure, Feature Stores, Microservices, XGBoost, MLflow) can you NOT back with a concrete example?"
19. "What was the actual manual 7-day process before automation — and how much of that was engineering time vs. approvals/waiting?"
20. "Pick the metric on your resume you're least confident defending, right now."

## 3. Technologies/concepts claimed but needing deeper prep
- **Continual learning theory** (EWC/Fisher information, replay buffers, LoRA-per-domain) — this is graduate-level ML and will be tested if you invoke the term.
- **LLM-as-judge evaluation methodology** (bias types, calibration against humans, RAGAS/DeepEval-style frameworks).
- **RAG internals**: bi-encoder vs. cross-encoder, chunking strategy trade-offs, vector index structures (HNSW/IVF).
- **Weak supervision** (Snorkel-style labeling functions and generative label models) vs. informal pseudo-labeling.
- **Langfuse internals** (trace/span/observation data model, async ingestion, cost-calculation logic).
- **OCR/PDF internals**: PDF content streams and why vector text extraction ≠ OCR.
- **Statistics of your own metrics**: averaging schemes, baselines, sample sizes — for every single percentage on the page.

## 4. Resume bullets most likely to be challenged (ranked)
1. 🥇 Sekyurity — CL + RAG, 300+ APIs, 84% (highest-density claim: two ML subfields + a large number + a big metric).
2. 🥈 EY — LLM-judge frameworks, 32% (requires deep eval-methodology knowledge).
3. 🥉 Sekyurity — RAG retrieval tuning, 25% hallucination reduction (three bundled changes, one metric).
4. EY — Langfuse observability, 35% (ownership-of-instrumentation question).
5. FloData — OCR pipeline, 95%/85% (terminology precision: "vector images" vs. vector text; accuracy units).
6. Sekyurity — Data & Automation team, 20+/day, 7→1 days (ambiguous unit; leadership scope).
7. EY — Eval gates standardization, 40% (org-scope claim, attribution).
8. Globussoft — Ad categorization, 85% (accuracy metric choice, fine-tune vs. off-the-shelf).
9. Globussoft — Email intent classifier, 0.88 F1 (averaging scheme, weak supervision specifics).

## 5. Metrics you need to be able to defend, with the numbers behind them
| Metric | Must be ready with |
|---|---|
| 35% debugging-time cut | Baseline definition, measurement method, sample size |
| 32% more defects caught | Raw counts, defect definition, false-positive check |
| 40% production defect reduction | Raw counts, "defect" definition, time window |
| 84% multi-turn context retention improvement | Metric definition, relative vs. absolute, benchmark used |
| 25% hallucination reduction | Hallucination definition, before/after absolute rates |
| 0.88 F1 | Averaging scheme, class distribution, test set construction |
| 85% ad categorization accuracy | Class distribution, majority-baseline comparison |
| 95% / 85% OCR accuracy | Unit of accuracy (char/field/doc), ground-truth method |
| 7 days → 1 day | What's included in "7 days," re-validated current number |
| 20+ integrations/day | Build rate vs. throughput, precise unit |

## 6. Missing technical details you should pre-prepare (since the resume doesn't state them)
- The specific vector database and embedding model used at Sekyurity.
- The specific LLM(s) used as judge at EY, and their prompt/rubric structure.
- Team sizes at every company (Sekyurity "Data & Automation team," EY agent teams).
- Whether any of this work involved fine-tuning a model at all, anywhere, vs. prompting/retrieval/classical-ML only.
- The actual CL algorithm name, if one exists, for the Sekyurity system.

## 7. Prioritized Preparation Roadmap

**Must know (cannot walk in without these):**
- Full, precise breakdown of the CL+RAG bullet — what CL mechanism, what RAG mechanism, how they interact, and the 84% metric's exact definition.
- Full breakdown of the LLM-judge bullet — judge model, rubric, bias mitigation, agreement rate.
- Raw numbers behind every percentage on the resume (at minimum: numerator/denominator or before/after values).
- Clear, rehearsed answer distinguishing personal contribution vs. team/framework/library for every bullet.

**Should know:**
- RAG internals (chunking trade-offs, bi-encoder vs. cross-encoder, vector index basics).
- Random Forest and weak-supervision mechanics well enough to whiteboard them.
- Langfuse's data model and async-ingestion behavior.
- PDF vector-text-extraction vs. OCR distinction, cold.

**Nice to know:**
- Named CL algorithms in depth (EWC math, replay-buffer sampling strategies) even if not exactly what you used — shows you understand the space you're claiming.
- RAGAS/DeepEval or other eval-framework internals for comparison points.
- DeepPavlov vs. spaCy vs. HuggingFace NER trade-offs.

**Deep-dive if time permits:**
- Tesseract's LSTM-based recognition internals.
- HNSW/IVF vector-index algorithmic detail.
- Generative label models in weak supervision (Snorkel's actual label-model math).

---

*This document is your reference. The live mock interview will proceed one question at a time in chat — answers will be graded, gaps will be drilled, and follow-ups will be chosen based specifically on what you say, not read off a script.*