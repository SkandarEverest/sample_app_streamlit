import streamlit as st
import yfinance as yf
import pandas as pd

st.sidebar.write(
    '''
    # Dashboard Saham

    Melakukan analisis saham pada GOOGLE , APPLE, dan MICROSOFT

    Sumber Data Eksternal : yahoo finance

    '''
)

tickerSymbol = st.sidebar.selectbox('Select ticker: ', ('GOOG', 'AAPL', 'MSFT'))
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(interval='1d',start='2022-1-1', end='2022-12-31')

"## Closing Price"
st.line_chart(tickerDf['Close'], use_container_width=True)

if (tickerSymbol == 'GOOG'):
    st.write("Plot tersebut menampilkan perubahan harga penutupan dalam rentang tanggal 1 Januari 2022 hingga 31 Desember 2022")

    st.write("Dalam grafik ini, terlihat bahwa saham Google mengalami tren penurunan pada tahun 2022.")

if (tickerSymbol == 'AAPL'):
    st.write("Plot tersebut menampilkan perubahan harga penutupan dalam rentang tanggal 1 Januari 2022 hingga 31 Desember 2022")

    st.write("Dalam grafik ini, terlihat bahwa saham Apple mengalami tren penurunan pada tahun 2022.")

if (tickerSymbol == 'MSFT'):
    st.write("Plot tersebut menampilkan perubahan harga penutupan dalam rentang tanggal 1 Januari 2022 hingga 31 Desember 2022")

    st.write("Dalam grafik ini, terlihat bahwa saham Microsoft mengalami tren penurunan pada tahun 2022.")

"## Trading Volume"
st.bar_chart(tickerDf['Volume'], use_container_width=True)

"## Penjelasan"

if (tickerSymbol == 'GOOG'):
    st.write("Plot tersebut menampilkan volume saham dengan periode hari dalam rentang tanggal 1 Januari 2022 hingga 31 Desember 2022")

    st.write("Dalam grafik ini, terlihat bahwa volume saham Google terbesar ada pada bulan februari")

if (tickerSymbol == 'AAPL'):
    st.write("Plot tersebut menampilkan volume saham dengan periode hari dalam rentang tanggal 1 Januari 2022 hingga 31 Desember 2022")

    st.write("Dalam grafik ini, terlihat bahwa volume saham Apple terbesar ada pada bulan mei")

if (tickerSymbol == 'MSFT'):
    st.write("Plot tersebut menampilkan volume saham dengan periode hari dalam rentang tanggal 1 Januari 2022 hingga 31 Desember 2022")

    st.write("Dalam grafik ini, terlihat bahwa volume saham Microsoft terbesar ada pada bulan januari")


