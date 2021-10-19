a = 4487
b = 9450
result = 0 #It will start on 0 until its iterated

#Since we have to work from a to b a range would be best, remember to add 1 so b its included
# x its any value in the range given. keep using x for our conditions!
for x in range(a,b + 1):
    # Since the problem ask odd numbers (impar) when divided by two they should have a different value from zero.
    if x % 2 != 0: 
        #Every iteration the value x will be added to previous result same equation as "result = result + x"
        result += x 
print(result)