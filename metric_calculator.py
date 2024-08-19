
class MetricCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_metrics(self):
        average_speed = self.data['average_speed'].mean()
        average_distance = self.data['following_distance'].mean()
        average_lane_keeping_accuracy = self.data['lane_keeping_accuracy'].mean()
        average_human_inputs = self.data['human_inputs'].mean()
        average_distance_travelled = self.data['distance_travelled'].mean()
        common_result = self.data['result'].value_counts().idxmax()

        return {
            'average_speed': average_speed,
            'average_distance': average_distance,
            'average_lane_keeping_accuracy': average_lane_keeping_accuracy,
            'average_human_inputs': average_human_inputs,
            'average_distance_travelled': average_distance_travelled,
            'common_result': common_result
        }