def add_prefix_un(word: str):
	return "un" + word

def make_word_groups(group):
	return ("::" + group[0]).join(group)

def remove_suffix_ness(word: str):
	without_ness = word.removesuffix("ness")
	if without_ness.endswith("i"):
		return without_ness.removesuffix("i") + "y"
	return without_ness

def adjective_to_verb(sentence: str, index):
	split_sentence = sentence.split()
	adjective = split_sentence[index]
	return adjective + "en"

print(add_prefix_un("happy"))
print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(remove_suffix_ness('sadness'))
print(adjective_to_verb("I need to make that bright", -1))