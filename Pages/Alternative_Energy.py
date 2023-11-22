import streamlit as st
import pyvista as pv
from stpyvista import stpyvista
from PIL import Image
pv.OFF_SCREEN = True
plotter_panel = pv.Plotter(window_size=[400, 400])
mesh_panel = pv.read('Models/new_solar.stl') 
mesh_panel.plot()
plotter_panel.add_mesh(mesh_panel, show_edges=True, color=True, line_width=1)
plotter_panel.camera_position= 'xy'
plotter_panel.background_color = "white"

#MAIN PAGE
st.header("Energy Alternatives:",divider='rainbow')
st.header("Solar Energy:")
stpyvista( plotter_panel,panel_kwargs=dict(orientation_widget=True, interactive_orientation_widget=True))
st.write('''Solar energy is increasing in popularity not only implementation, but recycling as well.
Excess electricity produced by solar panels on buildings can be redirected to the main energy grid.
A car park roof with solar panels provides shelter for vehicles while generating electricity from sunlight, promoting sustainability.''')

rot_panel=Image.open("Images/rotpan.jpg")
solaris=Image.open("Images/solaris.jpg")

col1,col2=st.columns(2)
col1.header('Solaris Float:')
col1.image(solaris)
col2.header('Rotating Solar Panels:')
col2.image(rot_panel)

st.header("Algae Energy System:")
algae=Image.open("Images/algae.jpg")
col1a,col2a=st.columns(2)
texta="""- Utilizes photosynthesis to convert the sun's energy into fuel.
- Algae rapidly grows within glass panels.
- Extracted and processed in a bio-converter to turn algae into biomass.
Potential to power cars with this biomass.

Main Purpose:
- Generate electricity and heat for building residents.
- Capable of producing excess energy to supply electricity to nearby buildings."""
col1a.markdown(texta,unsafe_allow_html=True)
col2a.image(algae)
              


