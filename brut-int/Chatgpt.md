Absolutely. I went through the resume line-by-line and will treat **every claim as something a skeptical Staff-level interviewer could attack**. I will not assume implementation details that are not stated; where the resume is ambiguous, I’ll turn that ambiguity into an interview question.

Resume source: 

# Brutal Interview Map — Shivam Shrivastava

## 0. Immediate interviewer assessment

Your resume has a very clear progression:

**Classical ML → OCR → RAG/Continual Learning → production agents → observability/evaluation/risk.**

That is good, but it also creates several **high-risk attack surfaces**.

The five claims I would attack first are:

1. **“Continual Learning + RAG”**
2. **“300+ enterprise APIs”**
3. **“84% improvement in multi-turn context retention”**
4. **LLM-judge evaluation and “32% more reasoning defects”**
5. **“40% reduction in production defects”**

Then I would move into:

6. **25% hallucination reduction**
7. **35% reduction in debugging time**
8. **20+ vendor integrations/day and 7 days → 1 day**
9. **0.88 F1 with Random Forest + Weak Supervision**
10. **95% / 85% OCR accuracy**

These numbers invite the interviewer to ask:

> “Exactly how did you calculate that?”

If you cannot define the metric, baseline, evaluation set, measurement procedure, and failure modes, the number becomes a liability rather than an advantage.

---

# 1. EY — Langfuse Observability

Resume claim:

> “Deployed Langfuse observability across 10+ LLM agents, unifying tracing for prompts, tool calls, tokens, and costs; cut agent-debugging time by 35% and enabled real-time monitoring.” 

## Technologies / concepts exposed

* Langfuse
* LLM agents
* distributed tracing
* prompts
* tool calls
* token accounting
* cost tracking
* observability
* real-time monitoring
* debugging
* 10+ agents
* 35% improvement

### 🟢 Direct

1. What exactly did you build at EY?
2. What did **you personally implement**?
3. What did Langfuse provide out of the box?
4. Why did the organization need Langfuse?
5. What did the architecture look like before Langfuse?
6. What changed after deployment?
7. What exactly do you mean by an “LLM agent”?
8. What information did you trace?
9. How did you trace prompts?
10. How did you trace tool calls?
11. How did you calculate token usage?
12. How did you calculate cost?

### 🟡 Implementation

13. How did you integrate Langfuse into the agents?
14. Where did instrumentation happen?
15. Did you instrument the LLM wrapper, agent framework, middleware, or individual functions?
16. How did you correlate an LLM call with subsequent tool calls?
17. How did you represent nested agent/tool execution?
18. How did you handle retries?
19. How did you handle failed tool calls?
20. How did you trace streaming responses?
21. How did you capture input/output tokens?
22. What happened when token information wasn't available from the provider?
23. How did you calculate cost across different LLM providers/models?
24. How did you handle asynchronous execution?

### 🔴 Internals

25. Explain distributed tracing using a concrete agent execution.
26. What is the difference between a **trace**, **span**, and **event**?
27. How would you model:

`user request → planner → LLM → tool → database → tool result → LLM → final answer`

28. How do trace IDs and span IDs work?
29. How would you propagate correlation IDs across microservices?
30. What happens if an agent calls another service?
31. How would you identify the exact span responsible for latency?
32. How would you distinguish model latency from tool latency?

### ☠️ Scale / Performance

33. What was the trace volume?
34. How many requests per day?
35. What was the average number of spans per request?
36. What was the storage backend?
37. Did observability itself introduce latency?
38. How did you measure that overhead?
39. What happens if traffic increases 100×?
40. Would you synchronously send telemetry during the request?
41. If not, how would you buffer/export it?
42. What happens if the observability backend goes down?

### 💀 Production

