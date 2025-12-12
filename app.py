import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# ─────────────────────────────
# Premium Glass UI
# ─────────────────────────────
st.markdown("""
    <style>
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }

    .neon-header {
        color: #39FF14;
        text-shadow: 0 0 10px #39FF14;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
/* Global dark background */
body {
    background-color: #0d1117 !important;
    color: white !important;
}

/* Streamlit main content */
[data-testid="stAppViewContainer"] {
    background-color: #0d1117;
    animation: fadeIn 1.2s ease-in-out;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827 !important;
    color: white !important;
}

/* Fade-in animation */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Make all labels and small text brighter and fully opaque */
label, .css-1v3fvcr, .css-1pnq3sl, .stMarkdown, p, span {
    color: #E6EEF8 !important;
    opacity: 1 !important;
    font-weight: 600 !important;
}

/* Make section titles even brighter */
.section-title, .glow-title, .neon-header {
    color: #e6fff6 !important;
    text-shadow: 0 0 14px rgba(0,234,255,0.16) !important;
}

/* Slider value (the numeric) — bigger & clearer */
[data-testid="stSlider"] .css-1dq8tca, .css-9ycgxx {
    color: #ff6b6b !important;    /* value color */
    font-weight: 700 !important;
    font-size: 15px !important;
}

/* Make the slider track and knob more visible */
input[type="range"] {
    accent-color: #ff6b6b !important;
}

/* For Streamlit's internal slider container (fallback) */
.stSlider > div, .css-1v3fvcr {
    color: #E6EEF8 !important;
    opacity: 1 !important;
}

/* Ensure sidebar labels are clear too */
[data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
    color: #dbeafe !important;
    opacity: 1 !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

    /* -------------------------------
       Glassmorphism Card Styling
    --------------------------------*/
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }

    /* -------------------------------
       NEON HEADER (Optional)
    --------------------------------*/
    .neon-header {
        color: #39FF14;
        text-shadow: 0 0 10px #39FF14;
        font-weight: bold;
    }

    /* -------------------------------
       GLOBAL BRIGHT HEADERS FIX
       This ensures ALL section headers
       like "Calculated Power Output"
       and "Live Power Gauges" become visible.
    --------------------------------*/
    h1, h2, h3, h4, h5 {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        text-shadow: 0 0 12px rgba(255,255,255,0.65);
        margin-top: 20px !important;
        margin-bottom: 10px !important;
    }

    /* Make section titles slightly larger */
    h2 {
        font-size: 28px !important;
    }

</style>
""", unsafe_allow_html=True)

from PIL import Image
import streamlit as st

# Load and display logo at top-left
logo = Image.open("IMG-20251213-WA0003.jpg")
st.image(logo, width=90)
st.set_page_config(
    page_title="Hybrid Energy System",
    page_icon="IMG-20251213-WA0003.jpg",
    layout="wide"
)
col1, col2 = st.columns([1, 9])

with col1:
    st.image(logo, width=70)

with col2:
    st.markdown("<h1 style='color:#72E7FF;'>Hybrid Renewable Energy System</h1>", unsafe_allow_html=True)


st.markdown("""
<style>

/* Neon Glowing Buttons */
.neon-btn {
    background: #14b8a6;
    color: white;
    border-radius: 10px;
    padding: 12px 20px;
    font-weight: bold;
    border: none;
    box-shadow: 0 0 12px #14b8a6;
    transition: 0.2s ease-in-out;
}
.neon-btn:hover {
    box-shadow: 0 0 18px #1fffe0;
    transform: scale(1.04);
}

/* Premium Section Cards */
.section-card {
    background: rgba(255, 255, 255, 0.1);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    margin-bottom: 30px;
    animation: fadeIn 1s ease-in-out;
}

/* Headings with glow */
.glow-title {
    font-size: 26px;
    font-weight: bold;
    color: #00eaff;
    text-shadow: 0 0 12px #00eaff;
}

</style>
""", unsafe_allow_html=True)





import plotly.graph_objects as go


# ─────────────────────────────
# Sidebar: Project Info & Tips
# ─────────────────────────────
st.sidebar.markdown("""
## 🌱 Hybrid Renewable Energy System
**Project Overview:**  
Simulates Solar, Hydro, and Wind energy output, predicts next-hour power, and gives optimization tips.

**Environmental Tips:**  
- ☀️ Adjust solar panels for max sunlight  
- 💧 Optimize water flow for hydro turbines  
- 🌬️ Position wind blades for max wind capture  

**Current Total Power:**  
""")

# Display total power in sidebar dynamically


