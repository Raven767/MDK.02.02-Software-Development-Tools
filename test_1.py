import unittest
import re
import myform
class Test_test_1(unittest.TestCase):
    def test_F(self):
        telefhone = ["", "1", "0987654321", "123456789012", "1224", "-84763554", ".99872632232"] 
        for i in range (len(list_mail)):
            regex=re.search('^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$', telefhone[i])
        self.assertFalse(regex)

if __name__ == '__main__':
    unittest.main()
