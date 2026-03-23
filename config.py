"""
Configuration settings for Smart Route Risk Predictor
Centralized configuration for easy customization
"""

# ============================================
# MODEL PATHS
# ============================================

MODEL_PATHS = {
    'random_forest': 'models/random_forest_model.pkl',
    'label_encoders': 'models/label_encoders.pkl',
    'scaler': 'models/scaler.pkl',
    'feature_mapping': 'models/feature_mapping.json'
}

# ============================================
# RISK THRESHOLDS
# ============================================

RISK_THRESHOLDS = {
    'low': 30,      # 0-30: Low risk
    'medium': 60,   # 30-60: Medium risk
    'high': 100     # 60-100: High risk
}

# ============================================
# RISK FACTOR WEIGHTS
# ============================================

RISK_WEIGHTS = {
    'traffic': 0.30,           # Traffic volume influence
    'accident_history': 0.35,  # Historical accidents influence
    'road_condition': 0.20,    # Road quality influence
    'driver_alertness': 0.15   # Driver fatigue influence
}

# ============================================
# RISK CATEGORIES
# ============================================

RISK_CATEGORIES = {
    'Low': {
        'color': '#28a745',
        'emoji': '✓',
        'description': 'Route is relatively safe',
        'background_color': '#d4edda',
        'text_color': '#155724'
    },
    'Medium': {
        'color': '#ffc107',
        'emoji': '⚠',
        'description': 'Drive with caution',
        'background_color': '#fff3cd',
        'text_color': '#856404'
    },
    'High': {
        'color': '#dc3545',
        'emoji': '🚨',
        'description': 'High risk - avoid if possible',
        'background_color': '#f8d7da',
        'text_color': '#721c24'
    }
}

# ============================================
# WEATHER CONDITIONS
# ============================================

WEATHER_OPTIONS = [
    'Clear',
    'Rainy',
    'Foggy',
    'Snowy',
    'Windy',
    'Thunderstorm',
    'Hail',
    'Sleet'
]

# ============================================
# TIME OF DAY OPTIONS
# ============================================

TIME_OPTIONS = [
    'Morning (6-12)',
    'Afternoon (12-18)',
    'Evening (18-21)',
    'Night (21-6)'
]

# ============================================
# ROAD TYPES
# ============================================

ROAD_TYPES = [
    'Highway',
    'Urban Street',
    'Rural Road',
    'Mountain Road',
    'Residential',
    'Construction Zone'
]

# ============================================
# INPUT PARAMETER RANGES
# ============================================

INPUT_RANGES = {
    'traffic_volume': {
        'min': 0,
        'max': 100,
        'default': 40,
        'step': 5,
        'help': '0=No traffic, 100=Heavy gridlock'
    },
    'accident_history': {
        'min': 0,
        'max': 100,
        'default': 30,
        'step': 5,
        'help': '0=No accidents, 100=Very accident-prone'
    },
    'road_condition': {
        'min': 0,
        'max': 100,
        'default': 20,
        'step': 5,
        'help': '0=Perfect, 100=Severely damaged'
    },
    'driver_alertness': {
        'min': 0,
        'max': 100,
        'default': 10,
        'step': 5,
        'help': '0=Fully alert, 100=Severe fatigue'
    },
    'speed_limit': {
        'min': 20,
        'max': 120,
        'default': 80,
        'step': 10,
        'help': 'Posted speed limit (km/h)'
    },
    'vehicle_count': {
        'min': 0,
        'max': 1000,
        'default': 150,
        'step': 50,
        'help': 'Estimated number of vehicles'
    }
}

# ============================================
# RECOMMENDATION TEMPLATES
# ============================================

RECOMMENDATIONS = {
    'High': [
        "🚨 STRONGLY AVOID this route if possible",
        "If unavoidable, drive VERY slowly",
        "Enable hazard lights",
        "Maintain maximum following distance",
        "Consider alternative routes"
    ],
    'Medium': [
        "⚠️ Drive with increased caution",
        "Reduce speed by 10-15%",
        "Avoid using phone while driving",
        "Stay alert to road conditions"
    ],
    'Low': [
        "✓ Route is relatively safe",
        "Maintain normal driving practices",
        "Standard precautions apply"
    ]
}

