import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

print("📊 === Titanic Data Summary Report ===\n")

print("🔢 Shape of dataset (rows, columns):", df.shape)

print("\n🚫 Missing Values Per Column:")
print(df.isnull().sum())

print("\n📈 Basic Statistics:")
print(df.describe())

print("\n👥 Average Age by Survival Status:")
print(df.groupby('Survived')['Age'].mean())

print("\n🛳️ Top 5 Embarkation Ports:")
print(df['Embarked'].value_counts().head(5))

summary = df.describe()
summary.to_excel("titanic_summary.xlsx")
print("\n📁 Summary exported to titanic_summary.xlsx")

df['Survived'].value_counts().plot(kind='bar', title='Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()
