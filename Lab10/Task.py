import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix,
                             mean_absolute_error, mean_squared_error, r2_score)
from sklearn.utils import resample

df_raw = pd.read_csv('bank_data.csv')

df_raw = df_raw[df_raw['user_id'].notna()].copy()
print(f"Records with valid user_id: {len(df_raw)}")

df_raw.dropna(how='all', inplace=True)

target_class = 'approved'
target_reg = 'approved_loan_amount'

print("\nData Types and Info")
print(df_raw.info())

print("\nFirst 5 rows")
print(df_raw.head())

print("\nMissing Values Count (after filtering)")
print(df_raw.isnull().sum())

numeric_cols = df_raw.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df_raw.select_dtypes(include=['object', 'string']).columns.tolist()
print(f"\nNumeric columns: {numeric_cols}")
print(f"Categorical columns: {categorical_cols}")

irrelevant = ['user_id', 'address', 'email']
df_raw.drop(columns=[col for col in irrelevant if col in df_raw.columns], inplace=True)

if 'date_of_birth' in df_raw.columns:
    df_raw['date_of_birth'] = pd.to_datetime(df_raw['date_of_birth'], errors='coerce')
    current_year = datetime.now().year
    df_raw['age'] = current_year - df_raw['date_of_birth'].dt.year
    df_raw.drop('date_of_birth', axis=1, inplace=True)
    df_raw['age'] = df_raw['age'].fillna(df_raw['age'].median())
    numeric_cols.append('age')
    print("Created 'age' from date_of_birth.")

for col in ['capital_gain', 'capital_loss']:
    if col in df_raw.columns:
        df_raw[col] = df_raw[col].apply(lambda x: max(0, x) if pd.notnull(x) else x)

initial_len = len(df_raw)
df_raw.drop_duplicates(inplace=True)
print(f"Removed {initial_len - len(df_raw)} duplicate rows.")

X = df_raw.drop(columns=[target_class, target_reg])
y_class = df_raw[target_class] if target_class in df_raw.columns else None
y_reg = df_raw[target_reg] if target_reg in df_raw.columns else None

num_imputer = SimpleImputer(strategy='median')
num_features = X.select_dtypes(include=['int64', 'float64']).columns
X[num_features] = num_imputer.fit_transform(X[num_features])

cat_imputer = SimpleImputer(strategy='most_frequent')
cat_features = X.select_dtypes(include=['object', 'string']).columns
if len(cat_features) > 0:
    X[cat_features] = cat_imputer.fit_transform(X[cat_features])

df_clean = X.copy()
df_clean[target_class] = y_class
df_clean[target_reg] = y_reg

df_clean.dropna(subset=[target_class, target_reg], inplace=True)
print(f"Clean dataset shape: {df_clean.shape}")

plt.figure()
df_clean[target_class].value_counts().plot(kind='bar', color=['red', 'green'])
plt.title('Loan Approval Status Distribution')
plt.xlabel('Approved (0=No    1=Yes )')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

if 'marital_status' in df_clean.columns:
    plt.figure()
    df_clean['marital_status'].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%')
    plt.title('Top 5 Marital Statuses')
    plt.ylabel('')
    plt.show()

if 'age' in df_clean.columns:
    plt.figure()
    sns.boxplot(x=target_class, y='age', data=df_clean)
    plt.title('Age Distribution by Loan Approval')
    plt.show()

approved_df = df_clean[df_clean[target_class] == 1]
if 'capital_gain' in approved_df.columns and len(approved_df) > 0:
    plt.figure()
    plt.scatter(approved_df['capital_gain'], approved_df[target_reg], alpha=0.5)
    plt.xlabel('Capital Gain')
    plt.ylabel('Approved Loan Amount')
    plt.title('Capital Gain vs Loan Amount (Approved Only)')
    plt.show()

numeric_clean = df_clean.select_dtypes(include=[np.number]).columns
if len(numeric_clean) > 1:
    plt.figure(figsize=(12, 8))
    corr = df_clean[numeric_clean].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.25)
    plt.title('Correlation Matrix of Numeric Features')
    plt.show()

X = df_clean.drop(columns=[target_class, target_reg])
y_class = df_clean[target_class]
y_reg = df_clean[target_reg]

cat_cols = X.select_dtypes(include=['object', 'string']).columns
X_encoded = pd.get_dummies(X, columns=cat_cols, drop_first=True)
print(f"After encoding, feature shape: {X_encoded.shape}")

scaler = StandardScaler()
numeric_cols_encoded = X_encoded.select_dtypes(include=[np.number]).columns
X_scaled = X_encoded.copy()
X_scaled[numeric_cols_encoded] = scaler.fit_transform(X_encoded[numeric_cols_encoded])
print("Numeric features standardized (mean=0, std=1).")

X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
    X_scaled, y_class, test_size=0.2, random_state=42, stratify=y_class
)

dt_clf = DecisionTreeClassifier(max_depth=10, random_state=42)
dt_clf.fit(X_train_cls, y_train_cls)
y_pred_cls = dt_clf.predict(X_test_cls)

