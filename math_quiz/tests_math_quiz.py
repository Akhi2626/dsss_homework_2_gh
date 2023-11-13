import unittest
from math_quiz import random_integer, random_math_operator, math_function


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for x in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Random integer generated is not in the specified range.") # Test if the number lies between the specified range

    def test_random_math_operator(self):
        # Test if the random operator is within the specified list
        operator_check = random_math_operator()
        self.assertIn(operator_check, ['+', '-', '*'], "Random oepratoe selected is not in the list")

    def test_math_function(self):
            # Test if the math_function is giving the required results
            # Formultaing the test cases
            test_cases = [
                (5, 2, '+', '5 + 2', 7), 
                (7, 8, '-', '7 - 8', -1), 
                (9, 9, '+', '9 + 9', 18),
                (2, 6, '*', '2 * 6', 12),
                (8, 2, '*', '8 * 2', 16)
            ]

            # Comparing the results
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = math_function(num1, num2, operator)
                self.assertEqual(PROBLEM, expected_problem, f"Expected problem:{expected_problem}, Result Obtained:{PROBLEM}") # Comparing the problem with expected problem
                self.assertEqual(ANSWER, expected_answer, f"Expected problem:{expected_answer}, Result Obtained:{ANSWER}") # Comparing the answers with expected answers            

if __name__ == "__main__":
    unittest.main()
