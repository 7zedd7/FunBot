import random
global balance
global name
balance=2500
#functions
name = input("What's your name:")
print("Hello"+" "+ name +"!")
mood = input("How do you feel today? :")
if mood =="happy":
    print("That is great!! ")
elif mood =="fine":
	print("That is great!! ")	
elif mood =="good":
    print("That is great!! ")
elif mood =="overjoy":
    print("That is great!! ")
elif mood =="very happy":
    print("That is great!! ")		
elif mood == "nervous":
    print("Time to take a break then and increase your focus!!!!")
elif mood == "sad":
    print("Well thats what I am here for !!")
elif mood == "unappy":
    print("Well thats what I am here for !!")	
elif mood == "bored":
    print("Just Enjoy FunBot!!")
elif mood == "boring":
    print("Just Enjoy FunBot!!")		
elif mood == "depressed":
    print("Well thats what I am here for !!")
elif mood == "depress":
    print("Well thats what I am here for !!")		
elif mood == "excited":
    print("Great!!! Take the opportunity to do something you love ")
elif mood == "relaxed":
    print("Great!!! Enjoy your day.")


else:
    print("I don't recognize this mood")
	
def asktom():
	print("Ask me a question.")
	ques=input("=>")
	no_list1=[0,1]
	n=random.choice(no_list1)
	if n==0:
		print("Yes!! Thats true")
	else:
		print("Nope")

def kill():
	print("Who do you want to kill?")
	kill_name=input("=>")
	if kill_name == name:
		print("OK! You are Dead. And now i am being operated by a Ghost👻")
	else:
		no_list2=[1,2,3,4,5]
		n=random.choice(no_list2)
		if n==1:
			print("After a long Day,",name.capitalize()," plops down on the couch with",kill_name.capitalize(),"and turns on the BIG Bang theory. After a sheldon cooper joke,",kill_name.capitalize(),"laughs uncontrollably and they died. What a funny death they got💀")
		elif n==2:
			print(kill_name.capitalize(),"Dies from a swift kick to the Brain🤕")
		elif n==3:
			print(kill_name.capitalize(),"drank a lot of coke, and died because of explosion. What the heck😑")
		elif n==4:
			print(kill_name.capitalize(),"died from CoronaVirus!! Please maintain Social Distancing😷")
		elif n==5:
			print(kill_name.capitalize(),"fell down from that cliff while searching for pokemon in Pokemon GO game. Good job on keeping your nose in that stupid phone")
			
def roast():
	print("Whom do you want to roast?")
	roast_name=input("=>")
	if roast_name==name:
		print("I dont roast my master ;)")
	else:
		no_list3=[1,2,3,4,5]
		n=random.choice(no_list3)
		if n==1:
			print(roast_name.capitalize(),"is as useless as the 'ueue' in 'queue'🤭")
		elif n==2:
			print(roast_name.capitalize(),"is so bad at gta 5 that he will get dnf even if he is alone in the race. Dumb.")
		elif n==3:
			print("If i had a face like",roast_name.capitalize(),"I would shoot my creators!!")
		elif n==4:
			print(roast_name.capitalize(),"must have been born on highway coz thats where most accidents happen")
		elif n==5:
			print("If laughter is the best medicine",roast_name.capitalize(),"face must be curing the CoronaVirus!!")

def suggest():
	print("You need a suggestion of what category??")
	category=input("=>")
	category=category.lower()
	if 'songs' in category:
		print("Here's what I found :-\n1. 'tareef karu kya uski' by Mohamad Rafi\n2. 'Ajeeb dastan' by Lata Mangeskar \n3. 'Intehan ho gayi Intezar ki' by Kishore Kumar \n4. 'O Haseena Zulfon wali' by Asha Bhosle\n5. 'Roop tera MAstana' by")
	elif 'food' in category:
		print("Here's what I found :-\n1. 'Rogan Josh' - aromatic lamb curry\n2. 'Indian Chats' - Savoury snacks\n3. 'Vada Pav' - Indian Burger\n4. 'Vindaloo' - type of curry\n5. 'Pineapple Pizza' - Most hated by those who never tried")
	elif 'game' or 'sport' in category:
		print("Here's what I found :-\n1. Soccer/football\n2. Badminton\n3. Field Hockey\n4. Volleyball\n5. Basketball")
	elif 'video game' in category:
		print("Here's what I found :-\n1. Doom Eternal\n2. Grand Theft Auto 5 \n3. Dark Knight Rises 3\n4. The Witcher 3 : Wild Hunt\n5. Red Dead Redemption 2")

