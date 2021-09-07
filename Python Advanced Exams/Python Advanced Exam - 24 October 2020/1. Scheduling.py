clock_cycles = [int(el) for el in input().split(', ')]
job_index = int(input())
tasks_done = []
priority_task = 0
for clock_cycle in range(len(clock_cycles)):
    if clock_cycle == job_index:
        priority_task = clock_cycles[clock_cycle]
        break

clock_cycles.sort()
for clock_cycle in range(len(clock_cycles)):
    if clock_cycles[clock_cycle] <= priority_task:
        tasks_done.append(clock_cycles[clock_cycle])
        continue
    break

print(sum(tasks_done))