import time
import random
from generator import InputGenerator
from algorithm import merge_sort


def calculate_effort(arr):
    effort_sum = 0
    for e in arr:
        effort_sum += e.effort
    return effort_sum


def run_experiment(input_size):
    input = InputGenerator(input_size)
    arr = input()
    # start timer
    start_time = time.time()
    # run algorithm
    merge_sort(arr, 0, input_size - 1)

    # time in seconds
    final_time = time.time() - start_time
    # quatity of comparisons
    effort = calculate_effort(arr)

    return final_time, effort


# Initialize random seed for result reproducibility
random.seed(42)

input_sizes = [10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]
repeat = 100
for input_size in input_sizes:
    mean_final_time = 0.0
    mean_effort = 0.0
    for i in range(repeat):
        final_time, effort = run_experiment(input_size)
        mean_final_time += final_time
        mean_effort += effort

    mean_final_time /= repeat
    mean_effort /= repeat
    print('----{input_size}----'.format(input_size=input_size))
    print('Time - {final_time} s'.format(final_time=mean_final_time))
    print('Comparisons quantity - {effort}'.format(effort=mean_effort))
