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

|"" | Account life|
|---|---|
Fraud| 87|
Non-Fraud| 402|

The 87 days are likely due to fraud being identified late.

![Description Ratio](images/acctcutoff.png)

It is better to leave this as a scaled linear feature.

# Data Pipeline
_Used for coworking in git using merges_


--- 

# Logistic Regression

Fit and tested on a ROC curve

![roc](images/roc_curve.png)
