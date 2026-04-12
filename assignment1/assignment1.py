# Write your code here

# Task 1
def hello():
    return("Hello!")

## print(hello())

# Task 2
def greet(name):
    return (f"Hello, {name}!")

## print(greet("Noor"))

# Task 3
def calc(a, b, c="multiply"):
    try:
        if c == "multiply":
            return(a * b)
        elif c == "add":
            return (a + b)
        elif c == "subtract":
            return(a - b)
        elif c == "divide":
            return(a/b)
        elif c == "int_divide":
            return(a//b)
        elif c == "modulo":
            return(a%b)
        elif  c == "power":
            return(a**b)
        else:
            return("Enter valid syntax!")
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return(f"You can't {c} those values!")
    except Exception as e:
        return(e)
        
## print(calc("1", "2", "multiply"))

# Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            result = int(value)
            return result
        elif data_type == "float":
            result = float(value)
            return result
        elif data_type == "str":
            result = str(value)
            return result    
        else:
            return(f"You can't convert {value} into a {data_type}.")       
    except Exception:
        return(f"You can't convert {value} into a {data_type}.")

## print(data_type_conversion(55.8, "int"))

# Task 5
def grade (*args):
    try:
        avg = sum(args)/len(args)
        if avg >= 90:
            result= "A"
            return result
        elif avg >= 80:
            result= "B"
            return result
        elif avg >= 70:
            result = "C"
            return result
        elif avg >= 60:
            result = "D"
            return result
        else:
            result = "F"
            return result
    except ZeroDivisionError:
        return("You can't divide by 0!")    
    except Exception:
        return("Invalid data was provided.")
## print(grade(79, 80, 76, 90, 85))

# Task 6
def repeat(word, count):
    repeated_word = ""
    for i in range(count):
        repeated_word += word
    return repeated_word

## print(repeat("Noor", 5))

# Task 7
def student_scores( option, **kwargs):
    if option == "best":
       highest_score = max(kwargs.values())
       for key, value in kwargs.items():
           if value == highest_score:
            return key 
    elif option == "mean":
         return round(sum(kwargs.values())/len(kwargs.values()), 2)
    else:
        return("Enter vilad option first")

## print(student_scores("best", joe=99, moh= 95, ali=98 ))
## print(student_scores("mean", joe=99, moh= 95, ali=98))        

# Task 8
def titleize(title):
    title_words = title.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result_words = []
    for index, word in enumerate(title_words):
        if index == 0 or index == len(title_words) -1: 
           result_words.append(word.capitalize())
        elif word.lower() in little_words:
            result_words.append(word.lower())
        else:
            result_words.append(word.capitalize())
    result_title = " ".join(result_words)
    return result_title

## print(titleize("harry potter And The sorcerer's stone"))

# Task 9
def hangman(secret, guess):
    secret_output = "" 
    for letter in secret:
        if letter in guess:
            secret_output += letter
        else:
            secret_output += "_"    
    return  secret_output
## print(hangman("alphabet" , "apht"))

# Task 10

def pig_latin(text):
    list_words = text.split()
    vowel_letters = "aeiou"
    result = []
    for word in (list_words):
        if word[0] in vowel_letters:
            result.append(word + "ay")
            continue
        elif word[:2] =="qu":
            result.append(word[2:] + word[:2]+ "ay")
            continue  
        elif word[:3] =="squ":
            result.append(word[3:] + word[:3] + "ay")
            continue
        for index, letter in enumerate(word):
          if letter in vowel_letters:
           result.append(word[index:] + word[:index] + "ay")
           break
        else:
         result.append(word + "ay")
    return " ".join(result)            
    
## print(pig_latin("apply emily smile noor quick quiet square"))  

