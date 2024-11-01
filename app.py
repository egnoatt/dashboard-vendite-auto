import streamlit as st
from streamlit import markdown

# Dati simulati delle vendite auto per ogni categoria temporale e tipo
vendite_data = {
    "Settimanale": {"Nuovo": 50, "Km0": 20, "Usato": 30},
    "Mensile": {"Nuovo": 200, "Km0": 80, "Usato": 120},
    "Annuale": {"Nuovo": 2400, "Km0": 960, "Usato": 1440}
}

# Titolo della dashboard
st.title("Dashboard Vendite Auto - KPI Temporali")

# Funzione per creare rettangoli con metriche di vendite
def display_sales_metrics(period, data):
    # Aggiungi il contorno per ciascun periodo con markdown CSS
    st.markdown(f"""
    <div style="border:2px solid #4CAF50; padding: 10px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="text-align: center;">Vendite Auto - {period}</h3>
        <div style="display: flex; justify-content: space-around;">
            <div style="text-align: center;">
                <h4>Nuovo</h4>
                <p style="font-size: 24px; font-weight: bold;">{data['Nuovo']}</p>
            </div>
            <div style="text-align: center;">
                <h4>Km0</h4>
                <p style="font-size: 24px; font-weight: bold;">{data['Km0']}</p>
            </div>
            <div style="text-align: center;">
                <h4>Usato</h4>
                <p style="font-size: 24px; font-weight: bold;">{data['Usato']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Visualizzazione delle vendite per ogni periodo
for periodo, dati in vendite_data.items():
    display_sales_metrics(periodo, dati)

st.write("Questa dashboard può essere ampliata per includere altri KPI e categorie.")
