import streamlit as st
from plotly import express as px

class Visualizer:
    def __init__(self, data):
        self.data = data
        
    def plot_result_distribution(self, chart_type='Bar Chart'):
        if chart_type == 'Pie Chart':
            fig = px.pie(self.data, names='result')
            st.plotly_chart(fig)
        else:
            st.bar_chart(self.data['result'].value_counts())

    def plot_metric_over_time(self, metric):

        self.data.set_index('test_date', inplace=True)
        st.line_chart(data=self.data[metric])

    def plot_correlation(self, option1, option2):
        st.scatter_chart(data=self.data, x=option1, y=option2, color='result')