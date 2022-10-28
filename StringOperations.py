def capitalize_title(title: str):
	return title.title()

def check_sentence_ending(sentence: str):
	return sentence.endswith('.')

def clean_up_spacing(sentence: str):
	
	return sentence.strip()

def replace_word_choice(sentence: str, old_word: str, new_word: str):
	return sentence.replace(old_word, new_word)

print(capitalize_title("my hobbies"))
print(check_sentence_ending("I Like to Hike, Bike and read."))
print(clean_up_spacing("   I like to go on hikes with my dog.    "))
print(replace_word_choice("I bake good cakes", "good", "amazing"))