43. Could sensitive enterprise data appear in traces?
44. How did you handle PII/secrets?
45. Should prompts containing confidential information be logged?
46. Who had access to the traces?
47. How would you implement tenant isolation?
48. What happens if Langfuse is unavailable?
49. Should an observability failure cause an agent request to fail?
50. How would you debug an agent whose production behavior changed but whose logs appeared normal?

---

## Metric attack: “35% reduction in debugging time”

Expect this immediately:

> **“How exactly did you calculate the 35%?”**

You need to be able to explain:

* definition of debugging time
* baseline
* post-Langfuse measurement
* number of incidents/tasks
* time period
* who performed the debugging
* whether the same engineers were compared
* whether issue complexity was controlled
* source of measurement
* median vs mean
* outliers
* reproducibility

### Brutal follow-up

> “If you tell me average debugging time dropped from 100 minutes to 65 minutes, how do you know Langfuse caused the reduction?”

Then:

> “What alternative explanations did you eliminate?”

Then:

> “Give me an example of a bug where Langfuse directly reduced debugging time.”

---

# 2. EY — LLM-Judge Evaluation

Resume claim:

> “Built LLM-judge evaluation frameworks scoring decision quality, correctness, and guardrail coverage; automated regression suites caught 32% more reasoning defects pre-release vs. manual review.” 

This is probably your **single highest-value interview attack surface**.

## 🟢 Direct

1. What is an LLM judge?
2. Why did you need one?
3. What exactly did you evaluate?
4. What was “decision quality”?
5. What was “correctness”?
6. What was “guardrail coverage”?
7. Why use an LLM to evaluate another LLM?
8. What models were being evaluated?
9. What model was acting as the judge?
10. What did your framework actually do?

## 🟡 Implementation

11. Describe the complete evaluation pipeline.
12. What was the input to the judge?
13. What was the output?
14. What was your evaluation prompt?
15. Did you use structured output?
16. How did you force the judge to produce consistent scores?
17. What scoring scale did you use?
18. How did you define pass/fail?
19. How did you handle ambiguous answers?
20. How did you create the evaluation dataset?
21. How did you generate regression cases?
22. How did you version evaluation datasets?
23. How did you version judge prompts?
24. How did you compare evaluations between model versions?

## 🔴 Judge reliability

25. Why should I trust an LLM judge?
26. What is judge bias?
27. What is position bias?
28. What is verbosity bias?
29. What happens if the judge prefers answers that sound confident?
30. How did you validate judge-human agreement?
31. Did you calculate inter-rater agreement?
32. How did you handle judge nondeterminism?
33. Did you use temperature 0?
34. Does temperature 0 guarantee deterministic behavior?
35. How did you detect judge drift?

### ☠️ Brutal

> “Suppose the candidate model produces an incorrect answer that is extremely well-written. Your judge gives it 9/10. How do you detect that?”

Then:

> “Suppose the judge and candidate use the same underlying model family. Why isn't the judge simply reproducing the same model's biases?”

Then:

> “How would you prove that your LLM judge is actually measuring correctness rather than linguistic quality?”

---

# 3. EY — Regression defects

Claim:

> “automated regression suites caught 32% more reasoning defects pre-release vs. manual review.” 

This number needs a **full statistical defense**.

You should expect:

### 🟡

* What is a reasoning defect?
* Who labeled it?
* What was the ground truth?
* How many test cases?
* How many releases?
* How many defects?
* What does “32% more” mathematically mean?

### ☠️

> “32% more than manual review means what exactly?”

Possible interpretations include:

* 32% increase in number detected
* 32 percentage-point increase
* 32% higher recall
* 32% relative improvement in detection rate

The interviewer will absolutely distinguish these.

### 💀

> “If manual review catches 50 defects and your framework catches 66, that's 32% more. But what if your framework generates 200 false positives? Is it actually better?”

Now you need:

* precision
* recall
* false positives
* false negatives
* reviewer workload
* defect severity
* calibration

---

# 4. EY — Risk-based release gates

Claim:

