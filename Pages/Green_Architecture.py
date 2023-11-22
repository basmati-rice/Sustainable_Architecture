import streamlit as st
from PIL import Image
# Content in Markdown format with styled and colorful text
st.header("Green Architecture:",divider='rainbow')
content = """
## <span>🌿 **Vertical Farming**</span>
- Grow multiple crops 
- Utilizing space
- Decreases the land requirement
- Provides a stress relief environment for residents
- Meets food requirements during natural disasters.

### <span>🏢 **Offices of Pasona**</span>

The future has already arrived. The Tokyo-based recruitment agency has dedicated 20% of their 215,000 square foot office to growing fresh vegetables, making it the largest urban farm in Japan.

### <span> 🌳 **Vertical Forest Skyscrapers**</span>

Employs nanotechnology by utilizing minor electrical signals to charge the windows, enabling a modification in the radiation properties they reflect. This process effectively aids in regulating the internal temperature of a building.

### <span>🌸 **The Blossom Tower**</span>
Tree tower - Archi-nature co-existing, Tokyo, Japan byArchitect Moshe Katz.
"""

# Image paths
image_path1 =Image.open(r"Images/eden-green-vertical-farm-facility.jpg")
image_path2 = Image.open(r"Images/pasona.jpg")
image_path3 = Image.open(r"Images/blossom.jpg")
bc=Image.open(r"Images/bioclamatic_skin.jpg")
fs=Image.open(r"Images/forest_skyscraper.jpg")
# Create columns for the layout
col1, col2 = st.columns(2)  # Adjust the ratio as needed

# Add the Markdown content to the left column
with col1:
    st.markdown(content, unsafe_allow_html=True)

# Add the images to the right column with captions
with col2:
    st.image(image_path1, caption="Vertical Farming")
    st.image(image_path2, caption="Office of Pasona")
    st.image(image_path3, caption="Blossom Tower",width=200)
cola,colb=st.columns(2)
cola.image(bc,caption="Bioclimatic Skin")
colb.image(fs,caption="Forest Skyscraper")
    
