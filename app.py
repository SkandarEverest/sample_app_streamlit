import streamlit as st
import yfinance as yf
import pandas as pd

st.sidebar.write(
    '''
    # Simple Stock Price App
    Made with **streamlit** by Fadhil Rausyanfikr
    '''
)

tickerSymbol = st.sidebar.selectbox('Select ticker: ', ('GOOG', 'AAPL', 'MSFT'))
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(interval='1d',start='2022-1-1', end='2022-12-31')

"## Closing Price"
st.line_chart(tickerDf['Close'], use_container_width=True)

"## Trading Volume"
st.bar_chart(tickerDf['Volume'], use_container_width=True)