import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="Global Supply Chain Risk Index", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #0F172A; }
    h1, h2, h3 { color: #F1F5F9 !important; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 600; }
    .stAlert { background-color: #1E293B; border: 1px solid #475569; color: #F1F5F9; }
    div[data-testid="stMetricValue"] { color: #38BDF8 !important; }
    </style>
    """, unsafe_allow_html=True)

# KREDIT PENUH KEPADA KHAIRUL
st.title("🌐 Global Supply Chain Risk Index (GSCRI)")
st.subheader("Lead Risk Architect: Mohd Khairul Ridhuan bin Mohd Fadzil")
st.caption("A minimalist framework evaluating macro geopolitical and infrastructure stress vectors on critical trade corridors.")
st.markdown("---")

st.sidebar.markdown("### 📊 Analysis Control")
severity_filter = st.sidebar.slider("Minimum Risk Score Focus:", 0, 100, 50)
st.sidebar.markdown("---\n**Methodology Note:** Aggregate stress index generated based on the MECE framework using open-source intelligence.")

data = pd.DataFrame([
    {"corridor": "Suez Canal / Red Sea Transit", "lat": 20.0, "lon": 38.0, "risk_score": 84, "primary_stressor": "Macro Conflict Volatility"},
    {"corridor": "Strait of Malacca Sector", "lat": 1.35, "lon": 103.8, "risk_score": 68, "primary_stressor": "Localized Congestion & Anomaly"},
    {"corridor": "Panama Canal Passageway", "lat": 9.1, "lon": -79.7, "risk_score": 72, "primary_stressor": "Hydrological / Climate Bottleneck"},
    {"corridor": "Taiwan Strait Shipping Lane", "lat": 24.4, "lon": 118.3, "risk_score": 88, "primary_stressor": "Regional Policy & Transit Constraints"}
])

filtered_data = data[data["risk_score"] >= severity_filter]

m1, m2, m3 = st.columns(3)
m1.metric("Monitored Corridors", f"{len(data)} Core Lanes")
m2.metric("High-Risk Alerts", f"{len(filtered_data[filtered_data['risk_score'] >= 75])} Zones", delta="Critical Stress")
m3.metric("Average Risk Index", f"{int(filtered_data['risk_score'].mean()) if not filtered_data.empty else 0} / 100")

st.markdown("### 🗺️ Geospatial Risk Mapping")
col1, col2 = st.columns()

with col1:
    view_state = pdk.ViewState(latitude=15.0, longitude=30.0, zoom=1.8, pitch=40)
    layer = pdk.Layer(
        "ColumnLayer",
        filtered_data,
        get_position="[lon, lat]",
        get_elevation="risk_score * 4000",
        elevation_scale=100,
        radius=250000,
        get_fill_color="[56, 189, 248, 150]", # Sky Blue Premium
        pickable=True,
        auto_highlight=True,
    )
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "Corridor: {corridor}\nRisk Score: {risk_score}"}))

with col2:
    st.markdown("#### 📈 Stress Distribution")
    if not filtered_data.empty: st.bar_chart(filtered_data.set_index("corridor")["risk_score"])
    else: st.write("No corridors match the current filter criteria.")

st.markdown("---")
st.markdown("### 📋 Director-Level Strategic Assessment")
if not filtered_data.empty:
    selected_corridor = st.selectbox("Select Corridor for Advisory Framework:", filtered_data["corridor"].tolist())
    corridor_info = filtered_data[filtered_data["corridor"] == selected_corridor].iloc
    st.info(f"""
    **STRATEGIC MEMORANDUM // SUBJECT: RISK MITIGATION FOR {selected_corridor.upper()}**
    * **Current Exposure Index:** {corridor_info['risk_score']}/100  
    * **Identified Vulnerability:** The core disruption vector is driven primarily by *{corridor_info['primary_stressor']}*.
    
    **Advisory Recommendations (Consulting Framework):**
    1. **Operational Diversification:** Distribute freight allocation by 15-20% to secondary overland or intermodal routes to reduce single-point-of-failure exposure.
    2. **Financial Hedging:** Re-evaluate cargo insurance structures immediately, pricing in the current asset volatility premium rather than relying on historical baselines.
    3. **Proactive Buffer Staging:** Increase safety stock parameters by a factor of 1.4x for all components routing through this sector within the next 30 days.
    """)
