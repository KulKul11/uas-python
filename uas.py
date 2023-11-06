import streamlit as st
from job import show_job
from fuel import show_fuel
from salaries import show_salaries
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title = "Data Menu",
        menu_icon="list",
        options=["Software Engineers Job Offers", "Fuel Consumption", "Salaries"],
        icons=["cart" ,"fuel-pump" ,"bank"]
    )


if selected == "Software Engineers Job Offers":
    show_job()

elif selected == "Fuel Consumption":
    show_fuel()

elif selected == "Salaries":
    show_salaries()