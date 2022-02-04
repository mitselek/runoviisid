import datetime
import numpy as np


start_time = datetime.datetime.now()
for i in range(0,1000000):
    size = 100
    b = [v/4 for v in range(4,16)]
    a = (b * (size // len(b) + 1))[:size]
end_time = datetime.datetime.now()
print(end_time - start_time)

start_time = datetime.datetime.now()
for i in range(0,1000000):
    a = np.empty(100)
    filler = np.arange(1,4,0.25)
    index = np.arange(a.size)
    np.put(a,index,filler)
end_time = datetime.datetime.now()
print(end_time - start_time)