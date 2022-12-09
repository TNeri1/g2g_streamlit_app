import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly as plt
import plotly.express as px

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu

# Read Data
df = pd.read_csv('streamlit-multipage-app-example\data_1.csv')
df_1 = pd.read_csv('streamlit-multipage-app-example\g2g_distance_to_roads_sales_relationship.csv')

# Create Plots
fig = px.scatter_mapbox(df_1, lat="Lat", lon="Long", size = "NEAR_DIST_road", color = "avg_tract_fuel_sales", color_continuous_scale= [(0, "red"), (.5, "yellow"), (1, "green")], range_color=[0,700000], zoom=6, height=400)
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Streamlit Menu
EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Traffic", "Population"],  # required
                icons=["house", "stoplights", "people"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"{selected}")
    st.write(df)
if selected == "Traffic":
    st.title(f"{selected}")

    # Relationship between g2g store distance from road and sales
    
    st.plotly_chart(fig, use_container_width= True)
if selected == "Population":
    st.title(f"{selected}")