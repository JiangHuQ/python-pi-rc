import useful_tools
from Student import Student
from Question import Question
question_prompts = [
	"what color are apples?\n (a) Red/Green (b) Purple (c) Orange\n\n",
	"what color are Bananas?\n (a) Teal (b) Magenta (c) Yellow\n\n",
	"what color are stawberries?\n (a) Yellow (b) Red (c) Blue\n\n"
]

questions = [
	Question( question_prompts[0], "a"),
	Question( question_prompts[1], "c"),
	Question( question_prompts[2], "b")
]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.question_prompts)
		if answer == question.answer:
			score += 1
	print("you got "+str(score) +"/"+str(len(questions)) +"correct")

run_test(questions)


student1 = Student("Jim", "Business", 3.1, False)

print(student1.name)

print(useful_tools.feet_in_mile)

# write to files

# read file
# mode a w r r+
employee_file = open("employees.txt","a")
print(employee_file.readable())
employee_file.write("\nKelly -- Customer Service")
#print(employee_file.read())
#for employee in employee_file.readlines():
#	print(employee)
#print(employee_file.readlines()[1])
employee_file.close()


try:
	result = 16/0
	number = int(input("Enter a number: "))
	print(number)
except ZeroDivisionError as err:
	print("Dividen by zero!")
	print(err)
except ValueError:
	print("Invalid input!")

def translate(phrase):
	translation = ""
	for letter in phrase:
		if letter in "AEIOUaeiou":
			translation = translation + "g"
		else:
			translation = translation + letter
	return translation

# print(translate(input("input phrase: ") ))


number_grid = [
	[1,2,3],
	[4,5,6],
	[7,8,9],
	[0]
]

"""
for row in number_grid:
	for col in row:
		print(col)
"""
secret_no = 15
guess = 0
guess_count = 0
guess_limit = 3

# input and while loop
"""
while guess !=  secret_no and guess_count < guess_limit:
	guess = int( input("Please input guess number :") )
	guess_count += 1
print("You win. The answer is :" + str(guess) )
"""

friends = ["Jim", "Kevin", "Keran"]

for friend in friends:
	print(friend)

is_male = False
if is_male:
	print("you are a male")
else:
	print("You are not a male")

"""
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
phrase = "RockyAcademy"
print(str(len(phrase)))
print(phrase)
print(phrase.isupper())
print(phrase.upper())
print(phrase.isupper())
phrase2 = phrase.upper()
print(phrase2)
print(phrase2.isupper())
print("The length of "+ phrase +" is "+ len(phrase).__str__())

"""