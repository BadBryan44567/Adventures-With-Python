EXPECTED_BAKE_TIME = 40

def bake_time_remaining(timeInOven):
	return EXPECTED_BAKE_TIME - timeInOven

def preparation_time_in_minutes(layers):
	prep_time_per_layer = 2
	return prep_time_per_layer * layers

def elapsed_time_in_minutes(numuber_of_layers, elapsed_bake_time):
	return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
