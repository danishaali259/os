# code for FCFS


def burst_time_initialize(burst_time):
    burst_time[0]=4
    burst_time[1]=3
    burst_time[2]=7
    burst_time[3]=9
...

def calculating_waiting_time():
    waiting_time[0]=0
    for process_no in range(1, no_of_processes):
        waiting_time[process_no]=0
        for running_process in range(0, process_no):
            waiting_time[process_no]+=burst_time[running_process]
        ...
    ...
...

def times_of_every_process():
    for process_no in range(0, no_of_processes):
        turnaround_time[process_no]=burst_time[process_no]+waiting_time[process_no]
        print(str("P")+str(process_no+1)+'\t\t\t\t'+str(burst_time[process_no])+'\t\t\t\t'+str(waiting_time[process_no])+'\t\t\t\t\t'+str(turnaround_time[process_no]))
    ...
...


def average_waiting_time_of_process(average_waiting_time):
    for process_no in range(0, no_of_processes):
        turnaround_time[process_no]=burst_time[process_no]+waiting_time[process_no]
        average_waiting_time+=waiting_time[process_no]
    ...
    average_waiting_time = average_waiting_time / no_of_processes
    return average_waiting_time
...



def average_turnaround_time_of_process(average_turnaround_time ):
    for process_no in range(0, no_of_processes):
        average_turnaround_time+=turnaround_time[process_no]
    ...
    average_turnaround_time=average_turnaround_time/no_of_processes
    return average_turnaround_time
...




#Main Body


burst_time=[None]*4
waiting_time=[None]*4
turnaround_time=[None]*4
average_waiting_time=0
average_turnaround_time=0
process_no=0
running_process=0
no_of_processes=4

burst_time_initialize(burst_time)
calculating_waiting_time()

print("Process\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time")
times_of_every_process()
print(str("Average Waiting Time : ")+str(average_waiting_time_of_process(average_waiting_time)))
print(str("Average Turnaround Time : ")+str(average_turnaround_time_of_process(average_turnaround_time)))
