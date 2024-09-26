#multiple inputs from argument

import sys

if len(sys.argv)<2:
    sys.exit("Two few arg")


#sys.argv[1:] this syntax starts taking
# argumet from position "1 OR ONE" 

for arg in sys.argv[1:]: 
    print("Hello, ",arg)
    
