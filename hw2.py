#copy the example text of lorem ipsum into a string 
lorem="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#split string into a list of words 
words= lorem.split()

#(in a single line) use dict comprehension to produce a dictionary in the format where the key is a (unique) word and the value is the number of times that word appears in the list 
#idea: dict={WORD HERE :list.count(WORD HERE) for NUMBER OF DISTINCT WORDS}
mydict={word: words.count(word) for word in words}


#calculate how many unique words appear in the text 
uniquewordcount=len(set(words))

print uniquewordcount
print mydict 

#using import Counter to count 
from collections import Counter 
counts= Counter(words)
print counts

#another way of doing this
uniqueWords = sorted(set(words)) #remove duplicate words and sort
for word in uniqueWords:
    print words.count(word), word

#more efficient algorithm is to step through each word in list but increment counter for a word each time it is encountered 
mydict2={}
for word in words:
    if word in mydict2:
    	mydict2[word]+=1
    else:
        mydict2.update({word:1})

print mydict2

#reading in file text and counting the occurrences of "found"
with open('myst.txt','r') as f: 
	fi = f.read()

gibber=fi.split()
#creating dictionary and printing (not most efficient)
mydict3={gib:gibber.count(gib) for gib in gibber}
print mydict3

#counting occurrences 
counter=0
for i in gibber:
		if "found" == i:
			counter+=1
print counter 
