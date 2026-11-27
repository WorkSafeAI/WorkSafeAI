import streamlit as st

import streamlit as st

# Configure page to wide layout to fit 4 columns comfortably
st.set_page_config(layout="wide")

# Custom CSS for the glowing, dark-themed containers
st.markdown("""
    <style>
    /* Main School Banner Box */
    .school-box {
        background: linear-gradient(135deg, #07162c 0%, #030a14 100%);
        border: 1px solid #102a45;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0, 102, 204, 0.2);
        margin-bottom: 30px;
    }
    
    /* Individual Team Member Cards */
    .member-card {
        background: linear-gradient(135deg, #07162c 0%, #030a14 100%);
        border: 1px solid #102a45;
        border-radius: 12px;
        padding: 25px 15px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 102, 204, 0.15);
        min-height: 220px;
    }
    
    /* Circular Initials Avatar */
    .avatar-circle {
        width: 60px;
        height: 60px;
        background-color: #0099ff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px auto;
        color: white;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 0 15px rgba(0, 153, 255, 0.4);
    }
    
    /* Text elements styling */
    .school-title { color: #8892b0; font-size: 12px; margin-bottom: 5px; }
    .school-name { color: #ffffff; font-size: 18px; font-weight: 600; }
    .member-name { color: #ffffff; font-size: 16px; font-weight: 600; margin-top: 10px; }
    .member-role { 
        display: inline-block;
        background-color: rgba(0, 153, 255, 0.1); 
        color: #0099ff; 
        font-size: 11px; 
        padding: 3px 10px; 
        border-radius: 20px;
        margin-top: 8px;
        border: 1px solid rgba(0, 153, 255, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. Top Section Text ---
import streamlit as st

# 1. Custom CSS for the TEAM badge box background and shape
st.markdown("""
    <style>
    .custom-team-badge {
        background-color: #0d213a;          /* <-- CHANGE THIS HEX CODE FOR BACKGROUND COLOR */
        color: #0099ff;                     /* Text color */
        border: 1px solid #1a3a60;          /* Subtle border outline */
        border-radius: 8px;                 /* Roundness of the box corners */
        padding: 6px 16px;                  /* Padding inside the box */
        font-weight: 600;                   /* Text thickness */
        font-size: 13px;                    /* Text size */
        letter-spacing: 1px;                /* Spacing between letters */
        display: inline-block;              /* Keeps the box tight around the text */
        box-shadow: 0 0 10px rgba(0, 153, 255, 0.1); /* Subtle glow effect */
    }
    </style>
""", unsafe_allow_html=True)

# 2. Render the badge box on your page
# Note: Keep this tag completely flush against the left margin of your code editor
st.markdown('<div class="custom-team-badge">ABOUT PROJECT</div>', unsafe_allow_html=True)


st.title('AI-powered PPE detection')
st.title('for safer construction sites')
st.write("WorkSafe AI is an AI-powered Personal Protective Equipment detection system that improves workplace safety using Computer Vision and YOLOv8 object detection.")

import streamlit as st

# Configure page layout to fill the wide web display area cleanly
st.set_page_config(layout="wide")

# --- 1. GLOBLAL DASHBOARD CSS STYLING ---
st.markdown("""
    <style>
    /* Base wrapper for grid cells */
    .dashboard-card {
        background: linear-gradient(135deg, #071324 0%, #030811 100%);
        border: 1px solid #10243d;
        border-radius: 14px;
        padding: 28px;
        height: 100%; /* Ensures cards in the same row stay uniform */
        box-shadow: 0 0 20px rgba(0, 112, 243, 0.05);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    /* Left problem card gets an explicit subtle red tone accent */
    .problem-card {
        border-color: #2c161d;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.03);
    }
    
    /* Small circular icon housings */
    .icon-circle {
        width: 38px;
        height: 38px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
    }
    
    .icon-red { background-color: rgba(239, 68, 68, 0.15); color: #ef4444; }
    .icon-blue { background-color: rgba(0, 153, 255, 0.15); color: #0099ff; }
    
    /* Typography formatting */
    .card-title {
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
        margin: 0 0 12px 0;
    }
    
    .card-body {
        color: #8892b0; /* Subdued slate gray exactly like the image */
        font-size: 14px;
        line-height: 1.6;
        margin: 0;
    }
    
    /* Centered Objectives Badge component */
    .badge-center-wrapper {
        text-align: center;
        margin-top: 50px;
        margin-bottom: 15px;
    }
    
    .objectives-badge {
        background-color: rgba(0, 102, 255, 0.12);
        color: #0070f3;
        border: 1px solid rgba(0, 112, 243, 0.25);
        border-radius: 50px;
        padding: 4px 14px;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 0.8px;
        display: inline-block;
    }
    
    .section-title {
        color: #ffffff;
        font-size: 32px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)


# --- 2. ROW 1: PROBLEM & SOLUTION GRID (2 COLUMNS) ---
top_col1, top_col2 = st.columns(2)

with top_col1:
    st.markdown("""
    <div class="dashboard-card problem-card">
        <div class="icon-circle icon-red">⚠️</div>
        <h3 class="card-title">Problem Statement</h3>
        <p class="card-body">
            Construction workers often fail to wear protective equipment, increasing the risk of accidents. 
            Manual monitoring is difficult, inconsistent and labour-intensive — and AI can automate the process 
            to keep everyone accountable and safe.
        </p>
    </div>
    """, unsafe_allow_html=True)

with top_col2:
    st.markdown("""
    <div class="dashboard-card">
        <div class="icon-circle icon-blue">🎛️</div>
        <h3 class="card-title">Our Solution</h3>
        <p class="card-body">
            WorkSafe AI applies a trained YOLOv8 deep-learning model to camera feeds and uploaded images, 
            instantly identifying which protective equipment each worker is wearing — and flagging anyone 
            who is non-compliant.
        </p>
    </div>
    """, unsafe_allow_html=True)


# --- 3. MIDDLE SECTION: OBJECTIVES TITLE ---
st.markdown("""
<div class="badge-center-wrapper">
    <div class="objectives-badge">OBJECTIVES</div>
</div>
<h2 class="section-title">What WorkSafe AI sets out to achieve</h2>
""", unsafe_allow_html=True)


# --- 4. ROW 2: OBJECTIVES CORE METRICS (4 COLUMNS) ---
bot_col1, bot_col2, bot_col3, bot_col4 = st.columns(4)

with bot_col1:
    st.markdown("""
    <div class="dashboard-card">
        <div class="icon-circle icon-blue">🛡️</div>
        <h3 class="card-title">Improve worker safety</h3>
        <p class="card-body">Ensure every worker is protected before entering hazardous zones.</p>
    </div>
    """, unsafe_allow_html=True)

with bot_col2:
    st.markdown("""
    <div class="dashboard-card">
        <div class="icon-circle icon-blue">👁️</div>
        <h3 class="card-title">Detect essential PPE</h3>
        <p class="card-body">Recognise helmets, safety vests, masks, gloves and boots.</p>
    </div>
    """, unsafe_allow_html=True)

with bot_col3:
    st.markdown("""
    <div class="dashboard-card">
        <div class="icon-circle icon-blue">📈</div>
        <h3 class="card-title">Real-time monitoring</h3>
        <p class="card-body">Continuously analyse sites with live computer-vision detection.</p>
    </div>
    """, unsafe_allow_html=True)

with bot_col4:
    st.markdown("""
    <div class="dashboard-card">
        <div class="icon-circle icon-blue">⚡</div>
        <h3 class="card-title">Reduce accidents</h3>
        <p class="card-body">Lower workplace incidents through proactive, automated alerts.</p>
    </div>
    """, unsafe_allow_html=True)


