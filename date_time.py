from datetime import date
from dateutil.relativedelta import relativedelta

def datecount(start, step):

    #generator creation
    while True:

        yield start
        
        #alternative --> +2 days
        if step=="alternative":
            start += relativedelta(days=2)
            
        #daily --> +1 days
        elif step=="daily":
            start += relativedelta(days=1)

        #monthly --> +30,+31,+28 days
        elif step=="monthly":
            start += relativedelta(months=1)

        #weekly --> 1 week --> 7 days
        elif step=="weekly":
            start += relativedelta(weeks=1)


dc = datecount(start=date.today(), step="alternative")
for i in range(10):
   print(next(dc))