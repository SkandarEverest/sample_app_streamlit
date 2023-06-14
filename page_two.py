import streamlit as st
import yfinance as yf

st.sidebar.write(
    '''
    # Dashboard Saham

    Made by Fadhil R

    '''
)

from st_pages import add_page_title

add_page_title(layout="wide")

stock = ['META', 'AMZN', 'AAPL', 'NFLX',  'GOOG']

# Tanggal awal dan akhir
start_date = '2017-01-01'
end_date = '2023-05-22'

data = yf.download(stock, start=start_date, end=end_date)

closeData = data['Close']
volumeData = data['Volume']

"### Grafik Perbandingan Harga Penutupan Saham"
st.line_chart(closeData, use_container_width=True)
"#### Penjelasan"
st.write("Plot tersebut menampilkan perubahan harga penutupan dengan interval 1 hari untuk setiap perusahaan saham yang dianalisis. Sumbu x adalah rentang tanggal dari 1 Januari 2017 hingga 31 Desember 2022, sedangkan sumbu y adalah harga penutupan saham untuk masing-masing perusahaan.")

st.write("1. Dalam grafik ini, terlihat bahwa saham AMZN, AAPL, dan GOOG mengalami tren kenaikan setiap tahunnya walaupun terdapat sedikit penurunan pada tahun 2022. Selain itu, grafik untuk saham-saham ini memiliki fluktuasi yang lebih kecil dan pergerakan yang lebih stabil, yang menunjukkan tingkat volatilitas yang lebih rendah.")

st.write("2. Di sisi lain, saham META dan NFLX mengalami penurunan signifikan pada akhir tahun 2021. Terutama pada saham NFLX, dimana harga penutupan sahamnya turun drastis dari 677 USD menjadi 177 USD.")

st.write("")
st.write("")

"### Grafik Perbandingan Volume Saham"
st.bar_chart(volumeData, use_container_width=True)
"#### Penjelasan"
st.write("Plot tersebut menampilkan perubahan volume saham dengan interval 1 hari untuk setiap perusahaan saham yang dianalisis. Sumbu x adalah rentang tanggal dari 1 Januari 2017 hingga 31 Desember 2022, sedangkan sumbu y adalah volume saham untuk masing-masing perusahaan.")

st.write("1. AAPL memiliki volume saham yang terbesar dan saham NFLX memiliki volume saham terkecil diantara kelima perusahaan FAANG, hal ini seringkali dapat diartikan AAPL memiliki jumlah Shares Outstanding (Saham yang diterbitkan dan dipegang secara aktif oleh pemegang saham) yang lebih tinggi sehingga jumlah saham yang diperdagangkan lebih banyak tiap harinya.")

st.write("2. Dalam grafik ini terlihat bahwa volume saham AAPL terbesar ada pada 21 Desember 2018, volume saham AMZN terbesar ada pada 27 Oktober 2017, volume saham GOOG terbesar ada pada 27 Oktober 2022, volume saham META terbesar ada pada 27 Oktober 2022, volume saham NFLX terbesar ada pada 21 April 2022")