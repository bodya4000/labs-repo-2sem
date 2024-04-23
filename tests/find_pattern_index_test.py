import unittest
from src.find_pattern_index import *


class TestFindingFirstIndexOfPatternInText(unittest.TestCase):
    def test_normal_case1(self):
        result = find_pattern_index_with_dfa("abxabcabcaby", "abcaby")
        self.assertEqual(result, 6)

    def test_normal_case2(self):
        result = find_pattern_index_with_dfa("sdadsadasdasdsa", "das")
        self.assertEqual(result, 6)

    def test_no_matches(self):
        result = find_pattern_index_with_dfa("нот еверейдж нот інгліш вордс", "just average english words")
        self.assertEqual(result, -1)

    def test_empty_haystack(self):
        result = find_pattern_index_with_dfa("", "abc")
        self.assertEqual(result, -1)