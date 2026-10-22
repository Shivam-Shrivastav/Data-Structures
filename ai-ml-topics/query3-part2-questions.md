Absolutely. For **Deep Learning + Fine-Tuning**, I’d keep the same philosophy as before: relatively few primary questions, but each should have the **technical follow-ups an interviewer can use to drill you**.

I’ll cover **every topic and subtopic you listed**, with extra emphasis on the things most relevant to modern LLM/AI interviews.

# Priority 18 — Deep Learning

## P0 — Neural Network Fundamentals

### 1. Explain a neural network mathematically from input to prediction.

**Q1. What happens during forward propagation in a neural network?**

For a layer:

$$
z = Wx+b
$$

then:

$$
a=f(z)
$$

where \(f\) is an activation function.

For multiple layers, the output of one layer becomes the input to the next.

```text id="nnbk1"
Input
 ↓
Linear transformation
 ↓
Activation
 ↓
Linear transformation
 ↓
Activation
 ↓
...
 ↓
Output
```

**Follow-ups:**

* Why do we need multiple layers?
* Why do we need nonlinear activation functions?
* What happens if every layer is linear?
* What is the difference between weights and biases?
* How does the final layer differ for regression vs classification?

---

# 2. Backpropagation

### Q2. Explain backpropagation mathematically.

Backpropagation calculates how much each parameter contributed to the final loss using the **chain rule**.

For:

$$
L=f(y),\quad y=g(x)
$$

we calculate:

$$
\frac{\partial L}{\partial x}
=
\frac{\partial L}{\partial y}
\frac{\partial y}{\partial x}
$$

The gradients propagate backward from the output toward earlier layers.

Then an optimizer updates parameters:

$$
W \leftarrow W-\eta\nabla_W L
$$

### Follow-ups

* Why is the chain rule required?
* What is a computational graph?
* What is the difference between forward and backward pass?
* Why don't we update weights during the forward pass?
* Why is backpropagation computationally efficient compared with calculating each parameter's effect independently?

---

# 3. Gradient Descent

### Q3. What exactly is gradient descent doing?

The gradient tells us the direction of **steepest increase** of the loss.

Therefore, we move in the opposite direction:

$$
\theta_{new}=\theta_{old}-\eta\nabla_\theta L
$$

where:

* \(\theta\) = model parameters
* \(\eta\) = learning rate.

### Follow-ups

* What happens if learning rate is too large?
* What happens if it's too small?
* Batch vs stochastic vs mini-batch gradient descent?
* Why is mini-batch generally preferred for deep learning?
* Can gradient descent get stuck in a local minimum?
* What is a saddle point?

---

# 4. Activation Functions

### Q4. Why do neural networks need nonlinear activation functions?

Without nonlinear activations:

$$
W_2(W_1x)=W_2W_1x
$$

which is still just a **linear transformation**.

So regardless of how many linear layers we stack, the network remains equivalent to one linear layer.

Nonlinear activations allow neural networks to model complex relationships.

### Know deeply:

**Sigmoid**

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

**Tanh**

Outputs between -1 and 1.

**ReLU**

$$
f(x)=\max(0,x)
$$

**GELU**

Common in Transformers.

**SwiGLU**

Common in modern LLM architectures.

### Follow-ups

* Why did ReLU become popular?
* What is the dying ReLU problem?
* Why is sigmoid problematic in deep hidden layers?
* Why is GELU common in Transformers?
* ReLU vs GELU vs SwiGLU?

---

# 5. Loss Functions

### Q5. How do you choose a loss function?

The loss should represent the learning objective.

Common examples:

**Regression**

$$
MSE=\frac1n\sum(y-\hat y)^2
$$

**Binary classification**

Binary cross-entropy:

$$
-[y\log p+(1-y)\log(1-p)]
$$

**Multiclass classification**

Cross-entropy over class probabilities.

### Follow-ups

* Why does MSE heavily penalize outliers?
* Why is cross-entropy preferred for classification?
* Why not use accuracy as a training loss?
* What happens to gradients when the loss saturates?

---

# 6. Weight Initialization

### Q6. Why is weight initialization important?

Bad initialization can cause:

* Vanishing gradients.
* Exploding gradients.
* Very slow convergence.
* Symmetry between neurons.

Common approaches:

**Xavier/Glorot initialization**

Useful for activations such as tanh.

**He initialization**

Designed for ReLU-like activations.

The initialization tries to maintain reasonable activation/gradient variance as information moves through the network.

### Follow-ups

* Why shouldn't all weights be initialized to zero?
* Why can zero initialization cause symmetry?
* Xavier vs He initialization?
* What happens if weights are extremely large?

---

# 7. Regularization + Dropout

### Q7. How does dropout reduce overfitting?

During training, dropout randomly sets a subset of activations to zero.

```text id="drop1"
Neural network
 ↓
Randomly drop neurons
 ↓
Train on different subnetworks
```

This prevents the model from relying too heavily on specific neurons and acts as a form of regularization.

During inference, dropout is disabled and activations are appropriately scaled.

### Follow-ups

* Why isn't dropout normally used during inference?
* Why can too much dropout cause underfitting?
* Dropout vs L2 regularization?
* Why can dropout be less common in some modern Transformer architectures?

---

# 8. BatchNorm

### Q8. What problem does Batch Normalization solve?

BatchNorm normalizes activations using statistics computed from the mini-batch, followed by learnable scale and shift parameters.

Conceptually:

$$
\hat{x}=\frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
$$

then:

$$
y=\gamma\hat{x}+\beta
$$

It can stabilize and accelerate training.

### Follow-ups

* Why does BatchNorm behave differently during training and inference?
* What statistics are used during inference?
* Why can very small batch sizes be problematic?
* Why is BatchNorm common in CNNs but LayerNorm more common in Transformers?

---

# 9. LayerNorm

### Q9. How is LayerNorm different from BatchNorm?

**BatchNorm:**

Normalizes using statistics across the batch for each feature/channel.

**LayerNorm:**

Normalizes across features within an individual example.

This makes LayerNorm much less dependent on batch size and is therefore well suited to sequence models and Transformers.

### Follow-ups

* Why does LayerNorm work well with variable sequence lengths?
* LayerNorm vs RMSNorm?
* Pre-LN vs Post-LN Transformer?

---

# 10. Adam vs AdamW

### Q10. Explain Adam and why AdamW is preferred for many modern models.

Adam combines:

* Momentum-like first-moment tracking.
* Second-moment tracking of squared gradients.

It adapts the learning rate for individual parameters.

AdamW modifies how **weight decay** is applied, decoupling weight decay from the gradient update.

This makes regularization behavior more controlled.

### Follow-ups

* SGD vs Adam?
* What is momentum?
* Why does Adam converge quickly?
* What is weight decay?
* Why isn't Adam's L2 regularization exactly equivalent to AdamW's weight decay?

---

# 11. Learning-Rate Schedules

### Q11. Why don't we always use a constant learning rate?

A large learning rate can help make rapid progress initially but may be too aggressive near convergence.

Common strategies:

* Warmup.
* Cosine decay.
* Step decay.
* Linear decay.

For Transformer training, a common pattern is:

```text id="lr01"
Small LR
   ↓
Warmup
   ↓
Peak LR
   ↓
Gradual decay
```

### Follow-ups

* Why is warmup useful?
* What happens if learning rate is too high?
* What happens if it's too low?
* Why can learning-rate scheduling affect generalization?

---

# 12. Vanishing & Exploding Gradients

### Q12. Why do gradients vanish or explode?

During backpropagation, gradients are repeatedly multiplied through layers.

If derivatives are mostly:

$$
<1
$$

gradients can shrink exponentially → **vanishing gradients**.

If they're mostly:

$$
>1
$$

they can grow exponentially → **exploding gradients**.

Solutions include:

* Proper initialization.
* ReLU-like activations.
* Normalization.
* Residual connections.
* Gradient clipping.
* LSTM/GRU for recurrent networks.

### Follow-up:

> Why are residual connections particularly useful?

They provide a more direct gradient path through deep networks.

---

# P1 — CNN / RNN

## 13. CNN

### Q13. Explain how a CNN extracts features from an image.

A convolutional filter slides across the input and computes local weighted combinations.