> “Standardized eval gates and risk-based release criteria across agent teams; reduced production defects by 40% compared to the pre-evaluation-framework baseline.” 

## Questions

1. What is an evaluation gate?
2. What happens when an agent fails the gate?
3. What criteria determine whether it passes?
4. What does “risk-based” mean?
5. How did you classify risk?
6. How did you assign severity?
7. Did all agents have the same threshold?
8. Why not?
9. Who decided the thresholds?
10. How were thresholds validated?
11. How did you prevent teams from gaming the evaluation?
12. What was your CI/CD integration?
13. Did evaluation block deployment automatically?
14. How did you handle emergency releases?

### ☠️ Design challenge

> “Design a release policy for three agents:
>
> * customer support
> * financial decision support
> * internal developer assistant.
>
> Would you use identical evaluation thresholds?”

Then:

> “What happens if the financial agent has 99.5% correctness but one failure could be catastrophic?”

Now you have to reason about **risk-weighted evaluation rather than raw accuracy**.

---

# 5. Sekyurity AI — Continual Learning + RAG

Resume claim:

> “Architected a Continual Learning (CL) + RAG system for the virtual assistant across 300+ enterprise APIs (AWS, GCP, Jira, Slack), mitigating catastrophic forgetting and improving multi-turn context retention by 84%.” 

🚨 **This is your biggest technical attack surface.**

An interviewer will likely spend **20–40 minutes here**.

---

## 🟢 First attack

> “Explain your architecture from user query to final answer.”

You need to be able to draw it mentally.

Then:

> “Where exactly does Continual Learning happen?”

This is critical.

Because **RAG and Continual Learning are different concepts**.

Expect:

> “Why did you need continual learning if you had RAG?”

That question alone can expose whether the architecture was genuinely understood.

---

## 🟡 Implementation

1. What exactly was being continually learned?
2. Was the base model updated?
3. Were adapters updated?
4. Were embeddings updated?
5. Was the retrieval index updated?
6. Were prompts updated?
7. Were tool-selection policies updated?
8. What data triggered learning?
9. What was the training pipeline?
10. How frequently was the model updated?
11. How did you prevent bad feedback from entering training?
12. How did you evaluate new versions?

---

## 🔴 Catastrophic forgetting

You need a fundamental explanation.

### Question:

> “What is catastrophic forgetting?”

Then:

> “Why does it happen in neural networks?”

Then:

> “Give me a concrete example from your system.”

Then:

> “How did your architecture mitigate it?”

Then:

> “Why wouldn't RAG alone solve catastrophic forgetting?”

Then:

> “What technique did you use to prevent forgetting?”

The interviewer may then drill into:

* replay
* rehearsal
* regularization
* parameter isolation
* adapters
* LoRA
* freezing layers
* task-specific components
* retrieval-based memory

**Do not claim any of these unless they were actually part of your implementation.**

---

# 6. “300+ enterprise APIs”

This sounds impressive but creates a huge attack surface.

### 🟢

> “What does supporting 300+ APIs actually mean?”

Was it:

* 300 API endpoints?
* 300 integrations?
* 300 services?
* 300 API specifications?
* 300 tool definitions?

You must distinguish these.

### 🟡

For one API:

> “Walk me through the complete lifecycle.”

For example:

`User intent → API/tool selection → parameter extraction → validation → authentication → request → response parsing → LLM interpretation → final response`

Then:

> “How did the agent know which API to call?”

Then:

> “How did it know what parameters to provide?”

Then:

> “What happened when it selected the wrong API?”

---

# 7. Enterprise API agent — brutal questions

### ☠️

> “Suppose two APIs can satisfy the same user request. How does the agent choose?”

> “What if the API schema is incomplete?”

> “What if the API returns a 200 but semantically incorrect data?”

> “What if the API times out after performing the operation?”

> “What if the agent retries and creates a duplicate Jira ticket?”

> “How did you handle idempotency?”

> “What if Slack succeeds but the final LLM call fails?”

