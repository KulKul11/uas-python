import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

data1 = pd.read_excel("Job Offers for Software Engineers in Poland.xlsx")

#ringkasan data
total_job = len(data1)
total_comp = data1['company'].nunique()
total_tech = data1['technology'].nunique()
total_loc = data1['location'].nunique()
min_salary = data1['salary employment min'].min()
max_salary = data1['salary employment max'].max()
avg_senior = data1['seniority'].max()
def show_job():
#membuat kolom atas
    st.title("Software Engineers Job Offers")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Job Offers", total_job)
    col2.metric("Minimum Salary", min_salary)
    col3.metric("Maximum Salary", max_salary)
    st.markdown("<br>", unsafe_allow_html=True)

    #membuat kolom bawah
    col4, col5, col6, col7 = st.columns(4)
    col4.metric("Total Location", total_loc)
    col5.metric("Total Company", total_comp)
    col6.metric("Total Technology used", total_tech)
    col7.metric("Average Seniority", avg_senior)

    st.markdown("<br>", unsafe_allow_html=True)


    #chart
    view_chart = st.radio(
            "view data in:",
            ["Bar Chart", "Scatter Chart", "Pie Chart"],
            horizontal=bool(True)
        )
    tab1, tab2, tab3, tab4 = st.tabs(["Data Preview" ,"Total Job", "Technology", "seniority"])

    with tab1:
        
        col_select1, col_select2 = st.columns(2)

        with col_select1:
            selected_companies = st.multiselect(
                "Select by Companies:",
                data1['company'].unique()
            )
        with col_select2:
            selected_location = st.multiselect(
                "Select by Location:",
                data1['location'].unique()
            )

        if selected_companies or selected_location:
            filtered_data = data1[(data1['company'].isin(selected_companies)) | (data1['location'].isin(selected_location))]
            st.write("Selected Data:")
            st.write(filtered_data)
        else:
            st.write("All Data:")
            st.write(data1)

    with tab2:

        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data1['location'].value_counts().reset_index()
            bar_chart.columns = ['Location', 'Job Count']

            fig = px.bar(bar_chart, x='Location', y='Job Count', color='Location',
                title=f'Total Job Offer per Location',
                labels={'Job Count': 'Jumlah Job Offer', 'Location': 'Location'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data1['location'].value_counts().reset_index()
            bar_chart.columns = ['Location', 'Job Count']
            scatter_chart = px.scatter(bar_chart, x='Location', y='Job Count', color='Location',
                                    title='Total Job Offer per Location',
                                    labels={'Job Count': 'Jumlah Job Offer', 'Location': 'Location'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data1['location'].value_counts().reset_index()
            bar_chart.columns = ['Location', 'Job Count']
            pie_chart = px.pie(bar_chart, values='Job Count', names='Location',
                            title='Percentage of Job Offers per Location',
                            labels={'Job Count': 'Total Job Offer', 'Location': 'Location'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)

    with tab3:

        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data1['technology'].value_counts().reset_index()
            bar_chart.columns = ['technology', 'Total Technology used']

            fig = px.bar(bar_chart, x='technology', y='Total Technology used', color='technology',
                title=f'Total Technology Used',
                labels={'Total Technology used': 'Total Technology used', 'technology': 'technology'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data1['technology'].value_counts().reset_index()
            bar_chart.columns = ['technology', 'Total Technology used']
            scatter_chart = px.scatter(bar_chart, x='technology', y='Total Technology used', color='technology',
                                    title='Total Technology used',
                                    labels={'Total Technology used': 'Total Technology used', 'technology': 'technology'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data1['technology'].value_counts().reset_index()
            bar_chart.columns = ['technology', 'Total Technology used']
            pie_chart = px.pie(bar_chart, values='Total Technology used', names='technology',
                            title='Total Percentage of Technology used',
                            labels={'Total Technology used': 'Total Technology used', 'technology': 'technology'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)

    with tab4:

        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data1['seniority'].value_counts().reset_index()
            bar_chart.columns = ['seniority', 'Total Seniority']

            fig = px.bar(bar_chart, x='seniority', y='Total Seniority', color='seniority',
                title=f'Total Seniority',
                labels={'Total Seniority': 'Total Seniority', 'seniority': 'seniority'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data1['seniority'].value_counts().reset_index()
            bar_chart.columns = ['seniority', 'Total Seniority']
            scatter_chart = px.scatter(bar_chart, x='seniority', y='Total Seniority', color='seniority',
                                    title='Total Seniority',
                                    labels={'Total Seniority': 'Total Seniority', 'seniority': 'seniority'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data1['seniority'].value_counts().reset_index()
            bar_chart.columns = ['seniority', 'Total Seniority']
            pie_chart = px.pie(bar_chart, values='Total Seniority', names='seniority',
                            title='Total Percentage of Seniority',
                            labels={'Total Seniority': 'Total Seniority', 'seniority': 'seniority'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)

    