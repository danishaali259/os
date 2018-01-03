# Code For Round Robin


def arrival_time_initialize(arrival_time):
    arrival_time[0] = 0
    arrival_time[1] = 2
    arrival_time[2] = 3
    arrival_time[3] = 5
    arrival_time[4] = 9
...


def burst_time_initialize(burst_time):
    burst_time[0] = 3
    burst_time[1] = 8
    burst_time[2] = 4
    burst_time[3] = 2
    burst_time[4] = 5
...


def remaining_time_initialize(remaining_time):
    remaining_time[0] = 3
    remaining_time[1] = 8
    remaining_time[2] = 4
    remaining_time[3] = 2
    remaining_time[4] = 5
...


def running_process():

    remaining_process = 5
    process_no = 0
    waiting_time = 0
    process_time_in_cpu=0
    turn_around_time=0

    while remaining_process != 0:
        if remaining_time[process_no] < time_quantum or remaining_time[process_no] == time_quantum and remaining_time[ process_no] > 0:
            process_time_in_cpu += remaining_time[process_no]
            remaining_time[process_no] = 0
            flag = 1
        elif remaining_time[process_no] > 0:
            remaining_time[process_no] -= time_quantum
            process_time_in_cpu += time_quantum
        ...

        if remaining_time[process_no] == 0 and flag == 1:
            remaining_process = remaining_process - 1
            print(str("P") + str(process_no + 1) + '   \t\t \t  ' + str(process_time_in_cpu - arrival_time[process_no]) + '  \t  \t \t   ' + str(process_time_in_cpu - arrival_time[process_no] - burst_time[process_no]))
            waiting_time += process_time_in_cpu - arrival_time[process_no] - burst_time[process_no]
            turn_around_time += process_time_in_cpu - arrival_time[process_no]
            flag = 0

            if process_no == no_of_process - 1:
                process_no = 0
            elif arrival_time[process_no + 1] <= process_time_in_cpu:
                process_no = process_no + 1
            else:
                process_no = 0
            ...
    ...

    print(str("Average Waiting Time :") + '\t' + str(waiting_time / no_of_process))
    print(str("Average Turnaround Time :") + '\t' + str(turn_around_time / no_of_process))
...



# Main Body


no_of_process = 5
arrival_time = [None] * 5
burst_time = [None] * 5
remaining_time = [None] * 5
time_quantum = 2

arrival_time_initialize(arrival_time)
burst_time_initialize(burst_time)
remaining_time_initialize(remaining_time)
print(str("Processes") + '     ' + str("Turnaround Time") + '     ' + str("Waiting Time"))
running_process()