> “How do you recover from partial failure?”

> “What if credentials expire?”

> “How are secrets supplied to the agent?”

> “Could the LLM see the credentials?”

> “How did you prevent prompt injection through API responses?”

That last question is especially important for an enterprise agent.

---

# 8. 84% multi-turn context retention

This is another **metric the interviewer will attack immediately**.

You need to define:

### What is “context retention”?

For example:

> User: “Find my latest invoice.”

> Assistant: “Invoice X.”

> User: “When was it paid?”

How did you determine whether the assistant retained the relevant context?

### Questions

1. What exactly was measured?
2. What was the evaluation dataset?
3. How many conversations?
4. How many turns?
5. What was the baseline architecture?
6. What was the new architecture?
7. What was the formula?
8. What was the baseline score?
9. What was the final score?
10. Was 84% relative improvement or percentage points?
11. Who labeled correctness?
12. Was evaluation automated?
13. What types of context failed?
14. Did performance degrade with conversation length?

### ☠️

> “Show me the exact mathematical calculation behind the 84%.”

Then:

> “Why are you calling that context retention rather than answer accuracy?”

Then:

> “Could retrieval quality have improved rather than context retention?”

That's a very strong interviewer question.

---

# 9. Data & Automation — 20+ vendor integrations/day

Claim:

> “Led the Data & Automation team, automating 20+ vendor integrations/day and cutting new-integration deployment time from 7 days to 1 day.” 

## 🟢

1. What is a vendor integration?
2. What exactly was automated?
3. What did the process look like before?
4. What did it look like after?
5. What did you personally build?
6. What was the biggest bottleneck?

## 🟡

7. How did you standardize integrations?
8. What varied between vendors?
9. Did you have a common interface?
10. How did you handle authentication differences?
11. How did you handle different schemas?
12. How did you validate vendor responses?
13. How did you test integrations?
14. How did you handle API version changes?

### ☠️

> “If you can integrate 20 vendors per day, why doesn't a bad integration get deployed 20 times faster too?”

This forces discussion of:

* validation
* CI/CD
* contract tests
* sandbox environments
* integration tests
* rollback
* quality gates

### Metric attack

> “How did you measure 7 days → 1 day?”

You need:

* same integration complexity?
* median or mean?
* sample size?
* start/end definition?
* engineering-hours vs calendar time?
* deployment time vs development time?

---

# 10. RAG tuning

Claim:

> “Tuned RAG retrieval (chunking, re-ranking, embedding strategy) across the API surface, reducing hallucination rate by 25%, improving overall response reliability for enterprise API queries.” 

This creates an entire RAG interview.

## 🟢

1. What is RAG?
2. Why RAG?
3. What was being retrieved?
4. What was your chunking strategy?
5. What embedding model did you use?
6. What vector database?
7. What was the reranker?
8. How many documents/chunks?
9. What was top-k?

## 🟡 Chunking

> “Why did you choose that chunk size?”

Then:

> “What happens if chunks are too small?”

Then:

> “What happens if they're too large?”

Then:

> “Did you use fixed-size or semantic chunking?”

Then:

> “How did overlap affect retrieval?”

---

# 11. RAG internals

Be ready for:

### 💀 Embeddings

* What is an embedding?
* How is semantic similarity represented?
* What does cosine similarity measure?
* What is Euclidean distance?
* Why might cosine similarity be preferable?
* What does vector dimensionality mean?
* What happens when the embedding model changes?

### 💀 Retrieval

> “Explain approximate nearest neighbor search.”

Potential follow-ups:

* HNSW
* IVF
* PQ
* indexing
* recall/latency tradeoff

### 🔴 Re-ranking

> “Why retrieve top 20 and rerank rather than retrieve top 5?”

Then:

> “What does a cross-encoder do that a bi-encoder doesn't?”

---

# 12. Hallucination reduction — 25%

Again:

> “Define hallucination.”

Then:

