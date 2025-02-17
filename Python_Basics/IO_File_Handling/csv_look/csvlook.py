import sys
#function to parse input

def parser(ip):
    #initializing
    lines=[]
    filepath=""
    delimiter="\t"
    quotechar='"'
    skiprows=0
    unique_columns=set()
    head=0
    tail=0

    #input split
    # ip = ip.split(' ')

    #if first word is 'csvlook', filepath to be the last
    if "csvlook" in ip:
        
        filepath=ip[len(ip)-1]

        # sys.exit()
        #if delimiter present, setting delimiter
        if "-d" in ip:
            delimiter = ip[ip.index("-d")+1]

        #if quotechar present, setting quotechar
        if "-q" in ip:
            quotechar = ip[ip.index("-q")+1]

        #if unique column values to be extracted
        if "-f" in ip:
            number= ip[ip.index("-f")+1]
            number=number.split(",")
            for num in number:
                unique_columns.add(int(num))

        #if rows to be skipped
        if "--skip-row" in ip:
            skiprows= int(ip[ip.index("--skip-row")+1])

        #if head to be displayed
        if "--head" in ip:
            head= int(ip[ip.index("--head")+1])

        #if tail to be displayed
        if "--tail" in ip:
            tail= int(ip[ip.index("--tail")+1])

        #appending lines of the file into a list
        with open(filepath,'r') as file:
            for line in file:
                lines.append(line)

        #start and stop pointer
        start=0
        stop=len(lines)

        #id rows to skip, shift start forward
        if int(skiprows)>0:
            start+=skiprows

        #if head needed, shift stop backward
        if int(head)>0:
            stop=head

        #if tail needed, shift start to tail-start
        if int(tail)>0:
            start= stop - tail

        #looping from start to stop
        for i in range(start,stop):
            
            #splitting words from lines
            result=lines[i].strip().split(",")
            
            #if unique columns needed
            if len(unique_columns)!=0:
                for words in unique_columns:
                    print(quotechar+"".join(result[words])+quotechar, end=f'{delimiter}')

            #if range of columns needed
            else:
                for word in result:
                    print(quotechar+"".join(word)+quotechar, end=f'{delimiter}')
            print()
    else:
        sys.exit()

#Taking command line input from user
parser(sys.argv)