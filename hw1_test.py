import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        input = "Billy"
        result = hw1.vowel_count(input)
        expected = 1
        self.assertEqual(expected,result)
    def test_vowel_count_2(self):
        input = "MANY vowels IN this SEntenCE"
        result = hw1.vowel_count(input)
        expected = 8
        self.assertEqual(expected,result)

    # Part 2
    def test_short_lists(self):
        input = [[4,3],[4,2],[9,2,3,1],[10,2], [6,4,3,5]]
        result = hw1.short_lists(input)
        expected = [4,3,4,2,10,2]
        self.assertEqual(expected,result)
    def test_short_lists_2(self):
        input = [[],[1,2],[3,4,5],[3,4],[99,100]]
        result = hw1.short_lists(input)
        expected = [1,2,3,4,99,100]
        self.assertEqual(expected,result)
    # Part 3
    def test_ascending_pairs(self):
        input = [[4,3],[3,4,5],[1,2],[0,10,5],[10,0]]
        result = hw1.ascending_pairs(input)
        expected = [[3,4],[3,4,5],[1,2],[0,10,5],[0,10]]
        self.assertEqual(expected,result)
    def test_ascending_pairs_2(self):
        input = [[1,2],[4,3],[100,200,30],[6,5]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2],[3,4],[100,200,30],[5,6]]
        self.assertEqual(expected,result)

    # Part 4
    def test_add_prices(self):
        input1 = data.Price(2,60)
        input2 = data.Price(1,80)
        result = hw1.add_prices(input1,input2)
        expected = 4,40
        self.assertEqual(expected,result)
    def test_add_prices_2(self):
        input1 = data.Price(100,45)
        input2 = data.Price(50,55)
        result = hw1.add_prices(input1,input2)
        expected = 151,0
        self.assertEqual(expected,result)


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