> “How did you detect it?”

Then:

> “What was the ground truth?”

Then:

> “How many queries?”

Then:

> “What was the baseline?”

Then:

> “What changed?”

Then:

> “How do you know retrieval caused the improvement?”

### ☠️ Experimental design

A strong interviewer may ask:

> “Design an experiment proving your new retrieval strategy actually reduced hallucination.”

You should discuss:

* fixed evaluation dataset
* baseline retrieval
* modified retrieval
* same generation model
* same prompt
* controlled variables
* human/automated evaluation
* statistical confidence
* error categorization

---

# 13. Globussoft — Random Forest + Weak Supervision

Claim:

> “Developed ML model for email intent classification achieving 0.88 F1 score using Random Forest and Weak Supervision on the Enron Dataset.” 

This gives the interviewer a bridge into classical ML fundamentals.

### 🟢

1. What was the classification problem?
2. What were the classes?
3. How large was the dataset?
4. How did you preprocess emails?
5. What features did you use?
6. Why Random Forest?
7. Why not logistic regression?
8. Why not SVM?
9. Why not BERT?

### 🟡 Random Forest

10. How does a decision tree split?
11. What is entropy?
12. What is Gini impurity?
13. How does Random Forest differ from a single tree?
14. Why does bagging help?
15. What is feature randomness?
16. How does Random Forest reduce variance?
17. What happens if trees are too deep?

### 🔴 Weak supervision

This is a likely attack.

> “What exactly did you mean by weak supervision?”

Then:

> “How did you generate labels?”

Then:

> “What labeling functions did you use?”

Then:

> “How did you combine conflicting labeling functions?”

Then:

> “How did you know the weak labels weren't introducing systematic bias?”

---

# 14. F1 = 0.88

You need to know this **cold**.

### 💀

> “Define precision.”

> “Define recall.”

> “Why is F1 the harmonic mean?”

> “Why not accuracy?”

> “When can F1 be misleading?”

> “Was your 0.88 macro-F1, micro-F1, or weighted-F1?”

That final question is especially important.

Then:

> “Give me the confusion matrix.”

And:

> “Which class had the worst recall?”

If you don't know the answer, this becomes a serious credibility problem.

---

# 15. Ad Context Categorization — BERT + NER

Claim:

> “Built ad context categorization model with 85% accuracy, integrating DeepPavlov’s BERT for Named Entity Recognition (NER).” 

Potential ambiguity:

**Is BERT performing NER, while another component performs categorization?**

An interviewer will ask.

### Questions

1. What was “ad context”?
2. What were the categories?
3. What was the input?
4. What was the output?
5. Why was NER necessary?
6. How did NER contribute to categorization?
7. What BERT model?
8. Was it pretrained?
9. Did you fine-tune it?
10. What dataset?
11. What entity types?
12. What evaluation metric?

### 🔴 NER fundamentals

> “Explain BIO tagging.”

> “What is B-I-O?”

> “How do you handle nested entities?”

> “What is token classification?”

> “How does BERT generate token-level predictions?”

### ☠️

> “Why does vanilla BERT's WordPiece tokenization create complications for NER?”

Then:

> “How do you map subword predictions back to original tokens?”

---

# 16. FloData — OCR

Claim:

> “Built an automated OCR pipeline for US (Ohio) accident data extraction – PyMuPDF for vector images (95% accuracy) and OpenCV + Pytesseract for raster images (85% accuracy), ingesting results into AWS S3.” 

This has several separate attack surfaces.

## 🟢

1. What type of PDFs were these?
2. What do you mean by “vector images”?
3. Why PyMuPDF for those?
4. Why OpenCV for raster images?
5. Why Pytesseract?
6. What preprocessing did you perform?
7. How did you decide which pipeline to use?
8. What did the extracted data look like?
9. How did you validate extraction?
10. How did you upload results to S3?

---

# 17. OCR internals

### 🔴

