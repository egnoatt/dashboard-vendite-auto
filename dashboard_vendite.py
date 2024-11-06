import os
import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Impostazioni di connessione Supabase
url = "https://nptwtnrcbhnymmxnoicz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5wdHd0bnJjYmhueW1teG5vaWN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA1NTEwOTMsImV4cCI6MjA0NjEyNzA5M30.HtLr0d0dC6qUoZEqFwi9pMrKLSW1Luwm-Vu9u86js0Y"

if not url or not key:
    st.error("Le credenziali di Supabase non sono impostate.")
    st.stop()

supabase: Client = create_client(url, key)

# Funzione per ottenere i dati
def get_data():
    try:
        response = supabase.table("vendite_auto").select("*").execute()
        data = response.data
        if not data:
            st.warning("Nessun dato restituito dal database.")
            return pd.DataFrame()
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error(f"Errore durante il recupero dei dati: {e}")
        return pd.DataFrame()

# Configura Streamlit
st.title("Dashboard Vendite Auto")

# Ottieni i dati e mostra nella dashboard
df = get_data()

if not df.empty:
    st.write("### Dati Vendite Auto")
    st.dataframe(df)

    # Esempio di visualizzazione grafica
    st.write("### Vendite per Tipo di Veicolo")
    sales_summary = df.groupby("tipo_veicolo")["quantita"].sum().reset_index()
    st.bar_chart(sales_summary.set_index("tipo_veicolo"))

    # Visualizzazione del Prezzo Medio di Vendita
    st.write("### Prezzo Medio di Vendita per Tipo di Veicolo")
    if 'prezzo_vendita' in df.columns:
        price_summary = df.groupby("tipo_veicolo")["prezzo_vendita"].mean().reset_index()
        st.bar_chart(price_summary.set_index("tipo_veicolo"))
    else:
        st.warning("La colonna 'prezzo_vendita' non è disponibile.")

    # Visualizzazione dei Dati di Acquisto
    st.write("### Dati di Acquisto")
    if 'data_acquisto' in df.columns and 'prezzo_acquisto' in df.columns:
        st.dataframe(df[['data_acquisto', 'prezzo_acquisto', 'luogo_vendita']])
    else:
        st.warning("Le colonne di acquisto non sono disponibili.")
else:
    st.write("Nessun dato disponibile.")

# Aggiungi una sezione per inserire nuovi dati
st.write("### Inserisci Nuove Vendite")

with st.form("inserimento_vendite"):
    col1, col2 = st.columns(2)
    with col1:
        data_vendita = st.date_input("Data Vendita")
        tipo_veicolo = st.selectbox("Tipo di Veicolo", ["Nuovo", "Km0", "Usato"])
        quantita = st.number_input("Quantità", min_value=1, step=1)
        prezzo_vendita = st.number_input("Prezzo Vendita", min_value=0.0, step=0.01)
        luogo_vendita = st.text_input("Luogo di Vendita")
    with col2:
        data_acquisto = st.date_input("Data Acquisto")
        prezzo_acquisto = st.number_input("Prezzo Acquisto", min_value=0.0, step=0.01)
    submitted = st.form_submit_button("Inserisci")

    if submitted:
        # Prepara i dati per l'inserimento
        nuovo_record = {
            "data": data_vendita.isoformat(),
            "tipo_veicolo": tipo_veicolo,
            "quantita": quantita,
            "prezzo_vendita": prezzo_vendita,
            "luogo_vendita": luogo_vendita,
            "data_acquisto": data_acquisto.isoformat(),
            "prezzo_acquisto": prezzo_acquisto
        }

        # Inserisci il nuovo record nel database
        try:
            response = supabase.table("vendite_auto").insert(nuovo_record).execute()
            if response.error:
                st.error(f"Errore durante l'inserimento dei dati: {response.error}")
            else:
                st.success("Dati inseriti con successo!")
                # Aggiorna i dati visualizzati
                df = get_data()
        except Exception as e:
            st.error(f"Errore durante l'inserimento dei dati: {e}")
