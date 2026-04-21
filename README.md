# HSI Contrarian Social Media Sentiment Trading Strategy

**Project for DataLouder Quant Trader / Research Engineer (Intern) Application**  
**Candidate:** Samin Yasir  
**Date:** April 2026

### Overview
This repository implements a **data-driven contrarian trading strategy** for the Hang Seng Index (HSI) using pre-market social-media Up/Down vote data.  
The strategy exploits the negative correlation between crowd sentiment and same-day open-to-close returns.

### Key Results (Final Backtest)
- **Buy & Hold HSI**: +9.7% total return, Sharpe 0.21, Max Drawdown -29.3%
- **Contrarian Strategy** (long only when Sentiment < 0): **+30.4%** total return, **Sharpe 1.04**, Max Drawdown **-13.6%**

The strategy significantly outperforms the market with much better risk-adjusted returns and lower drawdown.

### Key Files
- `hsi_data_exploration.py` → Data loading, cleaning & sentiment boxplot
- `hsi_eda_visualization.py` → Equity curve + return distribution plots
- `hsi_contrarian_backtest.py` → **Final backtest** with full metrics (Sharpe, volatility, win rate, max drawdown)
- Saved high-resolution plots:
  - `hsi_sentiment_boxplot.png`
  - `hsi_equity_curve.png`
  - `hsi_return_distribution.png`
  - `hsi_final_equity_curve.png`

### Strategy Highlights
- **Signal**: Long at Open, sell at Close when crowd Sentiment < 0 (bearish)  
- **Horizon**: Intraday only (no overnight gap risk)  
- **Threshold**: Simple rule (Sentiment < 0) chosen after testing stricter options

### How to Run
```bash
python hsi_data_exploration.py
python hsi_eda_visualization.py
python hsi_contrarian_backtest.py