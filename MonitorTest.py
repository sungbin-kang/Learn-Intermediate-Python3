import unittest
import monitor


class MonitorTest(unittest.TestCase):

    @unittest.expectedFailure
    def test_calculate_remaining_time_with_str(self):
        print("str Expected Failure test begins...")
        monitor.calculate_remaining_time("str")

    def test_calculate_remaining_time_incorrect_datatypes(self):
        print("Multiple Data Types Expected Failure test begins...")
        data_types = ["str", (0,), {}, [], None]
        for data_type in data_types:
            with self.subTest(data_type):
                self.assertRaises(TypeError, monitor.calculate_remaining_time,
                                  data_type)

    def test_calculate_remaining_time(self):
        print("Calcuate Remaining Time test begins...")
        for km in range(0, 100000):
            time = monitor.calculate_remaining_time(km)
            with self.subTest(km):
                self.assertEqual(time[0], int(km / (15 * 60)))
                self.assertIn(time[1], range(0, 60))

    def test_request_flight_attendant(self):
        print("Warning Raise test begins...")
        self.assertWarns(monitor.CustomerRequestWarning,
                         monitor.request_flight_attendant)


unittest.main()

# empty line
