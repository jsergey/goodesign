import unittest
import os

class TestAPI(unittest.TestCase):
    def test_extract_path(self):
        path = "test/code_maat/end_to_end/git2_live_data_test_with_group.clj"
        self.assertEqual(os.path.split(path)[0], "test/code_maat/end_to_end")


