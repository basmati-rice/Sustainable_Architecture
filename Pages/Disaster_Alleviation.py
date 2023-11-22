import streamlit as st
import pyvista as pv
from stpyvista import stpyvista
from PIL import Image

plotter_panel = pv.Plotter(window_size=[400, 400])
mesh_panel = pv.read(r"C:\Users\HP\Desktop\Sus-Website\models\earthwake.stl")  
mesh_panel.plot()
plotter_panel.add_mesh(mesh_panel, show_edges=True, color=True, line_width=1)
plotter_panel.camera_position= 'xy'
plotter_panel.background_color = "white"

base=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\base.png")
st.header("Disaster Alleviation:", divider='rainbow')
st.header("Seismic Systems:")
stpyvista( plotter_panel,panel_kwargs=dict(orientation_widget=True, interactive_orientation_widget=True))
st.image(base)
st.write('When flexible foundation moves, isolators absorb the seismic movement and prevent them from being transmitted to the entire building. They support vertical load, accept rotational deformational and also allow horizontal displacement, translating seismic activity into shear force onto its own body keeping the building stable.')
text1='''These buildings are integrated with:
- Computer-controlled weights on the roof to reduce movement
- Automated glass shutters to prevent falling glass
- Birdcage steel frames that prevent building from swaying horizontally beyond dangerous limit
- Cross-bracing and shear walls kept in mind when building foundations
- Foundations sunken in bedrock to avoid unstable clay
- Rubber shock-absorbers to absorb earth tremors, fitted with piezometers to generate additional energy using seismic forces
- Fire-resistant building material
- Outer panels attached flexibly to steel frames
- Large pendulum fitted with a hydraulic system to detect earthquakes and also generate modest amount of energy as backups'''


st.markdown(text1, unsafe_allow_html=True)
st.header("Flood Systems:")
amph=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\amphi_house.jpg")  
st.write("""Amphibious Housing:
\nThese structures have currently been optimized for building upto 3 storeys and have been qualified for flood 3 zones. Designed to float on the water's surface during floods, amphibious houses ensuring the safety of residents and minimizing damage to property. Equipped with buoyant foundations or floating platforms, these houses rise with the water level, reducing the risk of inundation and structural damage. Their adaptability to rising water levels makes them an effective and resilient approach in flood-prone regions, offering a sustainable and practical response to the increasing challenges posed by climate change and rising sea levels.""")
st.image(amph)

h1,h2,h3,h4=st.columns(4)
h1.subheader('Heavy rain flooding:')
h1.write("Runoff Reduction \n Capture precipitation on your property by installing rain barrels and increase previous (absorbent) surfaces by building rain gardens and french ditches. Move home heating and cooling equipment to higher floors to prevent flood water exposure.")
h2.subheader("Continual minor flooding:")
h2.write("Elevate home\nRetrofitting a home by elevating it above the height of most flood levels requires a large financial investment but can lead to a significant reduction in flood insurance premiums.")
h3.subheader("Single Area flooding:")
h3.write("Sump pump\nInstall a water removal system (sump pump) in any area that water collects to be moved (pumped) off of your property. Additional waterproofing around windows or french drains and gutter extensions may also help in moving the water to another area and keeping it out of your home.")
h4.subheader("CENTAUR:")
h4.write("an intelligent autonomous system for local urban flood risk reduction, which is installed in combined sewer systems in flood-prone areas. Combined sewer systems not only collect waste, but are designed to drain excess rainwater. This real-time control of sewer flow has many benefits. Not only does it reduce flood risk, but it can prevent sewage overflow, make the flow of our sewer systems to treatment works more efficient")

st.header("How can disaster solutions be used to a more sustainable cause?")
st.markdown("Integration with electromechanical transducers such as piezoelectric and electrostatic generators in superstructures i.e. earthquake and flood solutions into buildings but also into substructures such as the creation of composite materials with cement mortar, and structural health monitoring systems.  \n  \n Also ensuring the durability of superstructures becomes paramount as sustainability also implies longevity and resilience of structures without causing pollution or excess waste during disasters.  \n  \n Advancements in piezoelectric materials, featuring improved electromechanical properties, have led to the creation of diverse types such as single crystals, lead-free variants, high-temperature options, foams, and nanocomposites. Moreover, the concept of harnessing energy from various sources concurrently—utilizing hybrid generators combining piezoelectric, electromagnetic, triboelectric, and pyroelectric mechanisms—has been proposed in recent literature. ")



