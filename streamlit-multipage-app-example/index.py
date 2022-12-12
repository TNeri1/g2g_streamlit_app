import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly as plt
import plotly.express as px

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu

# Read Data
df = pd.read_csv('data_2.csv')
df_1 = pd.read_csv('g2g_distance_to_roads_sales_relationship.csv')

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
                options=["Dataset","Fuel Sales", "Traffic", "Population"],  # required
                icons=["data","house", "stoplights", "people"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Dataset":
    st.title(f"{selected}")
    st.write(df)
    st.write("""
            Data Dictionary:
            * tractcode
                * 
            * State
            * avg_tract_sales_volume_assets
            * POPULATION_2020
            * POP20_SQMI
            * SQMI
            * 2022_Median_Household_Income
            * lat
            * long
            * total_population
            * unemployed
            * percent_unemployed
            * med_income
            * med_age
            * avg_dist_traveled_per_person_from_tract_to_business_in_miles
            * count_gas_stations
            * avg_gas_station_visits_on_weekday
            * avg_gas_station_visits_on_weekend
            * land_m
             """)

if selected == "Fuel Sales":
    st.title(f"{selected}")
    
    st.write("This is a feature we designed calculating the average distance a person travelled in a tract to different points of interest in a tract estimating how much they drive")
    st.image('images/Distance and Fuel Sales.png')

    st.write('The 2022 Median Income within each tract to how many fuel sales/assets occurred in that tract')
    st.image('images/Income and Fuel Sales.png')

    st.title("Data Axle")
    st.write('Arizona sales volume and count of gas stations')
    st.image('images/Arizona sales volume and count of gas stations.png')

    st.write('Idaho sales volume and count of gas stations')
    st.image('images/Idaho sales volume and count of gas stations.png')

    st.write('Arizona Sales Volume by Tract')
    st.image('images/Arizona Sales Volume by Tract.png')

    st.write('Idaho Sales volume and Assets by Tract')
    st.image('images/Idaho sales volume.png')




if selected == "Traffic":
    st.title(f"{selected}")

    # Relationship between g2g store distance from road and sales
    st.plotly_chart(fig, use_container_width= True)


    st.title("Data Axle")
    st.write('Arizona Total Highway Miles by Tract')
    st.image('images/Arizona_Total_Highway_Miles_tract.png')

    st.write('Idaho Total Highway Miles by Tract')
    st.image('images/Idaho_Highway_miles_tract.png')


if selected == "Population":
    st.title(f"{selected}")

    st.title("Data Axle")
    st.write('Arizona sales volume and Median Household Income')
    st.image('images/Arizona sales volume and MHHI.png')

    st.write('Idaho sales volume and Median Household Income')
    st.image('images/Idaho sales volume and MHHI.png')

    st.write('Arizona sales volume and miles of highway')
    st.image('images/Arizona sales volume and miles of highway.png')

    st.write('Idaho sales volume and miles of highway')
    st.image('images/Idaho sales volume and highway miles and points.png')




