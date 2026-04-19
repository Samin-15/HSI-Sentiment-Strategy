import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('HSI.xlsx', sheet_name='Sheet1', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'])
df['Sentiment'] = df['Up votes'] - df['Down votes']
df['Daily_Return'] = (df['Close'] - df['Open']) / df['Open']

df_clean = df.dropna(subset=['Up votes', 'Down votes']).copy().reset_index(drop=True)

print("HSI Sentiment Data Exploration Results:")
print(f"Total days in file: {len(df)}")
print(f"Days with votes: {len(df_clean)}")
print(f"Sentiment vs Return correlation: {df_clean['Sentiment'].corr(df_clean['Daily_Return']):.4f}")  # expect negative ≈ -0.065

print("\nAverage daily return when crowd BULLISH:", df_clean[df_clean['Sentiment'] > 0]['Daily_Return'].mean())
print("Average daily return when crowd BEARISH:", df_clean[df_clean['Sentiment'] < 0]['Daily_Return'].mean())

plt.figure(figsize=(10, 5))
sns.boxplot(x=(df_clean['Sentiment'] > 0), y=df_clean['Daily_Return'])
plt.title('Open-to-Close Return: Crowd Bullish vs Bearish')
plt.xlabel('Is crowd bullish? (Sentiment > 0)')
plt.ylabel('Daily Return')
plt.savefig('hsi_sentiment_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()
