# ML System Design — Interview Q&A Reference

A concise, practical walkthrough of the 26 core questions interviewers ask when designing an ML system end-to-end.

---

## 1. End-to-end ML system design framework

**Q: How do you structure an ML system design answer?**

Almost every ML system can be broken into the same pipeline. Memorize this order and you can talk through any design question:

```
Requirements → ML formulation → Data → Labels → Features
   → Model → Training → Serving → Scaling → Evaluation
   → Monitoring → Retraining
```

Walking through it in order shows the interviewer you think systematically instead of jumping straight to "let's use XGBoost."

**Follow-ups to expect:** functional vs non-functional requirements, prediction frequency, latency budget, expected QPS, cost limits, what happens if the model goes down, batch vs real-time.

---

## 2. Requirements gathering

**Q: What do you clarify before designing anything?**

Split requirements into two buckets:

**Functional** — what the system actually does
- What are we predicting?
- Who/what consumes the prediction?
- What action follows from it?
- What data do we actually have access to?

**Non-functional** — how well it needs to do it
- Latency, throughput (QPS), availability, scalability, cost, consistency, privacy/security

**Why ask latency early?** Because it constrains everything downstream. A 99%-accurate model that takes 5 seconds to respond is useless behind a 100ms recommendation API — so latency shapes your model choice, not the other way around.

---

## 3. ML formulation

**Q: How do you turn a business problem into an ML problem?**

Example: *"Reduce fraudulent transactions"* becomes → **binary classification**: estimate P(fraud | transaction).

Then pin down:
- Prediction target and time horizon
- What features are actually available *at prediction time*
- Class definitions (what counts as positive/negative)
- Decision threshold
- Cost of a false positive vs a false negative (blocking a real customer vs missing a fraud)

**Why does the prediction horizon matter?** It defines the cutoff for what data is "fair game" — anything after that point is leakage.

---

## 4. Data & labels

**Q: How do you build the training dataset?**

```
Raw data → Cleaning → Feature generation → Label generation → Training set
```

Questions to resolve: data source and arrival frequency, how labels are generated, how much history you need, class balance, and how to handle missing/noisy labels.

**Hardest part of labeling?** Defining the correct labeling *window*.

> Example: predicting "will this transaction turn out to be fraud within 30 days" — you cannot use any information from those 30 days as an input feature, or you've leaked the future into the past.

---

## 5. Feature engineering

**Q: How do you design features for an online system?**

Things to check for every feature:
- Is it available at inference time (not just in the training log)?
- How fresh does it need to be?
- How expensive is it to compute?
- Does training-time value match serving-time value?
- How are missing values handled?
- Is it versioned?

**Key follow-up:** *How do you guarantee a feature computed during training equals the one computed during inference?* This is exactly the problem a **feature store** solves.

---

## 6. Feature store

**Q: What problem does a feature store solve?**

It's the shared source of truth for feature computation, so training and serving never drift apart.

```
                 Feature Store
                /              \
        Offline Store      Online Store
       (historical, for      (low-latency,
        training)             for serving)
```

**Training-serving skew** = when the offline and online computation of "the same" feature produce different values (different code paths, different data freshness) — silently breaking your model in production.

**Point-in-time lookup** = fetching the value of a feature *as it existed at the moment of that historical event*, not its current value — critical for avoiding leakage.

You often *don't* need a feature store for small, low-QPS, mostly-batch systems — it adds real infra overhead.

---

## 7. Offline vs online inference

**Q: When do you pick batch vs real-time inference?**

**Batch (offline):**
```
All users → predict on a schedule → store results
```
Good for: daily churn scores, weekly customer segments — anything that doesn't need to react *now*.

**Online (real-time):**
```
Request → fetch features → model → prediction → response
```
Good for: fraud detection, live recommendations.

**Can you mix both?** Yes — precompute expensive/stable features in batch, then combine with fresh real-time signals at request time. Very common pattern.

---

## 8. Batch vs synchronous vs asynchronous

**Batch:** many requests processed together, on a schedule.

**Synchronous:** `Client → API → Model → Response` — the client blocks and waits.

