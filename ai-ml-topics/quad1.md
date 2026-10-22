# ML Interview Prep — Answers

---

## 1. ML Fundamentals

### Q1. Bias–variance tradeoff
**Bias** is error from a model being too simple to capture the true pattern (underfitting). **Variance** is error from a model being too sensitive to the specific training set (overfitting). Total expected error ≈ Bias² + Variance + irreducible noise. As model complexity increases, bias falls but variance rises — there's a sweet spot that minimizes total error.

- **Diagnosing:** High bias → high training error *and* high validation error (both bad, close together). High variance → low training error but much higher validation error (big gap).
- **Fixing high bias:** add features, use a more complex model, reduce regularization, train longer.
- **Fixing high variance:** get more data, simplify the model, add regularization, use ensembling (bagging), early stopping.
- **Regularization** shrinks the hypothesis space, directly trading variance reduction for a small increase in bias.
- **Yes**, a model can have both — e.g., a poorly-tuned deep model with noisy, insufficient features can underfit the signal while still overfitting the noise.

### Q2. Overfitting, L1 vs L2
Overfitting = the model has learned noise/idiosyncrasies of the training set rather than the generalizable signal — great training performance, poor test performance. Regularization adds a penalty on model complexity (weight magnitude) to the loss function, discouraging the model from relying too heavily on any one feature.

- **L1 (Lasso):** penalty = λΣ|w|. Its penalty has a "corner" at zero in weight space, so the optimum often lands exactly on an axis — producing **sparse** solutions (some weights become exactly 0). Effectively performs feature selection.
- **L2 (Ridge):** penalty = λΣw². It's smooth and quadratic, so it shrinks weights proportionally but rarely to exactly zero — it spreads influence across correlated features instead of picking one.
- **λ too large:** the penalty dominates the loss, driving weights toward zero regardless of the data → severe underfitting.

### Q3. Data leakage
Leakage = information from outside the training set (often including the target, directly or indirectly) sneaks into the training process, inflating validation metrics that won't hold in production.

- **Preprocessing after splitting:** operations like scaling, imputation, or target encoding must fit their parameters (mean, std, category averages) **only on the training fold**, then apply to validation/test. Fitting on the full dataset lets test-set statistics leak into training.
- **Target leakage:** using a feature that is only available *because* the outcome happened (e.g., "was_hospitalized" as a feature to predict "has_disease") — it encodes the answer.
- **Temporal/point-in-time leakage:** using data that wouldn't have existed yet at prediction time in production (e.g., using a customer's total lifetime purchases to predict month-1 churn).

### Q4. Cross-validation
Use CV to get a more robust estimate of generalization performance and to tune hyperparameters without touching the test set — it averages performance across multiple train/validation splits, reducing variance from any single split.

- **Why random K-fold fails for time series:** it shuffles time, letting the model "see the future" (train on later data, test on earlier data), which never happens in production. Use **time-series/rolling-origin CV** instead (always train on the past, validate on the future).
- **Stratified K-fold:** preserves the class distribution in every fold — important for imbalanced classification so no fold accidentally has too few minority examples.
- **CV + tuning:** wrap CV inside the hyperparameter search (e.g., grid/random search) so each candidate hyperparameter set is scored by its average CV performance, then do a final fit on all training data with the winning hyperparameters — evaluated once on a held-out test set.

---

## 2. Classical Models

### Q5. Linear Regression assumptions
Core assumptions: linearity (relationship between X and y is linear), independence of errors, homoscedasticity (constant error variance), normality of residuals, and no severe multicollinearity.

- **Matter for prediction:** linearity and multicollinearity mostly matter for prediction accuracy/stability.
- **Matter mainly for inference:** normality of residuals and homoscedasticity are mostly needed for valid p-values/confidence intervals, not raw prediction accuracy.
- **Multicollinearity:** doesn't hurt predictions much, but makes individual coefficients unstable and hard to interpret (large standard errors).
- **Heteroscedasticity:** doesn't bias coefficients but makes standard errors (and thus significance tests) unreliable.
- **Why squared error:** it's differentiable everywhere, penalizes large errors more, and its minimizer has a closed-form solution (and corresponds to the maximum-likelihood estimate under Gaussian noise).
- **Ridge/Lasso:** add a penalty term to the OLS objective, shrinking coefficients to reduce variance at the cost of a small bias increase.

