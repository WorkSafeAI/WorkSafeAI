
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
        border-radius: 20px;                 /* Roundness of the box corners */
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
st.markdown('<div class="custom-team-badge">TEAM</div>', unsafe_allow_html=True)






st.title("The minds behind WorkSafe AI")
st.write("WorkSafe AI - AI-Based PPE Detection System, built by students...")

st.write("---") # Visual separator

# --- 2. School Container ---

import base64
import streamlit as st

# Function to safely convert local image file to base64 HTML string
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# ---- 1. Encode your image ----
try:
    school_logo_base64 = get_image_as_base64("dpslogo.png")
except FileNotFoundError:
    school_logo_base64 = "https://placehold.co"

# ---- 2. Inject CSS Styles ----
st.markdown("""
    <style>
    .school-box {
        background: linear-gradient(135deg, #07162c 0%, #030a14 100%);
        border: 1px solid #102a45;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 0 20px rgba(0, 102, 204, 0.2);
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px; 
    }
    
    .school-logo-img {
        width: 45px;
        height: 45px;
        object-fit: contain;
        border-radius: 6px;
    }
    
    .school-text-container {
        text-align: left;
    }
    
    .school-title { color: #8892b0; font-size: 12px; margin-bottom: 2px; }
    .school-name { color: #ffffff; font-size: 18px; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# ---- 3. Corrected School Container Render (Removed Indentation) ----
# Note: Keeping the HTML tags completely flush to the left wall forces Markdown to render it correctly!
st.markdown(f"""
<div class="school-box">
<img src="{school_logo_base64}" class="school-logo-img" alt="School Logo">
<div class="school-text-container">
<div class="school-title">School</div>
<div class="school-name">Delhi Public School Bangalore South</div>
</div>
</div>
""", unsafe_allow_html=True)







# --- 3. Team Members Grid (4 Columns) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="member-card">
            <div class="avatar-circle">DS</div>
            <div class="member-name">Daksh Singh</div>
            <div class="member-role">💼 Project Leader</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="member-card">
            <div class="avatar-circle">AR</div>
            <div class="member-name">Aditya Ranjan Sahoo</div>
            <div class="member-role">📊 Data Expert</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="member-card">
            <div class="avatar-circle">AA</div>
            <div class="member-name">Adishesh Anand</div>
            <div class="member-role">🔍 Information Researcher</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="member-card">
            <div class="avatar-circle">TB</div>
            <div class="member-name">Tanuj Byri</div>
            <div class="member-role">🛠️ Prototype Builder & Tester</div>
        </div>
    """, unsafe_allow_html=True)








