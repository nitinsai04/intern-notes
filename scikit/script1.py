import pandas as pd

# Load dataset
df = pd.read_csv('Resume.csv')

# View basic info
print("Dataset shape:", df.shape)
print("Columns:", df.columns)

# Sample data preview
print(df[['Resume_str', 'Category']].head())

# Count of each category
print("\nCategory distribution:")
print(df['Category'].value_counts())