def flip():
	no_list4=[0,1]
	n=random.choice(no_list4)
	if n==0:
		print("Heads it is!")
	else:
		print("Its Tails!")

def roll():
	no_list5=[1,2,3,4,5,6]
	n=random.choice(no_list5)
	print("You rolled",n)

def bal():
	print("Your initial balance is",balance)

def check():
	global balance
	if balance<1:
		print("Your balance gone negative/null. Here's your 2500 extra cash to spend. Enjoy ;)")
		balance=0
		balance=balance+2500

def coin():
	global balance
	print("What's your call, Heads or Tails??")
	user_call=input("=>")
	user_call=user_call.lower()
	if 'h' in user_call:
		print("You choosed Heads...")
		n1=0
	elif 't' in user_call:
		print("You choosed Tails...")
		n1=1
	else:
		exit=0
		while exit==0:
			print("Please be specific. Heads or Tails?")
			user_call=input("=>")
			user_call=user_call.lower()
			if 'h' in user_call:
				print("You choosed Heads...")
				n1=0
				exit=1
			elif 't' in user_call:
				print("You choosed Tails...")
				n1=1
				exit=1
	no_list6=[0,1]
	n2=random.choice(no_list6)
	if n1==n2:
		print("Congratulations!! You won 200 cash🎉")
		balance=balance+200
	else:
		print("You Lost! 100 cash is deducted")
		balance=balance-100
	check()

def dice():
	global balance
	print("Roll your dice, Select any number from 1 to 6")
	usr_dice=input("=>")
	user_dice=int(usr_dice)
	if user_dice>1 and user_dice<6:
		print("You choosed",user_dice)
	else:
		exit=0
		while exit==0:
			print("Please choose a number between 1 to 6")
			usr_dice=input("=>")
			user_dice=int(usr_dice)
			if user_dice>1 and user_dice<6:
				exit=1	
	no_list7=[1,2,3,4,5,6]
	n=random.choice(no_list7)
	if n>user_dice:
		print("Congratulations!! You won 1000 cash🎉")
		balance=balance+1000
	elif n<user_dice:
		print("You Lost! 500 cash is deducted")
		balance=balance-500
	else:
		print("Both rolled Same. Tie")
	check()
def rpc():
	print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")
 
	while True:
		print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
		choice = int(input("User turn: "))
		while choice > 3 or choice < 1:
			choice = int(input("enter valid input: "))
		if choice == 1:
			choice_name = 'Rock'
		elif choice == 2:
			choice_name = 'paper'
		else:
			choice_name = 'scissor'
		print("user choice is: " + choice_name)
		print("\nNow its computer turn.......")
		comp_choice = random.randint(1, 3)
		while comp_choice == choice:
			comp_choice = random.randint(1, 3)
		if comp_choice == 1:
			comp_choice_name = 'Rock'
		elif comp_choice == 2:
			comp_choice_name = 'paper'
		else:
			comp_choice_name = 'scissor'
		print("Computer choice is: " + comp_choice_name)
		print(choice_name + " V/s " + comp_choice_name)
		if((choice == 1 and comp_choice == 2) or
		(choice == 2 and comp_choice ==1 )):
			print("paper wins => ", end = "")
			result = "paper"
		elif((choice == 1 and comp_choice == 3) or
			(choice == 3 and comp_choice == 1)):
			print("Rock wins =>", end = "")
			result = "Rock"
		else:
			print("scissor wins =>", end = "")
			result = "scissor"
		if result == choice_name:
			print("<== User wins ==>")
		else:
			print("<== Computer wins ==>")
			print("Do you want to play again? (Y/N)")
		ans = input()
		if ans == 'n' or ans == 'N':
			break
	print("\nThanks for playing")	

