import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

data3 = pd.read_excel("salaries.xlsx")

exp_level = data3['experience_level'].nunique()
job_title = data3['job_title'].nunique()
max_sal = data3['salary_in_usd'].max()
min_sal = data3['salary_in_usd'].min()
emp_residence = data3['employee_residence'].nunique()
comp_loc = data3['company_location'].nunique()

def show_salaries():
    st.title("Fuel Consumption Data")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Experience Level Types", exp_level)
    col2.metric("Job Title", job_title)
    col3.metric("total employee residence", emp_residence)

    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    col4.metric("Highest Salary(USD)", max_sal)
    col5.metric("Lowest Salary(USD)", min_sal)
    col6.metric("Total Company Location", comp_loc)

    #chart
    view_chart = st.radio(
            "view data in:",
            ["Bar Chart", "Scatter Chart", "Pie Chart"],
            horizontal=bool(True)
        )
    
    tab1, tab2, tab3 = st.tabs(["Data Preview" ,"Company Size", "Experience Level"])

    with tab1:
        
        col_select1, col_select2 = st.columns(2)

        with col_select1:
            selected_exp = st.multiselect(
                "Select by Experience Level:",
                data3['experience_level'].unique()
            )
        with col_select2:
            selected_comp = st.multiselect(
                "Select by Company Location:",
                data3['company_location'].unique()
            )

        if selected_exp or selected_comp:
            filtered_data = data3[(data3['experience_level'].isin(selected_exp)) | (data3['company_location'].isin(selected_comp))]
            st.write("Selected Data:")
            st.write(filtered_data)
        else:
            st.write("All Data:")
            st.write(data3)

    with tab2:

        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data3['company_size'].value_counts().reset_index()
            bar_chart.columns = ['company_size', 'Total Company']

            fig = px.bar(bar_chart, x='company_size', y='Total Company', color='company_size',
                title=f'Total Company per company_size',
                labels={'Total Company': 'Total Company', 'company_size': 'company_size'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data3['company_size'].value_counts().reset_index()
            bar_chart.columns = ['company_size', 'Total Company']
            scatter_chart = px.scatter(bar_chart, x='company_size', y='Total Company', color='company_size',
                                    title='Total Company per company_size',
                                    labels={'Total Company': 'Total Company', 'company_size': 'company_size'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data3['company_size'].value_counts().reset_index()
            bar_chart.columns = ['company_size', 'Total Company']
            pie_chart = px.pie(bar_chart, values='Total Company', names='company_size',
                            title='Percentage of Total Company company_size',
                            labels={'Total Company': 'Total Company', 'company_size': 'company_size'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)

    with tab3:

        if view_chart == "Bar Chart":
            #bar chart
            bar_chart = data3['experience_level'].value_counts().reset_index()
            bar_chart.columns = ['experience_level', 'Total Company']

            fig = px.bar(bar_chart, x='experience_level', y='Total Company', color='experience_level',
                title=f'Total Company per experience_level',
                labels={'Total Company': 'Total Company', 'experience_level': 'experience_level'})

            st.plotly_chart(fig)

            st.markdown("<br>", unsafe_allow_html=True)

        elif view_chart == "Scatter Chart":
            # Scatter chart
            bar_chart = data3['experience_level'].value_counts().reset_index()
            bar_chart.columns = ['experience_level', 'Total Company']
            scatter_chart = px.scatter(bar_chart, x='experience_level', y='Total Company', color='experience_level',
                                    title='Total Company per experience_level',
                                    labels={'Total Company': 'Total Company', 'experience_level': 'experience_level'})

            # Menampilkan scatter chart pada Streamlit
            st.plotly_chart(scatter_chart)
        
        elif view_chart == "Pie Chart":
            # Pie chart
            bar_chart = data3['experience_level'].value_counts().reset_index()
            bar_chart.columns = ['experience_level', 'Total Company']
            pie_chart = px.pie(bar_chart, values='Total Company', names='experience_level',
                            title='Percentage of Total Company experience_level',
                            labels={'Total Company': 'Total Company', 'experience_level': 'experience_level'})

            # Menampilkan pie chart pada Streamlit
            st.plotly_chart(pie_chart)
