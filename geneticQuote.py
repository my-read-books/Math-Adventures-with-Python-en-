import random, string


random.seed()


target = "I never go back on my word, because that is my Ninja way."
characters = string.ascii_letters + ".,'?! "


def makeList():
    '''Returns a list of characters the same length
    as the target'''
    charList = [] #empty list to fill with random characters
    for i in range(len(target)):
        charList.append(random.choice(characters))
    return charList

def score(mylist):
    '''Returns one integer: the number of matches with target'''
    matches = 0
    for i in range(len(target)):
        if mylist[i] == target[i]:
            matches += 1
    return matches

def mutate(mylist):
    '''Returns mylist with one letter changed'''
    newlist = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0,len(target)-1)
    newlist[index] = new_letter
    return newlist

bestList = makeList()
bestScore = score(bestList)
guesses = 0


while True:
    guess  = mutate(bestList)
    guessScore = score(guess)
    guesses += 1
    if guessScore <= bestScore:
        continue
    print("".join(guess), str(round(guessScore / len(target) * 100, 2)) + " %", guesses)
    if guessScore == len(target):
        break

    bestList = list(guess)
    bestScore = guessScore