**Asynchronous:**
```
Client → Queue → Worker → Model → Result store/callback
```
Client fires the request and moves on; it picks up the result later.

**Use async when:** inference is slow, or the caller doesn't actually need an instant answer (e.g., "generate a report").

---

## 9. Queues

**Q: Why put a queue in front of an inference service?**

It decouples producers from consumers and absorbs bursts:

```
Requests → Queue → Workers → Model
```

Benefits: smooths traffic spikes, stops the service from getting overwhelmed, enables retries, lets workers scale independently.

**If consumers are slower than producers?** The queue backs up → latency climbs → eventually you hit storage/capacity limits. Fix with backpressure, autoscaling workers, rate limiting, or dropping/prioritizing low-value requests.

---

## 10. Caching

**Q: Where does caching fit in an ML system?**

Common layers: request cache, feature cache, embedding cache, model cache, prediction cache, LLM response cache.

> Example: if 10,000 users request the same product embedding, compute it once, cache it, and serve the rest from cache instead of recomputing.

**When does caching go wrong?** When the underlying data changes but the cached value doesn't — you serve a stale, incorrect prediction. Always pair caching with a sensible TTL or explicit invalidation.

---

## 11. Model serving

**Q: How do you actually serve a model in production?**

```
Client → Load Balancer → Inference API → Feature Store → Model → Prediction
```

Typically packaged with Docker + FastAPI/Flask (or a dedicated serving framework like TorchServe/Triton) and deployed on Kubernetes.

Follow-ups to be ready for: loading the model once at startup (not per-request), how you version models, and how you roll back a bad deployment quickly.

---

## 12. Load balancing

**Q: Why does model serving need a load balancer?**

```
              Load Balancer
             /      |       \
        Model Pod  Model Pod  Model Pod
```

It spreads requests across replicas → higher throughput, fault tolerance, horizontal scaling.

**If one instance crashes?** Traffic reroutes to the healthy ones — but only if health checks are actually configured to detect the failure.

---

## 13. Scaling

**Vertical scaling:** give one machine more CPU/RAM/GPU.

**Horizontal scaling:** add more replicas.

```
1 GPU → 4 GPUs (replicas)
```

Horizontal scaling generally wins on fault tolerance and scalability, but ML models can make it costly — each replica may need a full copy of GPU memory.

---

## 14. Sharding

**Q: What is sharding?**

Splitting data or workload across multiple machines so no single one is overloaded.

```
10M users
  ├── Shard 1: users 1–2.5M
  ├── Shard 2: users 2.5–5M
  ├── Shard 3: users 5–7.5M
  └── Shard 4: users 7.5–10M
```

**Downside:** uneven data distribution creates "hot shards," and operations spanning multiple shards get more complex.

---

## 15. Replication

**Sharding** splits data across machines; **replication** copies the *same* data/model across machines.

```
Sharding:                 Replication:
Data A → Server 1         Data A → Server 1
Data B → Server 2         Data A → Server 2
```

Replication mainly buys you availability, read throughput, and fault tolerance.

---

## 16. Autoscaling

**Q: How do you autoscale an inference service?**

Scale on signals like CPU/GPU utilization, requests/sec, queue depth, and latency. For async pipelines, **queue depth** is often the most reliable signal.

**Why isn't GPU utilization alone enough?** A model can show moderate GPU usage while still blowing its latency SLA (e.g., waiting on I/O or batching delays). You need signals tied to actual user-facing performance, not just hardware load.

---

## 17. Latency vs throughput

**Latency** = time to handle one request. **Throughput** = requests handled per second.

> Example: 50ms latency per request, 2,000 requests/sec throughput.

**Why do they trade off?** Batching requests together boosts throughput (more efficient GPU use) but makes individual requests wait longer for their batch to fill — hurting latency. Which one you optimize for depends on the product: a live chat needs low latency; a nightly batch job cares about throughput.

---

## 18. Availability

**Q: How do you make an inference service highly available?**

