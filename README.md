### Overview
This demo is designed to generate sample data from self driving vehicles for analysis and visualization. It provides tools for filtering data, calculating performance metrics, and creating interactive visualizations to assess vehicle performance.


### How to Run
- **On the web**
  - [https://self-driving-metrics.streamlit.app](https://self-driving-metrics.streamlit.app)
- **Locally**:
  - Clone this repository:
    ```bash
    git clone https://github.com/karamalaskar/self-driving-metrics/
    ```
  - Navigate into the project directory:
    ```bash
    cd self-driving-metrics
    ```
  - Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
  - Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
  - Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

### Features
- **Data Filtering**: 
    - Filter the test data based on date range, vehicle ID, and test result to focus on specific subsets of data.
- **Performance Metrics**: 
    - View and analyze key performance metrics, including average speed, following distance, lane-keeping accuracy, and distance traveled.
- **Visualizations**: 
    - Create various charts, such as bar charts, pie charts, and line charts, to visualize the distribution of test results, trends over time, and correlations between metrics.

### How to Use
1. **Home Page**:
    - The home page provides an overview of the dashboard and displays the primary data and metrics. Here, users can see filtered test data, performance metrics, and visualizations based on their selections.

2. **Filters**:
    - Utilize the sidebar to apply filters to the data:
        - **Date Range**: Select a specific range of dates to view test data within that period.
        - **Vehicle ID**: Choose a vehicle ID to view data related to a specific vehicle.
        - **Test Result**: Filter the data by the outcome of the tests (e.g., pass, partial pass, warning, fail).

3. **Viewing Data**:
    - After applying filters, the application will display the filtered test data along with calculated performance metrics. This section helps users assess the data based on their selected criteria.

4. **Generating Visualizations**:
    - Choose from different chart types and metrics to visualize the data. The visualizations help in understanding data trends, distributions, and relationships between various metrics.
