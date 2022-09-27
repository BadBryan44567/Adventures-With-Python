def is_critically_balanced(temprature, neutrons_emmited):
	return True if temprature < 800 and neutrons_emmited > 500 and temprature * neutrons_emmited < 500000 else False

def reactor_efficiency(voltage, current, thoretical_max_power):
	generated_power = voltage * current
	efficiency_percent = (generated_power / thoretical_max_power) * 100
	if efficiency_percent >= 80:
		return "green"
	elif efficiency_percent >= 60 and efficiency_percent < 80:
		return "orange"
	elif efficiency_percent >= 30 and efficiency_percent < 60:
		return "red"
	else:
		return "black"

def fail_safe(temprature, neutrons_produced_per_second, threshold):
	criticality = temprature * neutrons_produced_per_second
	low_threshold = 0.9 * threshold
	high_threshold = 1.1 * threshold

	if criticality < low_threshold:
		return "LOW"
	elif low_threshold <= criticality <= high_threshold:
		return "NORMAL"
	else:
		return "DANGER"

print(is_critically_balanced(750, 600))
print(reactor_efficiency(200, 50, 15000))
print(fail_safe(1000, 30, 5000))