import unittest
from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):

    def test_multiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR") 
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def test_division(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision, actualMoneyAfterDivision)

    def test_addtion(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")

        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def test_additionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actuallValue = portfolio.evaluate("USD")
        self.assertEqual(
                expectedValue, actuallValue, "%s != %s" % (expectedValue, actuallValue)
            )

if __name__ == '__main__':
    unittest.main()
