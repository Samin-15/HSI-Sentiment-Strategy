import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('HSI.xlsx', sheet_name='Sheet1', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'])
df['Sentiment'] = df['Up votes'] - df['Down votes']
df['Daily_Return'] = (df['Close'] - df['Open']) / df['Open']
df_clean = df.dropna(subset=['Up votes', 'Down votes']).copy().reset_index(drop=True)

df_clean['Cum_Market'] = (1 + df_clean['Daily_Return']).cumprod()
df_clean['Signal_Contrarian'] = np.where(df_clean['Sentiment'] < 0, 1, 0)
df_clean['Strategy_Return'] = df_clean['Signal_Contrarian'] * df_clean['Daily_Return']
df_clean['Cum_Strategy'] = (1 + df_clean['Strategy_Return']).cumprod()

plt.figure(figsize=(12, 6))
plt.plot(df_clean['Date'], df_clean['Cum_Market'], label='Buy & Hold HSI', linewidth=2)
plt.plot(df_clean['Date'], df_clean['Cum_Strategy'], label='Contrarian Sentiment Strategy', linewidth=2)
plt.title('Equity Curve: HSI Buy & Hold vs Contrarian Strategy (2022-2025)')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (Starting at 1)')
plt.legend()
plt.grid(True)
plt.savefig('hsi_equity_curve.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df_clean['Daily_Return'], bins=50, kde=True)
plt.title('Distribution of Daily Returns (HSI Open-to-Close)')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.savefig('hsi_return_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Market final cumulative return: {df_clean['Cum_Market'].iloc[-1]-1:.1%}")
print(f"Contrarian strategy final cumulative return: {df_clean['Cum_Strategy'].iloc[-1]-1:.1%}")
print("Equity curve saved as: hsi_equity_curve.png")
print("Return distribution saved as: hsi_return_distribution.png")