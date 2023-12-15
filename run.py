import cli;
from multiprocessing import Process
import time

def call_cli1(n):
    cli.cli(n)
    
if __name__ == '__main__':
    starttime = time.time()
    print('----- start time ------')
    print(starttime)
    
    n1 = 1
    n2 = 0
    
    process1 = Process(target=call_cli1,args=(n1,))
    process2 = Process(target=call_cli1,args=(n2,))
    
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
    
    process1.close()
    process2.close()