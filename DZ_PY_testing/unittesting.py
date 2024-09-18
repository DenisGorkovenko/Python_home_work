import unittest


def sort_list(new_list):
    return sorted(new_list)


class TestSorted(unittest.TestCase):
    def test_sorted(self):
        test_case = {(12, -3, 4): [-3, 4, 12],
                     ('wer', 're', 'asd', 'efghj'): ['asd', 'efghj', 're', 'wer'],
                     (3.5, -0.345): [-0.345, 3.5]}
        for inp, res in test_case.items():
            self.assertEqual(sort_list(inp), res)


if __name__ == '__main__':
    unittest.main()
