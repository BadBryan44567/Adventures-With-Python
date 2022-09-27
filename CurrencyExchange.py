def ExchangeMoney(budget, exchangeRate):
	return budget / exchangeRate

def GetChange(budget, exchangingValue):
	return budget - exchangingValue

def GetValueOfBills(denomination, number_of_bills):
	return denomination * number_of_bills

def GetNumberOfBills(budget, denomination):
	return budget // denomination

def GetLeftOverBills(budget, denomination):
	return budget - GetNumberOfBills(budget, denomination) * denomination

def ExchangableValue(budget, exchangeRate, spread, denomination):
	new_rate = exchangeRate + (exchangeRate * (spread / 100))
	total_new_currency = ExchangeMoney(budget, new_rate)
	bill_value_new_currency = int(total_new_currency / denomination)
	maximun_value_new_currency = bill_value_new_currency * denomination
	return maximun_value_new_currency

print(ExchangeMoney(127.5, 1.2))
print(GetChange(127.5, 120))
print(GetValueOfBills(5, 128))
print(GetNumberOfBills(127.5, 5))
print(GetLeftOverBills(127.5, 20))
print(ExchangableValue(127.5, 1.20, 10, 5))