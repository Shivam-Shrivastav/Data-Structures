# Deep Learning & Fine-Tuning — Full Answer Key

---

## P0 — Neural Network Fundamentals

### Q1. Forward propagation, explained
Forward propagation is just: multiply, add, squash, repeat.

For one layer:
```
z = Wx + b        (linear step: weighted sum + bias)
a = f(z)           (activation: adds nonlinearity)
```
The output `a` of one layer becomes the input `x` of the next.

```
Input → [Linear → Activation] → [Linear → Activation] → ... → Output
```

**Example:** A 2-layer network predicting house price from size and location does `z1 = W1·x + b1`, `a1 = ReLU(z1)`, then `z2 = W2·a1 + b2` gives the final price.

**Follow-ups**
- **Why multiple layers?** Each layer builds more abstract features from the previous one — like edges → shapes → objects in vision. One layer can only learn simple patterns.
- **Why nonlinear activations?** Without them, stacking layers is mathematically the same as one linear layer (see Q4) — no matter how deep, you'd only ever fit straight lines/planes.
- **What if every layer is linear?** The whole network collapses into a single linear transformation `W_combined·x + b_combined`. Depth becomes pointless.
- **Weights vs biases?** Weights control the strength/direction of each input's influence; the bias shifts the output up or down independent of the input, letting the activation trigger even when inputs are zero.
- **Final layer for regression vs classification?** Regression: no activation (or linear) on the output, since we want raw real numbers. Classification: softmax (multi-class) or sigmoid (binary) to turn outputs into probabilities.

---

### Q2. Backpropagation, mathematically
Backprop finds how much each weight contributed to the error, using the **chain rule**, then walks that gradient backward through the network.

For `L = f(y)` and `y = g(x)`:
```
∂L/∂x = ∂L/∂y · ∂y/∂x
```
Applied layer by layer, gradients flow from the output loss back to the first layer's weights. Then an optimizer nudges each weight opposite the gradient:
```
W ← W − η · ∇W L
```

**Example:** If a small change in a weight in layer 1 barely moves the loss, its gradient is near zero and it barely updates; if it moves the loss a lot, it gets a bigger update.

**Follow-ups**
- **Why the chain rule?** Because the loss depends on early-layer weights only *indirectly*, through several intermediate functions — chain rule is the tool for differentiating composed functions.
- **Computational graph?** A DAG (directed acyclic graph) representing every operation (matrix multiply, add, activation) as a node, so gradients can be computed automatically by walking it backward (autodiff).
- **Forward vs backward pass?** Forward: compute predictions and loss. Backward: compute gradients of the loss w.r.t. every parameter.
- **Why not update during forward pass?** You need the *full* loss value first — you can't know how "wrong" a weight was until you've seen the final error it caused.
- **Why is backprop efficient?** It reuses shared intermediate gradients (dynamic-programming style) instead of recomputing each parameter's effect from scratch — cost is roughly one extra forward pass, not thousands of separate ones.

---

### Q3. What gradient descent is really doing
The gradient `∇θ L` points in the direction of **steepest increase** in loss. So we step in the *opposite* direction:
```
θ_new = θ_old − η · ∇θ L
```
`η` (learning rate) controls step size.

```
loss
 |     \
 |      \___
 |          \___●  ← rolling downhill toward minimum
 |______________\____ θ
```

**Follow-ups**
- **LR too large?** Overshoots the minimum, can diverge or bounce around chaotically.
- **LR too small?** Extremely slow convergence, may get stuck in flat regions.
- **Batch vs stochastic vs mini-batch?** Batch uses the whole dataset per update (stable but slow); stochastic uses 1 sample (fast but noisy); mini-batch uses a small chunk (e.g., 32–512) — a practical middle ground.
- **Why mini-batch preferred for DL?** Good hardware (GPU) parallelism, stable-enough gradients, and the noise actually helps escape shallow local minima.
- **Stuck in local minimum?** In high-dimensional deep nets, true local minima are rare; the bigger issue is saddle points, not local minima.
- **Saddle point?** A point where the gradient is zero but it's a minimum in some directions and a maximum in others — flat and slow to escape, more common than local minima in high dimensions.

---

### Q4. Why nonlinear activations are required
Two stacked linear layers:
```
W2(W1 x) = (W2 W1) x
```
is still just one big linear transform. No amount of stacking linear layers adds expressive power. Nonlinear activations break this, letting the network approximate curves, boundaries, and complex functions.