Combine: multiple replicas, load balancing, health checks, autoscaling, multi-zone deployment, fallback models, timeouts, circuit breakers, monitoring, and fast rollback.

**If the model service goes down entirely?** Degrade gracefully instead of crashing the whole app:
- serve a cached prediction
- fall back to a simpler rule-based/older model
- queue the request for later
- return a controlled error

The rule: an ML failure should never take the whole product down.

---

## 19. Data drift vs concept drift

**Data drift** — the input distribution shifts: P(X) → P'(X)
> Example: your user base skews younger over time.

**Concept drift** — the relationship between inputs and the target shifts: P(Y|X) → P'(Y|X)
> Example: fraudsters change tactics, so the same transaction pattern that used to be safe is now risky.

**Which is harder to detect?** Concept drift — you usually need ground-truth labels/outcomes to notice it, whereas data drift can be spotted just by watching input distributions.

---

## 20. Monitoring

**Q: What do you monitor for a production model?**

- **Infra:** CPU/GPU, memory, error rate, throughput, latency
- **Data:** missing values, feature distributions, drift, schema changes
- **Model:** prediction distribution, calibration/confidence, accuracy/F1 once labels arrive, concept drift
- **Business:** conversion, revenue, fraud loss, CTR, user satisfaction

**Key principle:** a model can look perfectly healthy on infra metrics while quietly producing bad predictions — that's why data and business-level monitoring matter just as much as uptime.

---

## 21. Retraining

**Q: When should you retrain?**

Triggers: a fixed schedule, measured performance drop, detected data/concept drift, a meaningful amount of new labeled data, or a major product/business change.

Don't retrain blindly on a timer just because you can — tie the decision to model stability, how fast labels arrive, drift signals, and actual business impact. Retraining has a cost too (compute, validation, deployment risk).

---

## 22. Model registry

**Q: What problem does a model registry solve?**

It tracks every model version through its lifecycle:

```
Model v1 → v2 → v3 → Staging → Production → Archived
```

Stores version, training metadata, metrics, artifacts, dependencies, and approval status — making deployments and rollbacks reproducible instead of "someone remembers which model is live."

---

## 23. Canary deployment

**Q: What is a canary deployment?**

Route a small slice of traffic to the new model first, watch it closely, then ramp up:

```
95% traffic → Model v1 (stable)
 5% traffic → Model v2 (new)
```

Watch errors, latency, and both model and business metrics. If it's healthy, increase the percentage gradually; if not, roll back fast — only a small slice of users were affected.

---

## 24. Shadow deployment

**Canary vs shadow:**

- **Canary:** the new model's output actually reaches some real users.
- **Shadow:** the new model gets real production traffic, but its predictions are only logged — never shown to users.

```
Request → Model v1 → shown to user
        → Model v2 → logged only
```

Shadow mode lets you validate a new model against real traffic with zero risk to the user experience.

---

## 25. Blue-green deployment

**Q: What is blue-green deployment?**

Run two full, identical production environments:

```
Blue  = current live version
Green = new version
```

Traffic starts fully on Blue. Once Green is validated, you flip all traffic to Green at once. Because Blue is still running untouched, rollback is just flipping traffic back — fast and low-risk.

---

## 26. A/B testing

**Canary vs A/B test:**

- **Canary** answers: *"Can this new version safely handle production traffic?"* (stability/rollout focus)
- **A/B test** answers: *"Does this new version actually perform better?"* (impact focus, measured statistically)

```
Group A → Model v1
Group B → Model v2
     → compare business metrics
```

A model can pass a canary (stable, no crashes, normal latency) and still fail an A/B test if it doesn't actually move the metric you care about — stability and improvement are two different questions.

---

### Quick recap of the full pipeline
```
Requirements → Formulation → Data/Labels → Features → Feature Store
   → Model → Serving (batch/online) → Scaling/LB/Caching/Queues
   → Availability → Monitoring → Drift Detection → Retraining
   → Registry → Canary/Shadow/Blue-Green → A/B Testing
```

---
---

## 27. Rollback

**Q: When do you roll back a model?**

