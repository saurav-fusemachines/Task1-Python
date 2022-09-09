# def reverse_words(text):
#     words = text.split()
#     new_words = list(reversed(words))
#     new_sentence =[i[::-1] for i in new_words]
#     print(" ".join(new_sentence))

# reverse_words("This is an example!")
# reverse_words("apple")    

def reverse_words(text):
    words = text.split(" ")
    
    reversed_words = []
  
    for word in words:
        reversed_words.append(word[len(word)::-1])
    return " ".join(reversed_words)
        

reverse_words("This is an example!")
reverse_words("apple")    
reverse_words('a b c d')
reverse_words('The quick brown fox jumps over the lazy dog.')




