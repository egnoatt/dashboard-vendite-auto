import streamlit as st

# Dati simulati delle vendite, acquisti e servizi per ogni categoria temporale e tipo
vendite_data = {
    "Settimanale": {"Nuovo": 50, "Km0": 20, "Usato": 30},
    "Mensile": {"Nuovo": 200, "Km0": 80, "Usato": 120},
    "Annuale": {"Nuovo": 2400, "Km0": 960, "Usato": 1440}
}

acquisti_data = {
    "Settimanale": {"Nuovo": 30, "Km0": 10, "Usato": 15},
    "Mensile": {"Nuovo": 150, "Km0": 50, "Usato": 60},
    "Annuale": {"Nuovo": 1800, "Km0": 600, "Usato": 720}
}

servizi_cliente_data = {
    "Settimanale": {"Richieste": 40, "Interventi": 25, "Feedback": 15},
    "Mensile": {"Richieste": 160, "Interventi": 100, "Feedback": 60},
    "Annuale": {"Richieste": 1920, "Interventi": 1200, "Feedback": 720}
}

# Titolo della dashboard
st.title("Dashboard KPI - Vendite, Acquisti e Servizi al Cliente")

# Funzione per creare rettangoli con tabelle senza bordi interni
def display_sales_metrics(title, period, data):
    st.markdown(f"""
    <div style="border:2px solid #4CAF50; padding: 10px; border-radius: 10px; width: 100%; height: auto; margin: 5px;">
        <table style="width:100%; text-align: center; border-collapse: collapse;">
            <tr>
                <th colspan="3" style="font-size: 16px; padding: 5px; border: none;">{title} - {period}</th>
            </tr>
            <tr>
                <td style="font-size: 14px; font-weight: bold; padding: 5px; border: none;">{list(data.keys())[0]}</td>
                <td style="font-size: 14px; font-weight: bold; padding: 5px; border: none;">{list(data.keys())[1]}</td>
                <td style="font-size: 14px; font-weight: bold; padding: 5px; border: none;">{list(data.keys())[2]}</td>
            </tr>
            <tr>
                <td style="font-size: 18px; font-weight: bold; padding: 5px; border: none;">{data[list(data.keys())[0]]}</td>
                <td style="font-size: 18px; font-weight: bold; padding: 5px; border: none;">{data[list(data.keys())[1]]}</td>
                <td style="font-size: 18px; font-weight: bold; padding: 5px; border: none;">{data[list(data.keys())[2]]}</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# Sezione Vendite Auto
st.header("Vendite Auto")
col1, col2, col3 = st.columns(3)
with col1:
    display_sales_metrics("Vendite Auto", "Settimanale", vendite_data["Settimanale"])
with col2:
    display_sales_metrics("Vendite Auto", "Mensile", vendite_data["Mensile"])
with col3:
    display_sales_metrics("Vendite Auto", "Annuale", vendite_data["Annuale"])

# Spaziatura tra le sezioni
st.markdown("<br>", unsafe_allow_html=True)

# Sezione Acquisto Auto
st.header("Acquisto Auto")
col4, col5, col6 = st.columns(3)
with col4:
    display_sales_metrics("Acquisto Auto", "Settimanale", acquisti_data["Settimanale"])
with col5:
    display_sales_metrics("Acquisto Auto", "Mensile", acquisti_data["Mensile"])
with col6:
    display_sales_metrics("Acquisto Auto", "Annuale", acquisti_data["Annuale"])

# Spaziatura tra le sezioni
st.markdown("<br>", unsafe_allow_html=True)

# Sezione Servizi al Cliente
st.header("Servizi al Cliente")
col7, col8, col9 = st.columns(3)
with col7:
    display_sales_metrics("Servizi al Cliente", "Settimanale", servizi_cliente_data["Settimanale"])
with col8:
    display_sales_metrics("Servizi al Cliente", "Mensile", servizi_cliente_data["Mensile"])
with col9:
    display_sales_metrics("Servizi al Cliente", "Annuale", servizi_cliente_data["Annuale"])

st.write("Questa dashboard può essere ampliata per includere altri KPI e categorie.")
