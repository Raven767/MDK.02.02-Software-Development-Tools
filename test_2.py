import unittest
import re
import myform
class Test_test_2(unittest.TestCase):
    def test_T(self):
        telefhone = ["+79522242323","+74322099107","+84 42 2341232"]
        for i in range (len(list_mail)):
            regex=re.search('^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$', telefhone[i])
        self.assertTrue(regex)

if __name__ == '__main__':
    unittest.main()