import streamlit as st
from PIL import Image

st.header("Tools aiding in sustainable building design:",divider='rainbow')

text1="""### <span> **Green Building Studio, Energy Plus, and IES Energy Modeling:** </span>
- Focus on increasing sustainability.  
- Perform climate analysis and HVAC (Heating, Ventilation, and Air Conditioning) simulations. 
- Helps in determining the best materials to use and the ideal building orientation for maximum energy efficiency.  
- Allow you to predict a building's performance throughout the year before it's even constructed. """

tools=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\companies.png")
st.markdown(text1, unsafe_allow_html=True)
st.image(tools)

graviky=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\gravikylabs.jpg")

text2="""### <span> **Graviky Labs:** </span>
- Invents an ingenious tailpipe filter. 
- Captures pollutants.  
- Transforms pollutants into safe, high-quality art inks.  
- Potential for incorporating these filters on building roofs and street lamps.  """
st.markdown(text2,unsafe_allow_html=True)
st.image(graviky)

text3="""### <span> **Blueren, Singapore:**  </span>
- Upcycles waste plastic.  \n
- Converts it into eco-friendly carbon nanotubes.  \n
- Strengthens concrete.  \n
- Reduces current use by 30 percent.  \n"""
st.markdown(text3,unsafe_allow_html=True)


rec_eye=Image.open(r"C:\Users\HP\Desktop\Sus-Website\images\recycleeye.png")
text4="""### <span> **Recycle eye:**  </span>
- AI-driven system aimed at enhancing the value of recycling.  
- Utilizes AI for plastic waste sorting.  
- Incorporates artificial intelligence and a robotic arm.  
- Accurately identifies recyclable items within a mix of waste materials.  
- Effectively separates non-recyclables from recyclable items.  """
st.markdown(text4,unsafe_allow_html=True)
st.image(rec_eye)


