import random
import getpass
#--------------------------------------------------

def randomWordGenerator (): # picks a random word from a text file
    f = open("word_list.txt")
    lines = f.readlines()
    randomWordGenerator.rWord = lines [random.randint(0,49)]
    wordTest = (randomWordGenerator.rWord.replace("\n",""))
    randomWordGenerator.rWord2 = wordTest.lower()
    return randomWordGenerator.rWord2


def letterToUnderscope1():
        for char in randomWordGenerator.rWord2:
            print("_", end = " ", flush=True)

def converttostr(input_seq, seperator):   # transforms list into a string ( By Meenakshi Agarwal)
   final_str = seperator.join(input_seq)
   return final_str



def gameUserWord(): # game mechanics for a user generated word
    userLife = 6
    
    wordUnscr = len(userWord)*"_"
    userGuess1 = list(userWord)
    while True:
        
        guessLetter = input("Guess a letter\n " + str(name) + ":")
        if guessLetter in userGuess1:
            while guessLetter in userGuess1:
                    position = userGuess1.index(guessLetter)
                    userGuess1.pop(position)
                    userGuess1[position:position] = ["#"]
                    wordUnscr1 = list(wordUnscr)
                    wordUnscr1.pop(position)
                    wordUnscr1[position:position] = [guessLetter]
                    wordUnscr = converttostr(wordUnscr1,seperator)
                    print(wordUnscr)
                    if userWord == wordUnscr:
                        print("You win")
                        exit()
        elif guessLetter not in userGuess1:
            userLife = userLife - 1
            if userLife == 5:
                print("""
_|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 4:
                print("""  
     |/    
     |      
     |      
     |      
     |    
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 3:
                print("""
      _______
     |/      |
     |     
     |      
     |      
     |     
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 2:
                print("""
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 1:
                print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            if userLife == 0:
                print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
                print("You lose. The word was " + str(userWord))
                break
            print("Letter " + guessLetter + " is not in this word")
            print("You have " + str(userLife) + " lives left")



def gameAutoWord(): # game mechanics for a random generated word
    userLife = 6
    
    wordUnscr = len(randomWordGenerator.rWord2)*"_"
    userGuess1 = list(randomWordGenerator.rWord2)
    while True:
        
        guessLetter = input("guess a letter\n " + str(name) + ":")
        if guessLetter in userGuess1:
            while guessLetter in userGuess1:
                    position = userGuess1.index(guessLetter)
                    userGuess1.pop(position)
                    userGuess1[position:position] = ["#"]
                    wordUnscr1 = list(wordUnscr)
                    wordUnscr1.pop(position)
                    wordUnscr1[position:position] = [guessLetter]
                    wordUnscr = converttostr(wordUnscr1,seperator)
                    print(wordUnscr)
                    if randomWordGenerator.rWord2 == wordUnscr:
                        print("You win")
                        exit()
        elif guessLetter not in userGuess1:
            userLife = userLife - 1
            if userLife == 5:
                print("""
_|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 4:
                print("""  
     |/    
     |      
     |      
     |      
     |    
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 3:
                print("""
      _______
     |/      |
     |     
     |      
     |      
     |     
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=                """)
            elif userLife == 2:
                print("""
      _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            elif userLife == 1:
                print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
            if userLife == 0:
                print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
                print("You lose. The word was " + "__" + str(randomWordGenerator.rWord2) + "__")
                break
            print("Letter " + guessLetter + " is not in this word")
            print("You have " + str(userLife) + " lives left")
            print(wordUnscr)

#--------------------------------------------------

seperator = "" # used in a "listToSting" funtion
userWord = 0 # creates a variable for user word
letAutoWord = randomWordGenerator()
name = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 Hello,welcome to the Hangman!
 What is you name?
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n USER:""")
wordAnswer = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Hi """+ str(name) + """
  Would you like to use the pre existing word or would you like to input your own word?
   To choose a pre-existing word type - \"a\"
   To choose your own word type - \"b\".
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""" + str(name) + """: """)

#--------------------------------------------------

if wordAnswer == "b" or wordAnswer == "B":
    userWord = getpass.getpass("Please write the word that you want to use:\n")
    gameUserWord()
elif wordAnswer == "a" or wordAnswer == "A":
    print("Alright, let's proceed.")
    randomWordGenerator()
    gameAutoWord()
else:
    print("You can only pick option A or B")

#-------------------------------------------------------


