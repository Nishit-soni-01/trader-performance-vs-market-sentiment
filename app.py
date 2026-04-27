import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader vs Sentiment Dashboard", layout="wide")

st.title("Hyperliquid Trader Performance vs Market Sentiment")
st.markdown("This dashboard explores how Fear and Greed impact trader behavior.")

@st.cache_data
def load_data():
    
    df_sentiment = pd.read_csv('fear_greed_index.csv')
    df_history = pd.read_csv('historical_data.csv')
    
    df_sentiment['date'] = pd.to_datetime(df_sentiment['date'])
    def simplify_sentiment(x):
        if 'Fear' in x: return 'Fear'
        elif 'Greed' in x: return 'Greed'
        else: return 'Neutral'
    df_sentiment['Sentiment'] = df_sentiment['classification'].apply(simplify_sentiment)
    
    df_history['Datetime'] = pd.to_datetime(df_history['Timestamp IST'], format='%d-%m-%Y %H:%M')
    df_history['date'] = pd.to_datetime(df_history['Datetime'].dt.date)
    
    merged = pd.merge(df_history, df_sentiment[['date', 'value', 'Sentiment']], on='date', how='inner')
    return merged

df = load_data()


st.sidebar.header("Filter Data")
sentiment_filter = st.sidebar.multiselect("Select Market Sentiment", options=df['Sentiment'].unique(), default=df['Sentiment'].unique())

filtered_df = df[df['Sentiment'].isin(sentiment_filter)]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Trades", f"{len(filtered_df):,}")
col2.metric("Total PnL Generated", f"${filtered_df['Closed PnL'].sum():,.2f}")
col3.metric("Average Trade Size", f"${filtered_df['Size USD'].mean():,.2f}")

# Charts
st.subheader("PnL Distribution by Sentiment")
fig, ax = plt.subplots(figsize=(10, 4))
sentiment_pnl = filtered_df.groupby('Sentiment')['Closed PnL'].sum().reset_index()
sns.barplot(data=sentiment_pnl, x='Sentiment', y='Closed PnL', palette='viridis', ax=ax)
st.pyplot(fig)

st.markdown("""
### Strategy Recommendation
* **Fear Days:** Data shows PnL is highest here. Advise algorithmic traders to increase capital deployment during 'Fear' indexes.
* **Greed Days:** Market is choppy. Advise tightening stop-losses and lowering leverage.
""")