Early layers may detect:

```text id="cnn01"
edges
 ↓
textures
 ↓
shapes
 ↓
objects
```

Important concepts:

* Kernel/filter.
* Stride.
* Padding.
* Channels.
* Feature maps.
* Pooling.

### Follow-ups

* Why are CNNs translation tolerant?
* Why does convolution reduce parameter count compared with a fully connected layer?
* What does stride do?
* Same vs valid padding?
* Why do deeper CNN layers learn more abstract features?

---

# 14. RNN

### Q14. Why were RNNs designed for sequential data, and what problem do they have?

An RNN maintains a hidden state:

$$
h_t=f(W_xx_t+W_hh_{t-1}+b)
$$

So information from previous tokens influences the current prediction.

Problem:

> Gradients must propagate through many time steps.

This causes vanishing/exploding gradients, making long-range dependencies difficult to learn.

### Follow-ups

* Why can't vanilla RNNs remember information from very long sequences?
* Why are RNNs sequential and difficult to parallelize?
* How does an RNN differ from a Transformer?

---

# 15. LSTM

### Q15. How does LSTM solve the long-term dependency problem?

LSTM introduces a **cell state** and gates controlling information flow.

Main gates:

* Forget gate.
* Input gate.
* Output gate.

Conceptually:

```text id="lstm01"
Previous memory
      ↓
Forget old information
      ↓
Add relevant new information
      ↓
Updated memory
      ↓
Output
```

The cell state provides a relatively direct path for information and gradients.

### Follow-ups

* Explain each gate mathematically.
* Why does the forget gate matter?
* Why is LSTM better than vanilla RNN for long dependencies?
* Why are Transformers generally preferred now?

---

# 16. GRU

### Q16. GRU vs LSTM?

GRU simplifies the LSTM architecture.

It primarily uses:

* Update gate.
* Reset gate.

GRUs have fewer parameters and can be faster while often achieving comparable performance.

### Follow-ups

* Why might you choose GRU over LSTM?
* What information does the reset gate control?
* Why aren't GRUs dominant for modern LLMs?

---

# 🔥 Fine-Tuning

# 17. Full Fine-Tuning

### Q17. What does full fine-tuning mean?

Full fine-tuning updates **all model parameters** using a task/domain-specific dataset.

```text id="ft01"
Pretrained model
       ↓
Training data
       ↓
Update all weights
       ↓
Fine-tuned model
```

Advantages:

* Maximum flexibility.
* Can substantially adapt the model.

Disadvantages:

* Expensive.
* High GPU/memory requirements.
* Risk of catastrophic forgetting.
* Maintaining multiple fine-tuned copies is expensive.

---

# 18. SFT

### Q18. What is Supervised Fine-Tuning?

SFT trains a pretrained model using examples of desired behavior:

```text id="sft01"
Instruction
    +
Input
    ↓
Desired response
```

The model learns to generate the target response using standard next-token prediction/cross-entropy loss.

SFT is commonly used to turn a pretrained base model into an instruction-following model.

### Follow-ups

* Base model vs instruct model?
* What does the training dataset look like?
* Why does dataset quality matter so much?
* What happens if your SFT dataset contains noisy responses?

---

# 19. PEFT

### Q19. What is Parameter-Efficient Fine-Tuning?

PEFT updates only a **small subset of parameters** rather than the entire model.

Examples:

* LoRA.
* Adapters.
* Prefix/prompt tuning.

Benefits:

* Lower GPU memory.
* Faster training.
* Smaller trainable parameter set.
* Easier to maintain multiple task-specific adaptations.

---

# 20. LoRA

### Q20. Explain LoRA mathematically.

Instead of directly updating a large weight matrix \(W\), LoRA freezes \(W\) and learns a low-rank update:

$$
W'=W+BA
$$

where:

$$
B\in R^{d\times r},\quad A\in R^{r\times k}
$$

and:

$$
r\ll d,k
$$

So instead of learning all parameters in \(W\), we learn the much smaller matrices \(A\) and \(B\).

### Follow-ups

* Why does low-rank adaptation work?
* What does rank \(r\) control?
* What happens if rank is too small?
* What happens if rank is too large?
* Which Transformer layers are typically targeted by LoRA?
* Can LoRA adapters be merged into the base model?