> “What is the difference between text extraction and OCR?”

> “If a PDF contains selectable text, why run OCR?”

> “What does PyMuPDF actually extract?”

> “What happens when a PDF contains scanned pages?”

> “How does Tesseract recognize characters?”

> “What is thresholding?”

> “What is binarization?”

> “Why would grayscale improve OCR?”

> “What does deskewing accomplish?”

> “What happens if the document is rotated?”

> “How does resolution affect OCR?”

---

# 18. OCR accuracy — 95% vs 85%

Again, define **accuracy**.

Was it:

* character accuracy?
* word accuracy?
* field-level accuracy?
* document-level accuracy?
* exact-match accuracy?

Suppose:

> 95% of characters are correct.

That doesn't mean:

> 95% of extracted accident records are correct.

An interviewer may ask:

> “If a driver's name is 95% correct but the accident date is wrong, is that acceptable?”

This leads into **field-weighted evaluation** and domain-specific correctness.

---

# 19. AWS / Cloud attack surface

Your skills claim:

* AWS
* Azure
* GCP
* S3

And your experience explicitly mentions:

* AWS
* GCP
* Jira
* Slack

So expect cloud questions even if your bullets don't explain them.

### 🟡 AWS

* What is S3?
* Object vs block storage?
* S3 consistency model?
* IAM?
* Bucket policy vs IAM policy?
* Presigned URLs?
* Encryption?
* KMS?
* Versioning?
* Lifecycle policies?
* Multipart upload?

### ☠️

> “Your application needs to upload sensitive OCR output to S3. Design the secure architecture.”

Then:

> “What if the application server is compromised?”

Then:

> “Should the application have `s3:*`?”

Obviously the expected direction is least privilege—but you need to explain **how**.

---

# 20. Skills section attack

Your skills list itself creates questions.

You list:

* Python
* SQL
* TypeScript
* LLMs
* RAG
* Embeddings
* HuggingFace
* PyTorch
* TensorFlow
* Scikit-learn
* XGBoost
* LLMOps
* PySpark
* Pandas
* NumPy
* ETL
* Feature Stores
* Vector Databases
* FastAPI
* Flask
* Docker
* CI/CD
* Linux
* REST APIs
* Microservices
* AWS
* Azure
* GCP
* MLflow
* Git
* Langfuse

A senior interviewer can randomly select any one.

### Example:

> “You have PyTorch and TensorFlow on your resume. Explain when you would choose one over the other.”

Then:

> “Show me how automatic differentiation works.”

Then:

> “What is a computation graph?”

Then:

> “What is backpropagation actually calculating?”

Similarly:

> “You list Feature Stores. What problem does a feature store solve?”

Then:

> “Why can't I just use PostgreSQL?”

Then:

> “What is training-serving skew?”

That is how the skills section becomes dangerous.

---

# 21. Cross-company questions

These are extremely important because they test whether your career story is coherent.

### 🔥 RAG

> You used RAG at Sekyurity and evaluation/observability at EY. What did you learn about RAG in Sekyurity that influenced how you evaluated agents at EY?

### 🔥 Evaluation

> At Sekyurity you claim 25% hallucination reduction. At EY you built formal evaluation infrastructure. If you rebuilt the Sekyurity RAG evaluation today, what would you change?

### 🔥 Continual Learning

> Why did you need Continual Learning at Sekyurity but not mention it at EY?

### 🔥 Agents

> You worked with 10+ agents at EY and 300+ APIs at Sekyurity. What is the fundamental difference between an agent and an API orchestration workflow?

### 🔥 Observability

> If you had Langfuse while building the Sekyurity system, what bugs would it have helped you find?

### 🔥 Metrics

> Your EY work has 35%, 32%, and 40% metrics. Your Sekyurity work has 84%, 25%, 7→1 days. How did you ensure these metrics were measured rigorously?

### 🔥 Architecture

> Which system was technically harder: the 300+ API assistant or the multi-agent evaluation platform? Why?

