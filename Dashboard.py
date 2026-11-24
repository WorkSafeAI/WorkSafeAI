
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import os

st.set_page_config(layout="wide", page_title="Dashboard | WorkSafe AI")

# Custom CSS matching the dark theme of other pages
st.markdown("""
<style>
.custom-team-badge {
    background-color: #0d213a;
    color: #0099ff;
    border: 1px solid #1a3a60;
    border-radius: 20px;
    padding: 6px 16px;
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 1px;
    display: inline-block;
    box-shadow: 0 0 10px rgba(0, 153, 255, 0.1);
}
.metric-card {
    background: linear-gradient(135deg, #07162c 0%, #030a14 100%);
    border: 1px solid #102a45;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 0 15px rgba(0, 102, 204, 0.15);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-team-badge">DASHBOARD</div>', unsafe_allow_html=True)

import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(layout="wide")

# 2. Advanced Styling to overlay the file uploader invisible hitbox over the big box
st.markdown("""
    <style>
    /* Main Layout Cards styling */
    .upload-card, .result-card {
        background-color: #0b111e;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 24px;
        height: 400px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: relative;
    }
    
    /* Interactive dashed area */
    .dashed-wrapper {
        border: 2px dashed #334155;
        border-radius: 8px;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }
    
    .upload-icon, .detect-icon {
        font-size: 42px;
        color: #3b82f6;
        margin-bottom: 12px;
    }
    
    .title-text {
        font-size: 16px;
        font-weight: 600;
        color: #f8fafc;
        margin-bottom: 4px;
    }
    
    .sub-text {
        font-size: 13px;
        color: #94a3b8;
    }

    /* CRITICAL STEP: Makes the native Streamlit Uploader invisible but covers the entire card */
    .stFileUploader {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0;
        z-index: 10;
        cursor: pointer;
    }
    
    /* Ensure the wrapper inside streamlit spreads out to fill the container frame click box */
    .stFileUploader > div {
        width: 100%;
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize persistent session states for the image cycle
if 'raw_image' not in st.session_state:
    st.session_state.raw_image = None
if 'run_inference' not in st.session_state:
    st.session_state.run_inference = False

# Layout Structure splits (Left Side / Right Side)
col1, col2 = st.columns(2, gap="large")

# LEFT CARD: Clickable Upload Box
with col1:
    # Outer Card Wrapper Container
    with st.container():
        st.markdown('<div class="upload-card">', unsafe_allow_html=True)
        
        # Transparent invisible uploader handling system prompt triggers natively 
        uploaded_file = st.file_uploader(
            "uploader_hidden", 
            type=["jpg", "jpeg", "png"], 
            key="ppe_uploader",
            label_visibility="collapsed"
        )
        
        # Capture uploaded file event state directly into image data variables
        if uploaded_file is not None:
            st.session_state.raw_image = Image.open(uploaded_file)
            
        # CONDITIONAL RENDER: If image exists, draw it inside the box. Otherwise show text guidelines.
        if st.session_state.raw_image is not None:
            st.image(st.session_state.raw_image, use_container_width=True)
        else:
            st.markdown("""
                <div class="dashed-wrapper">
                    <div class="upload-icon">↑</div>
                    <div class="title-text">Drop an image here or click to upload</div>
                    <div class="sub-text">Supports JPG, JPEG, PNG</div>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write("") # Margin Spacer Row
    
    # Execution Command Button Row underneath card panel 
    btn1, btn2, btn3 = st.columns([1.5, 1.2, 1.3])
    with btn1:
        if st.button("🔍 Run Detection", type="primary", use_container_width=True, disabled=(st.session_state.raw_image is None)):
            st.session_state.run_inference = True
            
    with btn2:
        if st.button("🗑️ Clear Image", use_container_width=True):
            st.session_state.raw_image = None
            st.session_state.run_inference = False
            st.rerun()
            
    with btn3:
        st.button("📥 Download Result", use_container_width=True, disabled=not st.session_state.run_inference)


# RIGHT CARD: Live Evaluation Window Box
with col2:
    with st.container():
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        if not st.session_state.run_inference:
            st.markdown("""
                <div class="detect-icon">🔲</div>
                <div class="title-text">No detection yet</div>
                <div class="sub-text">Upload an image and run the detector to see results here.</div>
            """, unsafe_allow_html=True)
        else:
            # Placeholder representing the finalized computer vision inference target canvas
            st.image(st.session_state.raw_image, caption="Processed PPE Analysis Output Visualized", use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

