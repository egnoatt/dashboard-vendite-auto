import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Impostazioni di connessione Supabase
url = "https://nptwtnrcbhnymmxnoicz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

supabase: Client = create_client(url, key)

# Funzione per ottenere i dati
def get_data():
    response = supabase.table("vendite_auto").select("*").execute()
    if response.error:
        st.error(f"Errore durante il recupero dei dati: {response.error}")
        return pd.DataFrame()
    data = response.data
    df = pd.DataFrame(data)
    return df

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
else:
    st.write("Nessun dato disponibile.")
