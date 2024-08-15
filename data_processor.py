import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self, date_range, vehicle_id, result):
        filtered_data = self.data[(self.data['test_date'] >= pd.to_datetime(date_range[0])) & 
                                  (self.data['test_date'] <= pd.to_datetime(date_range[1]))]

        if result != "All":
            filtered_data = filtered_data[filtered_data['result'] == result]

        if vehicle_id != "All":
            filtered_data = filtered_data[filtered_data['vehicle_id'] == vehicle_id]

        return filtered_data