import streamlit as st
from PIL import Image
# Content in Markdown format with styled and colorful text
st.header("Cooling Systems:",divider='rainbow')
content = """
## <span>🌬️ **Key Factors for Efficient Cooling System Setup**</span>

- Shading of windows
- Urban geometry optimization to ensure proper air circulation
- Facade design for high-rise buildings to minimize direct sun exposure
- Conversion of city rooftops and facades into renewable energy production areas.

### <span>❄️ **Underground District Cooling System**</span>

A central plant cools water and distributes it to various structures (banks, residential towers, shopping malls, schools) to save up to 40% of electricity compared to traditional air conditioners.

### <span> 🪞 **Electrochromic Glass**</span>

Employs nanotechnology by utilizing minor electrical signals to charge the windows, enabling a modification in the radiation properties they reflect. This process effectively aids in regulating the internal temperature of a building.

### <span> 🌍 **Examples of Innovative Cooling Systems in India**</span>

- **AAETI, Rajasthan:** Utilizes a 3-stage cooling system, including indirect and direct evaporative cooling.
- **NIIT University, Rajasthan, and Sabhakhand Building, Gujarat Vidhyapith:** Employ earth air tunnel systems for heat absorption.
- **IIT Gandhinagar, Gujarat, and IIIT Delhi:** Implement district cooling and passive downdraft cooling systems.
"""

# Image paths
image_path1 = Image.open(r"Images/cooling1.png")
image_path2 = Image.open(r"Images/cooling2.png")
image_path3 = Image.open(r"Images/cooling3.png")
image_path4 = Image.open(r"Images/cooling4.png")
# Markdown content
st.markdown(content, unsafe_allow_html=True)

col1,col2=st.columns(2)
with col1:
    st.image(image_path1)
    st.image(image_path2)
with col2:
    st.image(image_path3)
    st.image(image_path4)
