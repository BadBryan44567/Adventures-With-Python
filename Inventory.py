def create_inventory(items: list):
	return {i: items.count(i) for i in items}

def add_items(inventory: dict, items: list):
	items = create_inventory(items)
	keys = list(inventory.keys()) + list(items.keys())
	return {key: inventory.get(key, 0) + items.get(key, 0) for key in keys}

def decrement_items(inventory, items):
	items = create_inventory(items)
	keys = list(inventory.keys()) + list(items.keys())
	return {key: inventory.get(key, 0) - items.get(key, 0) if inventory.get(key, 0) > items.get(key, 0) else 0 for key in keys }

def remove_item(inventory: dict, item):
	if item in inventory:
		inventory.pop(item)
		return inventory
	else:
		return inventory

def list_inventory(inventory: dict):
	return [item for item in inventory.items() if item[1] !=0]

print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))