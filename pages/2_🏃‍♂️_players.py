import streamlit as st

st.set_page_config(
    page_title="FIFA23",
    layout="wide"
)

# Usando os dados guardados na sessão da página Home
df_data = st.session_state["data"]

clubs = df_data["Club"].unique()
club = st.sidebar.selectbox("Club", clubs)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Player", players)

players_stats = df_players[df_players["Name"] == player].iloc[0]

st.image(players_stats["Photo"])
st.title(players_stats["Name"])

st.markdown(f"**Club:** {players_stats['Club']}")
st.markdown(f"**Position:** {players_stats['Position']}")

col1, col2, col3, col4, col5 = st.columns(5)
col1.markdown(f"**Age:** {players_stats['Age']}")
col2.markdown(f"**Height:** {players_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Weight:** {players_stats['Weight(lbs.)'] *0.453:.2f}")
st.divider()

# Linha divisória e barra de progresso
st.subheader(f"Overall: {players_stats['Overall']}")
st.progress(int(players_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label = "Market value", value = f"£ {players_stats['Value(£)']:,}")
col2.metric(label = "Wage", value = f"£ {players_stats['Wage(£)']:,}")
col3.metric(label = "Release Clause", value = f"£ {players_stats['Release Clause(£)']:,}")