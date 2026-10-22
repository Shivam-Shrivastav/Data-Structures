Absolutely. For **ML System Design + MLOps + LLMOps + Inference Optimization**, I'd make the questions heavily **scenario-based and trade-off-oriented**. These are areas where interviewers often keep drilling until they find whether you understand production architecture or have only used the tools.

I’ll cover **every topic/subtopic you listed**, but keep the number of primary questions manageable by attaching the important follow-ups to each.

# Priority 14 — ML System Design

## 1. End-to-end ML system design framework

### Q1. Design an ML system end-to-end. What steps would you follow?

You should be able to structure almost any ML system as:

```text
Requirements
    ↓
ML formulation
    ↓
Data
    ↓
Labels
    ↓
Features
    ↓
Model
    ↓
Training
    ↓
Serving
    ↓
Scaling
    ↓
Evaluation
    ↓
Monitoring
    ↓
Retraining
```

**Follow-up questions:**

* What are the functional and non-functional requirements?
* What exactly are we predicting?
* What is the prediction frequency?
* What is the acceptable latency?
* What is the expected QPS?
* What is the cost constraint?
* What happens when the model is unavailable?
* How do you decide between batch and real-time inference?

---

# 2. Requirements

### Q2. What requirements would you clarify before designing an ML system?

Separate them into:

**Functional**

* What are we predicting?
* Who consumes the prediction?
* What actions depend on it?
* What data is available?

**Non-functional**

* Latency.
* Throughput/QPS.
* Availability.
* Scalability.
* Cost.
* Consistency.
* Privacy/security.

**Grill:**

> "Why do you ask latency before choosing the model?"

Because model architecture depends on the serving constraint. A highly accurate model that takes 5 seconds may be useless for a 100-ms recommendation API.

---

# 3. ML formulation

### Q3. How do you convert a business problem into an ML problem?

Example:

> "Reduce fraudulent transactions."

Could become:

> Binary classification: predict \(P(fraud|transaction)\).

Then define:

* Prediction target.
* Prediction horizon.
* Features available at prediction time.
* Positive/negative classes.
* Decision threshold.
* Business cost of FP/FN.

**Follow-up:**

> Why is defining the prediction horizon important?

Because features and labels must respect **point-in-time correctness**.

---

# 4. Data + labels

### Q4. How would you design the training dataset for an ML system?

You need:

```text
Raw data
 ↓
Cleaning
 ↓
Feature generation
 ↓
Label generation
 ↓
Training dataset
```

Questions to resolve:

* Where does data come from?
* How frequently does it arrive?
* How are labels generated?
* How much historical data?
* What is the class distribution?
* How do we handle missing/noisy labels?
* Is there temporal leakage?

### Follow-up:

**"What is the hardest part of creating labels?"**

Often it's defining the correct **labeling window**.

Example:

> Predict whether a transaction will become fraudulent within 30 days.

You can't use information from those 30 days as features at prediction time.

---

# 5. Feature Engineering

### Q5. How would you design features for an online ML system?

Consider:

* Feature availability.
* Feature freshness.
* Computation cost.
* Training-serving consistency.
* Missing values.
* Feature versioning.
* Point-in-time correctness.

**Critical follow-up:**

> "How do you ensure the feature calculated during training is identical to the feature calculated during inference?"

This leads directly to **feature stores / shared feature transformation logic**.

---

# 6. Feature Store

### Q6. What problem does a feature store solve?

A feature store manages ML features consistently between **training and serving**.

Typically:

```text
              Feature Store
             /              \
            ↓                ↓
      Offline Store      Online Store
            ↓                ↓
       Training         Real-time serving
```

Offline storage is optimized for historical training data.

Online storage is optimized for low-latency feature retrieval.

### Follow-ups:

* Why can't we simply calculate features separately in training and production?
* What is **training-serving skew**?
* What is point-in-time lookup?
* Why does an online feature store need low latency?
* When would you not need a feature store?

---

# 7. Offline vs Online Inference

### Q7. When would you choose batch/offline inference vs online inference?

**Batch:**

```text
Millions of users
      ↓
Periodic prediction
      ↓
Store results
```

Useful when predictions don't need to be immediate.

Examples:

* Daily churn prediction.
* Weekly customer segmentation.