Roll back when any of these happen:
- Prediction quality drops
- A business KPI gets worse
- Latency breaches the SLA
- Error rate spikes
- The data pipeline breaks
- The model starts producing unsafe outputs

The goal of a good deployment system is to make rollback **fast and automated** — you don't want someone manually re-deploying an old Docker image at 2am.

---
# P1 — MLOps

## 28. What is MLOps?

**Q: What does MLOps solve that plain DevOps doesn't?**

DevOps manages the software lifecycle (code → build → deploy). ML adds several more moving parts on top:

```
Code + Data + Features + Model + Training config
```

So MLOps additionally focuses on: reproducible training, experiment tracking, data/model versioning, a model registry, deployment, monitoring, and retraining. In short — DevOps ships code; MLOps ships code **and** the data/model that code depends on.

---

## 29. MLflow

**Q: What would you use MLflow for?**

Mainly for experiment tracking and model packaging: logging metrics, parameters, and artifacts per run, then registering and deploying the winning one.

```
Run 1 → XGBoost, depth=5,  F1=.82
Run 2 → XGBoost, depth=8,  F1=.85   ← best
Run 3 → XGBoost, depth=10, F1=.83
        ↓
   Register Run 2 → Deploy
```

Without this, "which hyperparameters gave us the best model" turns into archaeology through Slack messages.

---

## 30. Data versioning

**Q: Why version your data?**

Say Model v7 was trained on January's dataset. Six months later you need to reproduce it exactly — without data versioning, you simply can't answer "which dataset produced this model?"

Reproducibility needs all of these tied together:

```
Code version + Data version + Feature version + Hyperparameters + Model artifact
```

Miss any one of these and a "reproduced" model is really just a similar one.

---

## 31. Airflow / data pipelines

**Q: What role does Airflow play in an ML pipeline?**

It's the **orchestrator** — it doesn't train models itself, it schedules and coordinates the steps around training:

```
Extract → Validate → Transform → Generate features
   → Train → Evaluate → Register → Deploy
```

It handles scheduling, step dependencies, retries on failure, and pipeline monitoring. Think of it as the conductor, not the orchestra.

---

## 32. CI/CD for ML

**Q: What should an ML CI/CD pipeline validate?**

**CI (before merging):** unit tests, data validation, feature tests, model code tests, evaluation tests.

**CD (deployment flow):**
```
Build → Test → Train/evaluate → Register
   → Deploy to staging → Canary/shadow → Production
```

The big difference from normal software CI/CD: **data and model quality become part of the pipeline gate**, not just "does the code compile."

---

## 33. Docker + Kubernetes

**Q: Why use Docker and Kubernetes for ML serving?**

**Docker** packages code + dependencies + runtime into one reproducible unit — the model behaves the same on your laptop and in prod.

**Kubernetes** manages the fleet running those containers: scaling, networking, health checks, rolling deployments, resource allocation.

**Why is GPU workload trickier on K8s?** You need GPU-aware scheduling, device plugins, the right node types, and sometimes specialized storage/networking — a plain CPU pod scheduler doesn't know how to hand out GPUs.

---

## 34. Model serving concerns

**Q: What matters when deploying a model?**

Model load time, memory footprint, latency, throughput, versioning, concurrency, batch support, hardware choice, autoscaling, health checks, and rollback readiness. Essentially: everything that determines whether the model behaves well *under real traffic*, not just in a notebook.

---
# P0 — LLMOps

## 35. What is LLMOps?

**Q: How is LLMOps different from MLOps?**

```
LLMOps = MLOps + LLM-specific operational concerns
```

Traditional ML is roughly `Data → Model → Prediction`. LLM apps add prompts, a model/provider choice, token accounting, tool calls, retrieval, context management, evaluation, and safety. So LLMOps needs monitoring layers that plain MLOps never had to think about: prompts, tokens, cost, latency, traces, evals, and guardrails.

---

## 36. Prompt management

**Q: Why treat prompts like code?**

Because a small wording change can significantly shift model behavior — just like a code change can introduce a bug. So version them the same way:

```
Prompt v1, v2, v3 — tracked alongside model version, parameters, eval results, deployment version
```

