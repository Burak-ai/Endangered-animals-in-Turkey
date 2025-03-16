import pandas as pd
import plotly.express as px

data = {
    "Hayvan Türü": [
        "Deniz Kaplumbağası", "Anadolu Parsı", "Akdeniz Foku", "Karakulak",
        "Dağ Keçisi", "Kelaynak Kuşu", "Turna Kuşu",
        "Alageyik", "İnci Kefali",
    ],
    "Bölge": [
        "Akdeniz", "Ege", "Akdeniz", "Doğu Anadolu", "Karadeniz",
        "Güneydoğu Anadolu", "Marmara", "Toroslar",
        "Van Gölü",
    ],
    "Enlem": [36.5, 38.4, 36.0, 39.7, 41.1, 37.5, 40.0, 37.3, 38.5],
    "Boylam": [30.5, 27.2, 29.0, 42.0, 37.5, 38.8, 28.3, 32.4, 43.3],
    "Koruma Durumu": [
        "Tehdit Altında", "Yok Olma Tehlikesi", "Hassas", "Tehdit Altında",
        "Düşük Risk", "Hassas", "Tehdit Altında",
        "Düşük Risk", "Yok Olma Tehlikesi",
    ],
    "Popülasyon Tahmini": [
        "5000-10000", "50-100", "1000-2000", "200-300",
        "10000-15000", "200-500", "10000-15000",
        "3000-5000", "50000-100000",
    ],
}

df = pd.DataFrame(data)

fig = px.scatter_geo(
    df,
    lat="Enlem",
    lon="Boylam",
    text="Hayvan Türü",
    title="Türkiye'de Nesli Tükenmekte Olan Hayvanların Dağılımı",
    scope="europe",
    labels={"Hayvan Türü": "Tür"},
    hover_data=["Koruma Durumu", "Popülasyon Tahmini", "Bölge"],
)

fig.update_geos(
    visible=True,
    resolution=50,
    showcountries=True,
    countrycolor="LightGrey",
    showcoastlines=True,
    coastlinecolor="LightBlue",
)

fig.write_html("index.html")

