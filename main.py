import random
# ask how many times to run it
times = int(input("Test Data Size? "))
# askpo which bubble to stick to
bubble = str(input("What Bubble?\n"
                   "A,B,C,or D \n"))
#  making a second variable cause we change the value of bubble away from this
f = bubble
# total correct guesses that are random
totalcorrectguess = 0
# total correct guesses with the given "bubble"
totalcorrectbubble = 0
# number of times ran starting at one, because it outputs how many times its ran BEFORE this is added to
num = 1
# how many times in total its ran with the given or a static answer
staticran = 0
# how many times its ran with no given answer,dynamically assigning a random number each time very bad variable name i know
dynamicran = 0
# these 2 are defined cause of weird syntax
b = None
static = None

#  this is kind of intresting so its gonna take some explaing
# this is whats called a list
# you can refrence things from this list, by using the [] operator
# it starts at 0 and counts up, so theres 3 things in this list including 0
#  so a = index[1] where a would = B
#  and a = index[0] would equal A
# its called indexing and the name of the list is indexing, kinda confusing
index = ["A","B","C","D"]


#  this is whats called a function
# its some code that can be ran where nothing changes over and over
#  all it does is return back a number between 0 and 3 or 4 different numbers
def GetRand():
    rand = random.randint(0,3)
    return rand

#  so it takes the amount of times we want to run it, from above, and runs it twice as many times
#  one for the static answers and one for the random answers
for i in range(times * 2):
    # here were executing that function above
    a = GetRand()
    # heres where that tricky indexing comes in from abovem line 25
    a = index[a]
    # here we're printing out the current guess we're on
    print(f"Guess number:{num}")

    # times is the total amount of times we want to run it, and  num is how many we have ran it
    # so here whats happening is what half way through, its switching between guessing and the static answer given above
    # this is the main driving code that switches half way through
    # throughtout all, a is equal to a random number and on the buttom part, so is b
    # on the top is says if times is greater than num to set b to the bubbled answer and set static to true to tell us if
    # were no longer changing b
    if num < times:
        b = bubble
        static = True
    # here this is before half way, telling us to keep b a random number everytime this is checked
    elif num > times:
        b = GetRand()
        #  more indexing to change the given random number to match with the letter we gave above
        b = index[b]
        # keeping static false so we know that b isnt the same number each time
        static = False
    #  if they match
    if a == b:
        #  if static is set to true
        if static:
            # add one to the total correct bubbled so we can get the total decimal of correct
            totalcorrectbubble += 1
        else:
            # if static isnt true, and a and b still match, add one to the other
            totalcorrectguess += 1
    # here we have the current guess stats
    #  all thats changing between these two, its the grammar between random answer and your answer
    if static == False:
        dynamicran += 1
        print(f"Random Question = {a}\n"
              f"Random Answer = {b}\n")
    if static == True:
        staticran += 1
        print(f"Random Question = {a}\n"
              f"Your Answer = {b}\n")
    # finally we add to that num, so we can get the current guess we're on
    num += 1
# and here we refrence those variables from above and print them out so we can read them all nice
print(f"Test Over!\n"
      f"Heres the Stats!\n"
      f"Total Times Ran Of No Set Answer: {dynamicran}\n"
      f"Total Times Ran With Set Answer: {staticran}\n"
      f"Total Guesses Combined: {staticran + dynamicran}\n"
      # rounds the answer to the 5th place
      f"Total Correct Random Guesses: {totalcorrectguess}, With A Ratio Of: {round(totalcorrectguess / times,5)}\n"
      f"Total Correct Guesses Of {f}: {totalcorrectbubble}, With A Ratio Of: {round(totalcorrectbubble / times,5)}\n")
