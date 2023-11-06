import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

data2 = pd.read_excel("Fuel Consumption Ratings 2023.xlsx", nrows=834)

vehicle_model = data2['Model'].nunique()
vehicle_class = data2['Vehicle Class'].nunique()
vehicle_fuel = data2['Fuel Type'].nunique()

def show_fuel():
    st.title("Fuel Consumption Data")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Vehicle Model", vehicle_model)
    col2.metric("Class", vehicle_class)
    col3.metric("Fuel Type", vehicle_fuel)

    st.markdown("<br>", unsafe_allow_html=True)

    #chart
    view_chart = st.radio(
            "view data in:",
            ["Bar Chart", "Scatter Chart", "Pie Chart"],
            horizontal=bool(True)
        )
    
    tab1, tab2, tab3, tab4 = st.tabs(["Data Preview" ,"Vehicle Class", "Transmission", "Fuel Type"])

    with tab1:
        
        col_select1, col_select2 = st.columns(2)

        with col_select1:
            selected_class = st.multiselect(
                "Select by Vehicle Class:",
                data2['Vehicle Class'].unique()
            )
        with col_select2:
            selected_trans = st.multiselect(
                "Select by Transmission:",
                data2['Transmission'].unique()
            )

        if selected_class or selected_trans:
            filtered_data = data2[(data2['Vehicle Class'].isin(selected_class)) | (data2['Transmission'].isin(selected_trans))]
            st.write("Selected Data:")
            st.write(filtered_data[['Year', 'Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']])
        else:
            st.write("All Data:")
            st.write(data2[['Year', 'Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']])

    with tab2:

        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data2['Vehicle Class'].value_counts().reset_index()
            bar_chart.columns = ['Vehicle Class', 'Total Vehicle']

            fig = px.bar(bar_chart, x='Vehicle Class', y='Total Vehicle', color='Vehicle Class',
                title=f'Total Vehicle per Vehicle Class',
                labels={'Total Vehicle': 'Total Vehicle', 'Vehicle Class': 'Vehicle Class'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data2['Vehicle Class'].value_counts().reset_index()
            bar_chart.columns = ['Vehicle Class', 'Total Vehicle']
            scatter_chart = px.scatter(bar_chart, x='Vehicle Class', y='Total Vehicle', color='Vehicle Class',
                                    title='Total Vehicle per Vehicle Class',
                                    labels={'Total Vehicle': 'Total Vehicle', 'Vehicle Class': 'Vehicle Class'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data2['Vehicle Class'].value_counts().reset_index()
            bar_chart.columns = ['Vehicle Class', 'Total Vehicle']
            pie_chart = px.pie(bar_chart, values='Total Vehicle', names='Vehicle Class',
                            title='Percentage of Total Vehicle Vehicle Class',
                            labels={'Total Vehicle': 'Total Vehicle', 'Vehicle Class': 'Vehicle Class'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)
    with tab3:
        
        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data2['Transmission'].value_counts().reset_index()
            bar_chart.columns = ['Transmission', 'Total Vehicle']

            fig = px.bar(bar_chart, x='Transmission', y='Total Vehicle', color='Transmission',
                title=f'Total Vehicle per Transmission',
                labels={'Total Vehicle': 'Total Vehicle', 'Transmission': 'Transmission'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data2['Transmission'].value_counts().reset_index()
            bar_chart.columns = ['Transmission', 'Total Vehicle']
            scatter_chart = px.scatter(bar_chart, x='Transmission', y='Total Vehicle', color='Transmission',
                                    title='Total Vehicle per Transmission',
                                    labels={'Total Vehicle': 'Total Vehicle', 'Transmission': 'Transmission'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data2['Transmission'].value_counts().reset_index()
            bar_chart.columns = ['Transmission', 'Total Vehicle']
            pie_chart = px.pie(bar_chart, values='Total Vehicle', names='Transmission',
                            title='Percentage of Total Vehicle Transmission',
                            labels={'Total Vehicle': 'Total Vehicle', 'Transmission': 'Transmission'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)
    with tab4:
        
        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data2['Fuel Type'].value_counts().reset_index()
            bar_chart.columns = ['Fuel Type', 'Total Vehicle']

            fig = px.bar(bar_chart, x='Fuel Type', y='Total Vehicle', color='Fuel Type',
                title=f'Total Vehicle per Fuel Type',
                labels={'Total Vehicle': 'Total Vehicle', 'Fuel Type': 'Fuel Type'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data2['Fuel Type'].value_counts().reset_index()
            bar_chart.columns = ['Fuel Type', 'Total Vehicle']
            scatter_chart = px.scatter(bar_chart, x='Fuel Type', y='Total Vehicle', color='Fuel Type',
                                    title='Total Vehicle per Fuel Type',
                                    labels={'Total Vehicle': 'Total Vehicle', 'Fuel Type': 'Fuel Type'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data2['Fuel Type'].value_counts().reset_index()
            bar_chart.columns = ['Fuel Type', 'Total Vehicle']
            pie_chart = px.pie(bar_chart, values='Total Vehicle', names='Fuel Type',
                            title='Percentage of Total Vehicle Fuel Type',
                            labels={'Total Vehicle': 'Total Vehicle', 'Fuel Type': 'Fuel Type'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)