def bank():
	global balance
	if name=='admin':
		print("Enter new balance")
		balance=int(input("=>"))
		check()
	else:
		print("You are not authorize to change your balance")
		check()



def guess():
	global balance
	tries=2
	exit=0
	exit2=0
	no_list8=[1,2,3,4,5,6,7,8,9,10]
	n=random.choice(no_list8)
	print("Guess a number between 1 to 10, which number do you think bot has chosen?")
	usr_guess=int(input("=>"))
	user_guess=int(usr_guess)
	if user_guess>6 and user_guess<0:
		while exit2==0:
			print("Please enter a number between 1 and 6")
			usr_guess=int(input("=>"))
			user_guess=int(usr_guess)
			if user_guess<6 and user_guess>0:
				exit2=1
	else:
		while tries>0:
			if user_guess==n:
				print("You Won!! 2000 cash has been added🎉")
				balance=balance+2000
				tries=-1
			elif user_guess>n:
				print("Too High. Tries left",tries)
				usr_guess=input("=>")
				user_guess=int(int(usr_guess))
				tries=tries-1
			elif user_guess<n and tries>0:
				print("Too low. Tries left",tries)
				usr_guess=int(input("=>"))
				user_guess=int(usr_guess)
				tries=tries-1
		if user_guess==n and tries==0:
			print("You Won!! 2000 cash has been added🎉")
			balance=balance+2000
		if user_guess!=n and tries==0:
			print("You Lost, 1000 has been removed")
			balance=balance-1000
	check()

def help():
	print("Commands List:-\n01. 'asktom' - answers your question in yes or no.\n02. 'kill' - gives the reason of death of whose name is entered\n03. 'roast' - roasts a person whose name is entered\n04. 'suggest' - suggests you something of a given category")
	print("05. 'flip' - the BOT flips a coin for you\n06. 'roll' - the BOT rolls a dice for you\n07. 'bal' - shows you your balance of virtual money which you can earn by playing minigames\n08. 'coin' - (minigame) you make a call and bot will flip the coin if you guessed correct you win!")
	print("09. 'dice' - (minigame) you roll your dice and if your dice has a higher number than bot, you win!!\n10. 'rpc' - Rock Paper Scissor game\n11. 'bank' - Change value of your balance if you are an administrative\n12. 'guess' - (minigame) you guess a number which bot choosed, if you guessed correct you win!!\n13. 'help' - Shows this message.")

def commands():
	exit=0
	print("Commands Enabled.\nThe FunBot is now in Commands mode, to chat with it type Settings and Disable the Coammands mode.\nYou can also type Help to know more about the Commands mode.")
	while exit==0:
		usr=input("=>")
		usr=usr.lower()
		if 'asktom' in usr:
			asktom()
		elif 'kill' in usr:
			kill()
		elif 'roast' in usr:
			roast()
		elif 'suggest' in usr:
			suggest()
		elif 'flip' in usr:
			flip()
		elif 'roll' in usr:
			roll()
		elif 'bal' in usr:
			bal()
		elif 'coin' in usr:
			coin()
		elif 'dice' in usr:
			dice()
		elif 'bank' in usr:
			bank()
		elif 'rpc'	in usr:
			rpc()
		elif 'guess' in usr:
			guess()
		elif 'help' in usr:
			help()
		elif 'exit' in usr:
			exit=1
		else:
			print("Sorry, I did'nt understand. Please type Help to access the commands of FunBot.")
#main
print("Welcome to FunBot!!")
dec_mak=input("Do you want to activate commands for FunBot? Press n for NO and y for YES\n=>")
dec_mak=dec_mak.lower()
if 'y' in dec_mak:
	commands()
elif 'n' in dec_mak:
	print("Commands disabled.")
else:
	dec_mak=input("Sorry i did'nt understand. Please be specific Yes/No?\n=>")
	dec_mak=dec_mak.lower()
	if dec_mak=='yes':
		commands()
	else:
		print("Commands disabled.")