**Online:**

```text
Request
 ↓
Features
 ↓
Model
 ↓
Prediction
```

Useful when prediction must happen immediately.

Examples:

* Fraud detection.
* Real-time recommendations.

### Grill:

> Can you combine both?

Yes.

For example, precompute expensive features/predictions in batch while calculating fresh features or final scoring online.

---

# 8. Batch vs Real-time vs Asynchronous

### Q8. Explain batch, synchronous online and asynchronous inference.

**Batch:**

Process many requests together periodically.

**Synchronous:**

```text
Client → API → Model → Response
```

Client waits for the result.

**Asynchronous:**

```text
Client
 ↓
Queue
 ↓
Worker
 ↓
Model
 ↓
Result store/event
```

Client doesn't need to wait for model execution.

### Follow-up:

> When would asynchronous inference be preferable?

When inference takes too long or immediate response isn't required.

---

# 9. Queues

### Q9. Why would you put a queue between an application and an ML inference service?

A queue provides **decoupling and buffering**.

```text
Requests
   ↓
Queue
   ↓
Workers
   ↓
Model
```

Benefits:

* Handles traffic spikes.
* Prevents overload.
* Enables asynchronous processing.
* Provides retry mechanisms.
* Allows worker scaling.

**Follow-up:**

> What happens if consumers are slower than producers?

The queue grows → latency increases → eventually storage/capacity limits are reached.

You need backpressure, autoscaling, rate limiting, or request dropping/prioritization.

---

# 10. Caching

### Q10. Where would you use caching in an ML system?

Potential locations:

```text
Request cache
Feature cache
Embedding cache
Model cache
Prediction cache
LLM response cache
```

Example:

If thousands of users request the same embedding:

```text
First request → compute embedding → cache
Next requests → cache hit
```

### Follow-up:

> When can caching produce incorrect predictions?

When the underlying data/features change but the cached result remains stale.

Therefore caching requires an appropriate **TTL/invalidation strategy**.

---

# 11. Model Serving

### Q11. How would you serve an ML model in production?

Typical architecture:

```text
Client
 ↓
Load Balancer
 ↓
Inference API
 ↓
Feature Store
 ↓
Model
 ↓
Prediction
```

The model can be packaged using:

* Docker.
* FastAPI/Flask.
* Dedicated serving frameworks.
* Kubernetes.

### Follow-ups:

* How do you load the model efficiently?
* Should the model be loaded for every request?
* How do you handle model versioning?
* How do you roll back a bad model?

---

# 12. Load Balancing

### Q12. Why do we need a load balancer for model serving?

Suppose we have:

```text
              Load Balancer
             /      |       \
          Model   Model    Model
          Pod 1   Pod 2    Pod 3
```

It distributes requests across instances.

Benefits:

* Higher throughput.
* Fault tolerance.
* Horizontal scaling.
* Better availability.

**Follow-up:**

> What happens if one model instance crashes?

Traffic is routed to healthy instances, assuming health checks are configured correctly.

---

# 13. Scaling

### Q13. Horizontal vs vertical scaling for ML inference?

**Vertical scaling:**

Give one machine more CPU/RAM/GPU.

**Horizontal scaling:**

Add more inference instances.

```text
1 GPU
 ↓
4 GPUs / replicas
```

Horizontal scaling usually provides better fault tolerance and scalability, but ML models can make scaling expensive because each replica may require significant GPU memory.

---

# 14. Sharding

### Q14. What does sharding mean in an ML system?

Sharding distributes data/work across multiple machines.

For example:

```text
10M users
 ↓
Shard 1 → users 1–2.5M
Shard 2 → users 2.5–5M
Shard 3 → users 5–7.5M
Shard 4 → users 7.5–10M
```

Useful when one machine cannot efficiently handle the entire dataset or workload.

**Follow-up:**

> What is a downside?

Uneven distribution can create **hot shards**, and cross-shard operations become more complicated.

---

# 15. Replication

### Q15. Sharding vs replication?

**Sharding:**

Splits data/workload across machines.

**Replication:**

Copies the same data/model/service across multiple machines.

```text
Sharding:
Data A → Server 1
Data B → Server 2

Replication:
Data A → Server 1
Data A → Server 2
```

