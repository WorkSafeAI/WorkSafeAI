import streamlit as st

# 1. Custom CSS for the TEAM badge box background and shape
st.markdown("""
    <style>
    .custom-team-badge {
        background-color: #0d213a;          /* <-- CHANGE THIS HEX CODE FOR BACKGROUND COLOR */
        color: #0099ff;                     /* Text color */
        border: 1px solid #1a3a60;          /* Subtle border outline */
        border-radius: 40px;                 /* Roundness of the box corners */
        padding: 6px 16px;                  /* Padding inside the box */
        font-weight: 800;                   /* Text thickness */
        font-size: 20px;                    /* Text size */
        letter-spacing: 3px;                /* Spacing between letters */
        display: inline-block;              /* Keeps the box tight around the text */
        box-shadow: 0 0 10px rgba(0, 153, 255, 0.1); /* Subtle glow effect */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center;"><div class="custom-team-badge" style="display: inline-block;">COMPUTER VISION YOLOV11</div></div>',
    unsafe_allow_html=True,
)

import base64
import streamlit as st

# Update this path to where you saved the uploaded .otf file
FONT_PATH = "StorystoneVintageAlphabet-ZpAPm.otf"

with open(FONT_PATH, "rb") as f:
    font_base64 = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'BourdewayVictorian';
        src: url(data:font/opentype;charset=utf-8;base64,{font_base64}) format('opentype');
        font-weight: normal;
        font-style: normal;
    }}
    </style>

    <h1 style="text-align: center; font-family: 'BourdewayVictorian', sans-serif; font-size: 3.2rem; line-height: 1.2;">
        WorkSafe AI: Intelligent<br>
        PPE Detection for <span style="color: #1c83e1;">Safer Workplaces</span>
    </h1>
    """,
    unsafe_allow_html=True,
)

st.write('-----------------')


st.markdown(
    """
    <p style="text-align: center; font-size: 1.35rem; margin: 0 auto 2rem auto; line-height: 1.6;">
        Using Computer Vision and YOLOv11 to automatically detect protective equipment like <br>
        helmets, safety vests in construction environments
    </p>
    """,
    unsafe_allow_html=True,
)

import streamlit as st

st.markdown(
    """
    <style>
    /* Base styling + subtle neon border glow for all buttons ('Learn more') */
    div.stButton > button {
        border-radius: 12px;
        height: 3.2rem;
        padding: 0 1.4rem;
        font-size: 1.05rem;
        font-weight: 600;
        border: 1.5px solid #00d2ff;
        color: #00d2ff;
        background-color: transparent;
        box-shadow: 0 0 8px rgba(0, 210, 255, 0.45), inset 0 0 6px rgba(0, 210, 255, 0.25);
        transition: all 0.3s ease-in-out;
    }

    div.stButton > button:hover {
        border-color: #38e8ff;
        color: #ffffff;
        background-color: rgba(0, 210, 255, 0.15);
        box-shadow: 0 0 14px rgba(0, 210, 255, 0.8), 0 0 28px rgba(0, 210, 255, 0.45);
    }

    /* Intense solid blue neon glow for primary button ('Try Detection →') */
    div.stButton > button[kind="primary"] {
        background-color: #1c83e1;
        color: #ffffff;
        border: 1.5px solid #4db8ff;
        box-shadow: 0 0 10px rgba(28, 131, 225, 0.8), 0 0 22px rgba(0, 210, 255, 0.5);
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #2196f3;
        color: #ffffff;
        border-color: #80d4ff;
        box-shadow: 0 0 16px rgba(28, 131, 225, 1), 0 0 34px rgba(0, 210, 255, 0.85), 0 0 50px rgba(0, 210, 255, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

left_space, col1, col2, right_space = st.columns([4, 1.2, 1, 4])

with col1:
    if st.button("Try Detection →", type="primary", use_container_width=True):
        st.switch_page("PPE Detection.py")

with col2:
    if st.button("Learn more", use_container_width=True):
        st.switch_page("abtproject.py")



import streamlit as st

st.markdown(
    """
    <style>
    .metrics-wrapper {
        display: flex;
        justify-content: center;
        align-items: stretch;
        gap: 1.5rem;
        margin: 2.5rem auto;
        flex-wrap: wrap;
        max-width: 900px;
    }

    .metric-box {
        flex: 1;
        min-width: 170px;
        max-width: 200px;
        padding: 1.4rem 1rem;
        border-radius: 14px;
        text-align: center;
        background: rgba(28, 131, 225, 0.08);
        border: 1.5px solid rgba(0, 210, 255, 0.5);
        box-shadow: 0 0 12px rgba(0, 210, 255, 0.25), inset 0 0 8px rgba(0, 210, 255, 0.15);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .metric-box:hover {
        transform: translateY(-4px);
        border-color: #00d2ff;
        box-shadow: 0 0 18px rgba(0, 210, 255, 0.6), inset 0 0 10px rgba(0, 210, 255, 0.25);
    }

    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(0, 210, 255, 0.7);
        margin-bottom: 0.3rem;
        line-height: 1.1;
    }

    .metric-label {
        font-size: 1rem;
        font-weight: 500;
        color: #9ec5e8;
        letter-spacing: 0.5px;
    }
    </style>

    <div class="metrics-wrapper">
        <div class="metric-box">
            <div class="metric-value">88.1%</div>
            <div class="metric-label">Precision</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">83.0%</div>
            <div class="metric-label">Recall</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">85.5%</div>
            <div class="metric-label">F1 Score</div>
        </div>
        <div class="metric-box">
            <div class="metric-value">2+</div>
            <div class="metric-label">PPE Classes</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)



