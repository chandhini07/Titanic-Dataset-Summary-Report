import pandas as pd

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
