numbers = [0.0, 75.0]
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)
print(average(numbers))

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
		return homework*0.1 + quizzes*0.3 + tests*0.6
