import random

def generator():
	while True:
		length = input("How many characters long should the password be: ")
		if length.isdigit():
			break
		else:
			print("Invalid input. Please enter a number.\n")

	#weak password
	weak = ''
	lowercase = 'abcdefghijklmnopqrstuvwxyz'
	for i in range (int(length)):
		randChar = random.choice(lowercase)
		weak = weak + randChar
	print("Weak password: \t\t" + weak)

	#moderate password
	moderate = ''
	uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for i in range (int(length)):
		randChar = random.choice(lowercase + uppercase)
		moderate = moderate + randChar
	print("Moderate password: \t" + moderate)
	
	#strong password
	strong = ''
	nums = '1234567890'
	specialChar = '!@#$%&*-;:.><?+=_[]{}()'
	for i in range (int(length)):
		randChar = random.choice(lowercase + uppercase + nums + specialChar)
		strong = strong + randChar
	print("Strong password: \t" + strong)

	return weak, moderate, strong



#==============================welcome msg======================================
print("Welcome to the password manager!\n\n")
choice = ''

#prompts the user on what they want to do and prompts until their respond isnt valid
while True:
	print("What would you like to do?")
	print("A. Generate new password \t B. Add an existing password to file \t C. Update password \t D. Look up a password\n")
	choice = input("Please press a letter to choose: ")

	if (choice == 'A' or choice == 'B' or choice == 'C' or choice == 'D'):
		break

if choice == 'A':
	#generates and prints the password
	weak, moderate, strong = generator()
elif choice == 'B':
	#call a function to do file IO stuff
	print("reached choice B")
elif choice == 'C':
	#update password for soemthing
	print("reached choice C")
elif choice == 'D':
	#Find a passwrd
	print("reached choice D")

usr_name = input("What is your name?")
file = open(usr_name+".txt", "w")
file.write("this is name of user: "+usr_name+"\n")
file.write("this is name of user: "+usr_name)
file.close()
