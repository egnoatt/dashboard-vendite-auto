import streamlit as st

# Dati simulati delle vendite auto per ogni categoria temporale e tipo
vendite_data = {
    "Settimanale": {"Nuovo": 50, "Km0": 20, "Usato": 30},
    "Mensile": {"Nuovo": 200, "Km0": 80, "Usato": 120},
    "Annuale": {"Nuovo": 2400, "Km0": 960, "Usato": 1440}
}

# Titolo della dashboard
st.title("Dashboard Vendite Auto - KPI Temporali")

# Funzione per creare rettangoli con tabelle
def display_sales_metrics(period, data):
    st.markdown(f"""
    <div style="border:2px solid #4CAF50; padding: 10px; border-radius: 10px; width: 100%; height: auto; margin: 5px;">
        <table style="width:100%; text-align: center; border-collapse: collapse;">
            <tr>
                <th colspan="3" style="font-size: 16px; padding: 5px;">Vendite Auto - {period}</th>
            </tr>
            <tr>
                <td style="font-size: 14px; font-weight: bold; padding: 5px;">Nuovo</td>
                <td style="font-size: 14px; font-weight: bold; padding: 5px;">Km0</td>
                <td style="font-size: 14px; font-weight: bold; padding: 5px;">Usato</td>
            </tr>
            <tr>
                <td style="font-size: 18px; font-weight: bold; padding: 5px;">{data['Nuovo']}</td>
                <td style="font-size: 18px; font-weight: bold; padding: 5px;">{data['Km0']}</td>
                <td style="font-size: 18px; font-weight: bold; padding: 5px;">{data['Usato']}</td>
            </tr>
        </table>
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
