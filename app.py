from pathlib import Path

import streamlit as st

from st_pages import Page, add_page_title, show_pages

st.sidebar.write(
    '''
    # Dashboard Saham

    Made by Fadhil R

    '''
)

show_pages(
    [
        Page("app.py", "Overview"),
        Page("page_one.py", "Data Explorer"),
        Page("page_two.py", "Insights"),
        Page("page_three.py", "Reference")
    ]
)

# add_page_title(layout="wide")

"# Analisis Saham FAANG"

'''
Di bidang keuangan, "FAANG" adalah akronim yang mengacu pada saham lima perusahaan teknologi terkemuka Amerika: Meta (META) (sebelumnya dikenal sebagai Facebook), Amazon (AMZN), Apple (AAPL), Netflix (NFLX), dan Alphabet (GOOG) (sebelumnya dikenal sebagai Google). 

Istilah ini dipopulerkan oleh Jim Cramer, pembawa acara televisi Mad Money di CNBC pada tahun 2013, yang memuji perusahaan-perusahaan ini karena "sangat dominan di pasar mereka." Awalnya, istilah "FANG" digunakan, dengan Apple - huruf "A" kedua dalam singkatan tersebut - ditambahkan pada tahun 2017.

'''

"### Memahami saham FAANG"

'''

Selain dikenal luas di kalangan konsumen, kelima saham FAANG adalah salah satu perusahaan terbesar di dunia, dengan kapitalisasi pasar gabungan sekitar 7 triliun USD pada Q1 2022.

Pertumbuhan substansial mereka baru-baru ini didukung oleh pembelian besar-besaran yang dilakukan oleh investor besar dan berpengaruh seperti Berkshire Hathaway (BRK), Soros Fund Management, dan Renaissance Technologies. Ini hanyalah beberapa dari banyak investor besar yang telah menambahkan saham FAANG ke dalam portofolio mereka karena kekuatan, pertumbuhan, atau momentum yang dirasakan. 

Setiap saham FAANG diperdagangkan di bursa Nasdaq dan termasuk dalam Indeks S&P 500. Karena S&P 500 adalah representasi pasar yang luas, pergerakan pasar mencerminkan pergerakan indeks. Pada Agustus 2021, FAANG membentuk sekitar 19% dari S&P 500 - angka yang mengejutkan mengingat S&P 500 secara umum dipandang sebagai proksi untuk ekonomi Amerika Serikat secara keseluruhan.

'''

"### Data yang akan dianalisis"

'''

- #### Closing Price : 
Closing Price (Harga penutupan) adalah harga mentah atau nilai tunai dari harga terakhir yang ditransaksikan pada sekuritas sebelum pasar secara resmi ditutup untuk perdagangan normal. Harga penutupan sering kali menjadi titik acuan yang digunakan investor untuk membandingkan performa saham sejak hari sebelumnya.

- #### Volume : 
Volume adalah jumlah aset atau sekuritas yang berpindah tangan selama periode waktu tertentu, biasanya dalam satu hari perdagangan. Contohnya, volume perdagangan saham mengacu pada jumlah saham yang diperdagangkan antara pembukaan dan penutupan harian. Volume perdagangan, dan perubahan volume selama periode waktu tertentu, merupakan input penting bagi trader teknikal.

'''



