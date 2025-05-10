# 🎯 A/B Test: Comparison of Bidding Methods on Conversion

This project compares two Facebook advertising bid strategies for an e-commerce website: **Maximum Bidding** and **Average Bidding**.

## 📌 Business Problem

Facebook introduced a new bid strategy called "Average Bidding" as an alternative to the existing "Maximum Bidding." The client wants to know whether this new strategy leads to higher conversions. An A/B test was run for one month, and results are analyzed based on the **Purchase** metric, which is the main success criterion.

## 🧾 Dataset

- Source: `ab_testing.xlsx` containing **Control Group** (Maximum Bidding) and **Test Group** (Average Bidding)
- Variables:
  - `Impression`: Number of ad views
  - `Click`: Number of clicks on the ad
  - `Purchase`: Number of purchases after clicks
  - `Earning`: Revenue after purchases

## 🔍 Analysis Steps

1. Data loading and initial inspection
2. Merging Control and Test groups
3. Normality test (Shapiro-Wilk)
4. Homogeneity of variances test (Levene)
5. Independent two-sample t-test

## 📊 Hypothesis Testing

- **H0**: There is no significant difference between the purchase means of control and test groups.
- **H1**: There is a significant difference between the purchase means of control and test groups.

| Test | p-value | Result |
|------|---------|--------|
| Normality (Shapiro) | 0.5891 | Fail to reject H0 |
| Homogeneity (Levene) | 0.1083 | Fail to reject H0 |
| T-Test (ttest_ind) | 0.3493 | Fail to reject H0 |

### 🧠 Interpretation

There is no statistically significant difference between the two groups. Therefore:
- The client can choose either strategy.
- The observed difference in means could be due to chance.
- Further analysis using different metrics (e.g., `Click`) is recommended.

## 📂 Project Files

| File | Description |
|------|-------------|
| `ab_testing.xlsx` | Dataset (Control & Test sheets) |
| `ab_testing.py` | Python script with analysis |
| `ab_test_sonuclar.txt` | Text output of the statistical tests |

## 🛠️ Used Libraries

```txt
pandas
numpy
matplotlib
scipy
```

## 👤 Author

- Ali  
- This project was developed as part of a data science portfolio.
