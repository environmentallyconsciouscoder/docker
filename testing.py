import unittest
import numpy as np

#i can import model because i use if __name__ == "__main__":
from heart_model import model

class TestHeartPrediction(unittest.TestCase):
    def test_heart_prediction(self):
        input_data = np.array([53,0,63,1,60,0,368000,0.8,135,1,0,22])
        input_data = input_data.reshape(1,-1)
        result_1 = model.predict(input_data)
        print(f"Test case 1 result is {result_1}")
        self.assertEqual(result_1, 1)

        input_data_2 = np.array([68,1,220,0,35,1,289000,0.9,140,1,1,20])
        input_data_2 = input_data_2.reshape(1,-1)
        result_2 = model.predict(input_data_2)
        print(f"Test case 2 result is {result_2}")
        self.assertEqual(result_2, 1)

if __name__ == "__main__":
    unittest.main()