---

# 21. QLoRA

### Q21. What is QLoRA and how is it different from LoRA?

QLoRA combines:

> **Quantized base model + LoRA adapters**

The base model is loaded in low precision, while LoRA parameters remain trainable.

This significantly reduces GPU memory requirements.

Conceptually:

```text id="qlo01"
Quantized frozen model
        +
Trainable LoRA adapters
        ↓
Fine-tuned model
```

### Follow-ups

* Why does quantizing the base model reduce memory?
* Are the quantized base weights updated?
* LoRA vs QLoRA?
* What tradeoff does QLoRA introduce?

---

# 22. Adapters

### Q22. What are adapter layers?

Adapters are small trainable modules inserted into a pretrained network while most of the original model remains frozen.

```text id="adp01"
Transformer
 ↓
Frozen layers
 ↓
Adapter
 ↓
Frozen layers
```

They allow task-specific behavior without maintaining a fully fine-tuned model.

### Follow-ups

* Adapter vs LoRA?
* Why are adapters parameter-efficient?
* Can multiple adapters be used with one base model?

---

# 23. Quantization

### Q23. What is quantization in fine-tuning/inference?

Quantization reduces numerical precision.

For example:

```text id="quant01"
FP32 → FP16 → INT8 → INT4
```

Benefits:

* Lower memory.
* Faster inference on compatible hardware.
* Lower deployment cost.

Tradeoff:

> Potential loss in model quality.

### Follow-ups

* Weight vs activation quantization?
* PTQ vs QAT?
* Why is INT4 particularly useful for LLM deployment?
* Why can quantization affect accuracy?

---

# 24. RLHF

### Q24. Explain RLHF at a high level.

RLHF = **Reinforcement Learning from Human Feedback**.

Typical pipeline:

```text id="rlhf01"
Pretrained model
      ↓
SFT
      ↓
Human preference data
      ↓
Reward model
      ↓
RL optimization
      ↓
Aligned model
```

The reward model learns to predict which outputs humans prefer.

The language model is then optimized to produce outputs with higher predicted reward.

### Follow-ups

* Why is SFT usually done before RLHF?
* What is a reward model?
* What problem does RLHF solve?
* Why can RLHF be unstable/expensive?
* What is reward hacking?

---

# 25. DPO

### Q25. What is DPO and why is it attractive compared with RLHF?

DPO = **Direct Preference Optimization**.

Instead of explicitly training a reward model and then running an RL algorithm, DPO directly optimizes the model using preference pairs:

```text id="dpo01"
Prompt
 ↓
Chosen response
Rejected response
 ↓
DPO training
 ↓
Preferred behavior
```

This simplifies the alignment pipeline.

### Follow-ups

* Why does DPO need preference pairs?
* RLHF vs DPO?
* Does DPO require an RL loop?
* What is the role of the reference model?

---

# 26. Preference Dataset

### Q26. What does a preference dataset look like?

Typically:

```text id="pref01"
Prompt
   ↓
Chosen response
Rejected response
```

Example:

```text
Prompt: Explain photosynthesis.

Chosen:
Clear, correct, concise explanation.

Rejected:
Incorrect explanation.
```

The training process learns to assign higher preference to the chosen response.

### Follow-ups

* How would you collect preference data?
* Human preferences vs synthetic preferences?
* What biases can annotators introduce?
* What happens if preference labels are noisy?

---

# 🔥 The Most Important Fine-Tuning Question

# 27. RAG vs Fine-Tuning

### Q27. When should you use RAG instead of fine-tuning?

This is **one of the most important questions in the entire GenAI interview syllabus.**

Use **RAG** when you need the model to access **external, changing or private knowledge**.

Example:

> "Answer questions using our company's latest HR policies."

You generally don't want to encode those policies into model weights.

Use:

```text id="ragft01"
Question
 ↓
Retrieve latest documents
 ↓
LLM
```

Use **fine-tuning** when you want to change the model's **behavior, style, task performance or output format**.

Examples:

* Specific classification behavior.
* Domain-specific response style.
* Consistent formatting.
* Specialized task behavior.

