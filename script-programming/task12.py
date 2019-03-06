string=raw_input("Write some words: ")

def vowels(word):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    num=0
    for x in word:
        for item in vowels:
            if item == x:
                num+=1
    return num

print(vowels(string)) # prints: 3
