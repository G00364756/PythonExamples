#Test for Tuesday app - 06/02/2018
#To try to emmulate the code given by Dr. McGloughlin in week 3 of course

import datetime

if datetime.datetime.today().weekday() == 1:
    print("Yay it is Tuesday!")
else:
    print("Boo, it's not Tuesday")