Replication improves:

* Availability.
* Read throughput.
* Fault tolerance.

---

# 16. Autoscaling

### Q16. How would you autoscale an inference service?

Scale based on signals such as:

* CPU utilization.
* GPU utilization.
* Requests/sec.
* Queue depth.
* Request latency.

For asynchronous inference, **queue depth** can be particularly useful.

### Grill:

> Why isn't GPU utilization alone sufficient?

A model may have high latency despite moderate GPU utilization, or GPU utilization may fluctuate significantly. You need metrics that reflect **user-facing demand and SLA**.

---

# 17. Latency vs Throughput

### Q17. Explain latency and throughput. Why can optimizing one hurt the other?

**Latency:**

Time to process one request.

**Throughput:**

Number of requests processed per unit time.

For example:

```text
Latency = 50 ms/request
Throughput = 2,000 requests/sec
```

Batching can increase throughput but potentially increase individual request latency because requests wait for a batch.

Therefore the optimization target depends on the product requirement.

---

# 18. Availability

### Q18. How would you design a highly available ML inference service?

Use:

* Multiple replicas.
* Load balancing.
* Health checks.
* Autoscaling.
* Multi-zone deployment.
* Model fallback.
* Timeouts.
* Circuit breakers.
* Monitoring.
* Rollback capability.

**Grill:**

> "What happens if the model service goes down?"

Depending on the product:

* Return cached prediction.
* Use simpler fallback model.
* Degrade functionality.
* Queue request.
* Return controlled error.

Never let an ML failure take down the entire application if graceful degradation is possible.

---

# 19. Drift

### Q19. What is data drift vs concept drift?

**Data drift:**

Input distribution changes.

$$
P(X) \rightarrow P'(X)
$$

Example:

Customer demographics change.

**Concept drift:**

Relationship between features and target changes.

$$
P(Y|X) \rightarrow P'(Y|X)
$$

Example:

Fraudsters change their behavior, so the same transaction patterns no longer have the same fraud probability.

### Follow-up:

> Which is harder to detect?

Concept drift is often harder because you need **labels/outcomes** to determine whether the feature-target relationship changed.

---

# 20. Monitoring

### Q20. What would you monitor for a production ML model?

At minimum:

### Infrastructure

* CPU/GPU.
* Memory.
* Errors.
* Throughput.
* Latency.

### Data

* Missing values.
* Feature distributions.
* Data drift.
* Schema changes.

### Model

* Prediction distribution.
* Confidence/calibration.
* Accuracy/F1/etc. when labels arrive.
* Concept drift.

### Business

* Conversion.
* Revenue.
* Fraud loss.
* CTR.
* User satisfaction.

**Critical principle:**

> A model can have healthy infrastructure but still be producing bad predictions.

---

# 21. Retraining

### Q21. When should an ML model be retrained?

Possible triggers:

* Scheduled retraining.
* Performance degradation.
* Data drift.
* Concept drift.
* New labeled data.
* Major business/product changes.

Don't blindly retrain every day.

The trigger should depend on **model stability, label availability, drift and business impact**.

---

# 22. Model Registry

### Q22. What problem does a model registry solve?

A model registry tracks models and their lifecycle:

```text
Model v1
Model v2
Model v3
       ↓
Staging
       ↓
Production
       ↓
Archived
```

It stores things such as:

* Model version.
* Training metadata.
* Metrics.
* Artifacts.
* Dependencies.
* Approval status.

This makes deployment and rollback reproducible.

---

# 23. Canary Deployment

### Q23. What is canary deployment for ML?

Deploy the new model to a **small percentage of traffic** first.

```text
100% traffic
      ↓
95% → Model V1
5%  → Model V2
```

Monitor:

* Errors.
* Latency.
* Model metrics.
* Business metrics.

If healthy → gradually increase traffic.

If bad → rollback.

---

# 24. Shadow Deployment

### Q24. Canary vs shadow deployment?

**Canary:**

New model affects real user responses.

```text
5% → V2
```

**Shadow:**

New model receives production traffic but its predictions **do not affect users**.

```text
Request
 ├── V1 → user response
 └── V2 → logged only
```

Shadow deployment is useful for testing a model safely on realistic production traffic.

---

