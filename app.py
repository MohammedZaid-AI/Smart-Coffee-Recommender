import streamlit as st
import joblib

# --- Load Model ---
model = joblib.load("model/coffee_model.pkl")
le_day = joblib.load("model/le_day.pkl")
le_time = joblib.load("model/le_time.pkl")
le_coffee = joblib.load("model/le_coffee.pkl")

# --- UI Styling ---
st.set_page_config(page_title="Coffee AI", page_icon="☕", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>☕ Smart Coffee Recommender</h1>
    <p style='text-align: center;'>Find the perfect coffee based on time & day</p>
""", unsafe_allow_html=True)

st.divider()

# --- Input Section ---
col1, col2 = st.columns(2)

with col1:
    day = st.selectbox("📅 Select Day", 
        ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

with col2:
    time = st.selectbox("⏰ Time of Day", 
        ["Morning","Afternoon","Night"])

st.divider()

# --- Mappings ---
day_mapping = {
    "Monday": 1, "Tuesday": 5, "Wednesday": 6, "Thursday": 4,
    "Friday": 0, "Saturday": 2, "Sunday": 3
}
time_mapping = {
    "Morning": 1, "Afternoon": 0, "Night": 2
}

# --- Prediction Function ---
def recommend(day, time):
    day_enc = day_mapping[day]
    time_enc = time_mapping[time]

    probs = model.predict_proba([[time_enc, day_enc]])[0]

    top3 = probs.argsort()[-3:][::-1]

    results = []
    for i in top3:
        coffee = le_coffee.inverse_transform([i])[0]
        confidence = probs[i] * 100
        results.append((coffee, confidence))

    return results

# --- Button ---
if st.button("✨ Recommend Coffee", use_container_width=True):
    results = recommend(day, time)

    st.success("Here are your recommendations:")

    for coffee, conf in results:
        st.markdown(f"""
        🔥 **{coffee}** — {conf:.1f}% confidence
        """)

st.divider()

st.caption("Built with ❤️ using Machine Learning")