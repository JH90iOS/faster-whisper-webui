import cli;
from multiprocessing import Process
import time

def call_cli1(n):
    cli(n)
    
if __name__ == '__main__':
    starttime = time.time()
    print('----- start time ------')
    print(starttime)
    
    process1 = Process(target=call_cli1,args=(1))
    process2 = Process(target=call_cli1,args=(2))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()

    endtime = time.time()
    print('----- end time ------')
    print(endtime)
    drt=endtime-starttime
    print('------ total duration ------')
    print(drt)