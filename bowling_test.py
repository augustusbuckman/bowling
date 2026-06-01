# Do not modify the code in this file
# Test for bowling scores

import unittest
import bowling
import tud_test_base as tud


class TestBowling(unittest.TestCase):

    def verify_case(self, name, g1, g2, g3):

        tud.set_keyboard_input(
            [name, str(g1), str(g2), str(g3)]
        )

        bowling.main()

        output = tud.get_display_output()

        average = (g1 + g2 + g3) // 3
        handicap = ((200 - average) * 80) // 100

        expected = [
            "Enter your name: ",
            "",
            "Enter Game 1: ",
            "Enter Game 2: ",
            "Enter Game 3: ",
            "",
            f"{name}'s average is: {average}",
            f"{name}'s handicap is: {handicap}"
        ]

        self.assertEqual(output, expected)

    def test_assignment_example(self):
        self.verify_case("Mike", 143, 128, 162)

    def test_all_zeroes(self):
        self.verify_case("John", 0, 0, 0)

    def test_perfect_games(self):
        self.verify_case("Sarah", 300, 300, 300)

    def test_typical_scores(self):
        self.verify_case("Bob", 150, 160, 170)

    def test_negative_handicap(self):
        self.verify_case("Chris", 300, 300, 299)

    def test_fractional_average_truncation(self):
        self.verify_case("Amy", 101, 102, 103)

    def test_random_case_1(self):
        self.verify_case("A", 123, 234, 145)

    def test_random_case_2(self):
        self.verify_case("B", 178, 205, 199)

    def test_random_case_3(self):
        self.verify_case("C", 77, 88, 99)

    def test_random_case_4(self):
        self.verify_case("D", 250, 275, 290)


if __name__ == "__main__":
    unittest.main()