# 25. Blue-Green Deployment

### Q25. What is blue-green deployment?

Maintain two production environments:

```text
Blue → current version
Green → new version
```

Traffic initially goes to Blue.

After validating Green, switch traffic:

```text
Blue: 0%
Green: 100%
```

Rollback is fast because Blue still exists.

---

# 26. A/B Testing

### Q26. A/B testing vs canary deployment?

**Canary:**

Primarily a safe rollout mechanism.

> "Can this version safely handle production traffic?"

**A/B test:**

Measures whether one version produces **better outcomes**.

```text
Group A → Model V1
Group B → Model V2
```

Compare business metrics statistically.

A model can pass a canary but fail an A/B test if it is stable but doesn't actually improve the business metric.

---

# 27. Rollback

### Q27. When would you roll back an ML model?

Rollback if:

* Prediction quality drops.
* Business KPI deteriorates.
* Latency violates SLA.
* Error rate increases.
* Data pipeline breaks.
* Model produces unsafe outputs.

A good ML deployment system should make rollback **fast and automated where possible**.

---

# P1 — MLOps

# 28. What is MLOps?

### Q28. What does MLOps solve that normal DevOps doesn't?

DevOps primarily manages software lifecycle.

ML adds additional dependencies:

```text
Code
+
Data
+
Features
+
Model
+
Training configuration
```

Therefore MLOps focuses on:

* Reproducible training.
* Experiment tracking.
* Data/model versioning.
* Model registry.
* Deployment.
* Monitoring.
* Retraining.

---

# 29. MLflow

### Q29. What would you use MLflow for?

Mainly:

* Experiment tracking.
* Metrics.
* Parameters.
* Artifacts.
* Model packaging.
* Model registry.

Example:

```text
Experiment
 ↓
Run 1 → XGBoost, depth=5, F1=.82
Run 2 → XGBoost, depth=8, F1=.85
Run 3 → XGBoost, depth=10, F1=.83
 ↓
Register Run 2
 ↓
Deploy
```

---

# 30. Data Versioning

### Q30. Why do you need data versioning?

Suppose Model V7 was trained using a dataset from January.

Six months later, you need to reproduce it.

Without data versioning:

> "Which exact dataset produced this model?"

You may not know.

MLOps should ideally track:

```text
Code version
+
Data version
+
Feature version
+
Hyperparameters
+
Model artifact
```

This enables reproducibility.

---

# 31. Airflow / Data Pipelines

### Q31. What role does Airflow play in an ML pipeline?

Airflow orchestrates workflows:

```text
Extract data
 ↓
Validate
 ↓
Transform
 ↓
Generate features
 ↓
Train
 ↓
Evaluate
 ↓
Register
 ↓
Deploy
```

It handles scheduling, dependencies, retries and workflow monitoring.

**Important:**

Airflow is primarily an **orchestrator**, not the ML training framework itself.

---

# 32. CI/CD for ML

### Q32. What should an ML CI/CD pipeline validate?

### CI

* Unit tests.
* Data validation.
* Feature tests.
* Model code tests.
* Evaluation tests.

### CD

```text
Build
 ↓
Test
 ↓
Train/evaluate
 ↓
Register
 ↓
Deploy staging
 ↓
Canary/shadow
 ↓
Production
```

The key difference from traditional software CI/CD is that **model/data quality also becomes part of deployment validation**.

---

# 33. Docker + Kubernetes

### Q33. Why use Docker and Kubernetes for ML serving?

**Docker** packages:

```text
Code
+
Dependencies
+
Runtime
```

so the model environment is reproducible.

**Kubernetes** manages:

* Containers/pods.
* Scaling.
* Networking.
* Health checks.
* Rolling deployments.
* Resource allocation.

**Follow-up:**

> Why can GPU-based ML workloads be more complicated on Kubernetes?

Because you need GPU scheduling, device plugins, resource allocation, node types and sometimes specialized networking/storage.

---

# 34. Model Serving

### Q34. What are the important concerns when deploying an ML model?

* Model loading time.
* Memory usage.
* Latency.
* Throughput.
* Versioning.
* Concurrency.
* Batch inference.
* Hardware selection.
* Autoscaling.
* Health checks.
* Rollback.

---

# P0 — LLMOps