**Key activations:**
- **Sigmoid:** `σ(x) = 1/(1+e^-x)` → squashes to (0,1); saturates for large |x|.
- **Tanh:** outputs (-1,1), zero-centered (better than sigmoid for hidden layers).
- **ReLU:** `f(x) = max(0,x)` → simple, fast, avoids vanishing gradients for positive inputs.
- **GELU:** smooth, probabilistic version of ReLU; standard in Transformers (BERT, GPT).
- **SwiGLU:** gated variant used in modern LLMs (LLaMA, PaLM) — better performance at similar compute.

**Follow-ups**
- **Why did ReLU get popular?** Cheap to compute, doesn't saturate for positive values, so gradients flow better than sigmoid/tanh in deep nets.
- **Dying ReLU?** If a neuron's input is always negative, its gradient is always 0 → it stops learning permanently ("dead" neuron).
- **Why is sigmoid problematic in deep hidden layers?** Its gradient is tiny except near x=0, so gradients shrink fast across many layers → vanishing gradients.
- **Why GELU in Transformers?** Smoother than ReLU, empirically gives better optimization behavior for large-scale language models.
- **ReLU vs GELU vs SwiGLU?** ReLU = simple/cheap; GELU = smoother, better for large models; SwiGLU = gated (learns which parts of a signal to pass), currently state-of-the-art for LLM feed-forward blocks.

---

### Q5. Choosing a loss function
The loss must match what you're actually trying to optimize.

| Task | Loss |
|---|---|
| Regression | MSE: `(1/n)Σ(y − ŷ)²` |
| Binary classification | Binary cross-entropy: `−[y log p + (1−y) log(1−p)]` |
| Multiclass classification | Cross-entropy over softmax probabilities |