### Q6. Logistic Regression
Logistic Regression models the **log-odds** of the positive class as a linear function of the features: log(p/(1-p)) = wᵀx + b. The sigmoid function squashes this linear output into (0,1), which we interpret as a probability. We use **log loss (cross-entropy)** instead of MSE because MSE on a sigmoid output is non-convex (multiple local minima, hard to optimize), while log loss is convex for this model and heavily penalizes confident-and-wrong predictions, matching the maximum-likelihood objective for Bernoulli outcomes.

- **Classification or regression?** It's a classification algorithm — despite fitting a linear (regression-style) model internally, the output is used to make a class decision via a threshold.
- **Coefficient meaning:** the change in log-odds of the positive class for a one-unit increase in that feature (holding others constant); exponentiate it to get an odds ratio.
- **Threshold effect:** raising the threshold increases precision but lowers recall (fewer positive predictions, but more confident ones); lowering it does the opposite.
- **Multiclass:** via one-vs-rest (train k binary classifiers) or softmax regression, which generalizes the sigmoid to multiple classes directly.

### Q7. 95% accuracy but bad minority-class performance
This is the classic sign of class imbalance — accuracy is dominated by the majority class. Investigate/fix:
- **Class weights:** penalize misclassifying the minority class more heavily in the loss.
- **Threshold:** the default 0.5 cutoff is usually wrong for imbalanced data — lower it to catch more minority-class cases.
- **Resampling:** oversample the minority class (e.g., SMOTE) or undersample the majority class.
- **PR-AUC instead of ROC-AUC/accuracy:** precision-recall curves are far more informative than accuracy when positives are rare.
- **Feature quality:** the model may simply lack signal to distinguish the minority class — check feature relevance.
- **Calibration:** check whether predicted probabilities are meaningful, not just rank-ordered.

### Q8. Decision Trees — splitting
At each node, the tree tries every feature/threshold combination and picks the split that most **reduces impurity** in the resulting child nodes.
- **Gini impurity:** 1 − Σpᵢ², measures the probability of misclassifying a randomly chosen sample if labeled according to the node's class distribution.
- **Entropy:** −Σpᵢ·log₂(pᵢ), from information theory, measures disorder/uncertainty.
Both are ~0 for a pure node and maximal for a 50/50 split; Gini is cheaper to compute and gives similar splits in practice.

- **Why trees overfit:** left unconstrained, a tree keeps splitting until every leaf is pure (sometimes a single training example), memorizing noise.
- **`max_depth`:** caps how many splits deep the tree can go. **`min_samples_split`:** minimum samples a node needs before it's allowed to split. **`min_samples_leaf`:** minimum samples required in a resulting leaf — prevents tiny, noise-driven leaves.
- **Insensitive to scaling:** splits are based on threshold comparisons per feature independently (x > t), not distances or dot products across features, so the scale of one feature doesn't affect how another is split.

### Q9. Random Forest
Random Forest trains many decision trees on **bootstrapped samples** (bagging) of the data, and at each split only considers a **random subset of features**, then averages (regression) or votes (classification) their predictions.
- **Why averaging reduces variance:** individual trees are high-variance/noisy but roughly unbiased; averaging many independent-ish predictions cancels out uncorrelated noise while the signal reinforces (variance of the mean of n samples shrinks with n, assuming low correlation between trees).
- **Random feature selection** decorrelates the trees further — without it, all trees would tend to split on the same dominant feature first, making them too similar for averaging to help much.
- **Can it overfit?** Yes, though far less than a single tree — with too few/weak trees, very deep trees, or too little randomness, it can still overfit, but adding more trees does not increase overfitting (it just adds compute).
- **No feature scaling needed:** same reason as single trees — splits are threshold-based per feature.
- **RF vs XGBoost:** see below.