### 🔥 Ownership

> Which project did you architect yourself from first principles, and which parts were primarily integration work?

That last question is a **bluff detector**.

---

# 22. Questions specifically designed to expose bluffing

These are questions I'd use if I suspected the candidate had memorized terminology.

### 💀 Level 1

> “Draw the architecture.”

If you can't draw it, problem.

### 💀 Level 2

> “Pick one request and walk me through it.”

No abstractions. One concrete request.

### 💀 Level 3

> “What happens internally?”

### 💀 Level 4

> “Why this design?”

### 💀 Level 5

> “What breaks at 100× scale?”

### 💀 Level 6

> “What was your worst production failure?”

### 💀 Level 7

> “What did the framework do versus what did you write?”

### 💀 Level 8

> “Show me the exact metric calculation.”

### 💀 Level 9

> “What alternative did you reject?”

### 💀 Level 10

> “If I removed [technology], how would you rebuild it?”

---

# 23. Particularly dangerous “framework did it” questions

Expect these around Langfuse, RAG, HuggingFace, DeepPavlov, PyMuPDF, Pytesseract, etc.

> “What did **you** implement versus what Langfuse implemented?”

> “What did **you** implement versus what the vector database implemented?”

> “What did **you** implement versus what HuggingFace implemented?”

> “What did **you** implement versus what DeepPavlov provided?”

> “What did PyMuPDF actually do for you?”

> “What did Pytesseract actually do for you?”

The ideal answer clearly separates:

**library capability → configuration → custom code → architecture → engineering decisions.**

---

# 24. Top 20 areas you must prepare

| Priority | Area                            |
| -------- | ------------------------------- |
| ☠️       | Continual Learning architecture |
| ☠️       | RAG architecture                |
| ☠️       | 84% context-retention metric    |
| ☠️       | LLM-as-a-judge                  |
| ☠️       | Evaluation methodology          |
| ☠️       | 32% defect-detection metric     |
| ☠️       | 40% production-defect reduction |
| ☠️       | Hallucination measurement       |
| 🔴       | Agent architecture              |
| 🔴       | Tool/API orchestration          |
| 🔴       | Distributed tracing             |
| 🔴       | Langfuse internals/integration  |
| 🔴       | RAG retrieval internals         |
| 🔴       | Embeddings                      |
| 🔴       | Re-ranking                      |
| 🔴       | Vector databases                |
| 🔴       | Random Forest                   |
| 🔴       | Weak supervision                |
| 🔴       | BERT/NER                        |
| 🟡       | OCR pipeline fundamentals       |

---

# 25. Top 20 questions most likely to expose weaknesses

1. **Draw your 300+ API assistant architecture.**
2. **Where exactly did Continual Learning happen?**
3. **Why did you need Continual Learning if you already had RAG?**
4. **Explain how you measured the 84% improvement.**
5. **What exactly is context retention?**
6. **How did you mitigate catastrophic forgetting?**
7. **Walk me through one API request end-to-end.**
8. **How did the agent select among 300+ APIs?**
9. **How did you measure the 25% hallucination reduction?**
10. **What exactly was an LLM judge evaluating?**
11. **How did you validate that the judge was correct?**
12. **What does “32% more defects” mathematically mean?**
13. **How did you measure the 40% production-defect reduction?**
14. **What did you personally implement in Langfuse?**
15. **How did you calculate the 35% debugging improvement?**
16. **What happens when a tool call partially succeeds?**
17. **How did you handle duplicate API operations?**
18. **What was your Random Forest feature representation for emails?**
19. **What exactly does your 0.88 F1 represent?**
20. **Define the 95% and 85% OCR accuracy metrics.**

---

# 26. Metrics you must be able to defend

You should have a precise answer for **every one**:

### EY

**35%**

* debugging time

**32%**

* reasoning defects caught

**40%**

* production defects

### Sekyurity

**84%**

