# code for Proirity Algorithem



def id_initializing():
    process_id[0]=1
    process_id[1]=2
    process_id[2]=3
    process_id[3]=4
...


def burst_time_initializing():
    burst_time[0]=3
    burst_time[1]=2
    burst_time[2]=6
    burst_time[3]=5
...


def proirity_intitializing():
    process_proirity[0]=3
    process_proirity[1]=1
    process_proirity[2]=4
    process_proirity[3]=2
...


def sorting_processes_by_proirity():
    for current_process in range(0, no_of_processes):
        process_to_run=current_process
        for next_process in range(current_process+1, no_of_processes):
            if(process_proirity[next_process]<process_proirity[process_to_run]):
                process_to_run=next_process
        ...
        swapping_variable=process_proirity[current_process]
        process_proirity[current_process]=process_proirity[process_to_run]
        process_proirity[process_to_run]=swapping_variable
        swapping_variable=burst_time[current_process]
        burst_time[current_process]=burst_time[process_to_run]
        burst_time[process_to_run]=swapping_variable
        swapping_variable=process_id[current_process]
        process_id[current_process]=process_id[process_to_run]
        process_id[process_to_run]=swapping_variable
    ...
...



def calculating_waiting_time():
    waiting_time[0]=0
    total_waiting_time=0
    for current_process in range(1, no_of_processes):
        waiting_time[current_process]=0
        for previous_process in range(0, current_process):
            waiting_time[current_process]+=burst_time[previous_process]
        ...
        total_waiting_time+=waiting_time[current_process]
    ...
    average_waiting_time=total_waiting_time/no_of_processes
    return average_waiting_time
...



def calculating_turnaround_time():
    total_waiting_time=0
    total_turnaround_time=0
    for current_process in range(0,no_of_processes):
        turnaround_time[current_process]=burst_time[current_process]+waiting_time[current_process]
        total_turnaround_time+=turnaround_time[current_process]
        print(str("P")+str(process_id[current_process])+'\t\t\t\t'+str(burst_time[current_process])+'\t\t\t\t'+str(waiting_time[current_process])+'\t\t\t\t\t'+str(turnaround_time[current_process]))
    ...
    average_turnaround_time=total_turnaround_time/no_of_processes
    return average_turnaround_time
...



#Main Body

burst_time=[None]*4
process_id=[None]*4
waiting_time=[None]*4
turnaround_time=[None]*4
process_proirity=[None]*4
no_of_processes=4

id_initializing()
burst_time_initializing()
proirity_intitializing()
sorting_processes_by_proirity()
calculating_waiting_time()
print(str("Process\t\t")+str("Burst Time\t\t")+str("Waiting Time\t\t")+str("Turnaround Time"))
print(str("Average Turnaround Time : ")+str(calculating_turnaround_time()))
print(str("Average Waiting Time : ")+str(calculating_waiting_time()))