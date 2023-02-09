def max_words(sentences):
    max_words=0
    for sentence in sentences:
        words=sentence.split()
        print(words)
        max_words=max(max_words,len(words))
    return max_words
sentences=input("enter the sentences seperated by comma:").split(',')
print(sentences)
print("maximum number of words in a sentence:",max_words(sentences))    
