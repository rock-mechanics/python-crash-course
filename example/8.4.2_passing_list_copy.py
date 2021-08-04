#!/usr/bin/env python3

task_list = ['c', 'python', 'go', 'ruby']

completed = []

def finish_task(tasks, completed) : 
    while tasks : 
        task = tasks.pop()
        print('finish task : {}.' .format(task))
        completed.append(task)

finish_task(task_list[:], completed)

# task_list is unmodifed
print('original tasks are {}'.format(task_list))
print('completed tasks are {}'.format(completed))

