import streamlit as st
import pandas as pd
import numpy as np

st.title("💪 Monitor aktywności fizycznej")
st.caption("Demo aplikacji w Streamlit!")

# 🧾 Dane wejściowe od użytkownika
name = st.text_input("Wpisz swoje imię:")
steps_goal = st.slider("Twój dzienny cel kroków:", 1000, 20000, 8000)
sport_type = st.selectbox("Wybierz aktywność:", ["Spacer", "Bieganie", "Rower"])

# 🔘 Opcje wykresów i mapy
show_charts = st.checkbox("Pokaż wykresy aktywności")
show_map = st.checkbox("Pokaż trasę na mapie")

if st.button("Rozpocznij analizę"):
    st.success(f"Cześć, {name}! Analizujemy Twoją aktywność: {sport_type}")
    st.balloons()

# 📈 Dane do wykresów – symulacja 10 dni aktywności
days = [f"Dzień {i}" for i in range(1, 11)]
steps = np.random.randint(3000, 15000, 10)
calories = steps * 0.04
heart_rate = np.random.randint(65, 150, 10)

df = pd.DataFrame({
    "Dzień": days,
    "Kroki": steps,
    "Kalorie": calories,
    "Tętno": heart_rate
})

df.set_index("Dzień", inplace=True)

# 📊 Wykresy
if show_charts:
    st.subheader("🚶‍♂️ Liczba kroków")
    st.line_chart(df["Kroki"])

    st.subheader("🔥 Spalone kalorie")
    st.bar_chart(df["Kalorie"])

    st.subheader("❤️ Tętno w czasie")
    st.area_chart(df["Tętno"])

# 🗺️ Mapa trasy aktywności
if show_map:
    st.subheader("🗺️ Przykładowa trasa z GPS (symulowana)")
    map_data = pd.DataFrame({
        "latitude": np.random.uniform(50.05, 50.10, 10),
        "longitude": np.random.uniform(19.90, 19.95, 10)
    })
    st.map(map_data)


