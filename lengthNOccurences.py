def len_occ(str):

    words = str.split()

    word_dict = {}

    for word in words:
        if word in word_dict: 
            word_dict[word]+=1
        else: 
            word_dict[word]=1

    word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]))

    print("Word\t\tLength\t\tOccurences")
    
    for key in word_dict:
        if word_dict[key]>1:
            print(key,"\t\t", len(key), "\t\t", word_dict[key])

abc = '''Python Multiline String Using Triple-Quotes
Using the triple quotes style is one of the easiest and most common ways to split a large string into a multiline Python string. 
Triple quotes can be used to create a multiline string. 
It allows you to format text over many lines and include line breaks. 
Put two triple quotes around the multiline Python string, one at the start and one at the end, to define it.
'''

len_occ(abc)