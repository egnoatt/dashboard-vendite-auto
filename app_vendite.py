import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Simulazione di un dataset giornaliero per "Vendite Auto" fino alla fine del 2024 con valori casuali
date_range = pd.date_range(start="2023-01-01", end="2024-12-31")  # Date giornaliere fino alla fine del 2024
num_days = len(date_range)

data = {
    "data": date_range,
    "Nuovo": np.random.randint(40, 60, size=num_days),  # Valori casuali tra 40 e 60 per ogni giorno
    "Km0": np.random.randint(15, 25, size=num_days),    # Valori casuali tra 15 e 25 per ogni giorno
    "Usato": np.random.randint(25, 35, size=num_days)   # Valori casuali tra 25 e 35 per ogni giorno
}

# Creazione del DataFrame
df = pd.DataFrame(data)

# Funzione per ottenere le vendite per un periodo specifico
def get_sales_for_period(df, period="settimanale"):
    today = datetime(2023, 11, 1)  # Usa una data fittizia per il testing
    
    if period == "settimanale":
        start_date = today - timedelta(days=today.weekday())  # Inizio della settimana corrente
        filtered_df = df[(df["data"] >= start_date) & (df["data"] <= today)]
        
    elif period == "mensile":
        start_date = today.replace(day=1)  # Inizio del mese corrente
        filtered_df = df[(df["data"] >= start_date) & (df["data"] <= today)]
        
    elif period == "annuale":
        start_date = today.replace(month=1, day=1)  # Inizio dell'anno corrente
        filtered_df = df[(df["data"] >= start_date) & (df["data"] <= today)]
        
    # Somma le vendite per Nuovo, Km0 e Usato per il periodo specificato
    sales_data = {
        "Nuovo": filtered_df["Nuovo"].sum(),
        "Km0": filtered_df["Km0"].sum(),
        "Usato": filtered_df["Usato"].sum(),
    }
    
    return sales_data

# Titolo della dashboard
st.title("Dashboard Vendite Auto - Dati Correnti")

# Funzione per visualizzare i dati di un periodo specifico
def display_period(period, data):
    st.markdown(f"""
    <div style="border:2px solid #333; padding: 10px; border-radius: 5px; text-align: center; margin-top: 20px;">
        <h3 style="font-size: 20px; margin-bottom: 10px;">{period}</h3>
        <table style="width:100%; text-align: center; border-collapse: collapse;">
            <tr>
                <th style="font-size: 16px; padding: 5px; border: none;">Nuovo</th>
                <th style="font-size: 16px; padding: 5px; border: none;">Km0</th>
                <th style="font-size: 16px; padding: 5px; border: none;">Usato</th>
            </tr>
            <tr>
                <td style="font-size: 18px; font-weight: bold; padding: 5px; border: 1px solid #ddd;">{data['Nuovo']}</td>
                <td style="font-size: 18px; font-weight: bold; padding: 5px; border: 1px solid #ddd;">{data['Km0']}</td>
                <td style="font-size: 18px; font-weight: bold; padding: 5px; border: 1px solid #ddd;">{data['Usato']}</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# Visualizzazione della sezione "Vendite Auto"
def display_vendite_section():
    st.subheader("Vendite Auto")

    # Creare le colonne per ogni periodo
    period_col1, period_col2, period_col3 = st.columns(3)

    # Visualizzazione dei dati per ciascun periodo
    with period_col1:
        sales_data = get_sales_for_period(df, "settimanale")
        display_period("Settimanale", sales_data)

    with period_col2:
        sales_data = get_sales_for_period(df, "mensile")
        display_period("Mensile", sales_data)

    with period_col3:
        sales_data = get_sales_for_period(df, "annuale")
        display_period("Annuale", sales_data)

# Esegui la visualizzazione della sezione
display_vendite_section()
