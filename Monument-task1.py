import subprocess
import time

##In commands, you are given a list of commands to execute.
##Use Popen to execute all commands at the same time.
##When the execution of all commands are finished, display a report with,
##total elapsed time, average / maximum / minimum execution time among all commands.
##Remember that processes started with Popen must be poll()'ed to make sure that they're finished and terminated properly.

commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]

commands_len=len(commands)
print(commands)

def main():
    task1(commands)
    
#Task 1: execute, simaltenously, all commands of array commands, using popen
def task1(commands):
    'executes commands given in commands'
    #Tracks Total elapsed time
    #start1 = time.process_time()
    start2 = time.perf_counter()
    
    #list holds helperClass elements
    p=[]
    
    print("Popen Go!")
    #loop command_array.size times creating a process for each command
    for i in range (0,commands_len-1):
        #individual command process time counter variable 1
        process_start=time.perf_counter()
        process=(subprocess.Popen(commands[i],shell=True))
        
        ##create helperClass to store process, start time, and command name
        pListItem=helperClass(process,process_start,commands[i])
        
        ##call task1_helper1 function: it calls poll(), waits for p[i].process to finish and then takes time for total op time
        task1_helper1(pListItem)
        p.append(pListItem)
        
    #end1 = time.process_time()
    end2 = time.perf_counter()
    #print("total time (process_time) elapsed: {}".format((end1-start1)))
    print("total time (perf_counter) elapsed: {}".format((end2-start2)))
    output(p)
    
#task1_helper1 -- A function which takes as parameters pList: list of subprocesses and index: index of a specific subprocess
    #Calls poll to wait for index subprocess and calls time and calculates total execution time for process.
def task1_helper1(helper):
    sTime=helper.get_time()
    while helper.get_process().poll() is None:
        time.sleep(0.5)
    
    #individual command process time counter variable 2
    eTime=time.perf_counter()
    #reset helper.time, from start time, to be the total time for operation
    helper.set_time((eTime-sTime))

#expects as a parameter a list of helperCLass objects
#the output function which prints the total time of a subprocess and the name
    #also calculates min, max, and avg op times among commands
def output(process_list):
    min=100
    max=0
    avg=0
    total=0
    min_command=""
    max_command=""
    for helper in process_list:
        process_time=helper.get_time()
        print("command: '{}' -- Op-time: {}".format(helper.get_command(),process_time))

        ##calculations for min, max, avg process time among commands
        total+=process_time
        
        if(process_time<min):
            min=process_time
            min_command=helper.get_command()
        if(process_time>max):
            max=process_time
            max_command=helper.get_command()
    avg=total/commands_len+1
    print("Max: ('{}', {}) -- Min: ('{}',{}) -- Avg: {}".format(max_command,max,min_command,min,avg))
            
##helper class used to store in one object - subprocessses, start_time/total_time, and a command
class helperClass(object):
    'a helper class for task1'
    def __init__(self,process,start_time,command):
        'constructor'
        self.process=process
        self.time=start_time
        self.command=command

    def get_process(self):
        'returns process of helperclass'
        return self.process

    def get_time(self):
        'returns time parameter of helperclass'
        return self.time

    def get_command(self):
        'returns command parameter'
        return self.command
    
    def set_time(self,time):
        'sets time parameter of helperclass'
        self.time=time



if __name__ == "__main__":
   main()

    
