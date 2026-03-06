# You are given a list of words.
#
# Return the k most frequent words.
#
# If two words have the same frequency, return them alphabetically.

# Example
# words = ["apple","banana","apple","orange","banana","apple"]
# k = 2

# Expected Output
# ["apple","banana"]

# Example 2
# words = ["i","love","coding","i","love","python"]
# k = 2

# Expected Output 2
# ["i","love"]

class TopFrequentWords:
    def get(self, words: [str], k: int) -> [str]:
        output = {}
        for w in words:
            if not output or not w in output:
                output[w] = 1
            else:
                output[w] +=1

        # -x[1] → frequency descending
        # x[0]  → alphabetical
        sorted_output = sorted(output.items(), key=lambda x: (-x[1], x[0]))

        return [word for word, count in sorted_output[:k]]


from collections import Counter

class TopFrequentWordsUsingCounter:
    def get(self, words: [str], k: int) -> [str]:
        output = Counter(words)

        # -x[1] → frequency descending
        # x[0]  → alphabetical
        sorted_output = sorted(output.items(), key=lambda x: (-x[1], x[0]))

        return [word for word, count in sorted_output[:k]]


words = ["apple","banana","apple","orange","banana","apple"]
k = 2

top_words = TopFrequentWordsUsingCounter()
print(top_words.get(words, k))

