const assert = require('assert');

class Money {
	constructor(amount, currency) {
		this.amount = amount;
		this.currency = currency;
	}

	times(multiplier) {
		return new Money(this.amount*multiplier, this.currency);
	}

	divide(divisor) {
		return new Money(this.amount/divisor, this.currency);
	}
}

//test-1-multiplication
let fiveDollars = new Money(5, "USD");
let tenDollars = new Money(10, "USD");
assert.deepStrictEqual(fiveDollars.times(2), tenDollars);

//test-2-multiplication
let tenEuros = new Money(10, "EUR");
let twentyEuros = new Money(20, "EUR");
assert.deepStrictEqual(tenEuros.times(2), twentyEuros);

//test-3-division
let originalMoney = new Money(4002, "KRW")
let actualMoneyAfterDivision = originalMoney.divide(4)
let expectedMoneyAfterDivision = new Money(1000.5, "KRW")
assert.deepStrictEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision)
