# fraud_detection_events
Fraud Detection Model for &lt;event-company>. Data is not included due to confidentiality.

---

# Pre-processing

---

Identify Fraudulent Response variable

```python
df['fraud'] = df['acct_type'].str.contains("fraud")
```

---

### Feature Selection

---
Short Descriptions ('body_length')

Fraudulent descriptions are most likely to have descriptions below 23 characters.

![Description Ratio](images/cutoff.png)

---
Account life

```python
df['account_life'] = df['event_created'] - df['user_created']
df['account_life'] = df['account_life'].dt.days
```

![Ratio for fraud to not-fraud](images/feature_imp.png)


Relative ratios of features for fraud and not-fraud

| Feature | Fraud | Not Fraud |
| --------| ----- | --------- |
| Account life| 0.18 | 0.82|
| fb_published| 0.13| 0.86|
|org_facebook |0.1|0.99|
|org_twitter|0.04|0.95|
|has_analytics|0.03|0.96|
|payout_type (exists)|0.4|0.6|
|event_life|0.39|0.6|
|Unused| | |
|listed(%)|0.49|0.51|
|show_map (%) |0.46 | 0.54|
|has_logo (%)| 0.43| 0.57 |


The 87 days are likely due to fraud being identified late.

![Description Ratio](images/acctcutoff.png)


It is better to leave this as a scaled linear feature.


---
# Data Pipeline
_Used for coworking in git using merges_


---

# Logistic Regression

Fit and tested on a ROC curve

![roc](images/roc_curve.png)

Optimal Threshold was 0.3 for our purposes.  

We lost accuracy by selecting a good threshold - but the intent was to capture more true positives.

---

Observed high p-values for some features
![pvalues](images/pvalues.png)


# Gradient Boost

Tried, but did not give much improvement in confusion_matrix after GridSearch.

# Random Forests

Train-Test Split: 0.75-0.25
Model parameters used -

```python
from sklearn.ensemble import RandomForestClassifier as RF
rf = RF(n_estimators=50, min_samples_split=20, min_samples_leaf=1,   min_impurity_split=1e-5, max_depth = 30, oob_score=True)
rf.score(X_test, y_test)
= 0.986
print 'Confusion matrix :\n', confusion_matrix(y_test, y_pred)
```

|Predcted |Observed  |
|--|--|
|TP: 288 | FP: 19 |
|FN: 30   | TN: 3242|
