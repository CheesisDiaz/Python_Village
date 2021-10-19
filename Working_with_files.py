from os import linesep


#This first line of code is to open the file with the data. In this case a directory its not neccessary as the text is on the same folder as the code
f = open('rosalind_workingwithfiles.txt')
#We start with one to consider all the lines (indexing doesn't work the same as in lists)
i = 1
#for each line on the file being read the condition is if the number is even the line will be printed
for line in f.readlines():
    if i % 2 == 0:
        print(line)
    #This is to continue to the next line of the text
    i += 1
