def round_scores(student_scores: list):
	return [round(i) for i in student_scores]

def count_failed_students(student_scores: list):
	count = 0
	for i in student_scores:
		if i < 40: 
			count+= 1
	return count

def above_threshold(student_scores, threshold):
	best= []
	for i in student_scores:
		if i >= threshold:
			best.append(i)
	return best

def letter_grades(highest):
	step = int((highest-40)/4)
	return [score for score in range(41, highest, step)]


print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
print(count_failed_students([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
print(above_threshold([90.33, 91.67, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3], 75))
print(letter_grades(100.0))