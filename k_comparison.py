import random
import time
import algorithms


def random_list(n):
    randlist = []
    for i in range(n):
        randlist.append(random.randrange(2, n * 2, 2))
    return randlist


def linear_speed(k, n):
    temp = random_list(n)  # generate a random list to test the speed on
    k_vals = []  # create an array to store the values of k

    for j in range(k):  # generate values of k with half of the values not in the list and the other half not
        if j + 1 > k // 2:
            k_vals.append(random.randrange(1, n * 2, 2))
        else:
            k_vals.append(random.choice(temp))

    start = time.time()  # begin timer
    for r in range(len(k_vals)):  # for loop to run the search on every value in k_vals
        linear = algorithms.linear_search(temp, k_vals[r])
    end = time.time()  # end timer
    return end - start  # return time took to execute linear search of k values


def binary_speed(k, n):
    temp = random_list(n)  # generate a random list to test the speed on
    k_vals = []  # create an array to store the values of k

    for i in range(k):  # generate values of k with half of the values not in the list and the other half not
        if i + 1 > k // 2:
            k_vals.append(random.randrange(1, n * 2, 2))
        else:
            k_vals.append(random.choice(temp))

    start = time.time()  # begin timer
    algorithms.merge_sort(temp)  # sort the list once
    for s in range(len(k_vals)):  # for loop to run the search on every value in k_vals
        binary = algorithms.binary_search(temp, k_vals[s])
    end = time.time()  # end timer
    return end - start  # return time took to execute binary search of k values


def smallest_k(n):
    k = 10
    flag = False
    while not flag:  # keep adding k until binary search is faster
        k = k + 1
        if binary_speed(k, n) < linear_speed(k, n):
            flag = True
            return "n = " + str(n) + ": smallest k where binary beats linear: " + str(k)  # return smallest k
        else:  # linear still faster, check for next k
            k = k + 1