### Q10. Gradient Boosting / XGBoost
Gradient Boosting builds trees **sequentially**: each new tree is trained to predict the **residual error** (technically, the negative gradient of the loss) of the current ensemble, and its predictions are added to the ensemble scaled by a learning rate. The model is optimizing the overall loss function (e.g., log loss, MSE) via functional gradient descent — each tree is one gradient-descent step in function space.

- **GB vs RF:** RF trees are trained independently and in parallel (variance reduction via averaging); GB trees are trained sequentially, each correcting the previous ensemble's mistakes (bias reduction via boosting). GB is more prone to overfitting and more sensitive to hyperparameters; RF is more robust out-of-the-box.
- **Learning rate:** shrinks each tree's contribution, trading more boosting rounds for smoother, more generalizable convergence — too high overfits/overshoots, too low undertrains unless you add many more trees.
- **`n_estimators`:** the number of boosting rounds (trees) — too many can overfit (especially with a high learning rate) unless combined with early stopping.
- **Regularization in XGBoost:** explicit L1/L2 penalties on leaf weights, plus tree-complexity penalties (γ per split, max depth, min child weight) — all fight the sequential model's tendency to keep chasing residual noise.
- **Why it can still overfit:** each tree specifically targets the remaining errors of the training set, including noise; without regularization/early stopping/limited depth, later trees start fitting training-set idiosyncrasies rather than true signal.

**"Why choose Random Forest over XGBoost?"** — strong answer:
- RF is simpler to tune (fewer critical hyperparameters), more robust to overfitting out-of-the-box, easily parallelizable (independent trees), and more stable with noisy data/outliers.
- XGBoost usually gets higher accuracy but needs careful tuning (learning rate, depth, regularization, early stopping) and is more sensitive to noise/outliers due to its sequential, error-correcting nature.
- Choose RF when you want a strong robust baseline fast, have limited time/expertise to tune, need easy parallel training, or interpretability/stability matters more than squeezing out the last bit of accuracy. Choose XGBoost when you have time to tune and need maximum predictive performance.

---

## 3. Unsupervised Learning

