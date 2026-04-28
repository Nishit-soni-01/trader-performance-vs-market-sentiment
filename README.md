# Trader Performance Vs. Market Sentiment Analysis 📊

**Applicant:** - Nishit soni

**Role applied for:** Data Science / Analytics Intern @ Primetrade.ai 

**Estimated Effort:** ~6 hours  

## 🎯 Objective
This project analyzes how cryptocurrency market sentiment (specifically the Fear & Greed Index) relates to trader behavior and performance on Hyperliquid. The goal is to uncover behavioral patterns to inform smarter, algorithmic trading strategies and risk management protocols.

---

## 🛠️ Methodology & Data Preparation
1. **Data Ingestion & Cleaning:** Loaded Bitcoin Market Sentiment and Hyperliquid Historical Trader Data. Verified data integrity (0 nulls, 0 duplicates).
2. **Alignment:** Standardized timestamps (`Timestamp IST` parsing) and aligned both datasets using a daily-level `inner` join.
3. **Feature Engineering:** Aggregated raw historical trades into daily performance metrics per account:
   * **Daily PnL**
   * **Win Rate** (Winning trades / All closed trades)
   * **Average Trade Size (USD)**
   * **Trade Frequency** (Trades per day)
   * **Long/Short Ratio** (Buys / Sells)
4. **Behavioral Archetyping (Bonus):** Applied Unsupervised Machine Learning (`K-Means Clustering`) to group traders into structural archetypes (Whales, Scalpers, Retail).

---

## 💡 Key Insights (Backed by Data)

By segmenting the traders based on Frequency, Consistency, and Capital Size, the data revealed three major patterns:

<img width="5353" height="1453" alt="segmentation_insights" src="https://github.com/user-attachments/assets/011d614b-c166-4152-971e-e5d387339c8a" />


1. **Volatility strictly favors the Hyper-Active Trader (Frequency Segment)**
   * **Evidence:** "Frequent" traders generate massive spikes in PnL specifically during **Fear** days (high volatility). Conversely, "Infrequent" traders perform horribly during Fear days but show stable returns during Greed days. 
   * **Takeaway:** Passive/swing traders get crushed by volatility during Fear markets, whereas active algorithmic scalpers thrive on the wide price swings.

2. **Inconsistent Traders get lucky in Greed Markets (Consistency Segment)**
   * **Evidence:** "Consistent Winners" (>50% historical win rate) maintain steady profitability across *both* Fear and Neutral markets. However, "Inconsistent" traders show a massive spike in profitability *only* during **Greed** days. 
   * **Takeaway:** Greed days are characterized by strong, singular upward trends where even inconsistent traders profit by blindly buying. Fear days ruthlessly wipe out inconsistent traders, leaving only skilled users profitable.

3. **Whales dictate the Fear Market (Capital Size Segment)**
   * **Evidence:** "Whales" (top 50% by avg trade size) completely dominate PnL generation during **Fear** days, while "Retail" users show flat/negative PnL. 
   * **Takeaway:** When the market enters panic/Fear, Retail scales down risk and steps away. Whales aggressively step in to absorb the panic selling, yielding massive outsized returns.

## 🚀 Actionable Output & Strategy Recommendations

Based on the empirical findings, I propose the following two data-driven strategy "rules of thumb" for algorithmic risk management:

### Strategy 1: The "Volatility Harvester" Rule (For Active/Whale Traders)
* **Rule:** "During **Fear** days, dynamically increase trade frequency limits and position sizing constraints exclusively for the *Frequent* and *Whale* trader segments."
* **Rationale:** Since high-frequency and well-capitalized traders generate their highest Alpha during Fear markets by aggressively "buying the dip", risk-management systems should actually loosen constraints on these specific segments during market panic to maximize profitability.

### Strategy 2: The "Trend-Rider Shield" Rule (For Retail/Swing Traders)
* **Rule:** "During **Fear** days, strictly reduce leverage and mandate tighter stop-losses for *Inconsistent* and *Infrequent* retail segments. Only increase their capital exposure during **Greed** days."
* **Rationale:** Inconsistent and Infrequent (Retail) traders are effectively wiped out by the volatility of Fear days but show highly profitable spikes during Greed days. Algorithms targeting these users should restrict over-leveraging during panics and encourage trend-following allocations when the index shifts back to Greed.

---

# 📊 Bitcoin & Trader Data Resources

## 1) Bitcoin Market Sentiment (Fear/Greed) 
- **Link:** [Download Bitcoin Market Sentiment Data](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing)

---

## 2) Historical Trader Data (Hyperliquid)
- **Link:** [Download Historical Trader Data](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing)


## 💻 Repository Structure & How to Run

### Files Included:
* `notebook.ipynb`: The core Jupyter Notebook containing data prep, analysis, segmentation, and K-Means clustering.
* `app.py`: A lightweight Streamlit dashboard for interactive exploration (Bonus).
* `historical_data.csv`: Raw Hyperliquid trade data.
* `fear_greed_index.csv`: Daily Bitcoin sentiment data.

### Setup Instructions:
1. Clone this repository to your local machine.
2. Ensure you have the required Python libraries installed:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn streamlit
