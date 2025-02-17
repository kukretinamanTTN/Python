
#open number.txt in read mode
with open('number.txt', 'r') as numbers:

    #extracting all numbers into a list
    num_list = [float(number.strip()) for number in numbers]

    # print(num_list)
    for i in num_list:

        #condition for number being integer
        if i == int(i):

            #condition for integer being even
            if i%2 == 0:
                with open('even.txt','a') as evens:
                    evens.write(str(int(i)))
                    evens.write('\n')

            #condition for integer being odd
            else:
                with open('odd.txt','a') as odds:
                    odds.write(str(int(i)))
                    odds.write('\n')

        #condition for number having decimal
        else:
            with open('float.txt','a') as floats:
                floats.write(str(i))
                floats.write('\n')