# Task 4

def make_hangman( secret_word):
    guesses = []
    def hangman_closure(guess):
        guesses.append(guess)
        result = ''
        for letter in secret_word:    
            if letter in guesses:
                result+= letter
            else:
                result += "_"
        print(result)              
        if "_" not in result:
            return True
        else:
            return False
    return hangman_closure    

# Start game loop
secret_word = input('Enter the secret word: ').lower()
game = make_hangman(secret_word)
game_over = False  
while True:
    guess = input('Enter a letter: ').lower()
    game_over = game(guess)
    if game_over == True:
       print(' game is over ')
       break
       

"""
print(game("a"))
print(game("b"))    
print(game("c"))    
print(game("a")) 
print(game("p"))    
print(game("e"))    
print(game("t"))    
print(game("e"))
print(game("h")) 
print(game("l"))  

"""