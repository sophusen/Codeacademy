n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result

n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
  result = ""
  for i in words:
    result = result+words[i]
print join_strings(n)

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print join_strings(n)
