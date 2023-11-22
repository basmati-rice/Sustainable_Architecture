import streamlit as st
from PIL import Image
# Content in Markdown format
st.header("Building Materials:",divider='rainbow')
content = """
## <span>🌱 **Sustainable Building Material**</span>

### <span>🍄 **Mycelium-Based Building Material**</span>

- Mycelium-based building material made from agricultural products.
- Non-toxic, low-energy production.
- Biodegradable mycelium bricks.
- Stronger and better insulation than concrete.
- Regenerates over time.

### <span>🔄 **Plastic Waste Solution**</span>

- Plastic and sand combined at high temperatures.
- Melted plastic binds the mixture.
- Compressed into bricks stronger than concrete and lighter.

### <span>🌳 **Cork Used for Blocks and Roof Tiles**</span>

- Offers durability and easy assembly.
- Versatile use in homes, hotels, studios, and exhibitions globally.
- Outstanding insulation for temperature and sound.
- Naturally moisture-resistant.

### <span>♻️ **Recycling Process**</span>

- Organic fibers
- Use in green energy and paper production.
- Plastic
- Into items like plastic cladding, deckling, and roof tiles.

### <span>🌍 **Carbon Capture Technique**</span>

- Captures carbon at the source before it enters the atmosphere.

### <span>🌊 **E-Concrete Advantages**</span>

- Boosts marine ecosystems.
- Minimizes environmental harm from sea wall, port, and marina structures.
- Traditional concrete disrupts marine ecosystems chemically.
- Includes additives to prevent chemical leaks into the water.
"""

# Image path
myc = Image.open(r"Images/mycelium.jpg")
pw = Image.open(r"Images/plastic_bottles.jpg")
cork= Image.open(r"Images/cork.jpg")
of= Image.open(r"Images/fabric.jpg")
cct= Image.open(r"Images/carbon_capture.png")
ec= Image.open(r"Images/concrete.jpg")
# Create columns for the layout
col1, col2 = st.columns(2)  # Adjust the ratio as needed

# Add the Markdown content to the left column
with col1:
    st.markdown(content, unsafe_allow_html=True)

# Add the image to the right column
with col2:
    st.image(myc, caption="Mycelium-Based Building Material",width=350)
    st.image(pw, caption="Plastic Waste",width=350)
    st.image(cork, caption="Cork Used for Blocks and Roof Tiles",width=350)
    st.image(of, caption="Organic fibers",width=350)
    st.image(ec, caption="E-Concrete ",width=350)
st.image(cct, caption="Carbon Capture Technique")
