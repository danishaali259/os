# code for Shortest Job First


def burst_time_initialize(burst_time):

    burst_time[0]=3
    burst_time[1]=2
    burst_time[2]=7
    burst_time[3]=5
...

def process_id_initialize(process_id):
    process_id[0]=1
    process_id[1]=2
    process_id[2]=3
    process_id[3]=4
...


def sorting_on_burst_time():
    for current_process in range(0,no_of_processes):
        process_to_run=current_process
        for next_process in range(current_process+1, no_of_processes):
            if(burst_time[next_process]<burst_time[process_to_run]):
                process_to_run=next_process
        ...
        temperary_varaible=burst_time[current_process]
        burst_time[current_process]=burst_time[process_to_run]
        burst_time[process_to_run]=temperary_varaible
        temperary_varaible=process_id[current_process]
        process_id[current_process]=process_id[process_to_run]
        process_id[process_to_run]=temperary_varaible
    ...
...


def calculating_waiting_time(average_waiting_time):
    waiting_time[0]=0
    total_waiting_time = 0
    for running_process_no in range(1,no_of_processes):
        waiting_time[running_process_no]=0
        for prevoius_process in range(0, running_process_no):
            waiting_time[running_process_no]+=burst_time[prevoius_process]
        ...
        total_waiting_time+=waiting_time[running_process_no]
    ...
    average_waiting_time=total_waiting_time/no_of_processes
    return average_waiting_time
...


def calculating_turnaround_time(average_turnaround_time):
    total_turnaround_time = 0
    for running_process_no in range(0, no_of_processes):
        turnaround_time[running_process_no]=burst_time[running_process_no]+waiting_time[running_process_no]
        total_turnaround_time+=turnaround_time[running_process_no]
        print(str("P")+str(process_id[running_process_no])+'\t\t\t\t'+str(burst_time[running_process_no])+'\t\t\t\t'+str(waiting_time[running_process_no])+'\t\t\t\t\t'+str(turnaround_time[running_process_no]))
    ...
    average_turnaround_time=total_turnaround_time/no_of_processes
    return average_turnaround_time
...



# Main Body

burst_time=[None]*4
waiting_time=[None]*4
turnaround_time=[None]*4
process_id=[None]*4
no_of_processes=4
average_waiting_time=0
average_turnaround_time=0
print("Process\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time")
burst_time_initialize(burst_time)
process_id_initialize(process_id)
sorting_on_burst_time()
calculating_waiting_time(average_waiting_time)
print(str("Average Turnaround Time : ")+str(calculating_turnaround_time(average_turnaround_time)))
print(str("Average Waiting Time : ")+str(calculating_waiting_time(average_waiting_time)))