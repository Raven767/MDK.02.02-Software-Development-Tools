import unittest
import re
import myform
class Test_test_2(unittest.TestCase):
    def test_T(self):
        list_mail = ["m.m@mail.ru", "m1@mail.ru","fgfg@mail.ru",'rfr@mail.ru']
        for i in range (len(list_mail)):
            regex=re.search(r'[a-zA-Z0-9_+-]+[@][a-zA-Z0-9-.]+[^.]\.[a-zA-Z0-9-.]{2,3}$', list_mail[i])
        self.assertTrue(regex)

if __name__ == '__main__':
    unittest.main()