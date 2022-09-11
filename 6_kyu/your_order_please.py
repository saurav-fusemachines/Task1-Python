def order(sentence):
    dict = {}
    list = []
    sentence_split = sentence.split(" ")
    for item in sentence_split:
        for char in item:
            a_code = ord(char)
            if a_code >= ord("0") and a_code <= ord("9"): 
                dict[char] = sentence_split.index(item)
                list.append(a_code - ord("0"))
                break
    list.sort()

    res = []
    for i in list:
        res.append(sentence_split[dict[str(i)]])
          
    return " ".join(item for item in res)



# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# def order(sentence):
#     if not sentence:
#         return ""
#     result = []    #the list that will eventually become our setence
      
#     split_up = sentence.split() #the original sentence turned into a list
  
#     for i in range(1,10):
#         for item in split_up:
#             if str(i) in item:
#                  result.append(item)    #adds them in numerical order since it cycles through i first
  
#     return " ".join(result)