"""
The start, we will generate a random interger between 1 and 20, and 
baded on the result of the random number we check to see if it falls under certain range 
if the number is greater than 15, then the result will be "Cherries"
otherwiths if number is >10, then the result will be "Orange"
oterwise if number is > 5, then the result willl be "plum"
othewiths if the numbes is >2, then the result will be "melon"
otherwise if the number is > 1, then the result will be "bar"

we iterate over using a loop three times and print the reults to the user. As an example "Plum cherries Melon"

"""
"""
import random 
num = generate random number

if num is greter thans 15, 
    then the result will be ""
Otherwise if num is greter thans 10, 
    then the result will be ""
Otherwise if num is greter thans 5, 
    then the result will be ""
Otherwise if num is greter thans 2, 
    then the result will be ""
Otherwise if num is greter thans 1, 
    then the result will be ""

loop three times
    print the output (fret) to the user
"""
def main():
    results = []
    for i in range (0,3):
        results.append(spin())

print("results", results) 
winner = jackpot(results)

if(winner):
    print("Winner! you win")
else:
    print("sorry try again")

option = input("play agian?")
if option.lower() == "y" or option.lower() == "yes"
 main()

def spin():
    rand_num = random. randint(1, 20)
    output = ""
    if (rand_num > 15):
        output cherries
    elif (rand_num >10):
        output = "Orange"
    elif (rand_num >5 ) :
        output = "plum"
    elif (rand_num > 2) :
        output= "Melon"
    else:
        output = "Bar"

def jackpot(results):
    return results[0] == resluts[1] == results[2]

def count(resluts):
    mone dict = {
        "Cherries" : 1, 
        "Orange" : .7,
        "Plum" : .6,
        "Bell" : .4, 
        "Melon" :  .2, 
        "Bar" : .1
    }

    for i in resuls: 
        total += money_dict[i]
    print("total:", total)
    return total_earned += toral 
main()