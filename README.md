# HSI Contrarian Sentiment Trading Strategy

**Project for DataLouder Quant Trader / Research Engineer Internship Application**  
**Candidate:** Samin Yasir  
**Date:** April 2026

### Overview
This repository implements a data-driven **contrarian trading strategy** for the Hang Seng Index (HSI) using pre-market social-media vote data.  
The strategy exploits the negative correlation between crowd sentiment and same-day open-to-close returns.

### Key Results (Day 2)
- Buy & Hold HSI: **+9.7%** cumulative return
- Contrarian Strategy: **+30.4%** cumulative return

### Key Files
- `hsi_data_exploration.py` → Data loading & boxplot
- `hsi_eda_visualization.py` → Equity curve + return distribution
- `hsi_contrarian_backtest.py` → Final backtest (added Day 3)
- Saved plots: `hsi_sentiment_boxplot.png`, `hsi_equity_curve.png`, `hsi_return_distribution.png`, `hsi_final_equity_curve.png`

### Strategy Highlights
- **Signal**: Long only when crowd is bearish (Sentiment < 0)
- **Horizon**: Intraday (open-to-close — no overnight gap risk)

### How to Run
```bash
python hsi_data_exploration.py
python hsi_eda_visualization.py
python hsi_contrarian_backtest.py