WEATHER_RECOMMENDATIONS = {
    'Rainy': "🌧️ Rainy conditions - Use headlights and reduce speed",
    'Foggy': "🌫️ Foggy conditions - Use low beam lights",
    'Snowy': "❄️ Snowy conditions - Reduce speed significantly",
    'Windy': "💨 Windy conditions - Be cautious, especially on curves",
    'Thunderstorm': "⛈️ Thunderstorm - Consider postponing travel",
    'Hail': "🧊 Hail - Seek shelter or reduce speed",
    'Sleet': "⛸️ Sleet - Extremely slippery, reduce speed"
}

TIME_RECOMMENDATIONS = {
    'Morning (6-12)': "Morning traffic increasing - avoid rush hours (7-9 AM)",
    'Afternoon (12-18)': "Afternoon traffic moderate - safer travel window",
    'Evening (18-21)': "Evening rush hour (5-7 PM) - expect heavy traffic",
    'Night (21-6)': "🌙 Night driving - increased vigilance needed"
}

# ============================================
# APP SETTINGS
# ============================================

APP_SETTINGS = {
    'title': 'Smart Route Risk Predictor',
    'subtitle': 'Real-Time Route Safety Assessment & Recommendations',
    'description': 'Analyze route safety with ML-powered risk predictions',
    'icon': '🚗',
    'layout': 'wide',
    'sidebar_state': 'expanded'
}

# ============================================
# HISTORICAL DATA SETTINGS
# ============================================

HISTORICAL_DATA = {
    'days_to_show': 30,
    'update_interval': 300,  # 5 minutes
    'data_source': 'data/historical_data.csv'
}

# ============================================
# VISUALIZATION SETTINGS
# ============================================

VISUALIZATIONS = {
    'chart_height': 400,
    'gauge_height': 300,
    'heatmap_height': 400,
    'line_chart_height': 400,
    'color_scheme': 'plotly',  # 'plotly', 'seaborn', 'ggplot'
    'show_grid': True,
    'show_legend': True
}

# ============================================
# PERFORMANCE METRICS
# ============================================

PERFORMANCE_METRICS = {
    'model_accuracy': 0.842,
    'f1_score': 0.783,
    'precision': 0.816,
    'recall': 0.842,
    'false_positive_rate': 0.137,
    'false_negative_rate': 0.150
}

# ============================================
# DEFAULT VALUES
# ============================================

DEFAULTS = {
    'route_id': 'RT-001',
    'time_of_day': 'Afternoon (12-18)',
    'weather': 'Clear',
    'road_type': 'Highway',
    'traffic_volume': 40,
    'accident_history': 30,
    'road_condition': 20,
    'driver_alertness': 10,
    'speed_limit': 80,
    'vehicle_count': 150
}

# ============================================
# HAZARD DETECTION THRESHOLDS
# ============================================

HAZARD_THRESHOLDS = {
    'high_traffic': 70,
    'accident_prone': 60,
    'poor_road': 70,
    'driver_fatigue': 70,
    'high_vehicle_count': 500
}

# ============================================
# COLOR PALETTE
# ============================================

COLORS = {
    'primary': '#2c3e50',
    'success': '#27ae60',
    'warning': '#f39c12',
    'danger': '#e74c3c',
    'info': '#3498db',
    'light': '#ecf0f1',
    'dark': '#34495e'
}

# ============================================
# EMOJIS
# ============================================

EMOJIS = {
    'route': '📍',
    'risk': '⚠️',
    'weather': '🌤️',
    'traffic': '🚗',
    'road': '🛣️',
    'alert': '🚨',
    'safe': '✓',
    'caution': '⚠',
    'recommendation': '💡',
    'trend': '📈',
    'statistics': '📊',
    'analysis': '📋'
}

# ============================================
# MESSAGES
# ============================================

MESSAGES = {
    'model_loading': "Loading prediction model...",
    'calculating_risk': "Calculating risk score...",
    'generating_recommendations': "Generating safety recommendations...",
    'loading_historical': "Loading historical data...",
    'success': "✓ Analysis complete!",
    'error': "❌ An error occurred. Please try again.",
    'no_data': "No data available for this route.",
    'welcome': "Welcome to Smart Route Risk Predictor!"
}