* multi-turn context retention

**20+**

* vendor integrations/day

**7 → 1 day**

* integration deployment time

**25%**

* hallucination reduction

### Globussoft

**0.88**

* F1

**85%**

* ad categorization accuracy

### FloData

**95%**

* PyMuPDF/vector extraction accuracy

**85%**

* OpenCV/Pytesseract/raster extraction accuracy

For every number, memorize:

> **Definition → formula → baseline → dataset → sample size → time period → measurement source → before → after → limitations.**

---

# 27. Missing details you should prepare privately

Your resume doesn't specify these, so **do not invent them**. Instead, prepare your real answers.

### Sekyurity

* Exact CL methodology
* Model(s)
* RAG architecture
* vector DB
* embedding model
* reranker
* chunking strategy
* retrieval k
* API orchestration mechanism
* evaluation dataset
* context-retention formula
* hallucination metric
* scale/traffic
* latency
* production deployment
* monitoring

### EY

* Agent framework(s)
* LLM providers/models
* Langfuse integration mechanism
* telemetry architecture
* evaluation architecture
* judge model
* evaluation dataset
* scoring methodology
* human-vs-LLM validation
* CI/CD integration
* risk taxonomy
* release gates
* defect definition
* production baseline

### Globussoft

* exact feature engineering
* class distribution
* train/test split
* preprocessing
* weak-label methodology
* Random Forest hyperparameters
* F1 averaging method
* confusion matrix

### FloData

* PDF characteristics
* extraction logic
* image preprocessing
* OCR configuration
* field schema
* accuracy definition
* error handling
* S3 architecture

---

# 28. Final priority roadmap

## 🔥 MUST KNOW

You should be able to explain these from first principles without notes:

* RAG
* embeddings
* vector similarity
* ANN search
* reranking
* LLM agents
* tool calling
* context/memory
* Continual Learning
* catastrophic forgetting
* LLM evaluation
* LLM-as-a-judge
* precision/recall/F1
* hallucination evaluation
* distributed tracing
* API architecture
* failure handling
* your exact metrics

## 🟡 SHOULD KNOW

* HNSW
* vector DB internals
* prompt/version management
* evaluation datasets
* CI/CD evaluation gates
* risk-based release
* model monitoring
* token/cost accounting
* AWS IAM/S3
* Docker
* FastAPI
* microservices
* Random Forest internals
* weak supervision
* BERT
* NER

## 🟢 NICE TO KNOW

* advanced ANN indexing
* sophisticated continual-learning algorithms
* advanced statistical significance testing
* distributed telemetry architecture
* model serving optimizations
* advanced cloud architecture

## ☠️ DEEP-DIVE IF TIME PERMITS

* catastrophic forgetting research
* LLM judge reliability/bias
* RAG evaluation frameworks
* agent security
* prompt injection
* tool poisoning
* distributed tracing internals
* evaluation calibration
* statistical experimental design
* production LLM cost optimization

---

# Now we start the actual mock interview

From this point forward, I will **not dump questions on you**.

I'll behave like the interviewer.

I'll ask **one question**, you answer naturally, and I'll then:

1. Score you **1–10**
2. Identify technically incorrect/missing points
3. Tell you what a Staff-level answer should contain
4. Attack the weakest part of your answer
5. Ask the next follow-up
6. Keep drilling until we reach first principles

I will **not rescue vague answers**.

## ☠️ Question 1 — Architecture

You claim:

> **“Architected a Continual Learning (CL) + RAG system for the virtual assistant across 300+ enterprise APIs.”**

**Do not give me a high-level marketing answer.**

Imagine I am sitting across the table from you with a whiteboard.

**Walk me through the complete architecture of this system, from the moment a user sends a request to the moment the final response is returned.**

Tell me:

* the major components,
* where RAG happens,
* where Continual Learning happens,
* how the 300+ APIs are represented/selected,
* and what you personally built.

**Go.**
