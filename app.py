import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Funzione per simulare il caricamento dei dati (puoi sostituire con il caricamento di file reali)
def load_data():
    data = {
        "Month": ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"],
        "2024": [41, 45, 55, 64, 53, 60, 75, 82, 70, 60, 50, 42],
        "2023": [40, 39, 50, 37, 32, 48, 62, 55, 65, 58, 47, 35],
        "2022": [58, 55, 42, 54, 39, 45, 60, 70, 68, 59, 49, 40],
        "2021": [55, 62, 73, 63, 57, 66, 80, 78, 65, 58, 52, 44]
    }
    df = pd.DataFrame(data)
    return df

# Carica i dati simulati
df = load_data()

# Titolo della dashboard
st.title("Dashboard Vendite Auto")

# Filtro per l'anno
year = st.selectbox("Seleziona l'anno", ["2024", "2023", "2022", "2021"])

# Filtro per categoria (qui simuliamo Nuove, Usate, Km0)
category = st.selectbox("Seleziona la categoria", ["Nuove", "Usate", "Km0"])

# Visualizzazione del grafico mensile per l'anno selezionato
st.subheader(f"Andamento Vendite Mensili ({year}) - Categoria: {category}")
fig, ax = plt.subplots()
ax.plot(df["Month"], df[year], marker='o', linestyle='-')
ax.set_title(f"Vendite Mensili {year}")
ax.set_xlabel("Mese")
ax.set_ylabel("Volume Vendite")
ax.grid()
st.pyplot(fig)

# Riepilogo delle vendite per ogni anno
st.subheader("Riepilogo delle vendite per ogni anno")
st.write(df)

st.write("Questa dashboard può essere ampliata con più dati e visualizzazioni interattive!")