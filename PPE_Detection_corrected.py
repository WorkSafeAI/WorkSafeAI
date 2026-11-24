
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

st.markdown('<div class="custom-team-badge">PPE DETECTION</div>', unsafe_allow_html=True)
st.title("PPE Detection Dashboard")
st.write("Upload an image of workers to detect hard hats and safety vests using the trained YOLOv11 model.")

# Resolve the model path relative to this Python file.
# Expected repository structure:
# WorkSafeAI/
#   PPE Detection.py
#   models/
#     best.pt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best.pt"


@st.cache_resource
def load_model():
    """Load and cache the YOLO model."""
    if not MODEL_PATH.is_file():
        st.error(f"Model file not found: {MODEL_PATH}")

        st.write("PPE Detection.py directory:", str(BASE_DIR))
        st.write("Project-root files:", sorted(p.name for p in BASE_DIR.iterdir()))

        models_dir = BASE_DIR / "models"
        if models_dir.is_dir():
            st.write(
                "Files inside models/:",
                sorted(p.name for p in models_dir.iterdir())
            )
        else:
            st.error("The 'models' folder does not exist beside PPE Detection.py.")

        return None

    try:
        return YOLO(str(MODEL_PATH))
    except Exception as exc:
        st.error(f"YOLO could not load the model: {exc}")
        return None


model = load_model()

if model is None:
    st.stop()

# Sidebar controls
with st.sidebar:
    st.header("Detection Settings")
    conf_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.25, 0.05)
    iou_threshold = st.slider("IoU Threshold", 0.1, 1.0, 0.45, 0.05)
    st.markdown("---")
    st.markdown("**Model Info**")
    st.write(f"Classes: {list(model.names.values())}")
    st.write("Model: YOLOv11n (WorkSafe AI)")

# File uploader
uploaded_file = st.file_uploader(
    "Upload an image (JPG, PNG, JPEG)",
    type=["jpg", "jpeg", "png"],
    help="Drag and drop or click to upload a workplace image"
)

col1, col2 = st.columns(2)

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    # Run inference
    with st.spinner("Running PPE detection..."):
        results = model.predict(
            source=img_array,
            conf=conf_threshold,
            iou=iou_threshold,
            verbose=False
        )

    result = results[0]
    annotated = result.plot()  # BGR numpy array with boxes
    annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    with col2:
        st.subheader("Detection Result")
        st.image(annotated_rgb, use_container_width=True)

    # Summary metrics
    st.markdown("---")
    st.subheader("Detection Summary")

    boxes = result.boxes
    if boxes is not None and len(boxes) > 0:
        class_ids = boxes.cls.cpu().numpy().astype(int)
        confidences = boxes.conf.cpu().numpy()
        names = [model.names[c] for c in class_ids]

        hat_count = names.count("hat")
        vest_count = names.count("vest")
        total = len(names)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total Detections", total)
        with m2:
            st.metric("Hard Hats (hat)", hat_count)
        with m3:
            st.metric("Safety Vests (vest)", vest_count)
        with m4:
            avg_conf = float(np.mean(confidences)) if len(confidences) > 0 else 0
            st.metric("Avg Confidence", f"{avg_conf:.2%}")

        # Detailed table
        st.markdown("#### Detected Objects")
        detection_data = []
        for i, (cls_id, conf) in enumerate(zip(class_ids, confidences)):
            detection_data.append({
                "ID": i + 1,
                "Class": model.names[cls_id],
                "Confidence": f"{conf:.2%}"
            })
        st.dataframe(detection_data, use_container_width=True, hide_index=True)
    else:
        st.warning("No PPE items detected. Try lowering the confidence threshold or use a clearer image.")
else:
    st.info("👆 Upload an image to start PPE detection.")
    st.markdown("""
    **Supported detections:**
    - 🪖 **hat** – Hard hat / safety helmet
    - 🦺 **vest** – High-visibility safety vest
    """)