# 35. What is LLMOps?

### Q35. How is LLMOps different from MLOps?

Think:

> **LLMOps = MLOps + LLM-specific operational problems.**

Traditional ML:

```text
Data → Model → Prediction
```

LLM applications additionally have:

```text
Prompt
+
Model/provider
+
Tokens
+
Tools
+
Retrieval
+
Context
+
Evaluation
+
Safety
```

Therefore LLMOps needs additional monitoring around **prompts, tokens, cost, latency, traces, evaluations and safety**.

---

# 36. Prompt Management

### Q36. Why should prompts be treated like code?

Because changing a prompt can significantly change model behavior.

Therefore track:

```text
Prompt v1
Prompt v2
Prompt v3
```

alongside:

* Model version.
* Parameters.
* Evaluation results.
* Deployment version.

This makes prompt changes reproducible and debuggable.

---

# 37. Model Routing

### Q37. What is model routing?

Instead of sending every request to one model:

```text
                 Request
                    ↓
                  Router
               /    |    \
          Small LLM  Medium  Large
```

The router chooses based on:

* Complexity.
* Cost.
* Latency.
* Capability.
* Privacy.
* Availability.

Example:

Simple classification → cheap model.

Complex reasoning → stronger model.

---

# 38. Model Fallback

### Q38. How would you design model fallback?

```text
Primary model
      ↓
   failure?
    /    \
  No      Yes
  ↓        ↓
Return   fallback
          ↓
        Return
```

Fallback can occur because of:

* Provider outage.
* Rate limit.
* Timeout.
* Model overload.

Important:

> The fallback model should ideally have compatible output/schema behavior.

---

# 39. Token Tracking

### Q39. Why is token tracking important in LLM production systems?

LLM cost is often related to:

* Input tokens.
* Output tokens.
* Model/provider pricing.

Track per:

* User.
* Request.
* Agent.
* Tool.
* Model.
* Application.

This helps identify expensive prompts, retrieval context bloat and inefficient agent loops.

---

# 40. Cost Tracking

### Q40. How would you reduce LLM application cost?

Possible strategies:

* Smaller models for simple tasks.
* Model routing.
* Prompt optimization.
* Reduce unnecessary context.
* Caching.
* Reduce output tokens.
* Batch requests where possible.
* Avoid unnecessary agent loops.
* Use cheaper embeddings.
* Optimize retrieval.

A key principle:

> **Don't optimize only model price; optimize cost per successful task.**

---

# 41. TTFT + Throughput

### Q41. What is TTFT and why does it matter?

**TTFT = Time To First Token.**

It measures how long the user waits before generation starts.

For streaming applications, TTFT strongly affects perceived responsiveness.

Also monitor:

**Tokens/sec** → generation throughput.

You can have:

```text
Low TTFT + slow generation
```

or:

```text
High TTFT + fast generation
```

Both produce different user experiences.

---

# 42. LLM Caching

### Q42. What types of caching can be used in LLM applications?

Examples:

**Response caching**

Same request → reuse answer.

**Embedding caching**

Same text → reuse embedding.

**Prefix caching**

Reuse computation for shared prompt prefixes.

**KV caching**

Reuse attention K/V states during autoregressive decoding.

Each solves a different problem.

---

# 43. LLM Evaluation Pipeline

### Q43. How would you build an automated LLM evaluation pipeline?

```text
Golden dataset
      ↓
Prompt/model version
      ↓
Run evaluation
      ↓
Quality metrics
      ↓
LLM judge / deterministic checks
      ↓
Compare against baseline
      ↓
Pass / Fail
      ↓
Deploy
```

This makes prompt/model changes behave more like software changes with regression testing.

---

# 44. LLM Tracing

### Q44. Why is tracing particularly important for LLM applications?

An LLM request can involve:

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Retriever
 ↓
Tool
 ↓
LLM
 ↓
Tool
 ↓
Final answer
```

A simple request/response log doesn't tell you **where latency, cost or quality problems occurred**.

Tracing lets you inspect:

* LLM calls.
* Prompts.
* Outputs.
* Retrieval.
* Tool calls.
* Latency.
* Tokens.
* Costs.
* Errors.

---

# 45. Provider Abstraction

### Q45. Why would you create a model/provider abstraction layer?

Instead of application code directly depending on one provider:

```text
Application
 ↓