**Follow-ups**
- **Why does MSE penalize outliers heavily?** Error is squared, so a point that's off by 10 contributes 100× more than one off by 1 — outliers dominate the loss.
- **Why cross-entropy for classification?** It directly measures how "surprised" the model is by the true label, gives strong gradients when the model is confidently wrong (unlike MSE on probabilities, which flattens out).
- **Why not use accuracy as a training loss?** Accuracy is not differentiable (it's a step function) — can't compute gradients from it.
- **Gradients when loss saturates?** They shrink toward zero (e.g., sigmoid + wrong confident prediction), slowing learning — this is why cross-entropy pairs well with softmax/sigmoid (their combined gradient stays well-behaved).

---

### Q6. Why weight initialization matters
Bad init → vanishing/exploding gradients, slow convergence, or symmetric neurons that all learn the same thing.

- **Xavier/Glorot:** scales weights based on layer size, good for tanh/sigmoid.
- **He init:** scales larger, designed to keep variance stable through ReLU (which zeroes out half the values).

**Follow-ups**
- **Why not all-zero init?** Every neuron computes the identical gradient and update → they never differentiate ("symmetry problem").
- **Why does zero init cause symmetry?** All neurons in a layer start identical and receive identical gradients, so they stay identical forever.
- **Xavier vs He?** Xavier assumes symmetric activations (tanh); He accounts for ReLU killing half the outputs, so it uses roughly 2× the variance.
- **Weights extremely large?** Activations blow up, gradients explode, training becomes unstable (NaNs are common).

---

### Q7. Dropout and overfitting
During training, dropout randomly zeroes a fraction of activations each step:
```
Full network → randomly drop neurons → train on a different "thinned" subnetwork each step
```
This forces the network to not rely on any single neuron, acting like an ensemble of many subnetworks. At inference, dropout is turned off and activations are rescaled to match training-time expected values.

**Follow-ups**
- **Why disabled at inference?** You want the full network's deterministic best prediction, not a random subset.
- **Too much dropout?** Removes too much signal → underfitting, slow/unstable training.
- **Dropout vs L2?** Dropout is a structural/stochastic regularizer (random subnetworks); L2 directly penalizes large weight magnitudes in the loss. They can be combined.
- **Why less common in modern Transformers?** Large-scale pretraining on massive data already has strong implicit regularization; dropout can even hurt performance at scale, so it's often reduced or dropped for big models.

---

### Q8. What BatchNorm solves
BatchNorm normalizes activations using the mean/variance of the **current mini-batch**, then applies learnable scale/shift:
```
x̂ = (x − μ_B) / √(σ_B² + ε)
y = γx̂ + β
```
This stabilizes activation distributions layer-to-layer, allowing higher learning rates and faster, more stable training.

**Follow-ups**
- **Training vs inference behavior?** Training uses batch statistics; inference uses a running average of mean/variance collected during training (since you may only have 1 sample at inference).
- **Inference statistics?** Fixed running mean/variance accumulated during training.
- **Small batch problem?** Batch statistics become noisy/unreliable with very few samples, hurting normalization quality.
- **BatchNorm in CNNs vs LayerNorm in Transformers?** CNNs typically have large, consistent batch sizes and spatial structure where batch stats work well. Transformers deal with variable sequence lengths and often small/varying batches (esp. at inference, batch=1), where per-example LayerNorm is more stable.

---

### Q9. LayerNorm vs BatchNorm
- **BatchNorm:** normalizes each feature *across the batch*.
- **LayerNorm:** normalizes *across features, within a single example*.

Because LayerNorm doesn't depend on other examples in the batch, it works the same regardless of batch size or sequence length — ideal for sequence models.

**Follow-ups**
- **Why LayerNorm suits variable sequence lengths?** It computes statistics per token/example, independent of how many tokens are in the batch or sequence.
- **LayerNorm vs RMSNorm?** RMSNorm skips mean-centering and only normalizes by root-mean-square magnitude — simpler, cheaper, and used in many modern LLMs (LLaMA) with similar quality.
- **Pre-LN vs Post-LN?** Pre-LN applies normalization *before* the sublayer (attention/FFN); Post-LN applies it *after*. Pre-LN gives more stable gradients for very deep Transformers and is the modern default.

---

### Q10. Adam vs AdamW
**Adam** tracks two moving averages per parameter:
- 1st moment (mean of gradients) → momentum-like direction.
- 2nd moment (mean of squared gradients) → adapts the effective learning rate per parameter.

**AdamW** decouples weight decay from the gradient-based update, applying it directly to the weights instead of mixing it into the adaptive gradient calculation — giving cleaner, more predictable regularization.

**Follow-ups**
- **SGD vs Adam?** SGD uses one fixed learning rate for all parameters (optionally + momentum); Adam adapts the learning rate per parameter, converging faster but sometimes generalizing slightly worse.
- **What is momentum?** Accumulates a running average of past gradients so updates keep moving in a consistent direction, smoothing out noisy steps (like a ball rolling downhill gaining momentum).
- **Why does Adam converge quickly?** Per-parameter adaptive rates mean it naturally takes bigger steps for infrequently-updated/flat directions and smaller steps for steep/noisy ones.
- **What is weight decay?** A penalty that shrinks weights toward zero each step, discouraging overly large weights (a form of L2 regularization).
- **Why isn't Adam's L2 the same as AdamW's decay?** In vanilla Adam, L2 penalty gets folded into the gradient, then divided by the adaptive second-moment term — distorting its effective strength. AdamW applies decay directly to weights, outside that adaptive scaling, so it behaves as intended.

---

### Q11. Learning-rate schedules
A constant LR is rarely optimal: large steps help early exploration but overshoot near convergence.

```
Small LR → Warmup → Peak LR → Gradual decay (cosine/linear/step)
```

**Follow-ups**
- **Why warmup?** Early in training, gradients/activations can be unstable (especially with Adam and large batches); starting small avoids destabilizing updates before things settle.
- **LR too high?** Instability, divergence, loss spikes.
- **LR too low?** Very slow training, may not reach a good minimum in time.
- **Why does scheduling affect generalization?** Decaying LR late in training lets the model settle into a flatter, more stable minimum, which often generalizes better than sharp minima found with a constant high LR.

---

### Q12. Vanishing & exploding gradients
Backprop repeatedly multiplies gradients across layers. If per-layer derivatives are consistently:
```
< 1  → gradients shrink exponentially  → vanishing
> 1  → gradients grow exponentially    → exploding
```

**Fixes:** proper initialization, ReLU-family activations, normalization (BatchNorm/LayerNorm), residual connections, gradient clipping, gated units (LSTM/GRU).

**Follow-up**
- **Why are residual connections useful?** `output = x + F(x)` gives gradients a direct "shortcut" path (`∂output/∂x` includes a clean `1`) back to earlier layers, bypassing the repeated multiplication that causes vanishing gradients — this is what let networks go from ~20 layers to 100+ (ResNet) and made very deep Transformers trainable.

---

## P1 — CNN / RNN

### Q13. How CNNs extract features
A convolutional filter slides across the input, computing local weighted sums (dot products) at each position.

```
edges → textures → shapes → objects   (as you go deeper)
```

**Key concepts:** kernel/filter (the small learnable weight grid), stride (step size while sliding), padding (border handling), channels (depth, e.g. RGB=3), feature maps (filter outputs), pooling (downsampling, e.g. max-pool).

**Follow-ups**
- **Why translation tolerant?** The same filter is applied everywhere, so a detected pattern (e.g., an edge) is recognized regardless of where it appears in the image.
- **Why fewer parameters than fully connected?** A filter has a small fixed number of weights (e.g., 3×3×channels) shared across the *entire* image, instead of a unique weight per pixel pair like a dense layer.
- **What does stride do?** Controls how far the filter moves each step; larger stride = smaller output, less overlap, faster but less detail.
- **Same vs valid padding?** "Same" pads the input so output size matches input size; "valid" uses no padding, so output shrinks each layer.
- **Why deeper layers learn more abstract features?** Each layer's receptive field (region of the original image it "sees") grows, letting later layers combine lower-level patterns into higher-level concepts.

---

### Q14. RNNs — design and problem
RNNs maintain a hidden state updated at each time step:
```
h_t = f(W_x·x_t + W_h·h_{t-1} + b)
```
so each prediction depends on everything seen before. **Problem:** gradients must flow back through *every* time step, so with long sequences they vanish or explode — long-range dependencies are hard to learn.

**Follow-ups**
- **Why can't vanilla RNNs remember long-range info?** Repeated multiplication through many time steps shrinks gradients toward zero, so early inputs get almost no learning signal by the time the error reaches them.
- **Why hard to parallelize?** Each hidden state depends on the previous one — the sequence must be processed step-by-step, unlike Transformers which process all tokens at once via attention.
- **RNN vs Transformer?** RNN: sequential, limited memory, cheap for very long streams but slow to train. Transformer: parallel, attention lets any token directly connect to any other token regardless of distance, but cost grows with sequence length².

---

### Q15. LSTM and long-term dependencies
LSTM adds a **cell state** (a long-term memory highway) plus gates that control what flows through it:

```
Previous memory → Forget gate (drop irrelevant) → Input gate (add new) → Updated memory → Output gate (what to expose)
```
- **Forget gate:** decides what to discard.
- **Input gate:** decides what new info to store.
- **Output gate:** decides what to output as the hidden state.

The cell state gives a much more direct path for gradients than a vanilla RNN's repeated matrix multiplications.

**Follow-ups**
- **Gates mathematically?** Each gate is `sigmoid(W·[h_{t-1}, x_t] + b)`, producing values in (0,1) that act as "how much to let through" multipliers on the cell state or candidate values.
- **Why does the forget gate matter?** It lets the network actively erase outdated information instead of being forced to remember everything, preventing memory clutter.
- **Why better than vanilla RNN?** The cell state's additive updates (rather than repeated multiplicative ones) preserve gradient magnitude over many steps.
- **Why Transformers preferred now?** Full parallelism, better long-range modeling via attention, and they scale better with data/compute than sequential LSTMs.

---

### Q16. GRU vs LSTM
GRU simplifies LSTM: no separate cell state, fewer gates — **update gate** (how much of the past to keep) and **reset gate** (how much past info to forget when computing a new candidate state). Fewer parameters, often comparable performance, usually a bit faster.

**Follow-ups**
- **When choose GRU over LSTM?** Smaller datasets, need faster training/inference, or memory constraints — GRU often matches LSTM performance with less compute.
- **What does the reset gate control?** How much of the previous hidden state to ignore when computing the new candidate hidden state (lets the model "start fresh" when needed).
- **Why aren't GRUs dominant in modern LLMs?** Both GRU and LSTM are sequential and don't parallelize like Transformers, and Transformers scale better with massive data/compute — so the whole recurrent family has been mostly displaced for large language models.

---

## 🔥 Fine-Tuning

### Q17. Full fine-tuning
Updates **every** parameter in a pretrained model on task-specific data.

```
Pretrained model → task data → update ALL weights → fine-tuned model
```
**Pros:** maximum flexibility, can substantially change behavior.
**Cons:** expensive (compute + memory), risk of catastrophic forgetting (losing general capabilities), costly to store a full copy per task.

---

### Q18. Supervised Fine-Tuning (SFT)
Trains the pretrained model on (instruction + input → desired response) pairs using standard next-token cross-entropy loss. This is how a raw "base model" becomes an instruction-following "chat model."

```
Instruction + Input → Desired Response → cross-entropy loss → update weights
```

**Follow-ups**
- **Base vs instruct model?** Base model just predicts likely next tokens from pretraining data (no notion of "following instructions"); instruct model has been SFT'd to respond helpfully to prompts/instructions.
- **What does the dataset look like?** Pairs/triples of (system prompt/instruction, user input, ideal assistant response) — curated to reflect desired tone, correctness, and format.
- **Why does dataset quality matter so much?** The model directly imitates the examples — noisy, wrong, or inconsistent responses get learned just as readily as good ones.
- **Noisy SFT data?** Model can learn incorrect facts, inconsistent style, or degraded reasoning — quality usually matters more than quantity for SFT.

---

### Q19. Parameter-Efficient Fine-Tuning (PEFT)
Instead of updating all weights, PEFT trains a small added/subset of parameters while keeping the base model frozen.

**Examples:** LoRA, adapters, prefix/prompt tuning.
**Benefits:** far less GPU memory, faster training, small artifacts (easy to store/swap many task-specific versions).

---

### Q20. LoRA, mathematically
Freeze the original weight matrix `W`; learn a **low-rank** update instead of a full one:
```
W' = W + BA
```
where `B ∈ R^(d×r)`, `A ∈ R^(r×k)`, and `r ≪ d, k`.

Instead of learning a full `d×k` matrix, you learn two much smaller matrices — drastically fewer trainable parameters.

**Example:** If `W` is 4096×4096 (~16.8M params) and rank `r=8`, `A` and `B` together have only ~65K params to train.

**Follow-ups**
- **Why does low-rank work?** The "direction" a fine-tuning task needs to shift a pretrained model's weights is empirically much lower-dimensional than the full weight space — task adaptation doesn't need full-rank updates.
- **What does rank `r` control?** The expressive capacity of the adaptation — higher rank = more flexible update, more parameters.
- **Rank too small?** Update lacks capacity, underfits the new task.
- **Rank too large?** Approaches full fine-tuning cost/overfitting risk, loses the efficiency benefit.
- **Which layers targeted?** Commonly attention projection matrices (query, key, value, output); sometimes feed-forward layers too.
- **Can LoRA be merged?** Yes — `W' = W + BA` can be computed once and folded into `W`, giving a single dense matrix with zero extra inference latency.

---

### Q21. QLoRA
Combines a **quantized** (low-precision, e.g. 4-bit) frozen base model with **trainable LoRA adapters** kept in higher precision.

```
Quantized frozen base model + Trainable LoRA adapters → Fine-tuned model
```

**Follow-ups**
- **Why does quantizing reduce memory?** Storing weights in 4-bit instead of 16/32-bit cuts memory ~4-8×, letting large models fit on consumer/single GPUs.
- **Are quantized base weights updated?** No — only the small LoRA adapter matrices are trained; the quantized base stays frozen.
- **LoRA vs QLoRA?** LoRA still needs the base model in full/half precision in memory; QLoRA compresses the frozen base further, enabling fine-tuning of much larger models on limited hardware.
- **Tradeoff?** Slight potential quality loss from quantization noise, plus extra compute overhead for dequantizing during the forward/backward pass.

---

### Q22. Adapter layers
Small trainable modules inserted **between** frozen pretrained layers.

```
Frozen layer → Adapter (small trainable bottleneck) → Frozen layer
```

**Follow-ups**
- **Adapter vs LoRA?** Adapters add new sequential modules (extra inference compute/latency); LoRA modifies existing weight matrices in parallel and can be merged in with zero extra latency.
- **Why parameter-efficient?** Adapters are small bottleneck networks (down-project → nonlinearity → up-project), a tiny fraction of the full model's size.
- **Multiple adapters, one base?** Yes — this is a common way to support many tasks/customers from one shared frozen base model, swapping in different adapter weights per task.

---

### Q23. Quantization
Reduces numeric precision of model weights (and sometimes activations):
```
FP32 → FP16 → INT8 → INT4
```
**Benefits:** less memory, faster inference on supported hardware, cheaper deployment. **Tradeoff:** potential accuracy/quality loss.

**Follow-ups**
- **Weight vs activation quantization?** Weight quantization compresses stored parameters; activation quantization also compresses the intermediate values computed during inference — combining both maximizes speed/memory gains but adds more risk to accuracy.
- **PTQ vs QAT?** Post-Training Quantization (PTQ) quantizes an already-trained model (fast, some quality loss); Quantization-Aware Training (QAT) simulates quantization *during* training so the model adapts to it (better quality, more expensive).
- **Why INT4 useful for LLM deployment?** Cuts memory footprint dramatically (4× vs FP16), allowing huge models to run on smaller/cheaper hardware, often with only modest quality loss for well-calibrated methods.
- **Why can quantization hurt accuracy?** Reduced precision means less fine-grained representation of weight values, which can accumulate rounding error, especially in sensitive layers.

---

### Q24. RLHF, high level
Reinforcement Learning from Human Feedback:
```
Pretrained model → SFT → Human preference data → Reward model → RL optimization → Aligned model
```
Humans rank/compare model outputs → a **reward model** learns to predict human preference scores → the LLM is optimized (typically via PPO) to produce outputs the reward model scores highly.

**Follow-ups**
- **Why SFT before RLHF?** RL is much more effective at *refining* an already-reasonable policy than teaching from scratch; SFT gives the model baseline instruction-following ability first.
- **What's a reward model?** A separate model trained on human comparison data (A vs B, which is better) to output a scalar "quality" score for any given response.
- **What problem does RLHF solve?** Aligns model outputs with subjective human preferences (helpfulness, tone, safety) that are hard to specify with a simple loss function.
- **Why can it be unstable/expensive?** RL training (e.g., PPO) is sensitive to hyperparameters, needs careful reward model calibration, and requires running the policy, reward model, and reference model together — computationally heavy.
- **Reward hacking?** The policy finds ways to score highly on the reward model without actually being "good" (e.g., excessive verbosity, flattery) — exploiting reward model blind spots rather than genuinely improving.

---

### Q25. DPO vs RLHF
Direct Preference Optimization skips the separate reward model and RL loop entirely — it directly optimizes the model on preference pairs using a closed-form loss derived from the same objective RLHF is trying to approximate.
```
Prompt → (Chosen response, Rejected response) → DPO loss → Preferred behavior
```

**Follow-ups**
- **Why need preference pairs?** The loss compares the model's relative likelihood of the chosen vs rejected response — it needs both to define "better than."
- **RLHF vs DPO?** RLHF: reward model + RL loop (complex, unstable, but flexible). DPO: single supervised-style loss on preference pairs (simpler, more stable, cheaper) — often achieves similar alignment quality.
- **Does DPO need an RL loop?** No — it's trained with standard gradient descent, no sampling/reward-model rollout needed.
- **Role of the reference model?** DPO's loss includes a frozen copy of the pre-DPO model as a reference, to keep the fine-tuned model from drifting too far from it (regularization, similar in spirit to RLHF's KL penalty).

