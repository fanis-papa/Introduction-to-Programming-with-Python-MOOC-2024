# Write your solution here

def no_shouting(words_list: list) -> list:
    only_lowers = []

    for i in words_list:
        if i.isupper():
            continue
        only_lowers.append(i)
        
    return only_lowers

  



if __name__ == "__main__":
    no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"])