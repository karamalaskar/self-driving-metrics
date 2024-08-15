import streamlit as st
from database_manager import DatabaseManager
from data_processor import DataProcessor
from metric_calculator import MetricCalculator
from visualizer import Visualizer
from sample_data_generator import SampleDataGenerator

class App:
    def __init__(self):
        # Initialize components
        self.db_manager = DatabaseManager('self_driving_tests.db')
        self.db_manager.create_table()

      # Check if the database is empty before inserting sample data
        if not self.db_manager.has_data():
            self.sample_data = SampleDataGenerator.generate_sample_data(100)
            self.db_manager.insert_data(self.sample_data)

        self.data = self.db_manager.load_data()
        self.data_processor = DataProcessor(self.data)
        self.metric_calculator = MetricCalculator(self.data)
        self.visualizer = Visualizer(self.data)
        
        # Sidebar configuration
        st.sidebar.title("Self Driving Vehicle Test Metrics Dashboard")
        st.sidebar.markdown("Demo developed by [Karam Al-Askar](https://github.com/karamalaskar)")

        self.app_mode = self.get_app_mode()

    def get_app_mode(self):
        home = st.sidebar.button("Home")
        documentation = st.sidebar.button("Documentation")

        if documentation:
            return "Documentation"
        else:
            return "Home"

    def run(self):
        if self.app_mode == "Home":
            self.display_home()
        elif self.app_mode == "Documentation":
            self.display_documentation()

    def display_home(self):
        # Sidebar for filters
        st.sidebar.header("Filters")
        date_range = st.sidebar.date_input("Select date range", 
                                            [self.data['test_date'].min(), self.data['test_date'].max()])

        vehicle_options = ["All"] + sorted(self.data['vehicle_id'].unique())
        vehicle_id = st.sidebar.selectbox("Select vehicle ID", vehicle_options)

        result_options = ["All", "pass", "partial pass", "warning", "fail"]
        result = st.sidebar.selectbox("Select result", result_options)

        # Filter data based on sidebar inputs
        filtered_data = self.data_processor.filter_data(date_range, vehicle_id, result)

        # Display filtered data
        st.subheader("Filtered Test Data")
        st.write(filtered_data)

        # Display metrics
        st.subheader("Performance Metrics")
        metrics = self.metric_calculator.calculate_metrics()
        st.write(f"Average Speed: {metrics['average_speed']:.2f} km/h")
        st.write(f"Average Following Distance: {metrics['average_distance']:.2f} s")
        st.write(f"Average Lane-Keeping Score: {metrics['average_lane_keeping_accuracy']:.2f} %")
        st.write(f"Average Distance Travelled (Per Day): {metrics['average_distance_travelled']:.2f} km")
        st.write(f"Most Common Result: {metrics['common_result']}")

        # Visualizations
        st.subheader("Test Result Distribution")
        bar_or_pie = st.radio("Select a chart type", ('Bar Chart', 'Pie Chart'))
        self.visualizer.plot_result_distribution(bar_or_pie)

        st.subheader("Metrics Over Time")
        metric = st.radio("Select a metric to plot", ('following_distance', 'lane_keeping_accuracy', 'human_inputs'))
        self.visualizer.plot_metric_over_time(metric)

        st.subheader("Correlation between Metrics")
        col1, col2 = st.columns(2)
        with col1:
            option1 = st.radio("Select a metric to plot (X)", 
                               ('average_speed', 'following_distance', 'lane_keeping_accuracy', 'human_inputs', 'distance_travelled'), 
                               key='1')
        with col2:
            option2 = st.radio("Select a metric to plot (Y)", 
                               ('average_speed', 'following_distance', 'lane_keeping_accuracy', 'human_inputs', 'distance_travelled'), 
                               key='2')
        self.visualizer.plot_correlation(option1, option2)

    def display_documentation(self):
        # Documentation page
        st.title("Documentation")
        
        with open("documentation.md", "r") as file:
          documentation_content = file.read()
          st.markdown(documentation_content)

# Run the application
if __name__ == "__main__":
    dashboard = App()
    dashboard.run()