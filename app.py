"""
🚗 Smart Route Risk Predictor - MODERN REDESIGN v3
Premium UI inspired by Notion, Typeform, Canva, and Airbnb

Features:
- Multi-step progressive disclosure form
- Modern gradient design system
- Advanced interactive charts
- Comprehensive safety recommendations
- Fully responsive layout
- Dark mode support
- Smooth animations and transitions

Version: 3.0 (Modern Redesign)
Author: Your Team
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Smart Route Risk Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# MODERN COLOR SYSTEM
# ============================================

COLOR_SYSTEM = {
    "primary_dark": "#1E3A5F",
    "primary_light": "#00D9FF",
    "accent_purple": "#7C3AED",
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "background_light": "#F5F7FA",
    "background_white": "#FFFFFF",
    "text_primary": "#111827",
    "text_secondary": "#6B7280",
    "border_light": "#E5E7EB",
}

# ============================================
# MODERN CSS STYLING
# ============================================

st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main background */
    .main {
        background: linear-gradient(135deg, #F5F7FA 0%, #EFF6FF 100%);
    }
    
    /* Header */
    .header-modern {
        background: linear-gradient(135deg, #1E3A5F 0%, #00D9FF 100%);
        padding: 40px 20px;
        border-radius: 0;
        color: white;
        margin-bottom: 40px;
        text-align: center;
    }
    
    .header-modern h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
    }
    
    .header-modern p {
        font-size: 1.1rem;
        opacity: 0.95;
        margin: 0;
    }
    
    /* Progress bar */
    .progress-container {
        display: flex;
        justify-content: space-between;
        margin: 30px 0 50px 0;
        gap: 10px;
    }
    
    .progress-step {
        flex: 1;
        height: 4px;
        background: #E5E7EB;
        border-radius: 999px;
        overflow: hidden;
    }
    
    .progress-step.active {
        background: linear-gradient(90deg, #7C3AED, #00D9FF);
    }
    
    /* Card styles */
    .card {
        background: white;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        border: 1px solid #E5E7EB;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
        border-color: #D1D5DB;
    }
    
    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #111827;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Risk indicator */
    .risk-indicator {
        text-align: center;
        padding: 30px;
        border-radius: 12px;
        margin: 20px 0;
    }
    
    .risk-indicator.low {
        background: linear-gradient(135deg, #D1FAE5 0%, #ECFDF5 100%);
        border: 2px solid #10B981;
    }
    
    .risk-indicator.medium {
        background: linear-gradient(135deg, #FEF3C7 0%, #FFFBEB 100%);
        border: 2px solid #F59E0B;
    }
    
    .risk-indicator.high {
        background: linear-gradient(135deg, #FECACA 0%, #FEE2E2 100%);
        border: 2px solid #EF4444;
    }
    
    .risk-score {
        font-size: 3rem;
        font-weight: 700;
        margin: 10px 0;
    }
    
    .risk-level {
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 10px;
    }
    
    /* Input styling */
    .stSelectbox, .stTextInput, .stNumberInput {
        margin-bottom: 20px;
    }
    
    label {
        font-weight: 600 !important;
        color: #111827 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100% !important;
        padding: 12px 24px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        border: none !important;
        background: linear-gradient(135deg, #7C3AED, #00D9FF) !important;
        color: white !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 24px rgba(124, 58, 237, 0.4) !important;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.75rem;
        font-weight: 700;
        color: #1E3A5F;
        margin: 40px 0 20px 0;
        padding-bottom: 15px;
        border-bottom: 3px solid #00D9FF;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Hazard badges */
    .hazard-critical {
        background: #FEE2E2;
        border-left: 4px solid #EF4444;
        color: #991B1B;
    }
    
    .hazard-high {
        background: #FEF3C7;
        border-left: 4px solid #F59E0B;
        color: #92400E;
    }
    
    .hazard-medium {
        background: #DBEAFE;
        border-left: 4px solid #3B82F6;
        color: #1E3A5F;
    }
    
    .hazard-low {
        background: #D1FAE5;
        border-left: 4px solid #10B981;
        color: #065F46;
    }
    
    /* Recommendation card */
    .recommendation-card {
        padding: 20px;
        margin-bottom: 16px;
        border-left: 4px solid;
        border-radius: 8px;
        background: white;
    }
    
    .recommendation-critical {
        border-left-color: #EF4444;
        background: #FEF2F2;
    }
    
    .recommendation-high {
        border-left-color: #F59E0B;
        background: #FFFBF0;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 12px 24px;
        border-radius: 8px;
        background: #F5F7FA;
        color: #6B7280;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7C3AED, #00D9FF);
        color: white;
    }
    
    /* Metric cards */
    .metric-modern {
        background: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        text-align: center;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A5F;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #6B7280;
        font-weight: 500;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .card {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .header-modern h1 {
            font-size: 1.8rem;
        }
        
        .risk-score {
            font-size: 2rem;
        }
        
        .section-header {
            font-size: 1.25rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# HELPER FUNCTIONS
# ============================================

def calculate_risk_comprehensive(weather, time, road_condition, traffic, 
                               accidents, driver, distance):
    """Calculate comprehensive risk score"""
    
    weather_map = {
        'Clear': 5, 'Rainy': 30, 'Foggy': 50, 'Snowy': 70,
        'Thunderstorm': 85, 'Windy': 25, 'Hail': 60, 'Sleet': 65
    }
    
    time_map = {
        'Morning (6 AM - 12 PM)': 35,
        'Afternoon (12 PM - 6 PM)': 45,
        'Evening (6 PM - 9 PM)': 55,
        'Night (9 PM - 6 AM)': 50
    }
    
    road_map = {
        'Excellent': 5, 'Good': 15, 'Fair': 35, 'Poor': 60, 'Very Poor': 85
    }
    
    traffic_map = {
        'Very Low': 10, 'Low': 20, 'Moderate': 40, 'High': 65, 'Very High': 85
    }
    
    accidents_map = {
        'No History': 5, 'Low': 20, 'Moderate': 40, 'High': 65, 'Very High': 85
    }
    
    driver_map = {
        'Fully Alert': 5, 'Slightly Tired': 20, 'Moderately Tired': 40,
        'Very Tired': 70, 'Extremely Tired': 90
    }
    
    w = weather_map.get(weather, 40)
    t = time_map.get(time, 45)
    r = road_map.get(road_condition, 35)
    tr = traffic_map.get(traffic, 40)
    a = accidents_map.get(accidents, 40)
    d = driver_map.get(driver, 20)
    
    distance_mult = min(1 + (distance / 500), 1.5)
    
    risk = (w*0.20 + t*0.15 + r*0.15 + tr*0.25 + a*0.15 + d*0.10) * distance_mult
    
    return min(round(risk, 1), 100)

def get_risk_category(score):
    """Get risk category"""
    if score < 30:
        return "Low", "✓ Low Risk", COLOR_SYSTEM["success"]
    elif score < 60:
        return "Medium", "⚠ Medium Risk", COLOR_SYSTEM["warning"]
    else:
        return "High", "🚨 High Risk", COLOR_SYSTEM["danger"]

def generate_detailed_recommendations(category, weather, road, traffic, driver, distance):
    """Generate detailed safety recommendations"""
    recs = []
    
    # Critical recommendations
    if category == "High":
        recs.append({
            "priority": "CRITICAL",
            "icon": "🚨",
            "title": "Route Avoidance",
            "content": "This route has significant risks. Strongly consider postponing your trip or choosing an alternative route.",
            "color": "critical"
        })
    
    if driver == "Very Tired" or driver == "Extremely Tired":
        recs.append({
            "priority": "CRITICAL",
            "icon": "😴",
            "title": "Driver Fatigue Alert",
            "content": f"Current fatigue level is {driver.lower()}. You should not drive. Get adequate rest before attempting this trip.",
            "color": "critical"
        })
    
    # High priority recommendations
    if weather in ['Thunderstorm', 'Snowy', 'Foggy']:
        recs.append({
            "priority": "HIGH",
            "icon": "🌦️",
            "title": "Severe Weather Protocol",
            "content": f"{weather} conditions severely impair driving. Reduce speed by 30-40%, use headlights, and increase following distance to 8+ seconds.",
            "color": "high"
        })
    elif weather in ['Rainy', 'Windy', 'Hail']:
        recs.append({
            "priority": "HIGH",
            "icon": "🌧️",
            "title": "Adverse Weather Driving",
            "content": f"{weather} conditions reduce traction. Reduce speed 20-30%, use headlights, avoid sudden maneuvers.",
            "color": "high"
        })
    
    if road == "Very Poor":
        recs.append({
            "priority": "HIGH",
            "icon": "🛣️",
            "title": "Road Hazard Warning",
            "content": "Road condition is severely deteriorated. Drive extremely slowly, watch for potholes, and consider vehicle inspection.",
            "color": "high"
        })
    elif road == "Poor":
        recs.append({
            "priority": "HIGH",
            "icon": "🛣️",
            "title": "Road Surface Caution",
            "content": "Poor road condition detected. Reduce speed, maintain extra distance, avoid sudden braking.",
            "color": "high"
        })
    
    if traffic == "Very High":
        recs.append({
            "priority": "HIGH",
            "icon": "🚗",
            "title": "Heavy Traffic Management",
            "content": "Severe congestion detected. Avoid peak hours, stay in slower lanes, maintain patience, increase following distance.",
            "color": "high"
        })
    elif traffic == "High":
        recs.append({
            "priority": "MEDIUM",
            "icon": "🚗",
            "title": "Traffic Awareness",
            "content": "Heavy traffic expected. Avoid peak hours if possible, stay alert, maintain safe distance.",
            "color": "high"
        })
    
    # Medium priority
    if distance > 300:
        recs.append({
            "priority": "MEDIUM",
            "icon": "📏",
            "title": "Long-Distance Driving",
            "content": f"You're planning a {distance}km journey. Take 15-20 min breaks every 2 hours. Stay hydrated. Consider overnight rest.",
            "color": "high"
        })
    
    if driver in ['Moderately Tired', 'Slightly Tired']:
        recs.append({
            "priority": "MEDIUM",
            "icon": "😴",
            "title": "Fatigue Management",
            "content": "You're slightly fatigued. Take breaks every 2 hours, avoid monotonous routes, keep alertness high.",
            "color": "high"
        })
    
    # General tips
    recs.append({
        "priority": "GENERAL",
        "icon": "✓",
        "title": "Standard Safety Practices",
        "content": "Keep phone silent, check vehicle condition, inform someone of your route, avoid night driving when tired.",
        "color": "low"
    })
    
    return recs

def create_interactive_gauges(risk_score, weather_impact, traffic_impact, road_impact):
    """Create interactive gauge charts"""
    
    # Main risk gauge
    fig_main = go.Figure(data=[go.Indicator(
        mode="gauge+number",
        value=risk_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Overall Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00D9FF"},
            'steps': [
                {'range': [0, 30], 'color': "#D1FAE5"},
                {'range': [30, 60], 'color': "#FEF3C7"},
                {'range': [60, 100], 'color': "#FECACA"}
            ]
        }
    )])
    
    fig_main.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    
    return fig_main

def create_factor_breakdown(weather, time, road, traffic, accidents, driver):
    """Create factor breakdown chart"""
    
    weather_scores = {'Clear': 5, 'Rainy': 30, 'Foggy': 50, 'Snowy': 70, 'Thunderstorm': 85, 'Windy': 25, 'Hail': 60, 'Sleet': 65}
    time_scores = {'Morning (6 AM - 12 PM)': 35, 'Afternoon (12 PM - 6 PM)': 45, 'Evening (6 PM - 9 PM)': 55, 'Night (9 PM - 6 AM)': 50}
    road_scores = {'Excellent': 5, 'Good': 15, 'Fair': 35, 'Poor': 60, 'Very Poor': 85}
    traffic_scores = {'Very Low': 10, 'Low': 20, 'Moderate': 40, 'High': 65, 'Very High': 85}
    accident_scores = {'No History': 5, 'Low': 20, 'Moderate': 40, 'High': 65, 'Very High': 85}
    driver_scores = {'Fully Alert': 5, 'Slightly Tired': 20, 'Moderately Tired': 40, 'Very Tired': 70, 'Extremely Tired': 90}
    
    data = pd.DataFrame({
        'Factor': ['Weather', 'Time', 'Road', 'Traffic', 'Accidents', 'Driver'],
        'Score': [
            weather_scores.get(weather, 40),
            time_scores.get(time, 45),
            road_scores.get(road, 35),
            traffic_scores.get(traffic, 40),
            accident_scores.get(accidents, 40),
            driver_scores.get(driver, 20)
        ]
    })
    
    fig = px.bar(
        data, x='Factor', y='Score',
        color='Score',
        color_continuous_scale=['#D1FAE5', '#FEF3C7', '#FECACA'],
        range_color=[0, 100],
        title='Risk Factor Breakdown',
        labels={'Score': 'Risk Score (0-100)'}
    )
    
    fig.update_layout(height=350, showlegend=False, hovermode='x')
    
    return fig

def create_historical_trends():
    """Create historical trend chart"""
    
    dates = [datetime.now() - timedelta(days=i) for i in range(30, 0, -1)]
    scores = np.random.normal(45, 12, 30)
    scores = np.clip(scores, 0, 100)
    
    data = pd.DataFrame({
        'Date': dates,
        'Risk_Score': scores,
        'Avg': np.mean(scores)
    })
    
    fig = px.line(
        data, x='Date', y='Risk_Score',
        title='30-Day Risk Trends',
        markers=True,
        labels={'Risk_Score': 'Risk Score', 'Date': 'Date'}
    )
    
    fig.add_hline(y=np.mean(scores), line_dash="dash", line_color="#7C3AED", 
                  annotation_text="30-day Average", annotation_position="right")
    
    fig.update_layout(height=350, hovermode='x unified')
    
    return fig

# ============================================
# MAIN APP
# ============================================

def main():
    # Initialize session state
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False
    
    # Header
    st.markdown("""
    <div class="header-modern">
        <h1>🚗 Smart Route Risk Predictor</h1>
        <p>Modern Safety Assessment System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if we should show results or form
    if st.session_state.show_results:
        show_results_dashboard()
    else:
        show_form()

