def finder(words, letters):
    result = []
    for i in words:
        if i in letters:
                result.append(i)
                letters = letters.replace(i,"")
    return result 


def main():
    words1 = ["list", "of", "wall", "words"]
    letters1 = "listofstoneletters"
    words2 = ["and", "do", "like", "for", "us", "of", "part", "can", "have", "view"]
    letters2 = "youcanhavepart"
    letters3 = "aaacehnoprtuvy"
    letters4 = "andcancanforfor"
    letters5 = "aabcdeefghiijklmnoopqrstuuvwxyz"

    words3 = ["abc", "a", "b", "c"]
    letters6 = "abc"
    
    print(finder(words1, letters1))     
    print(finder(words2, letters3))  
    print(finder(words2, letters4)) 
    print(finder(words2, letters5)) 
    print(finder(words3, letters6)) 


main()