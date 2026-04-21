# HSI Social-Media Sentiment Strategy - Research Notes

## Day 1 Summary

**What is open-to-close and why we chose it?**  
Open-to-close return is the percentage change from the market open price (9:30 AM HKT) to the close price (4:00 PM HKT) on the same trading day. I chose it because it completely removes overnight/gap risk - big news can hit while the market is closed and cause the next day's open to jump up or down a lot, which we can't control. This makes the strategy much cleaner and lower risk, which is perfect for a simple quant intraday approach.

**What does negative correlation mean for trading?**  
The correlation between the crowd Sentiment score and the actual Daily_Return is negative (around -0.065). That means when social media users are very bullish (high Up votes), the HSI actually tends to do slightly worse that day. When they are bearish (high Down votes), the HSI tends to do better. This is a classic contrarian signal - the crowd is often wrong at the extremes, so we can make money by going against the majority vote.

**Explain compounding with your own example.**  
Compounding is when your profits start earning profits too. For example, if I make +1% every trading day for 252 days, just adding them up gives +252%, but in reality the money grows much more because each day's gain is on the new higher amount. The formula (1 + 0.01)^252 - 1 gives about +1,126%. Even a small daily edge becomes huge over time when you let it compound.

**One thing that still confuses you.**  
I still need to understand how we should handle transaction costs, slippage, and whether we should add a stronger threshold like |Sentiment| > 0.2 instead of just Sentiment < 0. Also, how would this strategy behave in different market regimes (bull vs bear market)?

## Overall Reflection
I started this project with zero knowledge of trading or sentiment analysis. After Day 1, I now understand why open-to-close is used, what contrarian sentiment means, and why compounding is so powerful in quant strategies. The boxplot clearly shows the edge, and I'm excited to build the full backtest in the next days for the DataLouder application.


## Day 2 Summary

**Exploratory Data Analysis (EDA):**  
Today I created equity curves to visualise compounding and compared the contrarian strategy (long only when Sentiment < 0) to buy-and-hold. The equity curve clearly shows the strategy significantly outperforms the market.

**Key Results from Plots:**
- Equity Curve: Buy & Hold HSI = **+9.7%** cumulative return
- Contrarian Sentiment Strategy = **+30.4%** cumulative return
- The orange line (strategy) grows much smoother and ends substantially higher than the blue buy-and-hold line.
- Return distribution is roughly normal but with some fat tails, which is typical for daily market returns.

**Key Insights:**
- Compounding works powerfully - even a small daily edge turns into a large long-term advantage.
- The strategy reduces drawdowns compared to the market while capturing upside on bearish crowd days.

**One new question:**  
How much better does the strategy become with a sentiment threshold (e.g. Sentiment < -0.2) or by adding stop-loss / volatility filters?