This makes "why did output quality change last Tuesday" an answerable question instead of a guessing game.

---

## 37. Model routing

**Q: What is model routing?**

Instead of sending every request to the same (usually expensive) model, route based on the request:

```
Request → Router → [Small LLM | Medium LLM | Large LLM]
```

Routing decision factors: task complexity, cost, latency budget, capability needed, privacy, and provider availability.

> Example: a simple intent classification goes to a cheap small model; a multi-step reasoning task goes to the large one.

---

## 38. Model fallback

**Q: How do you design fallback?**

```
Primary model call
      ↓
   failed? ── No  → return result
      ↓ Yes
  Call fallback model → return result
```

Triggers: provider outage, rate limiting, timeout, model overload. Important detail: the fallback model's output format/schema should be compatible with the primary, or your downstream code breaks even though the fallback "worked."

---

## 39. Token tracking

**Q: Why track tokens?**

Because LLM cost is basically `input tokens + output tokens × provider pricing`. Track it broken down by user, request, agent, tool, model, and application — otherwise you can't tell whether a cost spike came from one runaway agent loop or genuinely higher traffic. It's also how you spot bloated retrieval context before it becomes an expensive habit.

---

## 40. Cost tracking / reduction

**Q: How would you reduce LLM application cost?**

- Route simple tasks to smaller models
- Trim/optimize prompts and unnecessary context
- Cache repeated responses/embeddings
- Cap or reduce output length
- Batch requests where possible
- Avoid runaway agent loops
- Use cheaper embedding models
- Improve retrieval so you send less irrelevant context

**Key principle:** optimize **cost per successful task completed**, not just raw price-per-token — a cheaper model that needs 3 retries can cost more than an expensive one that succeeds on the first try.

---

## 41. TTFT + throughput

**Q: What is TTFT and why does it matter?**

**TTFT = Time To First Token** — how long the user waits before anything starts appearing on screen. For streaming UIs, this drives *perceived* responsiveness even more than total completion time.

Also track **tokens/sec** (generation throughput) separately, because:

```
Low TTFT + slow generation   → feels fast to start, drags on
High TTFT + fast generation  → feels slow to start, then flies
```

Both are "the same total time" on paper but feel completely different to a user.

---

## 42. LLM caching

**Q: What kinds of caching exist for LLM apps?**

| Type | What it reuses |
|---|---|
| Response caching | Full answer for an identical request |
| Embedding caching | Embedding vector for identical text |
| Prefix caching | Computation for a shared prompt prefix |
| KV caching | Attention K/V states during decoding |

Each targets a different bottleneck — response caching saves a whole round trip, KV caching saves redundant computation inside a single generation.

---

## 43. LLM evaluation pipeline

**Q: How do you build automated LLM evaluation?**

```
Golden dataset → run prompt/model version → collect quality metrics
   → LLM judge / deterministic checks → compare vs baseline
   → pass/fail → deploy
```

This turns prompt and model changes into something you can **regression test**, the same way you'd test a code change, instead of eyeballing a handful of outputs and hoping.

---

## 44. LLM tracing

**Q: Why does tracing matter so much for LLM apps?**

A single user request can fan out into a long chain:

```
User → Agent → LLM → Retriever → Tool → LLM → Tool → Final answer
```

A flat request/response log won't tell you *where* in that chain the latency, cost, or quality problem happened. Tracing captures each LLM call, prompt, output, retrieval step, tool call, latency, token count, cost, and error — so you can pinpoint the exact hop that went wrong.

---

## 45. Provider abstraction

**Q: Why build a model/provider abstraction layer?**

Instead of your app code calling one provider's SDK directly everywhere:

```
Application → LLM abstraction layer → [Provider A | Provider B | Local model]
```

This buys you easy model swapping, built-in fallback paths, cost optimization by routing, easier A/B testing between models, and resilience if one provider has an outage.

---

## 46. Safety controls in LLMOps

**Q: Where should safety controls live?**

Not just "a good system prompt" — use defense in depth across the whole request path:

