#page path "C:\Users\HP\Desktop\Sus-Website\Main Page.py"
#3d path "C:\Users\HP\Desktop\Sus-Website\models\new_solar.stl"
#img path "C:\Users\HP\Desktop\Sus-Website\images\EVS group project.png"

import streamlit as st
import pyvista as pv
from stpyvista import stpyvista
from PIL import Image
st.set_page_config(
    page_title="Sustainable architecture",
    page_icon="👋",
)

st.sidebar.success("Select a page from above")

#MAIN PAGE
header_img=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\EVS group project.png") 
st.image(header_img)
st.header("Why sustainable architecture?",divider='rainbow')
st.header("The building sector:")
st.write('''The building industry accounts for about 40% of total energy consumption and greenhouse gas emission.
The 11th sustainable development goal is to ‘Make cities and human settlements inclusive, safe, resilient and sustainable‘.
The 2023 Global Sustainable Development Report finds that incremental and fragmented change is insufficient to achieve the Sustainable Development Goals (SDGs) in the remaining seven years.
More emphasis must be placed on the goal of sustainable architecture.

The International Energy Agency (IEA) tracks the progress of various sectors with regard to sustainability goals.
The building sector is graded as follows:''')

co2_graph=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\co2_emmissions.png") 
st.image(co2_graph)

col1,col2,col3=st.columns(3)
col1.header('Building Envelope:')
col1.write("The building's outer shell acts as a barrier between inside and outside, crucial for energy efficiency. Weather and heat protection are pivotal factors, making it a key concern for policymakers.The IEA grades this area as ‘not on track’.")
col2.header('Heating:')
col2.write("This covers how the building is actively heated, from wood-burning fireplaces to solar-powered electrical heaters. The IEA grades this area as ‘not on track’.")
col3.header('Heat Pumps:')
col3.write("Heat pumps are vital for sustainable heating with a focus on geothermal systems, mainly in new constructions, but costly for retrofits. The IEA grades this area as ‘more effort needed’.")

cola,colb,colc=st.columns(3)
cola.header('Cooling:')
cola.write("Cooling buildings is crucial due to global warming. We need innovative designs and adaptations for buildings to remain usable in this century. The IEA grades the area as ‘more effort needed’.")
colb.header('Lighting:')
colb.write("Lighting systems used in buildings have had the most impressive innovation, energy efficiency, adoption, and impact. The IEA grades this area as ‘on track’.")
colc.header('Appliances and Equipment:')
colc.write("This area is where replacement and adaptation are likely to be a far bigger issue than innovation and adoption in new builds. The IEA grades this area as ‘more work needed’.")
st.write("Overall, The IEA has the buildings sector set at ‘not on track’. This clearly implies that policymakers around the world have to act urgently in terms of regulations on new and existing stock, to even remotely meet the net neutral, mid-century targets. Banks should consider this a major short- and mid-term risk to collateral value and their balance sheets’ credit profiles.")

heat_map=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\urban_heat_island.png") 
           
           
st.header("Urban heat island:")
st.write("""Materials such as asphalt, concrete, and shingled roofs absorb greater heat from the sun compared to trees, a phenomenon known as the Urban Heat Island effect.
Heat waves are a major hazard, with a higher mortality rate than any other extreme weather condition. Consequently, urban planning must focus on addressing this critical issue.
According to NITI Aayog's India Energy Security Scenario of 2017, 65% of building energy consumption is linked to the needs of space cooling and heating.""")
st.image(heat_map)

st.video(r"C:\Users\HP\Desktop\Sus-Website\images\sus_bldg.mp4")
bldg=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\sus_bild.jpeg")
sus_bldg="""
### <span> A sustainable building can have: </span>
- Good insulation  
- Vegetation and terrace farming  
- Proper shading  
- Carbon zero building material  
- Natural cooling  
- Proper ventilation"""
st.image(bldg)
st.markdown(sus_bldg, unsafe_allow_html=True)


