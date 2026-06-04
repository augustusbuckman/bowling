# Do not modify the code in this file
# Test for bowling scores

import unittest
import ast
import bowling
import tud_test_base as tud


class TestBowling(unittest.TestCase):

    def run_program(self, name, game1, game2, game3):

        tud.set_keyboard_input([
            name,
            str(game1),
            str(game2),
            str(game3)
        ])

        bowling.main()

        return tud.get_display_output()

    def verify_case(self, name, game1, game2, game3):

        average = (
            game1 + game2 + game3
        ) // 3

        handicap = (
            (200 - average) * 80
        ) // 100

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

        output = self.run_program(
            name,
            game1,
            game2,
            game3
        )

        self.assertEqual(
            output,
            expected
        )

    def test_assignment_example(self):
        self.verify_case(
            "Mike",
            143,
            128,
            162
        )

    def test_all_zeroes(self):
        self.verify_case(
            "John",
            0,
            0,
            0
        )

    def test_average_truncation(self):
        self.verify_case(
            "Amy",
            100,
            101,
            102
        )

    def test_high_scores(self):
        self.verify_case(
            "Sarah",
            250,
            275,
            290
        )

    def test_negative_handicap(self):
        self.verify_case(
            "Chris",
            300,
            300,
            299
        )

 
    def test_prompt_format(self):

        output = self.run_program(
            "Mike",
            143,
            128,
            162
        )

        self.assertEqual(
            output[0],
            "Enter your name: "
        )

        self.assertEqual(
            output[2],
            "Enter Game 1: "
        )

        self.assertEqual(
            output[3],
            "Enter Game 2: "
        )

        self.assertEqual(
            output[4],
            "Enter Game 3: "
        )

    def test_no_extra_output(self):

        output = self.run_program(
            "Mike",
            143,
            128,
            162
        )

        self.assertEqual(
            len(output),
            8
        )

    def test_hidden_scores(self):

        hidden_cases = [

            ("A", 111, 123, 145),

            ("B", 89, 94, 105),

            ("C", 178, 199, 211),

            ("D", 160, 160, 160),

            ("E", 1, 299, 150)
        ]

        for case in hidden_cases:

            with self.subTest(case=case):

                self.verify_case(*case)

    def test_header_and_comments(self):

        with open("bowling.py") as f:

            code = f.read()

        required_header = [

            "# File:",
            "# Description:",
            "# Assignment Number:",
            "# Name:",
            "# SID:",
            "# Email:",
            "# Grader:"
        ]

        for item in required_header:

            self.assertIn(
                item,
                code,
                f"Missing header item: {item}"
            )

        lines = code.splitlines()

        meaningful_comments = 0

        for line in lines[15:]:

            stripped = line.strip()

            if (
                stripped.startswith("#")
                and len(stripped) > 15
            ):
                meaningful_comments += 1

        self.assertGreaterEqual(
            meaningful_comments,
            2,
            "Expected at least two explanatory comments."
        )

 
    def test_readability(self):

        with open("bowling.py") as f:

            tree = ast.parse(f.read())

        assignments = 0

        bad_names = []

        allowed_short_names = {
            "name"
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.Assign):

                assignments += 1

                for target in node.targets:

                    if isinstance(
                        target,
                        ast.Name
                    ):

                        variable_name = target.id

                        if (
                            len(variable_name) <= 2
                            and variable_name
                            not in allowed_short_names
                        ):
                            bad_names.append(
                                variable_name
                            )

        self.assertGreaterEqual(
            assignments,
            5,
            "Expected program to be broken into logical steps."
        )

        self.assertLessEqual(
            len(bad_names),
            2,
            f"Use more descriptive variable names instead of {bad_names}"
        )

    def test_main_exists(self):

        self.assertTrue(
            hasattr(
                bowling,
                "main"
            )
        )


if __name__ == "__main__":
    unittest.main()
