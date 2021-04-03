import pandas as pd         # To read csv file pandas has been imported
 
import sys                  # sys is imported to read Command line arguments


command_line_arguments = sys.argv   # reading command line arguments

#dictionary = pd.read_csv(command_line_arguments[1], header = None) 
#word = command_line_arguments[2]
#the first argument @ index 0 is script name itself, @ index 1 is csv file's name and @ index 2 is the word 

dictionary = pd.read_csv('dictionary.csv', header = None)  
word = 'hellp'

# This program uses the concept of Levenshtein Distance to suggest the correct words in order.

def levenshtein_distance(s, t): 
    if s == "":                             # if first string is empty
        return len(t)
    if t == "":                             # if last string is empty
        return len(s)
    if s[-1] == t[-1]:                      # calculation
        cost = 0
    else:
        cost = 1
       
    res = min([levenshtein_distance(s[:-1], t)+1,
               levenshtein_distance(s, t[:-1])+1, 
               levenshtein_distance(s[:-1], t[:-1]) + cost])            # recusive calls

    return res

wordlist = list(dictionary.iloc[:,0])           # extracting list of words from the given dictionary
dict2 = {}

for words in wordlist:
    val = levenshtein_distance(words,word)      # calculating levenshtein distance
    dict2[words] = val
    
dict2 = dict(sorted(dict2.items(), key=lambda item: item[1]))       # arranging on the basis of levenshtein distance

oplist = list(dict2.keys())                     # getting final order of correct spellings

for i in range(len(oplist) - 1):                # printing results
    print(oplist[i], end = ", ")                
print(oplist[len(oplist)-1],end="") 