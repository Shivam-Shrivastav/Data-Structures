# LLM & RAG Interview Prep — Answers

---

## 1. Tokenization

### Q1. What is tokenization, and why not just use characters or whole words?
Tokenization breaks text into smaller units (tokens) the model can map to numbers. Characters alone would make sequences very long and force the model to learn spelling from scratch before it can learn meaning. Whole words alone would blow up the vocabulary size and still fail on any word not seen during training. Subword tokenization is the middle ground — common words stay as one token, rare or unseen words get split into smaller known pieces.

- **BPE (Byte Pair Encoding):** starts with individual characters/bytes and repeatedly merges the most frequent adjacent pair into a new token, building up a vocabulary of common subwords, whole words, and word fragments.
- **Same word, multiple tokens:** whether a word gets split depends on whether it (or its pieces) appeared often enough in training data to earn its own token — rare words split into more pieces than common ones.
- **Affects inference cost:** cost and speed scale with number of tokens, not characters or words, so inefficient tokenization of a language or format directly means more compute and higher API cost for the same content.
- **Code, numbers, non-English languages:** the tokenizer's vocabulary was built mostly from its training data mix, so content types underrepresented there (e.g., some non-English languages, or unusual number formats) get split into more, smaller tokens — less "token-efficient."
- **Out-of-vocabulary word:** it gets broken down into smaller known subword pieces (down to individual characters/bytes if needed), so nothing is truly "unknown" — it's just represented less efficiently.

### Q2. Token vs token ID vs embedding vs vocabulary
- **Token:** a discrete text unit (a word, subword, or character produced by the tokenizer).
- **Token ID:** the integer index of that token in the vocabulary — how the token is represented before entering the model.
- **Embedding:** a dense numeric vector the model looks up (or learns) for each token ID, meant to capture meaning.
- **Vocabulary:** the full list of tokens the tokenizer knows, each mapped to a unique ID.

---

## 2. Embeddings

### Q3. What is an embedding, and how does a token become one?
An embedding is a dense vector of numbers that represents a token's meaning in a way the model can do math with. Each token ID is used to look up a row in a learned **embedding matrix** (size: vocabulary size × embedding dimension) — that row is the token's embedding.

