#Complete pig latin translator. Input=a word from the user. Output=The pig latin translation
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word=original.lower()
    first=original[0]
    new_word=word+first+pyg
    new_word=new_word[1:len(new_word)]
    print "the original word is " + original
    print "the Pig latin translation is " + new_word
else:
    print 'empty'