```
Input → input guardrails → LLM → output guardrails
   → tool authorization → business rules → monitoring
```

For agents specifically: **tool authorization must live outside the LLM** — never trust the model itself to decide it's allowed to call a dangerous tool; enforce that at the system level.

---
# P0 — Inference Optimization

## 47. Batching

**Q: Why does batching improve throughput?**

Instead of running requests one at a time, group them and run them together:

```
[Request 1, Request 2, Request 3] → one batched GPU pass
```

GPUs are built for parallel work, so batching uses that hardware far more efficiently. **Tradeoff:** bigger batches raise throughput but also raise per-request latency (you wait for the batch to fill) and memory usage.

---

## 48. Continuous batching

**Q: What is continuous batching?**

Regular batching waits for the whole batch to finish before starting a new one. **Continuous batching** swaps requests in and out of the batch dynamically as individual sequences finish generating:

```
Request A ──────────→ done
Request B ────→ done          (Request D slots in here)
Request C ──────────────→
```

This matters a lot for LLMs specifically, because different prompts generate wildly different output lengths — without this, a batch full of fast-finishing requests sits idle waiting on one long one.

---

## 49. Quantization

**Q: What is quantization and why does it help?**

Store weights/activations at lower numerical precision:

```
FP32 → FP16 → INT8 → INT4
```

Benefits: less memory, faster inference on supported hardware, higher throughput, and it lets bigger models fit on smaller GPUs. **Tradeoff:** quality can degrade at lower precision — the right level depends on the model, hardware, and how quality-sensitive the task is.

---

## 50. KV cache

**Q: Why is KV cache both a speedup and a bottleneck?**

It avoids recomputing attention for every previous token on every new step — a huge speedup. But it has to store those K/V tensors for *every* token of *every* active sequence, and that memory scales with:

```
sequence length × batch size × num KV heads × head dim × precision
```

That's why long-context, high-concurrency serving runs into memory limits fast — the KV cache, not the model weights, becomes the bottleneck.

---

## 51. Speculative decoding

**Q: What is speculative decoding?**

A small, fast "draft" model proposes several tokens ahead; the large model then verifies them all in one parallel pass instead of generating them one at a time:

```
Draft model:  "The capital of France is Paris"
Large model:  verifies the draft in parallel → accepts/rejects tokens
```

If the draft model guesses well, the big model effectively generates faster without changing what it would have produced on its own. **Tradeoff:** the speedup only shows up if the draft model's predictions actually match the target model often enough.

---

## 52. Prefix caching

**Q: What is prefix caching?**

When many requests share the same leading text — a system prompt, a long shared document, standard agent instructions — reuse the computation for that shared prefix instead of recomputing it per request:

```
[Shared system prompt + context] + [unique user query]
        ↑ cached                        ↑ computed fresh
```

Especially valuable for apps with long, mostly-static system prompts or repeated reference documents.

---

## 53. PagedAttention

**Q: What problem does PagedAttention solve?**

KV-cache memory tends to get fragmented and hard to manage efficiently as sequences grow and finish at different rates. PagedAttention manages it in **fixed-size blocks/pages**, similar to how an OS manages virtual memory — allocate pages as needed instead of one big contiguous chunk per sequence.

Result: better GPU memory utilization, less fragmentation, more concurrent sequences served, and smoother support for dynamic batch sizes. This is one of the core ideas behind high-throughput LLM serving engines like vLLM.

---

## 54. Tensor parallelism

**Q: What is tensor parallelism?**

Split the math *inside a single layer* across multiple GPUs:

```
One large layer's computation
         ↓
   ┌─────┴─────┐
  GPU 1       GPU 2
```

Useful when a layer (or the whole model) is too large to run efficiently on one GPU. The catch: the GPUs must constantly communicate, so inter-GPU bandwidth/latency becomes a real performance factor.

---

## 55. Model / pipeline parallelism

**Q: Tensor parallelism vs model parallelism — what's the difference?**

- **Tensor parallelism:** split the computation *within* a layer across GPUs.
- **Model/pipeline parallelism:** split *different layers* of the model across GPUs.

