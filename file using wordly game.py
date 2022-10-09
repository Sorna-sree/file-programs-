import random
import csv

def checkword(user_word,wordly_word):
	for x in user_word:
		print(x,end=" ") #print the user  input word
	print()
	for i in range(len(user_word)):
		if user_word[i] == wordly_word[i]: #the word is present in correct possition
			print(" green",end =" ")
		elif user_word[i] in wordly_word: #wordly word is present in userword
			print(" yellow ",end=" ")
		else:
			print(" red ",end=" ") #not present in wordly word in user word
	if user_word == wordly_word:
		return 1
	else:
		return 0
with open('C:\\Users\\sornasree\\Desktop\\words.csv', mode ='r')as file:
	csvFile = csv.reader(file)
	for lines in csvFile:
	    print(lines)
random_word = random.choice(lines) #choice the random word in files
print(random_word)
num = len(random_word) #calculate the len of random word
print("Let's Play Wordle")
while num > 0:
	user_word=input("\nEnter word: ") #enter the word
	if (len(user_word)==5 and user_word.isalpha()): # check the word is five letter word and alphat word
		num = num-1
		if checkword(user_word,random_word):
				print("\n","Game Over")
				break
		else:
			continue
	else:
		print("Please enter a valid word")
else:
	print("End of Game, the correct word is:",random_word) 