- **Embedding matrix:** a big lookup table, one row per vocabulary token, learned during training so that useful patterns end up encoded in the vector values.
- **Similar tokens, similar vectors:** during training, tokens that appear in similar contexts get nudged toward similar vectors because the model needs similar representations to make similar predictions — this falls naturally out of gradient descent on the prediction task.
- **Token vs sentence/document embeddings:** a token embedding represents one subword unit; a sentence/document embedding represents a whole passage, usually built by combining (e.g., pooling or using a special summary token from) many token-level representations.
- **Are dimensions individually meaningful?** Not usually — meaning is spread across the whole vector, not isolated to single dimensions, though occasionally specific directions do correlate with interpretable concepts.
- **Why not use token IDs directly:** IDs are arbitrary integers with no meaningful numeric relationship (ID 5 isn't "more" of anything than ID 3) — embeddings give the model a continuous, learnable space where distance and direction actually mean something.

### Q4. What makes a good embedding model for RAG?
- **Semantic quality:** captures meaning well, not just surface word overlap.
- **Domain coverage:** performs well on your specific content (legal, medical, code, etc.), not just general text.
- **Right dimensionality:** enough dimensions to capture nuance, but not so many that storage/search cost balloons unnecessarily.
- **Multilingual/domain performance:** matters if your data spans languages or specialized jargon.
- **Retrieval benchmark performance:** check results on retrieval-specific benchmarks (e.g., MTEB), not just general language benchmarks.
- **Latency and cost:** embedding is run on every document and every query, so speed and price at scale matter a lot.

---

## 3. Transformer

### Q5. Walk through the Transformer, input to output
Text → tokenizer splits it into tokens → tokens are converted to token IDs → each ID is looked up in the embedding table and combined with positional information → the result passes through a stack of Transformer blocks, each containing self-attention (tokens exchange information), a residual (skip) connection, normalization, a feed-forward network, and another residual connection → after the last block, the final hidden states go through the **LM head** (a linear layer projecting back to vocabulary size) → this produces **logits** (raw scores per vocabulary token) → softmax turns logits into a probability distribution over the next token.

- **Why Transformers replaced RNNs:** RNNs process tokens one at a time in sequence, which is slow to train and struggles to remember long-range dependencies; Transformers let every token attend to every other token directly and process a whole sequence at once during training.
- **Why highly parallelizable during training:** because attention computes relationships between all token pairs at once using matrix multiplication, rather than needing to wait for the previous step's hidden state like an RNN does.
- **Self-attention complexity:** O(n²) in sequence length n, since every token compares against every other token — this is why long context is expensive.
- **As context length increases:** compute and memory grow quadratically (from attention) and cache memory grows linearly (from KV cache), making very long contexts costly and eventually a practical bottleneck.

---

## 4. Attention (Q/K/V)

### Q6. Explain self-attention mathematically
Attention(Q,K,V) = softmax(QKᵀ/√d_k)·V

- **Query (Q):** a vector representing what the current token is "looking for" in other tokens.
- **Key (K):** a vector representing what information each token "advertises" that it holds.
- **Value (V):** the actual content/information a token contributes if it's attended to.
- **QKᵀ:** dot product between queries and keys — measures how relevant each token is to each other token (higher = more similar/relevant).
- **Softmax:** turns those raw similarity scores into normalized weights that sum to 1 (a probability-like distribution over which tokens to focus on).
- **Multiplying by V:** takes a weighted average of all tokens' value vectors, using the attention weights — so each token's new representation is a blend of the most relevant other tokens' information.

- **Why divide by √d_k:** without scaling, dot products grow large as dimensionality increases, pushing softmax into regions with extremely small gradients (saturation) — scaling keeps values in a range where softmax and training work well.
- **Why softmax:** it converts arbitrary scores into a smooth, differentiable probability distribution, letting the model do a "soft" weighted focus rather than picking just one token.
- **If d_k is very large:** dot products can get very large in magnitude, making softmax outputs close to one-hot (very peaked) and gradients close to zero — this is exactly the saturation problem the √d_k scaling fixes.
- **Why Q, K, V are different projections:** each is produced by multiplying the same input by a different learned weight matrix, so the model can learn distinct roles for "what I want," "what I offer," and "what I'd contribute" — using the same raw vector for all three would limit expressive power.

---

## 5. Self-attention vs causal attention

### Q7. Self-attention vs causal self-attention
Regular self-attention lets every token look at every other token, including ones that come later. **Causal attention** adds a mask that blocks each token from seeing future tokens — a token at position t can only attend to positions 1 through t. This is what lets the model generate text left-to-right, one token at a time, without "cheating" by peeking ahead.

- **Why necessary for autoregressive generation:** the model's job is to predict the next token from only what came before it — if it could see the future during training, it would learn to cheat and then fail completely at real generation, where the future genuinely doesn't exist yet.
- **Is the mechanism itself different?** No — it's the same QKᵀ/softmax/V computation; only a mask is added that sets disallowed (future) positions' scores to −∞ before softmax, so they get zero weight.
- **How masking is implemented:** typically by adding a triangular mask matrix (upper triangle = −∞) to the attention scores before the softmax step.

---

## 6. Encoder vs Decoder

### Q8. Encoder-only vs decoder-only vs encoder-decoder

| Architecture | Typical use |
|---|---|
| Encoder-only | Representation / classification (e.g., BERT) |
| Decoder-only | Text generation (e.g., GPT-style LLMs) |
| Encoder-decoder | Sequence-to-sequence tasks (e.g., translation, summarization) |

- **Why modern LLMs are mostly decoder-only:** it's a simpler, more flexible setup — one architecture handles both understanding and generation, scales well, and works naturally for open-ended chat/completion tasks that dominate current use cases.
- **Does BERT generate text?** Not naturally — it's trained with bidirectional attention to fill in masked tokens/understand context, not to generate text left-to-right, so it's used for classification/embedding tasks rather than generation.
- **Why an encoder uses bidirectional attention:** its job is to build a rich understanding of the whole input at once, so it's allowed to look both backward and forward — there's no "generation order" to protect.
- **Why a decoder uses causal attention:** it generates output one token at a time and must only rely on what's already been generated, matching how it will actually be used at inference time.
- **Why cross-attention in encoder-decoder models:** it lets the decoder look back at the encoder's full representation of the input while generating output — e.g., a translation decoder needs to keep referring back to the full source sentence as it writes the translation.

---

## 7. Positional Encoding

### Q9. Why do Transformers need positional information?
Self-attention treats input as a set, not a sequence — on its own it has no idea which token came first. "Dog bites man" and "Man bites dog" use identical tokens, but attention alone can't tell them apart without something encoding *order*. Positional encoding adds that missing order information into the token representations.

- **Why token embeddings alone aren't enough:** a token embedding only encodes *what* the token is, not *where* it sits in the sequence — attention would compute the same result regardless of word order without extra positional signal.
- **Absolute vs relative:** absolute positional encoding gives each position (1st, 2nd, 3rd...) a fixed representation; relative positional encoding instead encodes the *distance between* tokens, which tends to generalize better to sequence lengths not seen in training.
- **Why sinusoidal encoding originally:** it uses fixed sine/cosine waves of different frequencies per dimension, requires no extra learned parameters, and its mathematical structure lets the model infer relative positions even for sequence lengths longer than seen in training.

---

# P1 — Modern Transformer Architecture

## 8. RoPE

### Q10. What is RoPE and why is it useful?
Rotary Positional Embedding encodes a token's position by **rotating** its Query and Key vectors by an angle proportional to that token's position, rather than adding a separate positional vector. The clever part: when you compute QKᵀ between two rotated vectors, the result mathematically depends only on the *relative* distance between the two positions — so relative position information falls out naturally from the attention computation itself.

- **Why applied to Q and K, not V:** position needs to influence *how much* attention one token pays to another (which depends on Q and K's dot product), not the actual content being aggregated (V) — rotating V would distort the information being passed along for no benefit.
- **Advantage over absolute positional embeddings:** it generalizes better to longer sequences and naturally encodes relative distance, which is usually what matters for language (how far apart two words are) rather than their exact absolute position.
- **Beyond training context length:** the rotation angles extrapolate to unseen positions, but performance often degrades because the model never learned to handle attention patterns at those extreme relative distances.
- **Why long-context models need RoPE scaling:** techniques like position interpolation or NTK-aware scaling adjust the rotation frequencies so the model can handle longer sequences than it was originally trained on without falling apart.

---

## 9. LayerNorm vs RMSNorm

### Q11. What does normalization do, and why RMSNorm/LayerNorm?
Normalization rescales activations inside the network to keep values in a stable, consistent range as they flow through many layers — this makes training faster and more stable, and helps gradients flow well through deep networks.

- **LayerNorm:** normalizes using both the mean and variance of the activations (subtract mean, divide by std), then applies a learned scale/shift.
- **RMSNorm:** skips the mean-subtraction step and just normalizes by the root-mean-square of the activations — simpler, cheaper to compute, and works about as well in practice, which is why most modern LLMs use it.

- **Why normalization is needed:** without it, activation magnitudes can drift or explode/vanish as they pass through many stacked layers, making training unstable or very slow.
- **Pre-LN vs Post-LN:** Pre-LN applies normalization *before* the attention/FFN sub-layer (inside the residual branch); Post-LN applies it *after*, on the sum of the residual and the sub-layer output.
- **Why Pre-LN is more common now:** it keeps a clean, unmodified path for gradients to flow through the residual connections, making very deep models much easier and more stable to train than Post-LN.
- **Problems without normalization:** activations can grow or shrink exponentially with depth, causing exploding/vanishing gradients and making the model very hard or impossible to train well.

---

## 10. FFN / SwiGLU

### Q12. Role of the Feed-Forward Network
Attention lets tokens exchange/mix information with each other. The FFN then processes each token's representation **independently** (no cross-token mixing) through a non-linear transformation — typically an "up-projection" to a larger dimension, a non-linearity, and a "down-projection" back down: FFN(x) = W₂·σ(W₁x). Modern LLMs often use gated variants like **SwiGLU**, which add a second, gating projection that multiplies element-wise with the activated branch, giving the network more expressive control over what information passes through.

- **Why FFN dimension is usually larger:** the wider "hidden" layer (often 4x the model dimension) gives the network more capacity to represent complex, non-linear transformations at each position before compressing back down.
- **What the activation function does:** introduces non-linearity — without it, stacking linear layers would collapse mathematically into one linear layer, no matter how many you stack, severely limiting what the network could represent.
- **Why SwiGLU over plain ReLU/GELU:** the added gating mechanism lets the network learn to selectively pass or suppress information more flexibly, and empirically tends to improve model quality for a similar parameter budget.
- **Does FFN mix information between tokens?** No — it's applied to each token position separately; all cross-token mixing happens in the attention sub-layer.

---

## 11. Residual Connections

### Q13. Why residual connections?
Instead of a layer computing y = F(x), the Transformer computes y = x + F(x) — the original input is added back to the transformed output. This gives gradients a direct, unobstructed path backward through the network during training (they can flow through the "+x" shortcut even if F's gradient is small), which makes very deep networks much easier to optimize.

- **Without residuals:** gradients have to flow through every transformation at every layer, and in very deep networks they tend to vanish (or explode), making training slow, unstable, or impossible.
- **Why useful in deep networks:** the shortcut path means the network only has to learn a "correction" (F(x)) on top of the identity function at each layer, rather than having to reconstruct useful information from scratch at every layer.
- **Interaction with normalization:** in Pre-LN designs, normalization happens on the branch *going into* F, while the raw residual stream (x) stays untouched by normalization end-to-end — keeping that clean additive path is a big part of why deep Transformers train stably.

---

# P0 — Generation / Inference

## 12. Autoregressive generation

### Q14. How does a decoder-only LLM generate a sentence?
It predicts one token at a time: P(xₜ | x₁, ..., xₜ₋₁). Given "The capital of France is," it predicts "Paris," then appends that to the input and repeats the process to predict the next token, and so on, until it produces an end-of-sequence token or hits a length limit.

- **Why generation can't be fully parallelized like training:** during training, the whole target sequence is already known, so all positions can be computed at once (with causal masking). During generation, each new token depends on the *actual* token just produced, which isn't known until the previous step finishes — so it's inherently sequential.
- **Why generation slows with longer outputs:** each new token requires another full forward pass through the model (attending over an ever-growing context), so total generation time grows with output length, and per-step cost creeps up too as the KV cache grows.
- **Teacher forcing:** during training, the model is fed the *actual* ground-truth previous tokens as input (not its own possibly-wrong predictions) when predicting the next token — this stabilizes and speeds up training.
- **Training vs inference difference:** training processes a whole known sequence in parallel using teacher forcing; inference generates tokens one at a time, feeding each prediction back in as input for the next step (no ground truth available).

---

## 13. Temperature

### Q15. What does temperature do?
Temperature (T) rescales the logits before softmax: Pᵢ = e^(zᵢ/T) / Σⱼe^(zⱼ/T). Lower T sharpens the distribution (the top choices get even more probability mass, making output more deterministic/focused); higher T flattens it (probabilities become more even, making output more random/diverse).

- **Does it change the model's knowledge?** No — the underlying logits (and thus the model's learned probabilities/rankings) are the same; temperature only reshapes how those probabilities translate into sampling behavior.
- **At T → 0:** the distribution effectively collapses to always picking the single highest-probability token (equivalent to greedy decoding).
- **Why high temperature can increase hallucination:** it makes lower-probability (less likely, potentially less well-supported) tokens more likely to get sampled, increasing the chance of drifting into fabricated or inconsistent content.

---

## 14. Top-k vs Top-p

### Q16. Explain top-k and top-p sampling
- **Top-k:** only consider the k highest-probability tokens at each step, then sample among those (re-normalizing their probabilities).
- **Top-p (nucleus sampling):** instead of a fixed count, keep the *smallest* set of top tokens whose cumulative probability exceeds p, then sample from that set. So the candidate set size adapts — few tokens when the model is confident, more tokens when it's uncertain.

- **Which adapts better to different distributions:** top-p, because it responds to how peaked or flat the actual probability distribution is at each step, whereas top-k always keeps a fixed count regardless of confidence.
- **Can you use both?** Yes — many systems apply top-k first (a hard cap for efficiency/safety) and then top-p within that shortlist, or vice versa, to combine their benefits.
- **Interaction with temperature:** temperature is usually applied first to reshape the distribution, and then top-k/top-p is applied to that reshaped distribution — so temperature affects which and how many tokens end up qualifying under top-p.

---

## 15. Context Window

### Q17. What is a context window?
The context window is the maximum number of tokens the model can hold "in view" at once — covering system instructions, the user's prompt, prior conversation turns, retrieved documents, tool outputs, and the model's own generated output, all combined.

- **Exceeding the limit:** the request either gets rejected/truncated, or the application has to drop/summarize older content (e.g., trim old conversation turns) to fit within the limit.
- **Why bigger context ≠ automatically better RAG:** stuffing more retrieved text into context doesn't guarantee the model uses it well — irrelevant or excessive content can dilute attention, increase cost/latency, and sometimes even hurt answer quality ("lost in the middle" effects).
- **Effect on attention computation:** since self-attention is O(n²), a longer context directly and quadratically increases the compute needed per generation step.
- **Context rot:** the tendency for model performance/attention quality to degrade as context gets very long or cluttered — the model may pay less attention to, or partially "forget," information buried deep in a long context.

---

## 16. KV Cache

### Q18. What is KV caching and why does it matter?
During generation, each new token's attention calculation needs the Key and Value vectors of *all* previous tokens. Recomputing those from scratch at every single generation step would be extremely wasteful, since they don't change once computed. KV caching stores (caches) the Keys and Values for all previously processed tokens, so each new step only computes K/V for the *newest* token and reuses the cached ones for everything before it.

- **Why cache K and V but not Q:** Q is only needed for the current token being generated at each step (it's not reused for future steps), while K and V of *past* tokens are reused at every future step — so only K/V benefit from caching.
- **How KV-cache memory scales:** it grows linearly with context length (more tokens = more cached K/V vectors) and also with the number of attention heads/layers and model dimension.
- **Why long contexts eat GPU memory:** the cache has to store a K and V vector per token, per layer, per head — this adds up fast for long sequences, often becoming the dominant memory cost during inference (sometimes larger than the model weights themselves).
- **Effect of larger batch sizes:** memory needed scales roughly linearly with batch size too, since each sequence in the batch needs its own KV cache — batch size and context length together are the two main levers on inference memory.

---

## 17. Prefill vs Decode

### Q19. Explain prefill and decode phases
**Prefill** processes the entire input prompt at once, computing K/V for every prompt token in parallel and populating the KV cache — this step is **compute-heavy** since it's a big parallel matrix computation. **Decode** then generates output tokens one at a time, each step reusing the cache and computing just one new token — this step is **memory-bandwidth/latency-heavy** since each step is a small amount of compute but requires reading the whole (growing) KV cache from memory.

- **Why prefill can be parallelized:** all prompt tokens and their positions are already known upfront, so their K/V and attention outputs can be computed simultaneously with matrix operations — no dependency on a not-yet-generated token.
- **Why decode is sequential:** each new token depends on the model's actual chosen output from the previous step, which isn't known in advance — so steps must happen one after another.
- **TTFT (Time To First Token):** how long the user waits from sending a request until the first output token appears — dominated by prefill time.
- **Tokens/sec:** the generation throughput during decode — how fast subsequent tokens are produced once generation has started.
- **Why batching strategies differ:** prefill batches well because it's compute-bound and parallel-friendly; decode is memory-bound and latency-sensitive, so serving systems use techniques like continuous/dynamic batching to keep GPUs busy across many concurrent users' decode steps without hurting per-user latency too much.

---

## 18. Hallucination

### Q20. What is hallucination, technically, and why does it happen?
A hallucination is when the model generates content that is unsupported, incorrect, or made up — often stated with the same confident tone as accurate content. The core reason: LLMs are trained to predict the statistically likely next token, not to verify factual truth — so a fluent, plausible-sounding continuation can be generated even when it's factually wrong.

Common causes: the model genuinely lacks the relevant knowledge, the prompt is ambiguous, the query is far from anything in training data (distribution mismatch), retrieval (in RAG) returns weak or irrelevant context, the context is overloaded/confusing, the model's learned statistical associations mislead it into a plausible-but-wrong answer, or sampling randomness pushes it toward a less-likely (less-grounded) token.

- **Does temperature cause hallucination?** It can increase the *chance* of it, by making less-likely (potentially unsupported) tokens more samplable, but hallucination happens even at temperature 0 because it's fundamentally about the model's knowledge and training objective, not just randomness.
- **Can a zero-temperature model hallucinate?** Yes — greedy decoding just always picks the single most likely token, but "most likely" isn't the same as "true"; the model can be confidently and deterministically wrong.
- **Does RAG eliminate hallucination?** No — it reduces it by grounding answers in retrieved evidence, but the model can still misread, over-extend, or ignore the retrieved context, or the retrieval itself can be wrong/irrelevant.
- **Detecting hallucinations:** compare claims against retrieved/ground-truth sources, use a separate "fact-checking" model pass, check for internal consistency, or use citation/attribution requirements so unsupported claims are more visible.
- **Reducing hallucinations:** better retrieval/grounding (RAG), lower temperature for factual tasks, explicit instructions to say "I don't know" when unsure, citation requirements, and fine-tuning/RLHF specifically targeting faithfulness.

---

# P1 — Advanced Architecture

## 19. MHA vs MQA vs GQA

### Q21. Multi-Head, Multi-Query, and Grouped-Query Attention
- **MHA (Multi-Head Attention):** every attention head has its own separate Q, K, and V projections — most expressive, but the KV cache is large (one K/V set per head).
- **MQA (Multi-Query Attention):** all query heads still have their own Q, but they *share* a single K and V — dramatically shrinks the KV cache, at some cost to model quality/expressiveness.
- **GQA (Grouped-Query Attention):** a middle ground — query heads are split into groups, and each group shares one K/V pair, rather than sharing across *all* heads (like MQA) or having a fully separate K/V per head (like MHA).

The whole motivation is **reducing KV-cache memory and speeding up inference**, since KV-cache size scales with the number of K/V heads.

- **Why MQA reduces memory:** far fewer K/V vectors need to be stored and read per token (one shared set instead of one per head), directly shrinking cache size and memory-bandwidth cost during decode.
- **Tradeoff MQA introduces:** less representational diversity across heads (since they all share the same K/V), which can slightly reduce model quality compared to full MHA.
- **Why GQA is a good compromise:** it captures most of MQA's memory/speed savings while keeping more of MHA's representational power, by sharing K/V within smaller groups rather than across everything.

---

## 20. MoE

### Q22. What is Mixture-of-Experts?
Instead of running every token through the *entire* network, an MoE model contains many "expert" sub-networks (usually replacing the FFN layer) plus a small **router** network that, for each token, picks a small subset of experts (e.g., 2 out of 8) to actually process it. This lets the model have a huge **total parameter count** (lots of experts) while only "activating" — and paying the compute cost of — a small fraction of those parameters per token.

- **Dense vs MoE:** a dense model uses all its parameters for every token; an MoE model uses only a selected subset per token, letting total capacity scale up without proportionally scaling up compute per token.
- **"Active parameters":** the subset of the model's total parameters actually used to process a given token (the selected experts) — this number, not the total parameter count, roughly determines compute cost per token.
- **Load balancing:** techniques (often an auxiliary loss term) that encourage the router to spread tokens roughly evenly across experts, so no expert is overloaded while others sit idle.
- **If too many tokens go to one expert:** that expert becomes a bottleneck (slow, possibly capacity-capped, dropping tokens), while other experts are underused — hurting both efficiency and quality; this is exactly what load balancing tries to prevent.
- **Why MoE complicates distributed inference:** experts are often spread across different devices/GPUs, so tokens have to be routed and communicated across the network dynamically at runtime, adding real engineering complexity compared to a dense model where every device does the same fixed computation.

---

# P0 — RAG

## 21. End-to-end RAG architecture

### Q23. Walk through a production RAG pipeline
Documents → parsing (extract raw text/structure) → cleaning (remove noise, normalize formatting) → chunking (split into retrievable pieces) → embedding (convert chunks to vectors) → store in a vector DB → at query time: transform the user's query if needed → retrieve candidate chunks → apply metadata filtering → rerank the candidates for relevance → construct the final context → build the prompt → send to the LLM → produce an answer (ideally with citations back to source chunks).

**Grill: "RAG gives wrong answers — where's the failure?"** Any stage can be the culprit: bad **parsing** (garbled/lost text), poor **chunking** (broken context, orphaned references), weak **embedding model** (misses semantic relevance), bad **retrieval** (wrong chunks returned), incorrect **metadata filtering** (excludes the right docs or includes the wrong ones), a weak **reranker** (good chunks buried, bad ones surfaced), poor **context construction** (too much/too little, badly ordered), a flawed **prompt** (doesn't instruct the model to stick to context), the **LLM** itself hallucinating despite good context, or bad **citation generation** (attributing claims to the wrong source). Debugging RAG means checking each stage in isolation, not just blaming "the model."

---

## 22. Chunking

### Q24. Choosing chunk size and overlap
There's no single correct chunk size — you're balancing retrieval granularity (small enough that a chunk is specifically relevant to a likely query), semantic completeness (large enough that a chunk isn't cut off mid-idea), context budget (how many chunks you can afford to pass to the LLM), embedding quality (some embedding models work better on certain chunk lengths), and the document's own structure (natural sections, paragraphs).

- **Fixed-size vs recursive chunking:** fixed-size just splits every N tokens/characters regardless of content; recursive chunking tries to split along natural boundaries first (sections → paragraphs → sentences) and only falls back to a hard size cut when necessary — usually produces more coherent chunks.
- **Chunks too small:** lose context/meaning (a sentence fragment without its surrounding explanation), and you end up needing many chunks to answer one question, increasing noise and cost.
- **Chunks too large:** dilute relevance (a chunk about many topics makes it harder for the embedding to represent any one of them well) and waste context budget with irrelevant text once retrieved.
- **Semantic/structure-aware chunking:** useful when documents have meaningful structure (headers, sections, code blocks) that should be respected rather than cut arbitrarily — keeps logically related content together.
- **Why bigger chunks aren't always better:** past a point, larger chunks hurt embedding specificity and retrieval precision, and cost more context budget per retrieved chunk, without necessarily adding useful information.

---

## 23. Cosine Similarity

### Q25. Explain cosine similarity
cos(θ) = (A·B) / (||A||·||B||) — it measures the **angle** between two vectors, ignoring their magnitude/length. A value of 1 means the vectors point in the same direction (very similar), 0 means they're unrelated/orthogonal, and −1 means they point in opposite directions. In embedding retrieval, direction is treated as a proxy for semantic meaning, so cosine similarity tells us how semantically alike two pieces of text are, independent of how "long" or "intense" their raw vectors happen to be.

- **Cosine vs Euclidean distance:** Euclidean distance measures the straight-line distance between vector endpoints (sensitive to both direction and magnitude); cosine ignores magnitude entirely and focuses purely on direction — usually preferred for text embeddings, where vector magnitude often isn't meaningful.
- **Normalization and dot product:** if all vectors are pre-normalized to unit length, cosine similarity and the plain dot product become mathematically equivalent — which is why many systems just normalize embeddings once and use the (cheaper) dot product at search time.
- **Why embedding quality can matter more than the vector DB:** the vector database only finds the nearest vectors accurately and efficiently — but if the embeddings themselves don't capture meaning well, "nearest" won't mean "most relevant," no matter how good the search infrastructure is.

---

## 24. Vector Databases

### Q26. What does a vector database do?
It stores large collections of embedding vectors and lets you quickly find the vectors most similar to a query vector — using an **approximate nearest-neighbor (ANN) index** rather than comparing the query against every stored vector one by one. Examples: FAISS, Pinecone, pgvector.

- **Exact vs approximate nearest-neighbor search:** exact search guarantees finding the true closest vectors but scales poorly (linear or worse in dataset size); approximate search trades a small amount of accuracy for massive speed gains by using index structures (like graphs or trees) that skip most of the comparisons.
- **Why brute-force is expensive:** comparing a query against every single stored vector is O(n) per query — fine for small datasets, but far too slow at millions/billions of vectors and real-time latency requirements.
- **Metadata to store alongside vectors:** source document ID, chunk text, timestamps, permissions/access control, category/tags — anything needed for filtering or for constructing the final context after retrieval.
- **Updating/deleting documents:** re-embed and re-insert updated content (often with the old vector removed or replaced), and most vector DBs support direct deletion by ID; some ANN index types need periodic rebuilding/compaction to stay efficient after many updates.

---

## 25. HNSW

### Q27. Explain HNSW
HNSW (Hierarchical Navigable Small World) is a graph-based approximate nearest-neighbor search structure. It builds multiple layers of a graph — the top layers are sparse and let you jump around quickly to roughly the right neighborhood, and lower layers get progressively denser, letting you narrow in on the precise nearest neighbors. It gives a strong practical tradeoff between search speed, recall (accuracy), and memory usage, which is why it's widely used in vector databases.

- **`efSearch`:** controls how many candidate nodes are explored during a search — higher values check more candidates, improving recall at the cost of slower search.
- **`M`:** controls how many graph connections each node keeps — higher M means a denser, more accurate graph but more memory usage and slower index construction.
- **Why higher search quality means higher latency:** better recall requires exploring more of the graph (more candidates, more hops), which directly means more computation and time per query.
- **Approximate vs exact:** HNSW is approximate — it's not guaranteed to find the literal closest vectors every time, but it gets very close, very fast, which is the right tradeoff for most large-scale retrieval use cases.

---

## 26. FAISS vs Pinecone vs pgvector

### Q28. When to choose FAISS, Pinecone, or pgvector
- **FAISS:** a library, not a managed database — great for local/custom vector search where you want full control, but you have to build and operate the surrounding infrastructure yourself (persistence, scaling, filtering, etc.).
- **Pinecone:** a fully managed vector database — handles scaling, infrastructure, and operations for you, good when you want production-grade retrieval without running your own servers.
- **pgvector:** a PostgreSQL extension that adds vector search to a normal Postgres database — great when your vectors and relational/metadata data already live in Postgres, since it avoids adding a whole separate system for moderate-scale workloads.

**"Why not always use a dedicated vector DB?"** Because operational simplicity has real value — running a separate specialized system adds infrastructure, cost, and complexity. If your data already lives in Postgres and your scale/performance needs are moderate, pgvector can be simpler and cheaper while being good enough; a dedicated vector DB earns its complexity at larger scale or when you need advanced ANN tuning that Postgres-based solutions don't offer as well.

---

## 27. BM25

### Q29. Why still use BM25 alongside embeddings?
BM25 is a **lexical/keyword-based** retrieval algorithm built on term frequency, inverse document frequency, and document length normalization — it scores documents by how well their actual words match the query's actual words. This makes it excellent at exact matching, which pure semantic (embedding) search can be weak at — for example, searching for the exact string "ERR_CONNECTION_RESET" should return documents containing that literal code, but an embedding model might instead surface documents that are conceptually related to "connection errors" without containing that exact string. BM25 fills that gap.

---

## 28. Hybrid Search

### Q30. What is hybrid search?
Hybrid search combines **dense retrieval** (embeddings, for semantic/conceptual similarity) with **BM25** (for exact lexical/keyword matching), so the system handles both "find things that mean the same thing" and "find things containing this exact term/ID/name" well.

- **Combining scores:** normalize and weight the two scores (e.g., a weighted sum), or use rank-based fusion methods rather than trying to directly compare two different scoring scales.
- **Reciprocal Rank Fusion (RRF):** a simple, robust fusion method that scores each document based on its *rank* (not raw score) in each retrieval method's results, then sums those rank-based scores — sidesteps the problem of BM25 and cosine similarity scores not being on comparable scales.
- **Tuning the relative contribution:** adjust the weighting between the dense and lexical components based on validation data — how much each is favored often depends on your query types (more keyword-heavy queries vs more conceptual queries).

---

## 29. Reranking

### Q31. Why rerank if vector search already returns relevant docs?
Initial retrieval is optimized for **speed and recall** at large scale — pulling a reasonably good candidate set quickly out of potentially millions of documents. A **reranker** then takes that smaller candidate set (e.g., top 50) and applies a much more expensive, precise relevance model to reorder them, so the final small set (e.g., top 5) actually passed to the LLM is as relevant as possible.

- **Bi-encoder vs cross-encoder:** a bi-encoder embeds the query and each document *separately* and compares vectors (fast, used for initial large-scale retrieval); a cross-encoder feeds the query and a document *together* into one model that directly scores their relevance (much more accurate, but far more expensive per pair).
- **Why cross-encoders are more expensive:** they require a full model forward pass for every single query-document pair (no precomputed vectors to reuse), so cost scales with the number of candidates being scored — infeasible to run over an entire corpus, but fine over a small shortlist.
- **Why not rerank everything:** cross-encoder scoring is too slow/expensive to run over the entire document collection for every query — you rerank only the smaller candidate set that initial (cheap) retrieval already narrowed down.

---

## 30. Metadata Filtering

### Q32. Why filter during retrieval, not after?
If you retrieve your top-K results first and *then* filter by metadata (e.g., department = Finance), you might filter out most of your top results and be left with too few (or zero) genuinely relevant, in-scope documents — even though better-matching Finance documents existed further down the unfiltered ranking. Applying the filter *during* retrieval (searching only within the valid, pre-filtered candidate set) ensures the top-K results returned are both relevant *and* valid, and can also reduce the search space/cost.

---

## 31. Query Rewriting

### Q33. What problem does query rewriting solve?
Users often phrase queries in ways that are ambiguous or depend on prior conversation context — e.g., "What did he say about that?" gives the retriever nothing concrete to search for. Query rewriting uses the LLM (and conversation history) to turn such queries into a clearer, more retrieval-friendly form before searching, e.g., resolving "he" and "that" into their actual referents.

- **When rewriting can hurt:** if the rewrite guesses the wrong interpretation of an ambiguous reference, it can confidently retrieve the *wrong* documents — worse than the vague original, which at least wouldn't have committed to a wrong assumption.
- **Can it introduce incorrect assumptions?** Yes — the rewriting LLM might resolve ambiguity incorrectly or add specifics that weren't actually implied, subtly steering retrieval off course.
- **Evaluating it:** compare retrieval quality (e.g., recall/precision of relevant documents) with vs without rewriting on a labeled evaluation set, and check specifically for cases where the rewrite changes the query's actual intent.

---

## 32. Multi-query

### Q34. What is multi-query retrieval?
Instead of retrieving with just one search query, the LLM generates several different phrasings/angles of the original query, retrieves for each one separately, and then merges the results. This helps because different phrasings can surface different relevant documents that a single query might miss (embedding similarity is sensitive to exact wording).

- **Removing duplicates:** deduplicate merged results by document/chunk ID before passing them on, since the same document often gets retrieved by multiple query variants.
- **Effect on latency/cost:** directly increases both — you're now running multiple retrieval calls (and often an extra LLM call to generate the query variants) instead of one.
- **Evaluating whether it helps:** compare end-to-end answer quality or retrieval recall with multi-query vs single-query on a held-out evaluation set — the extra cost should demonstrably improve results to justify it.

---

## 33. HyDE

### Q35. What is HyDE and why can it help?
HyDE (Hypothetical Document Embeddings) works by having the LLM first generate a **hypothetical answer/document** in response to the query, then embedding *that* generated text (instead of the short original question) to perform retrieval. The idea: a fuller, answer-shaped hypothetical document is often semantically closer, in embedding space, to real relevant documents than a short, terse question would be.

- **Main risk:** the hypothetical document is generated by the LLM without grounding, so it can contain **hallucinated** details or wrong assumptions — and if retrieval is then based on those hallucinated specifics, it can pull in irrelevant or misleading documents.
- **Can hallucinated concepts hurt retrieval?** Yes — if the generated hypothetical answer confidently invents a wrong fact, the embedding used for search will reflect that wrong fact, actively steering retrieval away from the correct documents.
- **When normal query embedding is preferable:** for queries that are already clear, specific, and well-formed (or where the topic is unfamiliar enough that the LLM's "hypothetical answer" is likely to be low-quality/inaccurate), a direct query embedding is simpler and safer.

---

## 34. Contextual Retrieval

### Q36. What problem does contextual retrieval solve?
A chunk taken out of its surrounding document can lose critical context — e.g., "He joined the company in 2018" is meaningless on its own if we don't know who "he" refers to. Contextual retrieval addresses this by adding relevant surrounding context (e.g., a short summary of the source document, or the preceding section) to each chunk *before* it's embedded/indexed, so the chunk becomes more self-contained and retrievable on its own merits, without losing its original meaning.

---

## 35. Graph RAG

### Q37. When is Graph RAG better than conventional vector RAG?
Graph RAG explicitly represents entities and the relationships between them (people, projects, dependencies, organizational structure) as a graph, rather than relying only on independent, unstructured text chunks. It shines on questions that require **multi-hop reasoning across relationships** — e.g., "Which projects are affected by employees reporting to manager X?" requires traversing manager → employees → projects → dependencies, a chain of explicit relationships that's hard to reconstruct reliably from scattered, disconnected text chunks in a standard vector index, but is exactly what a graph structure is built to represent and traverse.

---

## 🔥 High-priority "whiteboard cold" list
1. Self-attention formula + what Q, K, V mean (Q6)
2. Causal masking and why it's needed for generation (Q7)
3. KV cache — what it stores, why, and how it scales (Q18)
4. Prefill vs decode — compute-bound vs memory-bound (Q19)
5. RoPE — relative position via rotation (Q10)
6. Hallucination — why it happens even at temperature 0 (Q20)
7. GQA/MQA — the KV-cache memory motivation (Q21)
8. Full RAG pipeline + where failures can occur (Q23)
9. Hybrid search + Reciprocal Rank Fusion (Q30)
10. Reranking — bi-encoder vs cross-encoder tradeoff (Q31)

Same meta-pattern as before: for any component, be ready to explain **what it does → why it's needed → what breaks without it → what the tradeoffs are**.