---

### Q26. Preference datasets
```
Prompt → Chosen response (good) + Rejected response (bad)
```
**Example:**
- Prompt: "Explain photosynthesis."
- Chosen: clear, accurate, well-structured explanation.
- Rejected: vague or factually wrong explanation.

**Follow-ups**
- **How to collect it?** Human annotators compare model outputs pairwise (or rank multiple candidates); increasingly, synthetic preferences from a strong "judge" model are also used.
- **Human vs synthetic preferences?** Human: higher quality/nuance, but slow and expensive. Synthetic (model-generated): scalable and cheap, but can inherit the judge model's own biases/blind spots.
- **Annotator biases?** Length bias (favoring longer answers), style/formatting bias, agreement with confident-sounding but wrong answers, cultural/political leanings.
- **Noisy preference labels?** The model learns a blurrier, less reliable notion of "better," which can degrade alignment quality or introduce inconsistent behavior.

---

## 🔥 The Most Important Fine-Tuning Question

### Q27. RAG vs Fine-Tuning
**Use RAG** when the model needs access to **external, changing, or private** knowledge.
```
Question → Retrieve latest documents → LLM answers using retrieved context
```
Example: "Answer using our latest HR policy" — you don't want to bake a policy that changes monthly into model weights.

**Use fine-tuning** when you need to change **behavior**: style, task performance, output format, specialized skills.

