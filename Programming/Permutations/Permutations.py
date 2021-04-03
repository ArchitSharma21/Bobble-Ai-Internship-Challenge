import pandas            # To read csv file pandas has been imported
 
import sys               # sys is imported to read Command line arguments
 
command_line_argument = sys.argv   # reading command line arguments


inputfile = pandas.read_csv(command_line_argument[1], header = None) 
#the first argument @ index 0 is script name itself and @ index 1 is csv file's name
#inputfile = pandas.read_csv('input.csv', header = None)   #used for checking purpose 
 
inputfile = inputfile.fillna('na')         # filling NULL values with 'na'
 
def permutation(n):              
    if n>=inputfile.shape[0]:
        emptyl=[""]
        return emptyl
    rec_call = permutation(n+1)            # recursive calls 
    answer=[str(i) + str(j) for i in inputfile.iloc[n] for j in rec_call if i != 'na' and j != 'na']
    return answer
 
 
result = permutation(0)                  # Calling The function 
 
 
for i in range(len(result)-1):           # Printing the result
    print(result[i],end=", ")            # printing n-1 terms
print(result[len(result)-1],end="")      # printing last term