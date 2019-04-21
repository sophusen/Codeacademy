original=raw_input("Enter a word in English:")
if len(original)>0:
    if original.isalpha():
        print(original)
    else:
        print "only letters allowed"
else:
    print("No characters detected")
