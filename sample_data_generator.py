import random
from datetime import datetime, timedelta

class SampleDataGenerator:
    # Define constants for thresholds and ranges
    PASS_THRESHOLD_BASE = 85
    PARTIAL_PASS_THRESHOLD_BASE = 75
    WARNING_THRESHOLD_BASE = 60
    MAX_DISTANCE = 3.0
    MIN_DISTANCE = 0.5
    MAX_ACCURACY = 100
    MIN_ACCURACY = 50
    MAX_HUMAN_INPUTS = 30
    MIN_HUMAN_INPUTS = 0

    @staticmethod
    def determine_result(following_distance, lane_keeping_accuracy, human_inputs, thresholds):
        # Determine the result based on provided metrics and thresholds.
        pass_threshold, partial_pass_threshold, warning_threshold = thresholds

        if lane_keeping_accuracy >= pass_threshold and following_distance >= 2 and human_inputs < 10:
            return 'pass'
        elif lane_keeping_accuracy >= partial_pass_threshold and following_distance >= 1.5 and human_inputs < 20:
            return 'partial pass'
        elif lane_keeping_accuracy >= warning_threshold and following_distance >= 1 and human_inputs < 30:
            return 'warning'
        return 'fail'

    @staticmethod
    def generate_sample_data(num_records):
        #Generate a list of sample data records
        sample_data = []
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 8, 30)
        delta_days = (end_date - start_date).days

        for _ in range(num_records):
            random_days = random.randint(0, delta_days)
            test_date = start_date + timedelta(days=random_days)
            test_date_str = test_date.strftime('%Y-%m-%d')

            days_since_start = (test_date - start_date).days
            total_days = delta_days

            vehicle_id = f'VEHICLE-{random.randint(1, 5)}'
            average_speed = round(random.uniform(30, 120), 2)

            # Vehicle-specific characteristics
            following_distance_mean = random.uniform(2.0, 3.0)
            lane_keeping_accuracy_mean = random.uniform(70, 85)

            # Generate thresholds
            thresholds = SampleDataGenerator.generate_thresholds(days_since_start, total_days)

            # Generate sample data
            following_distance = SampleDataGenerator.generate_following_distance(following_distance_mean, days_since_start, total_days)
            lane_keeping_accuracy = SampleDataGenerator.generate_lane_keeping_accuracy(lane_keeping_accuracy_mean, days_since_start, total_days)
            human_inputs = SampleDataGenerator.generate_human_inputs(days_since_start, total_days)

            distance_travelled = round(random.uniform(10.0, 150.0), 2)
            result = SampleDataGenerator.determine_result(following_distance, lane_keeping_accuracy, human_inputs, thresholds)
            sample_data.append((test_date_str, vehicle_id, average_speed, following_distance, lane_keeping_accuracy, human_inputs, distance_travelled, result))
        
        return sample_data

    @staticmethod
    def generate_thresholds(days_since_start, total_days):
        # Generate dynamic thresholds based on the date.
        return (
            SampleDataGenerator.PASS_THRESHOLD_BASE + (95 - SampleDataGenerator.PASS_THRESHOLD_BASE) * (days_since_start / total_days),
            SampleDataGenerator.PARTIAL_PASS_THRESHOLD_BASE + (85 - SampleDataGenerator.PARTIAL_PASS_THRESHOLD_BASE) * (days_since_start / total_days),
            SampleDataGenerator.WARNING_THRESHOLD_BASE + (75 - SampleDataGenerator.WARNING_THRESHOLD_BASE) * (days_since_start / total_days)
        )

    @staticmethod
    def generate_following_distance(mean, days_since_start, total_days):
        # Generate following distance using a Gaussian distribution.
        distance = round(
            random.gauss(mean + 2.0 * (days_since_start / total_days), 0.5),
            2
        )
        return min(max(distance, SampleDataGenerator.MIN_DISTANCE), SampleDataGenerator.MAX_DISTANCE)

    @staticmethod
    def generate_lane_keeping_accuracy(mean, days_since_start, total_days):
        # generate lane-keeping accuracy using a Gaussian distribution.
        accuracy = round(
            random.gauss(mean + 25 * (days_since_start / total_days), 10),
            2
        )
        return min(max(accuracy, SampleDataGenerator.MIN_ACCURACY), SampleDataGenerator.MAX_ACCURACY)

    @staticmethod
    def generate_human_inputs(days_since_start, total_days):
        # Generate human inputs based on the elapsed time.
        return round(
            max(SampleDataGenerator.MIN_HUMAN_INPUTS, SampleDataGenerator.MAX_HUMAN_INPUTS * (1 - (days_since_start / total_days)) + random.uniform(-10, 10))
        )