import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Pokedex App")

st.title("📖 Pokédex App")

web_url = "https://pokemondb.net/pokedex/all"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(web_url, headers=headers, timeout=10)
    response.raise_for_status()

    parsed_content = bs(response.text, "html.parser")

    table = parsed_content.find("table", id="pokedex")

    if table is None:
        st.error("Could not find Pokémon table on the website.")
        st.stop()

    table_body = table.find("tbody")
    list_of_rows = table_body.find_all("tr")

    pokedex = []

    for row in list_of_rows:
        stats = {}

        name_row = row.find("td", class_="cell-name")

        if name_row:
            stats["Name"] = name_row.a.text.strip()

        num_rows = row.find_all("td", class_="cell-num")

        if len(num_rows) >= 8:
            stats["Total"] = num_rows[1].text.strip()
            stats["HP"] = num_rows[2].text.strip()
            stats["Attack"] = num_rows[3].text.strip()
            stats["Defense"] = num_rows[4].text.strip()
            stats["Sp. Attack"] = num_rows[5].text.strip()
            stats["Sp. Defense"] = num_rows[6].text.strip()
            stats["Speed"] = num_rows[7].text.strip()

            pokedex.append(stats)

    pokedex_df = pd.DataFrame(pokedex)

    st.sidebar.title("Search Pokémon")

    pokemon_choice = st.sidebar.selectbox(
        "Choose Pokémon",
        ["All"] + sorted(pokedex_df["Name"].unique())
    )

    if pokemon_choice == "All":
        filtered_df = pokedex_df
    else:
        filtered_df = pokedex_df[pokedex_df["Name"] == pokemon_choice]

    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")