**Key distinction:**
- RAG changes *what the model can access*.
- Fine-tuning changes *how the model behaves*.

---

### Q28. RAG + Fine-Tuning together
Yes, and it's common in production systems:
```
Fine-tuned model (knows HOW to answer) + RAG (provides WHAT to answer with) → Specialized + current/private answers
```

**Grill: RAG retrieves the right document but the model still answers badly — do you fine-tune?**
Not automatically. First diagnose *where* the failure actually is:
- Prompting/instructions unclear?
- Context construction (chunking, formatting) poor?
- Model reasoning over the context weak?
- Grounding (ignoring the retrieved doc) failing?
- Output formatting wrong?
- Retrieval itself actually wrong despite appearing right?

Only fine-tune if the root cause is genuinely model capability/behavior — not a fixable prompting, retrieval, or context-construction issue.

---

### Q29. Prompting vs Fine-Tuning vs RAG

| Problem | Preferred approach |
|---|---|
| Simple behavior change | Prompting |
| Need current/private knowledge | RAG |
| Consistent specialized behavior | Fine-tuning |
| Specific output format | Prompting / structured output |
| Repeated task-specific behavior | Fine-tuning |
| Knowledge changes frequently | RAG |
| Need both behavior + knowledge | Fine-tuning + RAG |