print("\nClassification (Imbalanced Dataset)  Decision Tree")
print(f"Accuracy: {accuracy_score(y_test_cls, y_pred_cls):.4f}")
print("\nClassification Report:\n", classification_report(y_test_cls, y_pred_cls))
print("Confusion Matrix:")
cm = confusion_matrix(y_test_cls, y_pred_cls)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - Imbalanced (Decision Tree)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

reg_df = df_clean[df_clean[target_class] == 1].copy()
if reg_df.empty:
    raise ValueError("No approved loans for regression.")
print(f"\nApproved loans for regression: {len(reg_df)}")

X_reg = reg_df.drop(columns=[target_class, target_reg])
y_reg_target = reg_df[target_reg]

cat_reg = X_reg.select_dtypes(include=['object', 'string']).columns
X_reg_enc = pd.get_dummies(X_reg, columns=cat_reg, drop_first=True)
# Ensure same columns as X_encoded
for col in X_encoded.columns:
    if col not in X_reg_enc.columns:
        X_reg_enc[col] = 0
X_reg_enc = X_reg_enc[X_encoded.columns]
scaler_reg = StandardScaler()
X_reg_scaled = X_reg_enc.copy()
X_reg_scaled[X_encoded.columns] = scaler_reg.fit_transform(X_reg_enc[X_encoded.columns])

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg_scaled, y_reg_target, test_size=0.2, random_state=42
)

lin_reg = LinearRegression()
lin_reg.fit(X_train_reg, y_train_reg)
y_pred_reg = lin_reg.predict(X_test_reg)

print("\nRegression (Approved Loans)  Linear Regression")
print(f"MAE: {mean_absolute_error(y_test_reg, y_pred_reg):.2f}")
print(f"MSE: {mean_squared_error(y_test_reg, y_pred_reg):.2f}")
print(f"R2 Score: {r2_score(y_test_reg, y_pred_reg):.4f}")

plt.figure()
plt.scatter(y_pred_reg, y_test_reg - y_pred_reg, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Loan Amount')
plt.ylabel('Residuals')
plt.title('Residual Plot - Linear Regression')
plt.show()

approved = df_clean[df_clean[target_class] == 1]
rejected = df_clean[df_clean[target_class] == 0]
n_approved = len(approved)
n_rejected = len(rejected)
print(f"\nOriginal class sizes - Approved: {n_approved}, Rejected: {n_rejected}")

sample_size = min(500, n_approved, n_rejected)
print(f"Using balanced size: {sample_size}")

approved_bal = resample(approved, replace=False, n_samples=sample_size, random_state=42)
rejected_bal = resample(rejected, replace=False, n_samples=sample_size, random_state=42)
df_balanced = pd.concat([approved_bal, rejected_bal]).sample(frac=1, random_state=42)
print(f"Balanced dataset shape: {df_balanced.shape}")

X_bal = df_balanced.drop(columns=[target_class, target_reg])
y_bal = df_balanced[target_class]
cat_bal = X_bal.select_dtypes(include=['object', 'string']).columns
X_bal_enc = pd.get_dummies(X_bal, columns=cat_bal, drop_first=True)
for col in X_encoded.columns:
    if col not in X_bal_enc.columns:
        X_bal_enc[col] = 0
X_bal_enc = X_bal_enc[X_encoded.columns]
scaler_bal = StandardScaler()
X_bal_scaled = X_bal_enc.copy()
X_bal_scaled[X_encoded.columns] = scaler_bal.fit_transform(X_bal_enc[X_encoded.columns])

X_train_bal, X_test_bal, y_train_bal, y_test_bal = train_test_split(
    X_bal_scaled, y_bal, test_size=0.2, random_state=42, stratify=y_bal
)

dt_bal = DecisionTreeClassifier(max_depth=10, random_state=42)
dt_bal.fit(X_train_bal, y_train_bal)
y_pred_bal = dt_bal.predict(X_test_bal)

print("\nClassification (Balanced Dataset)  Decision Tree")
print(f"Accuracy: {accuracy_score(y_test_bal, y_pred_bal):.4f}")
print("\nClassification Report:\n", classification_report(y_test_bal, y_pred_bal))
print("Confusion Matrix:")
cm_bal = confusion_matrix(y_test_bal, y_pred_bal)
sns.heatmap(cm_bal, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - Balanced (Decision Tree)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print("\n Model_Comparison")
print(f"Imbalanced Accuracy (Decision Tree): {accuracy_score(y_test_cls, y_pred_cls):.4f}")
print(f"Balanced Accuracy   (Decision Tree): {accuracy_score(y_test_bal, y_pred_bal):.4f}")

print("\nConclusion:")
print("The balanced dataset provides a more honest assessment of the model's ability to detect rejected loans.")
print("Recommended: Use the Decision Tree trained on the balanced dataset for loan approval prediction.")
print("For regression (loan amount estimation) Linear Regression is suitable, but consider adding more features if R² is low.")
