# Pattern: dictionary / hashmap

# Problem
# -> Given a list of words, return the top K most frequent words.

# example
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# k = 2

# output
# ["apple", "banana"]

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
k = 2

# First, I count occurrences using a dictionary which takes O(n).
output = []
counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else :
        counter[word] = 1

# Then I sort the results by frequency which is O(m log m) where m is the number of unique words.
sorted = sorted(counter.items(), key=lambda x :x[1], reverse= True)

top_k = sorted[:k]

output = [word for word, count in top_k]

print(output)

# this could be done using Collections too, have a look later.