import streamlit as st
import pandas as pd

# Funzione per simulare il caricamento dei dati KPI (puoi sostituire con il caricamento di dati reali)
def load_kpi_data():
    data = {
        "Categoria": ["Vendite Auto", "Acquisto Auto", "Riparazioni in garanzia", "Riparazioni e altro", "Assicurazioni e altro", "Servizi al Cliente"],
        "Tipo": ["Nuovo", "Usato", "Nuovo", "Usato", "Nuovo", "Usato"],
        "Settimanale": [10, 5, 3, 7, 2, 8],
        "Mensile": [40, 30, 15, 28, 8, 25],
        "Annuale": [480, 360, 180, 336, 96, 300]
    }
    df = pd.DataFrame(data)
    return df

# Carica i dati KPI simulati
df_kpi = load_kpi_data()

# Titolo della dashboard
st.title("Dashboard KPI Aziendali Globali")

# Selettore per la frequenza (Settimanale, Mensile, Annuale)
frequenza = st.selectbox("Seleziona la frequenza", ["Settimanale", "Mensile", "Annuale"])

# Selettore per la categoria
categoria = st.selectbox("Seleziona la categoria", df_kpi["Categoria"].unique())

# Filtra i dati in base alla selezione
df_filtrato = df_kpi[(df_kpi["Categoria"] == categoria)]

# Visualizzazione KPI
st.subheader(f"KPI per {categoria} - Frequenza: {frequenza}")
for index, row in df_filtrato.iterrows():
    st.metric(label=f"{row['Tipo']} - {frequenza}", value=row[frequenza])

# Messaggio di nota per espandere la dashboard
st.write("Questa dashboard può essere ampliata con altri KPI e categorie man mano che si aggiungono nuovi dati.")