**Strong interview answer:** Start with the simplest solution that satisfies the requirement — prompting is cheapest, RAG adds external knowledge, fine-tuning changes learned behavior. Escalate only as needed.

---

## 🔥 High-Value Grill Questions — Quick Answers

- **Why do neural networks need nonlinear activations?** Stacked linear layers collapse into one linear function (Q4) — nonlinearity is what lets a network approximate complex, non-straight-line relationships.
- **Explain backprop via chain rule.** Loss depends on early weights only through a chain of intermediate functions; chain rule lets you compute `∂L/∂weight` by multiplying local derivatives backward through that chain (Q2).
- **What causes vanishing/exploding gradients, and fixes?** Repeated multiplication of derivatives <1 or >1 across layers/time steps (Q12); fixed via good init, ReLU-family activations, normalization, residual connections, gradient clipping, gated units.
- **Why do init, normalization, residuals help?** They all keep activation and gradient magnitudes in a healthy, stable range as signal passes through many layers — preventing vanishing/exploding effects.
- **Adam vs AdamW vs SGD — when?** SGD(+momentum): often best final generalization, common for CNNs with careful tuning. Adam: fast convergence, good default for Transformers/NLP. AdamW: preferred whenever weight decay/regularization matters (virtually all modern large-model training) since it decouples decay properly.
- **CNN vs RNN vs Transformer — problem each solves?** CNN: local spatial patterns (images) via shared filters. RNN: sequential/temporal dependencies via recurrent state. Transformer: long-range dependencies + full parallelism via self-attention.
- **Why did Transformers replace RNN/LSTM for NLP?** Full parallel training (no step-by-step dependency), attention directly connects any two tokens regardless of distance, and they scale much better with data and compute.
- **Why does LSTM beat vanilla RNN on long dependencies?** The additive cell-state path plus gating avoids the repeated multiplicative gradient shrinkage that plagues vanilla RNNs (Q15).
- **Full fine-tuning vs PEFT?** Full: max flexibility, high cost, forgetting risk. PEFT (e.g., LoRA): trains a tiny fraction of parameters, cheap, easy to maintain many task variants, usually near-comparable quality.
- **LoRA vs QLoRA?** QLoRA additionally quantizes the frozen base model to 4-bit, letting you fine-tune much larger models on limited GPU memory, at a small extra compute/quality cost (Q20–21).
- **RLHF vs DPO?** RLHF trains a separate reward model + runs RL (flexible, complex, unstable); DPO optimizes directly on preference pairs with a supervised-style loss (simpler, cheaper, more stable) (Q24–25).
- **What makes a good preference dataset?** Clear, consistent, low-bias comparisons that isolate genuine quality differences (not length or style superficialities), ideally cross-checked between multiple annotators or a calibrated judge model.
- **RAG vs fine-tuning — when combine?** RAG = what the model knows; fine-tuning = how it behaves. Combine when you need both current/private knowledge *and* consistent specialized behavior (Q27–28).

