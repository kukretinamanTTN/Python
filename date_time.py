from datetime import date, timedelta

def datecount(start, step):

    #generator creation
    while True:

        yield start

        #alternative --> +2 days
        if step=="alternative":
            start += timedelta(days=2)
            
        #daily --> +1 days
        elif step=="daily":
            start += timedelta(days=1)

        #monthly --> +30,+31,+28 days
        elif step=="monthly":
           
           #for months with 31 days
           if start.month in {3,5,7,8,10,12}:
               start += timedelta(days=31)

            #for months with 30 days
           elif start.month in {2,4,6,9,11}:
               start += timedelta(days=30)

            #for month with 28 days
           else:
               start += timedelta(days=28)

        #weekly --> 1 week --> 7 days
        elif step=="weekly":
            start += timedelta(weeks=1)

    else:
        return "Invalid"

    
dc = datecount(start=date.today(), step="monthly")
for i in range(10):
    print(next(dc))