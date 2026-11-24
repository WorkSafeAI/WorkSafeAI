import streamlit as st 


# Configure page to wide layout to fit 4 columns comfortably
st.set_page_config(layout="wide")



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
st.markdown('<div class="custom-team-badge">FEATURES</div>', unsafe_allow_html=True)


st.title("A complete toolkit for AI safety monitoring")
st.write("WorkSafe AI combines deep-learning detection, live monitoring and rich analytics into one cohesive platform.")

st.write("---") # Visual separator

import streamlit as st

# 1. Page & Layout Setup
st.set_page_config(layout="wide")

# Check if a card was clicked using URL parameters
clicked_card = st.query_params.get("card")
if clicked_card:
    st.toast(f"Card clicked: **{clicked_card.upper()}**")
    st.query_params.clear()

# 2. Inject Custom CSS for Advanced Typography, Curvier Borders, and Outer Neon Lighting Effect
st.html(
    """
    <style>
    /* Main Background Match */
    .stApp {
        background-color: #030a16 !important;
        color: #ffffff !important;
    }
    
    /* 3-Column Grid Layout */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px 0;
    }
    
    /* Clickable Anchor Wrapper */
    .card-link {
        text-decoration: none !important;
        color: inherit !important;
        display: block;
    }
    
    /* Exact Card Mockup Replication with curvier borders */
    .feature-card {
        background-color: #071329;
        border: 1px solid #10264c;
        border-radius: 30px; /* Curvier smooth corners */
        padding: 24px;
        min-height: 200px;
        cursor: pointer;
        position: relative; 
        box-sizing: border-box;
        
        /* Smooth transitions for outer box-shadow lighting */
        transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), 
                    border-color 0.2s ease, 
                    box-shadow 0.2s ease;
    }
    
    /* High-Tech Lighting Effect (Triggers strictly outside the card frame) */
    .feature-card:hover {
        transform: translateY(-4px);
        border-color: #38bdf8; /* Brighter neon blue edge */
        
        /* Dual-layer sharp and blooming box-shadow tracking outward */
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.35), 
                    0 0 24px rgba(56, 189, 248, 0.15);
    }
    
    /* Proportional Inner Icon Container */
    .icon-container {
        width: 48px;
        height: 48px;
        background-color: #0b2554;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 16px;
    }
    
    /* Bolder Heading Font Configuration */
    .card-title {
        font-size: 1.15rem;
        font-weight: 800 !important; /* Heavy extra bold appearance */
        color: #ffffff !important;
        margin-bottom: 8px !important;
        margin-top: 0px !important;
        letter-spacing: -0.01em; /* Tightens bold spacing modernly */
    }
    
    /* Brighter White Subtext Configuration */
    .card-desc {
        font-size: 0.9rem;
        color: #f8fafc !important; /* Brighter crisp white for clear contrast */
        line-height: 1.5;
        margin: 0;
        opacity: 0.9; /* Keeps text smooth without blinding glare */
    }
    
    /* Responsive adjustment for mobile viewports */
    @media (max-width: 768px) {
        .grid-container {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """
)

# 3. Features Data Matrix
features = [
    {
        "id": "realtime",
        "icon": "🎯",
        "title": "Real-Time PPE Detection",
        "desc": "Detect protective equipment instantly across images and video.",
    },
    {
        "id": "yolo",
        "icon": "🌐",
        "title": "YOLOv11 Deep Learning Model",
        "desc": "A modern, high-accuracy object-detection architecture.",
    },
    {
        "id": "computervision",
        "icon": "👁️",
        "title": "Computer Vision Technology",
        "desc": "Pixel-level alignment of workers and their gear.",
    },
    {
        "id": "upload",
        "icon": "📤",
        "title": "Image Upload Support",
        "desc": "Drag and drop JPG, PNG or JPEG images for analysis.",
    },
    {
        "id": "analytics",
        "icon": "📊",
        "title": "Dashboard Analytics",
        "desc": "Track compliance rates, violations and detection trends.",
    },
    {
        "id": "alerts",
        "icon": "🛡️",
        "title": "Violation Alerts",
        "desc": "Get notified the moment required PPE is missing.",
    },
    {
        "id": "history",
        "icon": "🕒",
        "title": "Detection History",
        "desc": "A searchable log of every detection event over time.",
    },
    {
        "id": "predictions",
        "icon": "⚡",
        "title": "Fast & Accurate Predictions",
        "desc": "Low-latency inference optimised for real-world sites.",
    },
    {
        "id": "interface",
        "icon": "🛠️",
        "title": "User-Friendly Interface",
        "desc": "A clean, intuitive UI anyone on site can operate.",
    },
]

# 4. Generate the complete Grid Block
html_grid = '<div class="grid-container">'

for item in features:
    html_grid += f"""
    <a href="?card={item['id']}" target="_self" class="card-link">
        <div class="feature-card">
            <div class="icon-container">
                <span style='font-size: 20px;'>{item['icon']}</span>
            </div>
            <div class="card-title">{item['title']}</div>
            <div class="card-desc">{item['desc']}</div>
        </div>
    </a>
    """

html_grid += "</div>"

# Render the compiled structure 
st.html(html_grid)

st.write('-----------')
# Note: Keep this tag completely flush against the left margin of your code editor


# 1. Custom CSS for the TEAM badge box background and shape
st.markdown("""
    <style>
    .custom-team-badge {
        background-color: #0d213a;          /* <-- CHANGE THIS HEX CODE FOR BACKGROUND COLOR */
        color: #0099ff;                     /* Text color */
        border: 1px solid #1a3a60;          /* Subtle border outline */
        border-radius: 20px;                 /* Roundness of the box corners */
        padding: 6px 16px;                  /* Padding inside the box */
        font-weight: 700;                   /* Text thickness */
        font-size: 15px;                    /* Text size */
        letter-spacing: 1px;                /* Spacing between letters */
        display: inline-block;              /* Keeps the box tight around the text */
        box-shadow: 0 0 10px rgba(0, 153, 255, 0.1); /* Subtle glow effect */
    }
    </style>
""", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center;"><div class="custom-team-badge" style="display: inline-block;">TECHNOLOGY STACK</div></div>',
    unsafe_allow_html=True,
)