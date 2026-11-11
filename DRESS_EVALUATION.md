# Dress recommendation coursework evaluation

The archived [R exercise](Simplilearn_1.R) created a split but fitted on the full dataset. It also reused plotting variables from a different exercise. The follow-up [Python evaluation](evaluate_dress.py) uses a stratified 375/125 split, fits preprocessing on the training rows, excludes Dress_ID, and compares logistic regression with a majority-class baseline.

| Model | Held-out accuracy | Held-out balanced accuracy |
|---|---:|---:|
| Majority baseline | 0.5840 | 0.5000 |
| Logistic regression | 0.5440 | 0.5183 |

The logistic model had lower accuracy than the baseline on this split. The small balanced-accuracy difference is descriptive and does not establish a reliable improvement.

Run `python evaluate_dress.py` from the repository root. The recorded run used pandas 2.2.3 and scikit-learn 1.8.0 with the committed CSV.
