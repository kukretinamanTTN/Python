def even_vowels(str):

    words = str.split()

    for i in words:
        count = 0

        for char in i:
            if char in 'aeiouAEIOU':
                count += 1
                
        if count>0 and count%2 == 0:
            print(i)


even_vowels('Hi My name is Naman')