st.markdown("""
<div class="glass-card">
    <h1 style='text-align: center;' class='neon-header'>
        🌱 Hybrid Energy AI Simulator
    </h1>
    <p style='text-align: center; color: white;'>
        Smart Digital Twin • Real-time Simulation • AI Predictions
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* ---------- GENERAL TEXT VISIBILITY ---------- */
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: #E8E8E8 !important;     /* Bright gray text for visibility */
}

/* ---------- SECTION HEADERS ---------- */
h1, h2, h3 {
    font-weight: 700 !important;
    color: #ffffff !important;     /* Full white headers */
    text-shadow: 0px 0px 8px rgba(255,255,255,0.25);
}

/* ---------- SLIDER LABEL FIX ---------- */
.css-81oif8, .css-1pz7awu, .css-10trblm, .css-16idsys {
    color: #E8E8E8 !important;
}

/* ---------- WARNING / CAUTION / SUCCESS BOXES ---------- */
.warning-box {
    background-color: #8B0000 !important;    /* Dark red */
    border: 2px solid #FF4C4C !important;
    color: white !important;
    border-radius: 10px;
    padding: 12px;
}

.caution-box {
    background-color: #996c00 !important;
    border: 2px solid #FFD54F !important;
    color: black !important;
    border-radius: 10px;
    padding: 12px;
}

.success-box {
    background-color: #004d1a !important;
    border: 2px solid #00FF88 !important;
    color: white !important;
    border-radius: 10px;
    padding: 12px;
}

/* ---------- BUTTON VISIBILITY FIX ---------- */
div.stButton > button {
    color: #ffffff !important;                
    font-weight: 600 !important;
    background-color: #2b2f38 !important;     
    border: 2px solid #6C63FF !important;     
    padding: 10px 18px !important;
    border-radius: 12px !important;
}

div.stButton > button:hover {
    background-color: #6C63FF !important;
    color: white !important;
    transform: scale(1.03);
    transition: 0.2s;
}

/* ---------- GAUGE HEADER VISIBILITY ---------- */
.block-container h2, .block-container h3 {
    color: white !important;
}

/* ---------- SIDEBAR TEXT ---------- */
.sidebar .sidebar-content, .css-1d391kg {
    color: #E8E8E8 !important;
}

/* ---------- CARDS (GLASS UI) ---------- */
.glass-card {
    background: rgba(255, 255, 255, 0.10);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

.neon-header {
    color: #39FF14 !important;
    text-shadow: 0 0 12px #39FF14;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.write("This software simulates Solar, Wind, and Hydro energy output based on your real hardware model.")

# ─────────────────────────────
# 1. User enters hypothetical readings (since no microcontroller)
# ─────────────────────────────
st.markdown("<h2 class='section-title'>✨ Enter Your Observed Hardware Readings</h2>", unsafe_allow_html=True)

# ─────────────────────────────
# Digital Twin: Environmental Conditions
# ─────────────────────────────


# ─────────────────────────────
# Colorful Columns for Inputs
# ─────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center; color: orange;'>☀️ Solar Panel</h3>", unsafe_allow_html=True)
    solar_v = st.number_input("Voltage (V)", 0.0, 24.0, 12.0, key="solar_v")
    solar_i = st.number_input("Current (A)", 0.0, 10.0, 2.0, key="solar_i")

with col2:
    st.markdown("<h3 style='text-align: center; color: blue;'>💧 Hydro Turbine</h3>", unsafe_allow_html=True)
    hydro_v = st.number_input("Voltage (V)", 0.0, 24.0, 5.0, key="hydro_v")
    hydro_i = st.number_input("Current (A)", 0.0, 10.0, 1.5, key="hydro_i")

with col3:
    st.markdown("<h3 style='text-align: center; color: purple;'>🌬 Wind Generator</h3>", unsafe_allow_html=True)
    wind_v = st.number_input("Voltage (V)", 0.0, 24.0, 8.0, key="wind_v")
    wind_i = st.number_input("Current (A)", 0.0, 10.0, 1.0, key="wind_i")

st.markdown("<h2 class='section-title'>🌤 Digital Twin Controls (Simulated Environment)</h2>", unsafe_allow_html=True)

sunlight = st.slider("Sunlight Intensity (%)", 0, 100, 70)
water_flow = st.slider("Water Flow Rate (%)", 0, 100, 60)
wind_speed = st.slider("Wind Speed (%)", 0, 100, 50)

# Auto-adjust readings based on environment
solar_v *= (sunlight / 100)
solar_i *= (sunlight / 100)

hydro_v *= (water_flow / 100)
hydro_i *= (water_flow / 100)

wind_v *= (wind_speed / 100)
wind_i *= (wind_speed / 100)
# ─────────────────────────────
# 2. Calculate power outputs
# ─────────────────────────────
solar_p = solar_v * solar_i
hydro_p = hydro_v * hydro_i
wind_p = wind_v * wind_i


from sklearn.linear_model import LinearRegression

# Simple prediction based on current total power
X = [[solar_p + hydro_p + wind_p]]
y = [solar_p + hydro_p + wind_p]  # since we have only one time point, just echo
model = LinearRegression()
model.fit(X, y)
predicted = model.predict([[solar_p + hydro_p + wind_p]])[0]
st.sidebar.metric(label="Total Power (W)", value=round(solar_p + hydro_p + wind_p, 2))
st.sidebar.metric(label="Predicted Next-Hour Output (W)", value=round(predicted, 2))

# ─────────────────────────────
# Sidebar metrics: display power
# ─────────────────────────────
st.sidebar.metric(label="Total Power (W)", value=round(solar_p + hydro_p + wind_p, 2))
st.sidebar.metric(label="Predicted Next-Hour Output (W)", value=round(predicted, 2))


data = {
    "Source": ["Solar", "Hydro", "Wind"],
    "Power (W)": [solar_p, hydro_p, wind_p]
}

df = pd.DataFrame(data)
st.subheader("Calculated Power Output")
st.dataframe(df)

# ─────────────────────────────
# 3. Visualize the power
# ─────────────────────────────

# ─────────────────────────────
# 🎛 Animated Circular Gauges
# ─────────────────────────────
st.subheader("⚡ Live Power Gauges (Animated)")

gauge_col1, gauge_col2, gauge_col3 = st.columns(3)

# Solar Gauge
with gauge_col1:
    fig_solar = go.Figure(go.Indicator(
        mode="gauge+number",
        value=solar_p,
        title={'text': "Solar (W)"},
        gauge={
            'axis': {'range': [0, max(solar_p, 50)]},
            'bar': {'color': "orange"}
        }
    ))
    st.plotly_chart(fig_solar, use_container_width=True)

# Hydro Gauge
with gauge_col2:
    fig_hydro = go.Figure(go.Indicator(
        mode="gauge+number",
        value=hydro_p,
        title={'text': "Hydro (W)"},
        gauge={
            'axis': {'range': [0, max(hydro_p, 50)]},
            'bar': {'color': "blue"}
        }
    ))
    st.plotly_chart(fig_hydro, use_container_width=True)

# Wind Gauge
with gauge_col3:
    fig_wind = go.Figure(go.Indicator(
        mode="gauge+number",
        value=wind_p,
        title={'text': "Wind (W)"},
        gauge={
            'axis': {'range': [0, max(wind_p, 50)]},
            'bar': {'color': "purple"}
        }
    ))
    st.plotly_chart(fig_wind, use_container_width=True)


st.subheader("📊 Power Comparison Graph")

colors = ['orange', 'blue', 'purple']
plt.figure(figsize=(6,4))
plt.bar(df["Source"], df["Power (W)"], color=colors, edgecolor='black')
plt.title("Power Output per Source", color='green', fontsize=14)
plt.ylabel("Power (W)", fontsize=12)
plt.xlabel("Energy Source", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(plt)

# ─────────────────────────────
# 4. AI Insights (simulated machine learning)
# ─────────────────────────────
# ─────────────────────────────
# 4. AI Insights (simulated machine learning)
# ─────────────────────────────
st.subheader("🧠 AI Insight & Digital Twin Alerts")

total = solar_p + hydro_p + wind_p

if total < 20:
    st.markdown(
        """
        <div style='background-color:#8B0000; padding:15px; border-radius:10px;'>
            <h4 style='color:white;'>⚠️ WARNING</h4>
            <p style='color:white;'>Your total output is very low. Increase sunlight, water flow, or wind speed.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif total < 50:
    st.markdown(
        """
        <div style='background-color:#B8860B; padding:15px; border-radius:10px;'>
            <h4 style='color:white;'>🙂 CAUTION</h4>
            <p style='color:white;'>System is working moderately. Optimizing conditions will improve output.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.markdown(
        """
        <div style='background-color:#006400; padding:15px; border-radius:10px;'>
            <h4 style='color:white;'>🚀 EXCELLENT</h4>
            <p style='color:white;'>Your hybrid system is performing at high efficiency.</p>
        </div>
        """,
        unsafe_allow_html=True
    )





# ─────────────────────────────
# 5. Simple Machine Learning Prediction (AI model)
# ─────────────────────────────
st.markdown("<h2 class='section-title'>🔮 AI Prediction for Next Hour Output</h2>", unsafe_allow_html=True)


# Prepare training data
X = df["Power (W)"].values.reshape(-1, 1)
y = df["Power (W)"].values  # simple prediction

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[sum([solar_p, hydro_p, wind_p]) / 3]])[0]

st.write(f"**Predicted Power Output Next Hour:** {predicted:.2f} W")

# ─────────────────────────────
# Sidebar metrics (after calculation)
# ─────────────────────────────
st.sidebar.metric(label="Total Power (W)", value=round(solar_p + hydro_p + wind_p, 2))
st.sidebar.metric(label="Predicted Next-Hour Output (W)", value=round(predicted, 2))

# Optimization tips
st.subheader("🧠 AI Optimization Tip")
if solar_p < hydro_p and solar_p < wind_p:
    st.write("🌞 Increase solar exposure — angle the panel or add reflective surfaces.")
elif hydro_p < solar_p and hydro_p < wind_p:
    st.write("💧 Increase water flow or turbine blade efficiency.")
else:
    st.write("🌬️ Improve wind direction or increase blade surface area.")


# ─────────────────────────────
# 6. PDF Report Generator
# ─────────────────────────────
from fpdf import FPDF

st.markdown("<h2 class='section-title'>📄 Generate PDF Report</h2>", unsafe_allow_html=True)


if st.button("Create Energy Report PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Hybrid Renewable Energy Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt="--- Input Readings ---", ln=True)
    pdf.cell(200, 10, txt=f"Solar: {solar_v:.2f}V, {solar_i:.2f}A", ln=True)
    pdf.cell(200, 10, txt=f"Hydro: {hydro_v:.2f}V, {hydro_i:.2f}A", ln=True)
    pdf.cell(200, 10, txt=f"Wind: {wind_v:.2f}V, {wind_i:.2f}A", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt="--- Power Outputs ---", ln=True)
    pdf.cell(200, 10, txt=f"Solar Power: {solar_p:.2f} W", ln=True)
    pdf.cell(200, 10, txt=f"Hydro Power: {hydro_p:.2f} W", ln=True)
    pdf.cell(200, 10, txt=f"Wind Power: {wind_p:.2f} W", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt="--- AI Prediction ---", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Next-Hour Output: {predicted:.2f} W", ln=True)
    pdf.ln(5)

    pdf.output("energy_report.pdf")

    with open("energy_report.pdf", "rb") as f:
        st.download_button(
            label="Download PDF Report",
            data=f,
            file_name="energy_report.pdf",
            mime="application/pdf"
        )
# ─────────────────────────────
# 7. Interactive Digital Twin Animation (Super Visual)
# ─────────────────────────────
st.markdown("<h2 class='section-title'>🌐 Live Digital Twin Animation</h2>", unsafe_allow_html=True)


solar_intensity = int(sunlight / 10)
wind_rotation = int(wind_speed / 10)
water_level = int(water_flow / 10)

# Create simple live ASCII animation
solar_display = "☀️" * solar_intensity if solar_intensity > 0 else "☀️"
wind_display = "🌀" * wind_rotation if wind_rotation > 0 else "🌀"
water_display = "💧" * water_level if water_level > 0 else "💧"

colA, colB, colC = st.columns(3)

with colA:
    st.markdown("### Solar Panel\nBrightness:")
    st.markdown(f"<h2 style='color:orange;'>{solar_display}</h2>", unsafe_allow_html=True)

with colB:
    st.markdown("### Wind Turbine\nRotation:")
    st.markdown(f"<h2 style='color:purple;'>{wind_display}</h2>", unsafe_allow_html=True)

with colC:
    st.markdown("### Water Turbine\nFlow Rate:")
    st.markdown(f"<h2 style='color:blue;'>{water_display}</h2>", unsafe_allow_html=True)


# ─────────────────────────────
# 8. Voice Assistant (AI Talks to Judges)
# ─────────────────────────────
st.markdown("<h2 class='section-title'>🗣️ AI Voice Assistant</h2>", unsafe_allow_html=True)


import base64

def text_to_speech(text):
    from gtts import gTTS
    tts = gTTS(text)
    tts.save("voice.mp3")
    with open("voice.mp3", "rb") as f:
        audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    return f"<audio controls src='data:audio/mp3;base64,{b64}'></audio>"

# Create dynamic voice message
voice_message = f"""
Current total power is {total:.2f} watts.
Solar output is {solar_p:.2f} watts.
Hydro output is {hydro_p:.2f} watts.
Wind output is {wind_p:.2f} watts.

AI Suggestion: 
"""

if solar_p < hydro_p and solar_p < wind_p:
    voice_message += "Increase solar exposure or panel angle."
elif hydro_p < solar_p and hydro_p < wind_p:
    voice_message += "Increase water flow or improve turbine blades."
else:
    voice_message += "Wind performance is low. Increase blade area or direction."

if st.button("🔊 Speak Insights"):
    audio_html = text_to_speech(voice_message)
    st.markdown(audio_html, unsafe_allow_html=True)


