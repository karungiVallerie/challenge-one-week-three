from sort_list import *
import unittest

class testsort_list(unittest.TestCase)
    def testsort_list(self):
        result = sort_list{1,15}
        print('result>>>',result)
        self.assertEqual(result,{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196})
if __name__ =='_main_':
    unittest.main()