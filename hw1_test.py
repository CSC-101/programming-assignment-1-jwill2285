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
    def test_rectangle_area(self):
        input = data.Rectangle(data.Point(7, 20), data.Point(12, 10))
        result = hw1.rectangle_area(input)
        expected = 50
        self.assertEqual(expected,result)
    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(5,5), data.Point(-5,-5))
        result = hw1.rectangle_area(input)
        expected = 100
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author(self):
        input1 = 'David Hasslehoff'
        input2 = [data.Book(['David Hasslehoff'], 'Good Omens'), data.Book(['Bob Frank'], 'The Teaching')]
        result = hw1.books_by_author(input1,input2)
        expected = ['Good Omens']
        self.assertEqual(expected,result)
    def test_books_by_author_2(self):
        input1 = 'Spongebob Squarepants'
        input2 = [data.Book(['David Hasslehoff'],'Good Omens'),data.Book(['Spongebob Squarepants'], 'Bikini Bottom'), data.Book(['Spongebob Squarepants'], 'How to make Krabby Patties')]
        result = hw1.books_by_author(input1,input2)
        expected = ['Bikini Bottom', 'How to make Krabby Patties']
        self.assertEqual(expected,result)

    # Part 7
    def test_circle_bound(self):
        input = data.Rectangle(data.Point(1,2), data.Point(3,4))
        result = hw1.circle_bound(input)
        expected = 1.4142135623730951
        self.assertEqual(expected,result)
    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(-5,10), data.Point(3,-4))
        result = hw1.circle_bound(input)
        expected = 9.219544457292887
        self.assertEqual(expected,result)

    # Part 8
    def test_below_pay_average(self):
        input = [data.Employee('Bob',100),data.Employee('Billy',200),data.Employee('Frank',300)]
        result = hw1.below_average_pay(input)
        expected = ['Bob']
        self.assertEqual(expected,result)
    def test_below_pay_average_2(self):
        input = [data.Employee('Becky', 100000), data.Employee('Charles',200000), data.Employee('Derek',20), data.Employee('Stella',500)]
        result = hw1.below_average_pay(input)
        expected = ['Derek', 'Stella']
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
