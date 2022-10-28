def is_panagram(sentence: str):
	letters = ['a', 'b', 'c', 'd', 'e', 'f',' g', 'h', 'i', 'j', 'k', 'l' , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w', 'x', 'y', 'z']
	has_all = all([letter in sentence for letter in letters])
	return has_all

print(is_panagram("The quick brown fox jumps over the lazy dog"))