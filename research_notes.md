# HSI Social-Media Sentiment Strategy - Research Notes

## Day 1 Summary

**What is open-to-close and why we chose it?**  
Open-to-close return measures the price change from market open (9:30 AM) to close (4:00 PM) on the same day. We use it because it removes overnight/gap risk - news that hits while the market is closed can cause big jumps at the next open, which we cannot control. This makes the strategy cleaner and lower-risk for an intraday quant approach.

**What does negative correlation mean for trading?**  
The correlation between Sentiment and Daily_Return is negative (≈ -0.065). This means when the crowd is bullish (high Up votes), the HSI tends to perform worse that day, and when the crowd is bearish (high Down votes), the HSI tends to perform better. This is a classic contrarian signal - we can profit by doing the opposite of what social-media users vote.

**Explain compounding with your own example.**  
Compounding is when returns build on previous returns. Example: If I make +1% every trading day for 252 days, simple addition gives +252%, but real compounding is (1 + 0.01)^252 - 1 ≈ +1,126%. Even small daily edges become huge over time when you reinvest the profits.

**One thing that still confuses you.**  
I still want to understand how we add transaction costs and slippage in the backtest, and whether we should use a sentiment threshold (e.g. |Sentiment| > 0.2) instead of just >0.