---

## 🔥 The Ultimate Interviewer Grill Chain — Worked Answer

**Prompt: "You have a 7B open-source LLM and need to specialize it for a company's customer-support application. What would you do?"**

Don't jump straight to "I'll fine-tune it." Reason through the decision tree first:

```
Requirement
    ↓
Is the problem knowledge or behavior?
    ↓
┌───────────────┬────────────────┐
↓               ↓                ↓
Knowledge      Behavior         Both
↓               ↓                ↓
RAG          Prompt/SFT      RAG + FT
                ↓
          PEFT / LoRA?
                ↓
         QLoRA if GPU-constrained
                ↓
       Build evaluation dataset
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

**Step-by-step reasoning a strong candidate gives:**

1. **Classify the problem.** Does support quality fail because the model doesn't *know* current product/policy info (→ knowledge gap → RAG), or because it doesn't *respond* the way support agents should — tone, escalation rules, formatting (→ behavior gap → fine-tuning)? Most real support bots need **both**.
2. **Try the cheapest fix first.** Good prompting/system instructions often solve simple behavior issues without any training.
3. **If knowledge is missing:** wire up RAG over the company's knowledge base/tickets/policies — this keeps answers current without retraining.
4. **If behavior needs to change (style, consistent structured responses, domain-specific handling):** fine-tune, and default to **LoRA/PEFT** first, not full fine-tuning — cheaper, faster, easier to iterate and maintain.
5. **If GPU memory is limited:** use **QLoRA** (quantized frozen base + LoRA adapters) to fine-tune the 7B model on modest hardware.
6. **Build a proper SFT dataset** from real (or carefully synthesized) support conversations showing the desired response style and correctness.
7. **If you need finer preference alignment** (e.g., "prefer concise, empathetic responses over verbose ones") beyond what SFT captures, add a **DPO** stage on preference pairs.
8. **Evaluate offline** before deployment: held-out support queries, human or LLM-judge grading, regression checks against known-good answers.
9. **Run safety evaluation:** check for hallucinated policy claims, PII handling, tone under abusive input, refusal behavior for out-of-scope requests.
10. **Deploy and monitor:** track live quality (thumbs up/down, escalation rates, hallucination reports), and set up a feedback loop to catch drift or emerging failure modes.

**Follow-up drills, answered:**

- **Why RAG instead of fine-tuning (for knowledge)?** Company policies/product info change frequently; baking them into weights would need constant retraining and risks stale/incorrect answers. RAG keeps knowledge swappable and current (Q27).
- **Why LoRA instead of full fine-tuning?** Full fine-tuning of a 7B model needs a lot of GPU memory and risks catastrophic forgetting of general ability; LoRA trains a tiny fraction of parameters, is cheap to iterate on, and adapters can be swapped/merged easily (Q20).
- **Why QLoRA?** If GPU budget is limited (e.g., single consumer/enterprise GPU rather than a multi-GPU cluster), quantizing the frozen base to 4-bit while training LoRA adapters makes fine-tuning a 7B model feasible without heavy infrastructure (Q21).
- **What rank would you choose for LoRA?** Start modest (commonly r=8–16) for a narrow behavior-adaptation task like support tone/format; increase only if evaluation shows the model is underfitting the desired behavior (Q20).
- **Which layers would you apply LoRA to?** Typically the attention projections (query/key/value/output); optionally extend to feed-forward layers if the attention-only adapters underfit.
- **How would you construct your SFT dataset?** Curate real support transcripts (or synthetic ones reviewed by support experts) covering common intents, edge cases, and correct escalation behavior; prioritize quality and consistency over sheer volume (Q18).
- **How would you prevent catastrophic forgetting?** Use PEFT (frozen base preserves general knowledge) rather than full fine-tuning, keep the SFT dataset focused but not so narrow it overwrites general reasoning, and evaluate on general benchmarks alongside the support-specific ones.
- **How would you evaluate whether fine-tuning helped?** Compare fine-tuned vs base model on a held-out support-query set using human or calibrated LLM-judge grading, track task-specific metrics (resolution rate, tone adherence, format compliance), and check for regressions on general capability tests.
- **Why DPO instead of RLHF?** DPO gets similar preference-alignment benefits without needing to train a separate reward model and run an unstable RL loop — simpler, cheaper, and easier to debug for a well-scoped use case like support tone (Q25).
- **What if RAG retrieves the correct context but the model still answers wrong?** Don't default to fine-tuning — first check whether the failure is in context construction (formatting/length), instruction clarity, or the model's reasoning over the given context (Q28).
- **How do you know if the problem is retrieval or the model?** Manually inspect failing cases: if the correct document *is* in the retrieved context and the model still gets it wrong, it's a model/grounding issue; if the correct document is missing or ranked low, it's a retrieval issue (fix chunking, embeddings, or ranking, not the model).