LLM abstraction
 ├── Provider A
 ├── Provider B
 └── Local model
```

Benefits:

* Easy model switching.
* Fallbacks.
* Cost optimization.
* A/B testing.
* Provider outage resilience.

---

# 46. Safety Controls in LLMOps

### Q46. Where should safety controls exist in a production LLM system?

Not only at the prompt.

Use defense in depth:

```text
Input
 ↓
Input guardrails
 ↓
LLM
 ↓
Output guardrails
 ↓
Tool authorization
 ↓
Business rules
 ↓
Monitoring
```

For agents, **tool authorization must exist outside the LLM**.

---

# P0 — Inference Optimization

# 47. Batching

### Q47. Why does batching improve inference throughput?

Instead of processing:

```text
Request 1
Request 2
Request 3
```

individually, process them together:

```text
Batch
 ├── Request 1
 ├── Request 2
 └── Request 3
```

GPUs are highly parallel, so batching can improve hardware utilization.

**Tradeoff:**

Larger batches can increase throughput but also increase latency and memory usage.

---

# 48. Continuous Batching

### Q48. What is continuous batching and why is it important for LLM serving?

Traditional batching waits for a batch to complete.

Continuous batching dynamically adds/removes requests as sequences finish.

```text
Request A ────────────────→ finish
Request B ───────→ finish
Request C ────────────────→
              Request D joins
```

This keeps GPU utilization high despite different generation lengths.

It is particularly important for **autoregressive LLM inference**.

---

# 49. Quantization

### Q49. What is quantization and why does it improve inference?

Quantization represents model weights/activations using lower precision.

Example:

```text
FP32 → FP16 → INT8 → INT4
```

Benefits:

* Lower memory usage.
* Faster inference on supported hardware.
* Potentially higher throughput.
* Larger models can fit on smaller GPUs.

Tradeoff:

> Lower precision can reduce model quality.

The right precision depends on the model, hardware and workload.

---

# 50. KV Cache

### Q50. Why is KV cache both an optimization and a memory bottleneck?

It avoids recomputing previous tokens during decoding.

But it stores K/V tensors for every sequence and token.

Therefore KV-cache memory grows roughly with:

```text
sequence length
× batch size
× number of KV heads
× head dimension
× precision
```

This becomes a major bottleneck for long-context and high-concurrency serving.

---

# 51. Speculative Decoding

### Q51. What is speculative decoding?

Use a **small draft model** to generate several candidate tokens.

Then the larger model verifies them in parallel.

Conceptually:

```text
Small model
 ↓
Draft: "The capital of France is Paris"
 ↓
Large model verifies
 ↓
Accept/reject tokens
```

If many tokens are accepted, the large model generates text faster without changing the target model's intended distribution under the correct algorithm.

**Tradeoff:**

Benefit depends on how well the draft model predicts the target model.

---

# 52. Prefix Caching

### Q52. What is prefix caching?

If many requests share the same prompt prefix:

```text
System prompt
+
Large common context
+
User query
```

the model can reuse computation for the shared prefix rather than recomputing it.

This is especially useful for:

* Long system prompts.
* Repeated documents.
* Shared agent instructions.

---

# 53. Paged Attention

### Q53. What problem does PagedAttention solve?

KV-cache memory can become fragmented and difficult to manage efficiently.

PagedAttention manages KV cache in **fixed-size blocks/pages**, similar conceptually to virtual memory.

Benefits:

* Better GPU memory utilization.
* Less fragmentation.
* Higher serving capacity.
* Better support for dynamic batches.

This is particularly important for high-throughput LLM serving.

---

# 54. Tensor Parallelism

### Q54. What is tensor parallelism?

Split the computation of a **single model layer** across multiple GPUs.

```text
Large layer
     ↓
 ┌───┴───┐
