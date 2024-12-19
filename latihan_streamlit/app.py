import streamlit as st

# st.title("Hallo Mabro🤩")
# st.markdown("Selamat di rumah coding")
# st.image("Image.jpg", caption="Ini gambar")

dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung😱")

pg = st.navigation(
    {
        "Menu Utama" : [dashboard],
        "Transaksi" : [nabung],

    }
)

if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []

pg.run()