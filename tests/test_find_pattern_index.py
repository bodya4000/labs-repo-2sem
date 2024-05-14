import unittest
from src.find_pattern_index import *


class TestFindingFirstIndexOfPatternInText(unittest.TestCase):
    def test_normal_case1(self):
        result = find_needle("abxabcabcaby", "abcaby")
        self.assertEqual(result, [6])

    def test_with_several_needles_in_haystack(self):
        result = find_needle("sdadsadasdasdsa", "das")
        self.assertEqual(result, [6, 9])

    def test_no_matches(self):
        result = find_needle("нот еверейдж нот інгліш вордс", "just average english words")
        self.assertEqual(result, -1)

    def test_empty_haystack(self):
        result = find_needle("", "abc")
        self.assertEqual(result, -1)