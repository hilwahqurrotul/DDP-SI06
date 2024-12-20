import streamlit as st

st.title("Halaman Dashboard")
st.image("Image.jpg", caption="Gambar Rumah")

# fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(t['Jumlah']
                        for t in st.session_state['total_semua']
                        if t ['Tipe'] == 'Menabung')
    total_penarikan = sum(t['Jumlah']
                        for t in st.session_state['total_semua']
                        if t ['Tipe'] == 'Penarikan')
    saldo = total_nabung - total_penarikan
    
    return total_nabung, total_penarikan, saldo

total_semua = st.session_state['total_semua']
total_nabung, total_penarikan, saldo = total()

st.metric("Total Menabung", f"Rp {total_nabung}")
st.metric("Total Penarikan", f"Rp {total_penarikan}")
st.metric("Sisa saldo anda", f"Rp {saldo}")