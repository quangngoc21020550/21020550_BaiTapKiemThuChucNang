import unittest
import heathAnalyze


class TestCalc(unittest.TestCase):
    def test_r1(self):
        with self.assertRaises(ValueError):
            heathAnalyze.heathAnalyze("20")
    def test_r2(self):
        with self.assertRaises(ValueError):
            heathAnalyze.heathAnalyze(-1)

    def test_r3(self):
        self.assertEqual(heathAnalyze.heathAnalyze(17.5), "Underweight")

    def test_r4(self):
        self.assertEqual(heathAnalyze.heathAnalyze(25), "Normal")

    def test_r5(self):
        self.assertEqual(heathAnalyze.heathAnalyze(30), "Overweight")

    def run_test():
        unittest.main(verbosity=2)
