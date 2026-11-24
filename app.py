import streamlit as st

# 1. Configure page
st.set_page_config(page_title="WorkSafe AI: Intelligent PPE Detection for :blue[Safer Workplaces]", layout="wide")

# 2. Add the global logo (appears upper left)
st.logo("logo.png")

# 3. Define your pages
home_page = st.Page("home.py", title="Home", icon="🏠")
team_page=st.Page('Team.py',title='Team',icon='👥')
abtproject_page=st.Page('abtproject.py',title='About Project',icon="🛠️")
features_page=st.Page('Features.py',title='Features',icon='🌟')
ppedetection_page=st.Page('PPE Detection.py',title='PPE Detection', icon='🦺')
futurescope_page=st.Page('FutureScope.py',title='Future Scope',icon='🔭')
# 4. Initialize navigation at the TOP
pg = st.navigation([home_page,abtproject_page,features_page,ppedetection_page,team_page,futurescope_page], position="top")

# 5. Execute the active page
pg.run()


import base64
import streamlit as st

# Function to convert local image to base64
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Replace with your actual local image file path
img_path = 'background1.png' 
img_base64 = get_base64_of_bin_file(img_path)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)









