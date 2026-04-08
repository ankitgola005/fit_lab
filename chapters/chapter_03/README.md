# Chapter 3: Linear Models for Regression

This chapter explores linear regression from a **functional, probabilistic, and geometric perspective**.

---

## Experiments

| Experiment | Title                            | Concept                                      | Link                              |
| ---------- | -------------------------------- | -------------------------------------------- | --------------------------------- |
| 01         | Basis Functions & Model Capacity | Feature mapping, underfitting vs overfitting | [Open](./experiment_01/README.md) |
| 02         | Least Squares = MLE              | Gaussian likelihood, closed-form solution    | [Open](./experiment_02/README.md) |
| 03         | Bias-Variance Decomposition      | Error decomposition, model stability         | [Open](./experiment_03/README.md) |
| 04         | Regularization (Ridge)           | Ill-conditioning, weight shrinkage           | [Open](./experiment_04/README.md) |
| 05         | Bayesian Linear Regression       | Prior, posterior over weights                | [Open](./experiment_05/README.md) |
| 06         | Predictive Uncertainty           | Variance in predictions                      | [Open](./experiment_06/README.md) |

---

## Key Ideas

- Linear models become powerful via **basis functions**
- Least squares corresponds to **maximum likelihood under Gaussian noise**
- Model complexity introduces **bias-variance tradeoff**
- Ill-conditioning reveals the need for **regularization**
- Bayesian view provides **uncertainty over weights and predictions**

---

## Concept Flow

```text
Basis Functions
      ↓
Least Squares (MLE)
      ↓
Bias-Variance Tradeoff
      ↓
Regularization (Ridge)
      ↓
Bayesian Linear Regression
      ↓
Predictive Uncertainty
```

---

## Outcome

After completing this chapter, you should:

- understand regression as **projection in feature space**
- see overfitting as a **structural consequence**
- connect optimization with **probabilistic assumptions**
- anticipate why **regularization is necessary**
