def add_me_to_the_queue(express_queue: list, normal_queue: list, ticket_type, person_name):
	if ticket_type == 1:
		express_queue.append(person_name)
		return express_queue
	if ticket_type == 0:
		normal_queue.append(person_name)
		return normal_queue

def find_my_friend(queue: list, friend_name):
	return queue.index(friend_name)

def add_me_with_friends(queue: list, index, person_name):
	queue.insert(index, person_name)
	return queue

def remove_mean_person(queue: list, person_name):
	queue.remove(person_name)
	return queue

def how_many_name_fellows(queue: list, person_name):
	return queue.count(person_name)

def remove_last_person(queue: list):
	queue.remove(queue[-1])
	return queue

def sorted_names(queue: list):
	queue.sort()
	return queue

print(add_me_to_the_queue(["Tony", "Bruce"], ["Robot Guy", "WW"], 1, "RichieRich"))
print(find_my_friend(["Natasha", "Steve", "T'Challa", "Wanda"], "Wanda"))
print(add_me_with_friends(["natasha", "Steve", "T'Challa", "Wanda"], 1, "Bucky"))
print(remove_mean_person(["natasha", "Steve", "T'Challa", "Wanda"], "Steve"))
print(how_many_name_fellows(["natasha", "Steve", "T'Challa", "Wanda", "Steve"], "Steve"))
print(remove_last_person(["natasha", "Steve", "T'Challa", "Wanda"]))
print(sorted_names(["natasha", "Steve", "T'Challa", "Wanda"]))
