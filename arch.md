# Azure OpenAI RLM — Architecture

```text
                 ┌──────────────────────────┐
                 │        User / CLI        │
                 │ PDF path + query + flags │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │      PDF Ingestion       │
                 │ pypdf → _split_pages()   │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │         DSPy RLM         │◄────────────────────┐
                 │    Iterative reasoning   │                     │
                 └────────────┬─────────────┘                     │
                              │                                   │
                 ┌────────────┴─────────────┐                     │
                 ▼                          ▼                     │
       ┌────────────────────┐   ┌───────────────────────────┐    │
       │   Azure OpenAI v1  │   │      REPL / Interpreter    │────┘
       │   Language model   │   │  Executes generated Python │
       └────────────────────┘   │  code + exposes tools      │
                                └─────────────┬─────────────┘
                                              │
                                              ▼
                                ┌───────────────────────────┐
                                │   Document Retrieval      │
                                │ search_document()         │
                                │ get_page() / get_pages()  │
                                └─────────────┬─────────────┘
                                              │
                                              ▼
                                ┌───────────────────────────┐
                                │  Retrieved text / output  │
                                └─────────────┬─────────────┘
                                              │
                                              └──────► Back to RLM
                                                           │
                                                           ▼
                                              ┌────────────────────┐
                                              │    Final Answer    │
                                              │       SUBMIT       │
                                              └─────────┬──────────┘
                                                        │
                                                        ▼
                                              ┌────────────────────┐
                                              │ Trace & Observability│
                                              │ trajectory + usage │
                                              └─────────┬──────────┘
                                                        │
                                               ┌────────┴────────┐
                                               ▼                 ▼
                                         ┌───────────┐     ┌───────────┐
                                         │trace.json │     │trace.html │
                                         └───────────┘     └───────────┘
```

## Block and Function Responsibilities

| Block / Function | Functionality |
|---|---|
| **User / CLI** | Accepts the PDF path, question, and run options. |
| **PDF Ingestion** | Extracts PDF text using `pypdf`. |
| **`_split_pages()`** | Splits extracted text into page-aware sections for targeted retrieval. |
| **DSPy RLM** | Orchestrates iterative reasoning, tool calls, and final submission. |
| **Azure OpenAI v1** | Generates the reasoning steps and Python code requested by the RLM. |
| **REPL / Interpreter** | Executes the model-generated Python code and provides access to retrieval tools. |
| **`search_document()`** | Searches extracted document text for relevant passages. |
| **`get_page()`** | Retrieves text from one specified page. |
| **`get_pages()`** | Retrieves text from a specified page range. |
| **Retrieved text / output** | Returns tool results to the REPL/RLM for the next reasoning step. |
| **`SUBMIT` / Final Answer** | Ends the RLM loop and returns the final response. |
| **Trajectory capture** | Records iterations, generated code, tool calls, and outputs. |
| **Usage tracking** | Collects available prompt, completion, and total token counts. |
| **`trace.json`** | Stores structured run and trace data. |
| **`trace.html`** | Displays the trace in a browser-friendly visual format. |
| **`LATEST.txt`** | Points to the latest run directory, when written by the script. |

## Configuration

- **`AZURE_OPENAI_ENDPOINT`** — Azure resource endpoint.
- **`AZURE_OPENAI_API_KEY`** — Authenticates requests to Azure.
- **`AZURE_OPENAI_DEPLOYMENT`** — Azure deployment used by the root RLM.
- **`AZURE_OPENAI_SUB_DEPLOYMENT`** — Optional separate deployment for recursive model calls.
- **`AZURE_OPENAI_TEMPERATURE`** — Controls response randomness, if supported by the deployment.
