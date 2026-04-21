import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('HSI.xlsx', sheet_name='Sheet1', parse_dates=['Date'])
df['Date'] = pd.to_datetime(df['Date'])
df['Sentiment'] = df['Up votes'] - df['Down votes']
df['Daily_Return'] = (df['Close'] - df['Open']) / df['Open']

df_clean = df.dropna(subset=['Up votes', 'Down votes']).copy().reset_index(drop=True)

threshold = 0
df_clean['Signal'] = np.where(df_clean['Sentiment'] < threshold, 1, 0)
df_clean['Strategy_Return'] = df_clean['Signal'] * df_clean['Daily_Return']

df_clean['Cum_Market'] = (1 + df_clean['Daily_Return']).cumprod()
df_clean['Cum_Strategy'] = (1 + df_clean['Strategy_Return']).cumprod()

def calculate_metrics(returns, name):
    total_return = (1 + returns).cumprod().iloc[-1] - 1
    annualized_return = (1 + total_return) ** (252 / len(returns)) - 1
    volatility = returns.std() * np.sqrt(252)
    sharpe = annualized_return / volatility if volatility != 0 else 0
    win_rate = (returns > 0).mean()
    cum_returns = (1 + returns).cumprod()
    drawdowns = cum_returns / cum_returns.cummax() - 1
    max_dd = drawdowns.min()
    
    print(f"\n=== {name} Performance ===")
    print(f"Total Return: {total_return:.1%}")
    print(f"Annualized Return: {annualized_return:.1%}")
    print(f"Annualized Volatility: {volatility:.1%}")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Win Rate: {win_rate:.1%}")
    print(f"Max Drawdown: {max_dd:.1%}")
    print(f"Number of Trades: {df_clean['Signal'].sum()}")

calculate_metrics(df_clean['Daily_Return'], "Buy & Hold HSI")
calculate_metrics(df_clean['Strategy_Return'], "Contrarian Sentiment Strategy")

plt.figure(figsize=(12, 6))
plt.plot(df_clean['Date'], df_clean['Cum_Market'], label='Buy & Hold HSI', linewidth=2)
plt.plot(df_clean['Date'], df_clean['Cum_Strategy'], label=f'Contrarian Strategy (Sentiment < {threshold})', linewidth=2)
plt.title('Final Equity Curve - HSI Contrarian Sentiment Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)
plt.savefig('hsi_final_equity_curve.png', dpi=300, bbox_inches='tight')
plt.show()

print("Final equity curve saved as: hsi_final_equity_curve.png")