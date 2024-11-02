# Simulazione di un dataset giornaliero per "Vendite Auto" fino alla fine del 2024
data = {
    "data": pd.date_range(start="2023-01-01", end="2024-12-31"),  # Date giornaliere fino alla fine del 2024
    "Nuovo": [50] * 730,  # Dati simulati per vendite "Nuovo"
    "Km0": [20] * 730,    # Dati simulati per vendite "Km0"
    "Usato": [30] * 730   # Dati simulati per vendite "Usato"
}

# Creazione del DataFrame
df = pd.DataFrame(data)
def get_sales_for_period(df, period="settimanale"):
    # Usa una data fittizia per il testing
    today = datetime(2023, 11, 1)
    
    if period == "settimanale":
        start_date = today - timedelta(days=today.weekday())
        filtered_df = df[(df["data"] >= start_date) & (df["data"] <= today)]
        
    elif period == "mensile":
        start_date = today.replace(day=1)
        filtered_df = df[(df["data"] >= start_date) & (df["data"] <= today)]
        
    elif period == "annuale":
        start_date = today.replace(month=1, day=1)
        filtered_df = df[(df["data"] >= start_date) & (df["data"] <= today)]
        
    sales_data = {
        "Nuovo": filtered_df["Nuovo"].sum(),
        "Km0": filtered_df["Km0"].sum(),
        "Usato": filtered_df["Usato"].sum(),
    }
    
    return sales_data
    