GPU 1   GPU 2
```

Useful when the model doesn't fit efficiently on one GPU.

But GPUs need communication between them, so network bandwidth/latency becomes important.

---

# 55. Model Parallelism

### Q55. Tensor parallelism vs model parallelism?

**Tensor parallelism:**

Split individual tensor/layer computation across GPUs.

**Model/pipeline parallelism:**

Split different parts/layers of the model across GPUs.

Example:

```text
GPU 1 → Layers 1–20
GPU 2 → Layers 21–40
GPU 3 → Layers 41–60
```

The exact terminology can vary across systems, but the key distinction is:

> **Tensor parallelism splits computation within layers; pipeline/model parallelism splits the model itself across devices.**

---

# 56. GPU Utilization

### Q56. GPU utilization is low. Does that automatically mean the model is inefficient?

No.

Low GPU utilization could be caused by:

* CPU bottleneck.
* Data loading.
* Network latency.
* Small batch sizes.
* Memory bandwidth.
* Synchronization.
* Poor kernel utilization.
* Requests arriving too slowly.

You need to profile the **entire inference pipeline**, not just GPU utilization.

---

# 57. Memory Bandwidth

### Q57. Why can LLM decoding be memory-bandwidth bound?

During autoregressive decoding, each new token requires accessing large model weights and KV-cache data.

The computation per token may not be enough to fully hide the cost of moving this data through the memory hierarchy.

Therefore decode performance can depend heavily on:

> **How quickly the GPU can move model/KV data**, not simply how many FLOPs it can perform.

This is one reason quantization and KV-cache optimization are so important.

---

# 58. CPU vs GPU

### Q58. When would you use CPU vs GPU inference?

**GPU:**

* Large neural networks.
* High throughput.
* Low latency.
* Parallel computation.
* LLMs.

**CPU:**

* Small models.
* Low traffic.
* Cost-sensitive workloads.
* Models that don't benefit much from GPU acceleration.

The decision should consider:

```text
Model size
+
QPS
+
Latency SLA
+
Cost
+
Memory
```

---

# 🔥 The 15 questions I'd prioritize

If your goal is **ML Engineer / ML Systems / AI Engineer interviews**, master these first:

### ML System Design

1. **Design an ML system end-to-end from requirements → monitoring → retraining.**
2. **Batch vs online vs asynchronous inference.**
3. **Feature store + training-serving skew + point-in-time correctness.**
4. **Design a scalable model-serving architecture.**
5. **Latency vs throughput and how to scale the system.**
6. **Data drift vs concept drift + monitoring/retraining.**
7. **Canary vs shadow vs blue-green vs A/B testing.**

### MLOps

8. **What does MLOps add beyond normal DevOps?**
9. **MLflow + experiment tracking + model registry + reproducibility.**
10. **Design an ML CI/CD pipeline.**

### LLMOps

11. **Design an LLMOps architecture for production.**
12. **How would you track tokens, cost, latency, TTFT and traces?**
13. **Model routing + fallback + provider abstraction.**

### Inference

14. **Continuous batching + KV cache + paged attention.**
15. **Quantization + speculative decoding + tensor/model parallelism.**

---

# 🔥 The ultimate ML System Design grill question

You should eventually be able to answer this without preparation:

> **"Design a production-grade fraud detection system that processes 10,000 transactions/sec, must return a decision within 100 ms, has highly imbalanced labels, receives delayed fraud labels, and needs to retrain automatically."**

A strong answer should naturally lead you through:

```text
Requirements
     ↓
ML formulation
     ↓
Data ingestion
     ↓
Point-in-time labels
     ↓
Feature engineering
     ↓
Offline feature store
     ↓
Online feature store
     ↓
Model training
     ↓
MLflow / registry
     ↓
Validation
     ↓
Canary deployment
     ↓
Load balancer
     ↓
Online inference
     ↓
Caching
     ↓
Monitoring
 ┌───┴─────────────┐
 ↓                 ↓
Data drift      Model performance
 ↓                 ↓
Retraining ← delayed labels
```

And then the interviewer can attack each component:

> **Why online inference?**
> **Why this model?**
> **Why a feature store?**
> **How do you prevent leakage?**
> **What happens if the feature store is down?**
> **How do you handle 10× traffic?**
> **How do you detect concept drift?**
> **How do you roll back a bad model?**
> **How do you deal with delayed labels?**
> **What happens when the model takes >100 ms?**

That is the level of questioning I'd use to prepare you for **actual ML system-design grilling**, rather than memorizing definitions of Kubernetes, MLflow, Docker, etc.
