import streamlit as st

# Dati simulati delle vendite auto per ogni categoria temporale e tipo
vendite_data = {
    "Settimanale": {"Nuovo": 50, "Km0": 20, "Usato": 30},
    "Mensile": {"Nuovo": 200, "Km0": 80, "Usato": 120},
    "Annuale": {"Nuovo": 2400, "Km0": 960, "Usato": 1440}
}

# Titolo della dashboard
st.title("Dashboard Vendite Auto - KPI Temporali")

# Funzione per creare rettangoli con metriche di vendite, con layout centrato
def display_sales_metrics(period, data):
    st.markdown(f"""
    <div style="border:2px solid #4CAF50; padding: 10px; border-radius: 10px; width: 100%; height: 150px; margin: 5px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <h4 style="margin: 0; font-size: 16px; padding-bottom: 5px;">Vendite Auto - {period}</h4>
        <div style="display: flex; justify-content: space-around; width: 100%; padding-top: 5px;">
            <div style="text-align: center; flex: 1;">
                <h5 style="margin: 0; font-size: 14px; padding-bottom: 5px;">Nuovo</h5>
                <p style="font-size: 18px; font-weight: bold; margin: 0;">{data['Nuovo']}</p>
            </div>
            <div style="text-align: center; flex: 1;">
                <h5 style="margin: 0; font-size: 14px; padding-bottom: 5px;">Km0</h5>
                <p style="font-size: 18px; font-weight: bold; margin: 0;">{data['Km0']}</p>
            </div>
            <div style="text-align: center; flex: 1;">
                <h5 style="margin: 0; font-size: 14px; padding-bottom: 5px;">Usato</h5>
                <p style="font-size: 18px; font-weight: bold; margin: 0;">{data['Usato']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Disposizione in colonne per visualizzare i tre periodi (settimanale, mensile, annuale) su una stessa riga
col1, col2, col3 = st.columns(3)

with col1:
    display_sales_metrics("Settimanale", vendite_data["Settimanale"])
with col2:
    display_sales_metrics("Mensile", vendite_data["Mensile"])
with col3:
    display_sales_metrics("Annuale", vendite_data["Annuale"])

st.write("Questa dashboard può essere ampliata per includere altri KPI e categorie.")
