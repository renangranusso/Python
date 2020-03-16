'''Create a program, to run a loop for 1 minute'''


#loop for 1 minute in python

from datetime import datetime
from datetime import timedelta

#Define the time where loop must stop, im the example i Use 60 seconds (1 minute)

temp_final = datetime.now() + timedelta(seconds=60)

#define the inicial time for the loop

temp_start = datetime.now()

while (temp_start <= temp_final):
    print(temp_start)
    temp_start = datetime.now()
    
#While temp_inicial <= temp_final