### Q11. K-Means
K-Means minimizes **within-cluster sum of squared distances (inertia)**: Σ over clusters Σ over points ||x − centroid||². It alternates two steps — assign each point to its nearest centroid, then recompute centroids as the mean of their assigned points — and provably converges because both steps never increase the objective (it's a coordinate-descent procedure on a bounded-below objective).

- **Initialization matters:** K-Means only finds a *local* minimum; bad random starting centroids can lead to poor, suboptimal clusterings.
- **K-Means++:** a smarter initialization that spreads initial centroids apart (probabilistically favoring points far from existing centroids), which speeds convergence and improves final cluster quality.
- **Choosing K:** elbow method (inertia vs K), silhouette score, gap statistic, or domain knowledge.
- **Sensitive to scaling/outliers:** it uses Euclidean distance, so a feature with a larger numeric range dominates the distance calculation; outliers pull centroids away from the bulk of the true cluster since it uses means.

### Q12. K-Means' shape preference
Because it minimizes Euclidean distance to a single centroid per cluster, K-Means implicitly assumes clusters are **roughly spherical/convex and similarly sized/dense** — it can't represent elongated, nested, or irregularly shaped clusters well.
- For different shapes/densities, use **GMM** (allows elliptical clusters via covariance, soft assignment), **DBSCAN** (density-based, finds arbitrary shapes, handles noise/outliers, no need to specify K), or **hierarchical clustering** (builds a dendrogram, no assumption of cluster shape, useful when the number of clusters isn't known upfront).

### Q13. PCA
PCA finds new axes (principal components) that capture the maximum variance in the data, ordered by how much variance each explains. The **covariance matrix** captures how features vary together; its **eigenvectors** point in the directions of maximum variance in the data, and the corresponding **eigenvalues** quantify how much variance lies along each direction — this falls directly out of maximizing wᵀΣw subject to ||w||=1 via Lagrange multipliers, whose solution is exactly the eigenvector equation Σw = λw.

- **Why maximize variance:** directions with more variance carry more information/discriminative signal about the data; low-variance directions are closer to noise.
- **Explained variance:** the fraction of total dataset variance captured by a given component (eigenvalue / sum of eigenvalues).
- **Standardize first:** PCA is scale-sensitive — without standardizing, features with larger numeric ranges dominate the variance calculation and hijack the "top" components regardless of actual importance.
- **PCA vs feature selection:** PCA creates new features (linear combinations of originals) and is unsupervised/doesn't consider the target; feature selection keeps a subset of original, interpretable features and can be supervised.
- **Information loss:** yes — dropping lower components discards some variance (assumed to be mostly noise, but not always).

---

## 4. Classification Evaluation

### Q14. Precision, Recall, Specificity, F1
Given a confusion matrix (TP, FP, TN, FN):
- **Precision** = TP/(TP+FP) — of predicted positives, how many were actually positive. Matters when false positives are costly (e.g., spam filters flagging real emails).
- **Recall (sensitivity)** = TP/(TP+FN) — of actual positives, how many were caught. Matters when false negatives are costly (e.g., missing a cancer diagnosis).
- **Specificity** = TN/(TN+FP) — of actual negatives, how many were correctly identified.
- **F1** = 2·(Precision·Recall)/(Precision+Recall) — harmonic mean, balances precision and recall, useful for imbalanced data with no strong cost asymmetry.

- **Tradeoff:** raising the decision threshold usually raises precision but lowers recall, and vice versa.
- **F1 high, model still bad:** yes — F1 says nothing about calibration, ranking quality on other slices of data, or performance on genuinely important edge cases; it's also threshold-dependent.
- **Accuracy misleading on imbalance:** predicting "always negative" on a 99%-negative dataset gives 99% accuracy while being useless.

### Q15. ROC-AUC vs PR-AUC
**ROC-AUC** plots True Positive Rate vs False Positive Rate across thresholds and measures ranking quality overall. **PR-AUC** plots Precision vs Recall across thresholds, focusing specifically on positive-class performance. Prefer PR-AUC when positives are **rare** (imbalanced data) and you care most about how well the model finds/ranks the minority class.

- **Classic grill — why ROC-AUC can look great but be useless on imbalanced data:** FPR = FP/(FP+TN), and with a huge number of true negatives, even a large *absolute* number of false positives is a tiny *fraction* of all negatives, so FPR stays low and ROC-AUC looks strong — while precision (FP relative to *predicted* positives) can be terrible, meaning most flagged cases are false alarms. PR-AUC exposes this because it doesn't have TN in its denominator at all.

### Q16. Good ROC-AUC but poor business performance
ROC-AUC measures ranking ability across *all* thresholds — it says nothing about whether you picked a good **operating threshold**, whether probabilities are **calibrated**, whether the **costs of FP vs FN** are properly weighted, whether there's **class imbalance** making ROC-AUC overly optimistic (see Q15), whether there's **distribution shift** between training and production data, or whether ROC-AUC was simply the **wrong metric** for the business objective (e.g., it doesn't reflect $ cost of specific errors).

### Q17. Choosing the classification threshold in production
Pick the threshold that optimizes a business-relevant objective — expected cost, F-beta score, or a target precision/recall — using a **validation set**, not the test set (which should stay untouched for final unbiased evaluation).
- **Why not 0.5:** it implicitly assumes balanced classes and equal cost of FP/FN, which is rarely true in practice.
- **FN costs 10× more than FP:** shift the threshold lower (accept more false positives to catch more true positives), formally by minimizing expected cost = FN_count·10 + FP_count·1 over the validation set's threshold sweep, or by using a cost-sensitive/F-beta (β=√10-ish, favoring recall) metric.
- **Avoiding test-set leakage:** tune the threshold using cross-validation or a dedicated validation split; only run the test set once, at the very end, with the threshold already frozen.

### Q18. Log loss
Log loss = −(1/n)Σ[y·log(p) + (1−y)·log(1−p)]. Because of the log term, as a predicted probability for the wrong class approaches 1 (i.e., the model is very confident and very wrong), −log(p) shoots toward infinity — so log loss punishes **confident, wrong** predictions far more harshly than mildly wrong ones, unlike accuracy which treats a 51%-confident wrong guess the same as a 99%-confident wrong guess.
- **Calibration:** a model is calibrated if, among all cases it predicts "70% probability positive," roughly 70% actually are positive — its probabilities reflect true frequencies, not just correct rank-ordering.
- **Same accuracy, different log loss:** yes — two models can make the same right/wrong calls at a 0.5 threshold but differ wildly in confidence, so log loss (which uses the raw probabilities) will differ even though accuracy (a hard-threshold metric) doesn't.

---

## 5. Regression Evaluation

### Q19. MAE vs MSE vs RMSE
- **MAE** = mean(|y − ŷ|) — average absolute error, in the target's original units, treats all errors linearly.
- **MSE** = mean((y − ŷ)²) — squares errors, so **large errors are penalized disproportionately more**, making it more sensitive to outliers; units are squared (harder to interpret directly).
- **RMSE** = √MSE — brings the units back to the same scale as the target (easy to interpret, e.g., "off by $500 on average") while retaining MSE's extra sensitivity to large errors.
- **Choose MAE** when you want a robust, easily interpretable metric and outliers shouldn't dominate; **choose RMSE/MSE** when large errors are especially bad and should be penalized more.

### Q20. R²
R² = 1 − (SS_residual / SS_total) — the fraction of variance in the target explained by the model, relative to simply predicting the mean.
- **Can be negative:** yes — if the model performs *worse* than just predicting the mean (SS_residual > SS_total), R² goes negative; this can happen on a test set even if training R² is positive.
- **Adding features never decreases training R²:** more features give the model strictly more flexibility to fit the training data (in the worst case, it can ignore a useless feature by giving it weight ≈0), so training-set fit can only stay the same or improve.
- **High R² not sufficient:** doesn't mean the model generalizes (could be overfit), doesn't check residual patterns/assumptions, and doesn't reflect real-world error cost.
- **Adjusted R²** penalizes R² for the number of predictors, so it can decrease when you add a feature that doesn't meaningfully improve fit — useful for comparing models with different numbers of features.

---

## 6. Statistics

### Q21. Bayes' Theorem
P(A|B) = P(B|A)·P(A) / P(B). P(A|B) and P(B|A) differ because they condition on different base rates — e.g., P(has disease | positive test) is usually much lower than P(positive test | has disease), because a rare disease means most positive tests come from the much larger healthy population producing false positives (this is the classic base-rate fallacy).

### Q22. Central Limit Theorem
The CLT states that the sampling distribution of the **mean** of a sufficiently large number of independent, identically distributed samples approaches a **normal distribution**, regardless of the shape of the underlying population distribution. This underpins most classical inference (confidence intervals, hypothesis tests) even when raw data isn't normal.
- **Original data need not be normal** — the CLT is exactly what lets us use normal-based methods even on skewed underlying data, as long as the sample size is large enough (rule of thumb: n ≥ 30, more for heavily skewed distributions).
- **As n increases:** the sampling distribution of the mean gets narrower (standard error = σ/√n shrinks) and looks increasingly normal/bell-shaped.

### Q23. Confidence Interval
A 95% confidence interval means: if you repeated the sampling-and-interval-construction process many times, **95% of the resulting intervals would contain the true population parameter**. It's a statement about the long-run reliability of the *procedure*, not a probability statement about one specific, already-computed interval.
- **Grill — is "95% probability the true parameter is in this interval" correct?** No (in the frequentist framework). Once the interval is computed, the true parameter either is or isn't in it — there's no more randomness left; the 95% describes the method's success rate across repeated sampling, not this particular interval. (A Bayesian *credible* interval, by contrast, does support a direct probability statement about the parameter — but that's a different framework.)

### Q24. Hypothesis testing
- **Null hypothesis (H₀):** the "no effect/no difference" baseline assumption.
- **p-value:** the probability of observing data at least as extreme as what you got, *assuming H₀ is true*.
- **Significance level (α):** the pre-chosen threshold (commonly 0.05) below which you reject H₀.
- **Type I error:** rejecting H₀ when it's actually true (false positive) — its rate is exactly α.
- **Type II error:** failing to reject H₀ when it's actually false (false negative) — its rate is β.

- **Decreasing α:** makes it harder to reject H₀, reducing Type I errors but increasing Type II errors (lower power) unless you compensate with more data.
- **α, β, power relationship:** power = 1 − β; there's a direct tradeoff between α and β for a fixed sample size — tightening one loosens the other.
- **Statistically significant but practically useless:** yes — with a large enough sample, even a tiny, meaningless effect size can produce a very small p-value.

### Q25. Statistical power
Power = probability of correctly rejecting H₀ when it's actually false (1 − β) — i.e., the test's ability to detect a real effect. Increase power by: **increasing sample size**, targeting/expecting a **larger effect size**, **reducing variance** (better measurement, controlling confounders), or **increasing α** (accepting more Type I error risk).

---

## 7. Statistical Tests

### Q26. Choosing a statistical test

| Situation | Test |
|---|---|
| Mean of one/two groups, population σ unknown | t-test |
| Mean, population σ known (or large-sample) | z-test |
| Categorical variables / independence | Chi-square |
| Compare means across 3+ groups | ANOVA |

- **t-test assumptions:** roughly normal data (or large enough n via CLT), independent observations, and (for the standard two-sample test) roughly equal variances between groups (otherwise use Welch's t-test).
- **What ANOVA tests:** whether there's a statistically significant difference **somewhere** among 3+ group means (via comparing between-group vs within-group variance — hence "analysis of variance"), not which specific groups differ.
- **Significant ANOVA tells you which groups differ?** No — it only tells you *at least one* group differs from the others.
- **Post-hoc tests:** needed to pinpoint *which* pairs of groups differ (e.g., Tukey's HSD) while controlling the inflated false-positive rate from making multiple pairwise comparisons.
- **Mann-Whitney vs t-test:** use Mann-Whitney (a non-parametric, rank-based test) when data is not normally distributed, is ordinal, or has significant outliers that would distort a mean-based t-test.

---

## 8. Data & Feature Engineering

### Q27. MCAR vs MAR vs MNAR
- **MCAR (Missing Completely At Random):** missingness is unrelated to any observed or unobserved variable — pure randomness. Simple imputation (mean/median) or listwise deletion is relatively safe.
- **MAR (Missing At Random):** missingness depends on *other observed* variables (e.g., income missing more often for younger respondents, but not on income itself). Model-based imputation (e.g., regression/KNN imputation using other features) is appropriate.
- **MNAR (Missing Not At Random):** missingness depends on the *unobserved value itself* (e.g., high earners are less likely to report income). Hardest case — often needs domain knowledge, missingness indicators as features, or specialized modeling; naive imputation can bias results.

### Q28. Handling missing values
Approach depends on the missingness mechanism and data type: drop rows/columns if missingness is minimal and MCAR; impute otherwise. Mean imputation isn't a good universal solution because it **distorts the feature's distribution** (artificially reduces variance, can create a spike at the mean) and ignores relationships with other features.
- **Numerical vs categorical:** numerical often uses mean/median/model-based imputation; categorical uses mode, a new "missing" category, or model-based imputation.
- **Missingness indicators:** add a binary "was_missing" flag alongside the imputed value so the model can learn if missingness itself is informative (especially useful under MAR/MNAR).
- **Model-based imputation:** predict the missing value from other features (regression, KNN, iterative imputation) — more accurate than a single constant but adds complexity and risk of leakage if not fit only on training data.
- **Distribution distortion:** naive imputation can shrink variance and create artificial patterns/outliers at the imputed value, misleading downstream models.

### Q29. Standardize vs normalize
**Standardize** (z-score: subtract mean, divide by std) when the algorithm assumes/benefits from roughly-Gaussian, zero-centered features (regression with regularization, PCA, most gradient-based models). **Normalize** (min-max scaling to [0,1]) when you need bounded ranges, e.g., for neural nets with certain activation functions or when the distribution isn't Gaussian.
- **Scaling-sensitive:** KNN, K-Means, SVM, PCA, and Linear/Logistic Regression with regularization (since the penalty term treats all coefficients' scales equally, so unscaled features get unfairly penalized/protected).
- **Generally insensitive:** Decision Trees, Random Forest, XGBoost (threshold-based splits per feature, not distance-based).

### Q30. Outliers
Detect via z-score/IQR thresholds, visualization (box plots, scatter plots), or model-based methods (isolation forest, DBSCAN). Handling depends on cause: remove/cap if it's a data error; keep (and possibly use robust models) if it's a legitimate rare event that matters for your use case (e.g., fraud detection literally targets outliers).
- **Legitimate rare events:** don't blindly remove them — they may be exactly what you're trying to detect or predict; consider robust scaling or models that handle them explicitly instead of deleting.
- **Tree models more robust:** splits are based on rank/threshold position rather than the actual distances/magnitudes, so an extreme value just ends up in an extreme leaf rather than distorting a mean or a distance calculation.

### Q31. Encoding categorical variables
- **One-hot encoding:** creates a binary column per category — no ordinal relationship implied, but can blow up dimensionality with high-cardinality features.
- **Ordinal encoding:** maps categories to integers reflecting a real order (e.g., low/medium/high) — wrong to use when categories have no natural order.
- **Target encoding:** replaces each category with the mean target value for that category — compact and powerful for high-cardinality features, but **prone to target leakage**: a category's encoding is computed using the very target values you're trying to predict, especially problematic for rare categories with few samples (can essentially memorize the training target).
- **Safe implementation:** compute target encodings using **only out-of-fold data** (via K-fold target encoding) or add smoothing/regularization toward the global mean, so a row's encoding is never derived from its own target value.

### Q32. Feature selection with 500 features, 5,000 samples
With a high feature-to-sample ratio, overfitting risk is high, so combine several approaches: **regularization** (L1/Lasso to zero out weak features automatically), **univariate statistical selection** (correlation, chi-square, mutual information with the target as a fast filter), **tree-based feature importance** (from Random Forest/XGBoost, capturing non-linear relevance), **PCA** (dimensionality reduction if interpretability of individual features isn't required), **domain knowledge** (drop known-irrelevant or redundant features upfront), and **CV-based selection** (e.g., recursive feature elimination validated via cross-validation to avoid overfitting the selection process itself to one split).

---

## 🔥 The 10 highest-priority "whiteboard cold" answers
1. Bias–variance tradeoff + diagnosis (Q1)
2. L1 vs L2 regularization (Q2)
3. Data leakage + point-in-time leakage (Q3)
4. Logistic Regression, sigmoid, log loss (Q6)
5. Decision Tree splits via Gini/entropy (Q8)
6. Random Forest vs XGBoost (Q9/Q10)
7. Gradient boosting mechanism (Q10)
8. ROC-AUC vs PR-AUC + threshold choice (Q15/Q17)
9. PCA mathematically (Q13)
10. Hypothesis testing, p-value, Type I/II, power (Q24/Q25)

The meta-skill being tested throughout is the chain: **why → tradeoff → failure mode → mitigation** — for any technique, be ready to say *why* you'd use it, what you give up, how it breaks, and how you'd fix or detect that. 