# HSI Contrarian Sentiment Trading Strategy

**Project for DataLouder Quant Trader / Research Engineer Internship Application**  
**Candidate:** Samin Yasir  
**Date:** April 2026

### Overview
This repository implements a data-driven contrarian trading strategy for the Hang Seng Index (HSI) using pre-market social-media vote data. The strategy exploits the negative correlation between crowd sentiment and same-day open-to-close returns.

### Key Files
- `hsi_data_exploration.py` → Data loading, cleaning, sentiment calculation and visualisation
- `research_notes.md` → Detailed research notes and insights
- `hsi_eda_visualization.py` (added on Day 2)
- `hsi_contrarian_backtest.py` (added on Day 3)

### Strategy Highlights
- **Signal**: Contrarian (long only when crowd is bearish)
- **Horizon**: Intraday (open-to-close)
- **Backtest Period**: 2022–2025
- Full backtest metrics, equity curves and performance report included.

### How to Run
```bash
python hsi_data_exploration.py