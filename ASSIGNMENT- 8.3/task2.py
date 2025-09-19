import unittest
def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

class TestAssignGrade(unittest.TestCase):
    # Valid A grade tests
    def test_grade_A_boundaries(self):
        self.assertEqual(assign_grade(100), "A")
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(95), "A")

    # Valid B grade tests
    def test_grade_B_boundaries(self):
        self.assertEqual(assign_grade(89), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(85), "B")

    # Valid C grade tests
    def test_grade_C_boundaries(self):
        self.assertEqual(assign_grade(79), "C")
        self.assertEqual(assign_grade(70), "C")

if __name__ == "__main__":
    unittest.main()