### The key distinction:

> **RAG changes what the model can access.**
> **Fine-tuning changes how the model behaves.**

---

# 28. RAG + Fine-Tuning Together

### Q28. Can you use RAG and fine-tuning together?

Absolutely.

For example:

```text id="both01"
Fine-tuned model
       +
RAG
       ↓
Specialized behavior
+
Current/private knowledge
```

Fine-tuning can teach the model **how to answer**, while RAG provides **what information to use**.

### Grill:

> If your RAG system retrieves the correct document but the model still produces a bad answer, would you fine-tune?

Not automatically.

First determine whether the problem is:

* Prompting.
* Context construction.
* Model reasoning.
* Grounding.
* Output formatting.
* Retrieval.

Fine-tuning should be used when the problem is actually **model behavior/capability**, not simply because the RAG system is failing.

---

# 29. Fine-Tuning vs Prompt Engineering

### Q29. When would you use prompting, fine-tuning or RAG?

Think:

| Problem                         | Preferred approach            |
| ------------------------------- | ----------------------------- |
| Simple behavior change          | Prompting                     |
| Need current/private knowledge  | RAG                           |
| Consistent specialized behavior | Fine-tuning                   |
| Specific output format          | Prompting / structured output |
| Repeated task-specific behavior | Fine-tuning                   |
| Knowledge changes frequently    | RAG                           |
| Need both behavior + knowledge  | Fine-tuning + RAG             |

**Strong interview answer:**

> Start with the simplest solution that satisfies the requirement. Prompting is cheapest, RAG adds external knowledge, and fine-tuning changes learned behavior.

---

# 🔥 High-Value Deep Learning Grill Questions

These are the questions I'd make sure you can answer **without memorized definitions**:

### Neural networks

1. **Why do neural networks need nonlinear activation functions?**
2. **Explain backpropagation using the chain rule.**
3. **What causes vanishing/exploding gradients and how do you fix them?**
4. **Why do initialization, normalization and residual connections help training?**
5. **Adam vs AdamW vs SGD — when would you choose each?**

### Architecture

6. **CNN vs RNN vs Transformer — what problem does each solve?**
7. **Why did Transformers largely replace RNN/LSTM architectures for NLP?**
8. **Why does LSTM handle long-term dependencies better than vanilla RNN?**

### Fine-tuning

9. **Full fine-tuning vs PEFT.**
10. **Explain LoRA mathematically.**
11. **LoRA vs QLoRA.**
12. **RLHF vs DPO.**
13. **What makes a good preference dataset?**
14. **RAG vs fine-tuning — and when would you combine them?**

---

# 🔥 The ultimate interviewer grill chain

I'd particularly practice this sequence:

> **"You have a 7B open-source LLM and need to specialize it for a company's customer-support application. What would you do?"**

A strong answer shouldn't immediately say **"I'll fine-tune it."**

The interviewer will expect you to reason:

```text id="grill01"
Requirement
    ↓
Is the problem knowledge or behavior?
    ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Knowledge      Behavior       Both
 ↓               ↓                ↓
RAG          Prompt/SFT      RAG + FT
                ↓
           PEFT / LoRA?
                ↓
          QLoRA if GPU
          constraints
                ↓
       Evaluation dataset
                ↓
        SFT / DPO if needed
                ↓
       Offline evaluation
                ↓
       Safety evaluation
                ↓
          Deployment
                ↓
         Monitoring
```

Then the interviewer can drill:

> **Why RAG instead of fine-tuning?**

> **Why LoRA instead of full fine-tuning?**

> **Why QLoRA?**

> **What rank would you choose for LoRA?**

> **Which layers would you apply LoRA to?**

> **How would you construct your SFT dataset?**

> **How would you prevent catastrophic forgetting?**

> **How would you evaluate whether fine-tuning actually helped?**

> **Why DPO instead of RLHF?**

> **What if the model gets the correct retrieved context but still gives incorrect answers?**

> **How do you know whether the problem is retrieval or the model?**

If you can handle that chain technically, you'll cover a **very large portion of the practical Deep Learning + Fine-Tuning interview surface area** without needing to memorize dozens of isolated questions.
