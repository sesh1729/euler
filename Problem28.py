
##%debug
import time
start_time = time.time()
#Problem 480 in Euler
def getnextword(currentword,unique_letters_array,unique_letter_counts,maxletters):
    if currentword == "": 
        return "NoMoreWords"
    #print currentword
    nextword = currentword
    currentword_array =sorted(list(currentword))
    currentword_array_unique_letters = []
    currentword_array_letter_counts = [] 
    #print currentword
    for i in range(1,len(currentword_array)+1):
        if currentword_array[i-1] in currentword_array_unique_letters:
            currentword_array_letter_counts[currentword_array_unique_letters.index(currentword_array[i-1])] = currentword_array_letter_counts[currentword_array_unique_letters.index(currentword_array[i-1])] + 1
        else: 
            currentword_array_unique_letters.append(currentword_array[i-1])
            currentword_array_letter_counts.append(1)
    
    if len(currentword_array) < maxletters:
        for j in range(0,len(unique_letters_array)):
            if unique_letters_array[j] not in currentword_array_unique_letters \
                or currentword_array_letter_counts[currentword_array_unique_letters.index(unique_letters_array[j])] < unique_letter_counts[j]:
                nextword = currentword + unique_letters_array[j]
                break
    elif len(currentword_array) == maxletters:
        if unique_letters_array.index(list(currentword)[-1])+1 < len(unique_letters_array):
            for j in range(unique_letters_array.index(list(currentword)[-1])+1,len(unique_letters_array)):
                if unique_letters_array[j] not in currentword_array_unique_letters \
                    or currentword_array_letter_counts[currentword_array_unique_letters.index(unique_letters_array[j])] < unique_letter_counts[j]:
                    nextword = currentword[:-1] + unique_letters_array[j]
                    break
            if nextword == currentword:
                currentword = currentword[:-1]
                return getnextword(currentword,unique_letters_array,unique_letter_counts,maxletters-1)
        else: 
            currentword = currentword[:-1]
            return getnextword(currentword,unique_letters_array,unique_letter_counts,maxletters-1)
            
    return nextword

def findindex(searchword,knownword,knownindex,unique_letters_array,unique_letter_counts,maxletters):
    currentwordl = knownword
    currentindexl = knownindex
    nextwordl = ""
    while nextwordl != "NoMoreWords":
        nextwordl = getnextword(currentwordl,unique_letters_array,unique_letter_counts,maxletters)
        currentindexl = currentindexl + 1
        if nextwordl == searchword:
            return currentindexl
            break
    return 0

def NumWordsStartingWith(firstletter,unique_letters_array,unique_letter_counts,maxletters):
    local_letter_counts = unique_letter_counts
    local_letter_counts[unique_letters_array.index(firstletter)] = local_letter_counts[unique_letters_array.index(firstletter)] - 1
    if maxletters == 1:
        return 1
    total_words = 1
    for i in range(0,len(unique_letters_array)):
        localmaxletters = maxletters - 1        
        #print total_words,firstletter, unique_letters_array[i], unique_letter_counts, local_letter_counts, localmaxletters
        if local_letter_counts[i] > 0:
            total_words = total_words + \
                NumWordsStartingWith(unique_letters_array[i],unique_letters_array,local_letter_counts,localmaxletters)
            local_letter_counts[i] = local_letter_counts[i] + 1
    return total_words

test_string = "thereisasyetinsufficientdataforameaningfulanswer"
#test_string = "abcd"
test_array = sorted(list(test_string))

test_array_unique_letters = []
test_array_letter_counts = [] 
for i in range(1,len(test_array)+1):
    if test_array[i-1] in test_array_unique_letters:
        test_array_letter_counts[test_array_unique_letters.index(test_array[i-1])] = \
            test_array_letter_counts[test_array_unique_letters.index(test_array[i-1])] + 1
    else: 
        test_array_unique_letters.append(test_array[i-1])
        test_array_letter_counts.append(1)

#for i in range(0,len(test_array_unique_letters)):
#    print test_array_unique_letters[i], test_array_letter_counts[i]
        
#alphalist= ["a"]
#currentword = "a"
#nextword = ""

#while nextword != "NoMoreWords":
#    nextword = getnextword(currentword,test_array_unique_letters,test_array_letter_counts,3)
#   alphalist.append(nextword)
#    currentword = nextword
#    i = i+1

#for i in range(0,len(alphalist)):
#    print i+1, alphalist[i]

#print getnextword(currentword,test_array_unique_letters,test_array_letter_counts,2)
#searchword = "euler"
#print "index of ", searchword , "is ",  findindex(searchword,"a",1,test_array_unique_letters,test_array_letter_counts,15)

print NumWordsStartingWith("c",test_array_unique_letters,test_array_letter_counts,6)

print time.time() - start_time

