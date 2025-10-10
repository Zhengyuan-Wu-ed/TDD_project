import unittest

class TestMoney(unittest.TestCase):
#    def TestFoo(self):
#        self.assertEqual('foo'.upper(), 'FOO')
    def test_foo(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_multiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)

if __name__ == '__main__':
    unittest.main()
