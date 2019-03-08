sentence = "You are so close , - but I am thinking of the problem"
word_list=sentence.split()

def longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if (len(longest_word) < len(word)):
            longest_word = word
    return longest_word

print(longest_word(word_list))



