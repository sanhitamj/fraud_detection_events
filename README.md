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

| Feature | Fraud | Not Fraud |
| --------| ----- | --------- |
| Account life| 82 | 402 (days)|
| fb_published(%)| 2| 13|
|org_facebook (mean)|1|8.6|
|org_twitter(mean)|0.29|4.6|
|has_analytics(%)|0.3|8|
|payout_type (exists %)|65|99|
|previous_payout (mean of amount)|183|2340|
|Unused| | |
|listed(%)|83|85|
|has_header (%)|7| 21|
|show_map (%) |75 | 85|
|has_logo (%)| 64| 86 |


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

|--|--|
|TN: 3242 | FP: 19 |
|FN: 30   | TP: 288|