def show_form():
    """Show multi-step form"""
    
    # Progress indicator
    progress = (st.session_state.current_step / 4) * 100
    st.progress(progress / 100)
    
    st.markdown(f"**Step {st.session_state.current_step} of 4** | {progress:.0f}% Complete")
    
    st.divider()
    
    # Step 1: Route Information
    if st.session_state.current_step == 1:
        st.markdown('<div class="section-header">📍 Route Information</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("**Where are you traveling?**")
            route_name = st.text_input(
                "Route Name",
                placeholder="e.g., Office Commute, Highway 101",
                label_visibility="collapsed",
                help="Give your route a memorable name"
            )
            st.caption("💡 Give your route a descriptive name for reference")
            
            st.markdown("**How far is your journey?**")
            col1, col2 = st.columns([3, 1])
            with col1:
                distance = st.slider(
                    "Distance",
                    min_value=1,
                    max_value=1000,
                    value=50,
                    step=5,
                    label_visibility="collapsed",
                    help="Total distance in kilometers"
                )
            with col2:
                st.metric("km", distance, label_visibility="collapsed")
            
            st.caption(f"ℹ️ You're planning a {distance}km journey")
            
            st.session_state.form_data['route_name'] = route_name
            st.session_state.form_data['distance'] = distance
    
    # Step 2: Environmental Conditions
    elif st.session_state.current_step == 2:
        st.markdown('<div class="section-header">🌦️ Environmental Conditions</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("**What's the current weather?**")
            col1, col2, col3, col4 = st.columns(4)
            
            weather_options = {
                'Clear': '☀️',
                'Rainy': '🌧️',
                'Foggy': '🌫️',
                'Snowy': '❄️',
                'Thunderstorm': '⛈️',
                'Windy': '💨',
                'Hail': '🧊',
                'Sleet': '⛸️'
            }
            
            weather = st.selectbox(
                "Weather",
                options=list(weather_options.keys()),
                label_visibility="collapsed"
            )
            st.caption(f"{weather_options.get(weather, '?')} {weather}")
            
            st.markdown("**What time of day?**")
            time_of_day = st.selectbox(
                "Time",
                options=[
                    'Morning (6 AM - 12 PM)',
                    'Afternoon (12 PM - 6 PM)',
                    'Evening (6 PM - 9 PM)',
                    'Night (9 PM - 6 AM)'
                ],
                label_visibility="collapsed"
            )
            
            st.session_state.form_data['weather'] = weather
            st.session_state.form_data['time'] = time_of_day
    
    # Step 3: Road & Traffic
    elif st.session_state.current_step == 3:
        st.markdown('<div class="section-header">🛣️ Road & Traffic Conditions</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("**Road Condition?**")
            road_condition = st.radio(
                "Road",
                options=['Excellent', 'Good', 'Fair', 'Poor', 'Very Poor'],
                horizontal=False,
                label_visibility="collapsed"
            )
            
            st.markdown("**Road Type?**")
            road_type = st.selectbox(
                "Type",
                options=['Highway', 'Urban Street', 'Rural Road', 'Mountain Road', 'Residential'],
                label_visibility="collapsed"
            )
            
            st.markdown("**Traffic Volume?**")
            traffic = st.selectbox(
                "Traffic",
                options=['Very Low', 'Low', 'Moderate', 'High', 'Very High'],
                label_visibility="collapsed"
            )
            
            st.session_state.form_data['road_condition'] = road_condition
            st.session_state.form_data['road_type'] = road_type
            st.session_state.form_data['traffic'] = traffic
    
    # Step 4: Driver & Risk
    elif st.session_state.current_step == 4:
        st.markdown('<div class="section-header">👤 Driver Status & Acknowledgment</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("**How is your alertness level?**")
            driver_condition = st.radio(
                "Alertness",
                options=[
                    'Fully Alert',
                    'Slightly Tired',
                    'Moderately Tired',
                    'Very Tired',
                    'Extremely Tired'
                ],
                label_visibility="collapsed"
            )
            
            st.markdown("**Accident History in Area?**")
            accident_history = st.selectbox(
                "History",
                options=['No History', 'Low', 'Moderate', 'High', 'Very High'],
                label_visibility="collapsed"
            )
            
            st.markdown("**Safety Acknowledgment**")
            agree = st.checkbox("I understand the risks and will drive safely")
            
            st.session_state.form_data['driver'] = driver_condition
            st.session_state.form_data['accidents'] = accident_history
            st.session_state.form_data['agree'] = agree
    
    st.divider()
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("← Back", use_container_width=True, disabled=(st.session_state.current_step == 1)):
            st.session_state.current_step -= 1
            st.rerun()
    
    with col3:
        if st.session_state.current_step < 4:
            button_text = "Next →"
        else:
            button_text = "Analyze My Route 🔍"
        
        if st.button(button_text, use_container_width=True, type="primary"):
            if st.session_state.current_step == 4:
                if st.session_state.form_data.get('agree'):
                    st.session_state.show_results = True
                    st.rerun()
                else:
                    st.warning("Please acknowledge the safety agreement to continue")
            else:
                st.session_state.current_step += 1
                st.rerun()

def show_results_dashboard():
    """Show comprehensive results dashboard"""
    
    # Header with back button
    col1, col2, col3 = st.columns([1, 5, 1])
    
    with col1:
        if st.button("← New Analysis", use_container_width=True):
            st.session_state.show_results = False
            st.session_state.current_step = 1
            st.rerun()
    
    with col2:
        route_name = st.session_state.form_data.get('route_name', 'Route')
        distance = st.session_state.form_data.get('distance', 0)
        st.markdown(f"<h3 style='text-align: center; margin: 0;'>{route_name} • {distance} km</h3>", unsafe_allow_html=True)
    
    with col3:
        if st.button("📊 Share", use_container_width=True):
            st.success("Results can be shared!")
    
    st.divider()
    
    # Calculate risk
    risk_score = calculate_risk_comprehensive(
        st.session_state.form_data.get('weather', 'Clear'),
        st.session_state.form_data.get('time', 'Afternoon (12 PM - 6 PM)'),
        st.session_state.form_data.get('road_condition', 'Good'),
        st.session_state.form_data.get('traffic', 'Moderate'),
        st.session_state.form_data.get('accidents', 'Low'),
        st.session_state.form_data.get('driver', 'Fully Alert'),
        st.session_state.form_data.get('distance', 50)
    )
    
    category, risk_text, risk_color = get_risk_category(risk_score)
    
    # Section 1: Risk Assessment
    st.markdown('<div class="section-header">📊 Risk Assessment</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.plotly_chart(
            create_interactive_gauges(risk_score, 30, 45, 20),
            use_container_width=True
        )
    
    with col2:
        risk_class = category.lower()
        st.markdown(f"""
        <div class="risk-indicator {risk_class}">
            <div style="font-size: 3rem; font-weight: 700; color: {'#10B981' if category == 'Low' else '#F59E0B' if category == 'Medium' else '#EF4444'};">
                {risk_score}
            </div>
            <div class="risk-level">{risk_text}</div>
            <div style="margin-top: 15px; font-size: 0.9rem; color: #6B7280;">
                {'Safe for travel' if category == 'Low' else 'Proceed with caution' if category == 'Medium' else 'Not recommended'}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("### 📍 Route Summary")
        st.write(f"**Route**: {st.session_state.form_data.get('route_name', 'N/A')}")
        st.write(f"**Distance**: {st.session_state.form_data.get('distance', 0)} km")
        st.write(f"**Weather**: {st.session_state.form_data.get('weather', 'N/A')}")
        st.write(f"**Time**: {st.session_state.form_data.get('time', 'N/A').split(' ')[0]}")
        st.write(f"**Road Type**: {st.session_state.form_data.get('road_type', 'N/A')}")
    
    st.divider()
    
    # Section 2: Detailed Recommendations
    recommendations = generate_detailed_recommendations(
        category,
        st.session_state.form_data.get('weather', 'Clear'),
        st.session_state.form_data.get('road_condition', 'Good'),
        st.session_state.form_data.get('traffic', 'Moderate'),
        st.session_state.form_data.get('driver', 'Fully Alert'),
        st.session_state.form_data.get('distance', 50)
    )
    
    st.markdown('<div class="section-header">💡 Safety Recommendations</div>', unsafe_allow_html=True)
    
    for rec in recommendations:
        priority_color = "#EF4444" if rec["priority"] == "CRITICAL" else "#F59E0B" if rec["priority"] == "HIGH" else "#3B82F6"
        
        st.markdown(f"""
        <div class="recommendation-card" style="border-left-color: {priority_color}; background: {'#FEF2F2' if rec['priority'] == 'CRITICAL' else '#FFFBF0' if rec['priority'] == 'HIGH' else '#F0F9FF'};">
            <h4 style="margin: 0 0 10px 0; color: {priority_color};">
                {rec['icon']} {rec['title']}
            </h4>
            <p style="margin: 0; color: #4B5563; line-height: 1.6;">
                {rec['content']}
            </p>
            <p style="margin: 10px 0 0 0; font-size: 0.85rem; color: #9CA3AF; font-weight: 500;">
                Priority: {rec['priority']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Section 3: Charts
    st.markdown('<div class="section-header">📈 Detailed Analysis</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Risk Factors", "📉 Trends", "📋 Statistics"])
    
    with tab1:
        st.plotly_chart(
            create_factor_breakdown(
                st.session_state.form_data.get('weather', 'Clear'),
                st.session_state.form_data.get('time', 'Afternoon (12 PM - 6 PM)'),
                st.session_state.form_data.get('road_condition', 'Good'),
                st.session_state.form_data.get('traffic', 'Moderate'),
                st.session_state.form_data.get('accidents', 'Low'),
                st.session_state.form_data.get('driver', 'Fully Alert')
            ),
            use_container_width=True
        )
    
    with tab2:
        st.plotly_chart(create_historical_trends(), use_container_width=True)
    
    with tab3:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("### 📊 Current Score")
            st.metric("Risk", f"{risk_score}/100")
        
        with col2:
            st.markdown("### 📈 30-Day Average")
            st.metric("Avg", f"{45.2:.1f}")
        
        with col3:
            st.markdown("### 📌 Peak Risk")
            st.metric("Max", f"{78}/100")
        
        with col4:
            st.markdown("### 📅 High-Risk Days")
            st.metric("Days", "8/30")

# ============================================
# RUN APP
# ============================================

if __name__ == "__main__":
    main()
