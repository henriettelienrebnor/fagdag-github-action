import re

def is_haiku(commit_message: str) -> bool:
    string_list = commit_message.split(sep="-")
    haiku = False
    
    if len(string_list) != 3:
        return False

    for i in len(string_list):
        if count_syllables_in_line(string_list[i]) == 5:
            if i != 1:
                haiku = True
            else:
                return False
        
        elif count_syllables_in_line(string_list[i]) == 7 and i == 1:
            haiku = True

        else:
            return False
    
    return haiku

def count_syllables_in_line(line: str) -> int:
    words = line.split(" ")
    count = 0

    for word in words:
        count += count_syllables(word)
    
    return(count)


def count_syllables(word: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    #vowels
    for i in len(word):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1

        elif i == 0 and word[i] in vowels:
            count += 1
        
        #y
        elif word[i] == "y" and word[i-1] not in vowels:
            count += 1
        
        elif i == 0 and word[i] == "y":
            count += 1
    
    #silent e
    if word[-1] == "e":
        count -= 1

    #le or les endings
    if word.endswith("le") and word[-3] not in vowels:
        count += 1
    
    elif word.endswith("les") and word[-4] not in vowels:
        count += 1

    return(count)