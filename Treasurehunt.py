def get_coordinate(tuple):
	return tuple[1]

def convert_coordinate(coordinate: str):
	return tuple(coordinate)

def compare_records(record1, record2):
	new_coordinate = convert_coordinate(record1[1])
	if new_coordinate == record2[1]:
		return True
	return False

def create_record(record1: tuple, record2: tuple):
	if compare_records(record1, record2) == True:
		return record1 + record2
	return "not a match"

def clean_up(combined_record_group):
	data = [(x[0], x[2], x[3], x[4]) for x in combined_record_group]
	lines = [f"{x}\n" for x in data]
	return "".join(lines)

print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))
print(convert_coordinate("2A"))
print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))
print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
print(create_record(('Brass Spyglass', '4B'), (('1', 'C'), 'Seaside Cottages', 'blue')))
print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))