```
GPU 1 → layers 1–20
GPU 2 → layers 21–40
GPU 3 → layers 41–60
```

(Naming varies a bit across frameworks, but that's the core distinction: split inside a layer vs split across layers.)

---

## 56. GPU utilization

**Q: Low GPU utilization — does that mean the model itself is inefficient?**

No, not automatically. Low GPU utilization can come from a CPU bottleneck, slow data loading, network latency, batch sizes too small to saturate the GPU, memory bandwidth limits, synchronization stalls, poor kernel efficiency, or requests simply arriving too slowly to keep the GPU busy.

**Takeaway:** profile the *whole* pipeline (data → network → compute), not just the GPU utilization number in isolation.

---

## 57. Memory bandwidth

**Q: Why can LLM decoding be memory-bandwidth bound rather than compute bound?**

Every new token during autoregressive decoding requires pulling large model weights and KV-cache data through memory — and the actual math (FLOPs) needed per token is often small relative to how much data has to move. So decode speed frequently depends more on **how fast you can move data** than on raw compute power. This is exactly why quantization (less data to move) and KV-cache optimizations matter so much for decode-heavy workloads.

---

## 58. CPU vs GPU

**Q: When do you use CPU vs GPU for inference?**

**GPU:** large neural nets, high throughput needs, low-latency requirements, anything that benefits from massive parallelism — this is where LLMs live.

**CPU:** small models, low/sporadic traffic, cost-sensitive workloads, or models that just don't get much speedup from GPU acceleration anyway.

Decide based on: model size + expected QPS + latency SLA + cost budget + memory constraints — not just "GPU is always faster."

---
---

## 🔥 The 15 questions to master first

If you're prepping for ML Engineer / ML Systems / AI Engineer interviews, prioritize these:

**ML System Design**
1. Design an ML system end-to-end, requirements through retraining.
2. Batch vs online vs asynchronous inference.
3. Feature store, training-serving skew, and point-in-time correctness.
4. Design a scalable model-serving architecture.
5. Latency vs throughput, and how you'd scale the system.
6. Data drift vs concept drift, and how monitoring/retraining respond to each.
7. Canary vs shadow vs blue-green vs A/B testing — when to use which.

**MLOps**
8. What MLOps adds on top of normal DevOps.
9. MLflow, experiment tracking, model registry, reproducibility.
10. Designing an ML CI/CD pipeline.

**LLMOps**
11. Designing an LLMOps architecture for production.
12. Tracking tokens, cost, latency, TTFT, and traces.
13. Model routing, fallback, and provider abstraction.

**Inference**
14. Continuous batching, KV cache, PagedAttention.
15. Quantization, speculative decoding, tensor/model parallelism.

---

## 🔥 The ultimate ML system design grill question

Eventually you should be able to answer this cold:

> *"Design a production-grade fraud detection system that processes 10,000 transactions/sec, must return a decision within 100ms, has highly imbalanced labels, receives delayed fraud labels, and needs to retrain automatically."*

A strong answer flows through the full pipeline naturally:

```
Requirements → ML formulation → Data ingestion → Point-in-time labels
   → Feature engineering → Offline feature store → Online feature store
   → Model training → MLflow/registry → Validation → Canary deployment
   → Load balancer → Online inference → Caching → Monitoring
                          ┌───────────┴───────────┐
                     Data drift            Model performance
                          └───────────┬───────────┘
                              Retraining ← delayed labels
```

And then expect the interviewer to poke at every joint:
- Why online inference here specifically, not batch?
- Why this model family, given the 100ms budget?
- Why a feature store — what breaks without one?
- How do you prevent label leakage with delayed fraud labels?
- What happens if the feature store goes down mid-traffic?
- How do you absorb 10× a traffic spike?
- How do you detect concept drift when fraud labels arrive late?
- How do you roll back a bad model fast?
- What's the fallback when inference exceeds 100ms?

The goal isn't memorizing what Kubernetes or MLflow *is* — it's being able to justify **why each piece belongs in this specific system**, under these specific constraints.