import streamlit as st
import yfinance as yf
import pandas as pd

from st_pages import add_page_title

st.sidebar.write(
    '''
    # Dashboard Saham

    Made by Fadhil R

    '''
)

add_page_title(layout="wide")

CHOICES = {"META": "Facebook (META)", "AMZN": "Amazon (AMAZN)", "AAPL": "Apple (AAPL)", "NFLX": "Netflix (NFLX)", "GOOG": "Google (GOOG)"}


def format_func(option):
    return CHOICES[option]



"### Konfigurasi"
# tickerSymbol = st.selectbox('Select ticker: ', ('META', 'AMZN', 'AAPL', 'NFLX', 'GOOG',))
tickerSymbol = st.selectbox("Select ticker", options=list(CHOICES.keys()), format_func=format_func)
tickerInterval = st.selectbox('Select Interval:', ('1h','1d','5d','1wk','1mo','3mo'))
tickerStartDate = st.date_input('Pick Start Date') 
tickerEndDate = st.date_input('Pick End Date') 

tickerDf = yf.Ticker(tickerSymbol).history(interval=tickerInterval,start=tickerStartDate, end=tickerEndDate)

"### Preview Data"
st.dataframe(tickerDf)

"### Closing Price"
st.line_chart(tickerDf['Close'], use_container_width=True)


"## Trading Volume"
st.bar_chart(tickerDf['Volume'], use_container_width=True)



