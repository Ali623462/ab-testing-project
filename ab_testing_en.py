import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Step 1: Read the datasets
dataframe_control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
dataframe_test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()

# Function to check data
def check_df(dataframe, head=5):
    print(dataframe.shape)
    print(dataframe.dtypes)
    print(dataframe.head())
    print(dataframe.tail())
    print(dataframe.isnull().sum())
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df_control)
check_df(df_test)

# Step 2: Merge the datasets
df_control["group"] = "control"
df_test["group"] = "test"
df = pd.concat([df_control, df_test], axis=0, ignore_index=False)

# Step 3: Define hypotheses
# H0: M1 = M2 (No significant difference between the purchase means of the two groups)
# H1: M1 != M2 (Significant difference between the purchase means of the two groups)

# Step 4: Analyze group means
print(df.groupby("group").agg({"Purchase": "mean"}))

# Step 5: Check assumptions for hypothesis testing

# Normality assumption
test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Shapiro Test (Control) - Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])
print('Shapiro Test (Test) - Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Variance homogeneity
test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
print('Levene Test - Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Step 6: Perform the independent two-sample t-test
test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)
print('T-Test - Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Step 7: Interpretation
# Based on the p-value > 0.05, we fail to reject the null hypothesis.
# There is no statistically significant difference in purchase means between the groups.
