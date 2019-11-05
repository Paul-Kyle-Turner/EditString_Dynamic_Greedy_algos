import numpy as np


# x and y should be lists of symbols
def longest_common_subsequence(x, y):
    m = len(x)
    n = len(y)
    b = np.ndarray((m, n), dtype=object)
    c = np.zeros((m + 1, n + 1))
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i - 1, j - 1] = 'diag'  # "diag"
            elif c[i, j - 1] >= c[i - 1, j]:
                c[i, j] = c[i, j - 1]
                b[i - 1, j - 1] = 'left'  # "up"
            else:
                c[i, j] = c[i - 1, j]
                b[i - 1, j - 1] = 'up'  # "left"
    return c, b


def longest_subsequence(a):
    n = len(a)
    d = [1] * n
    index_list = [0] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                index_list[i] = j
    amount_left = 0
    starting_index = 0
    for i in range(n):
        if d[i] > amount_left:
            amount_left = d[i]
            starting_index = i
    return index_list, amount_left, starting_index


def print_ls_recursive(p, amount_left, index, a):
    if amount_left == 0:
        return
    else:
        print([a[index]])
        print_ls_recursive(p, amount_left - 1, p[index], a)


def print_lcs_recursive(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i, j] == 1:  # diag
        print_lcs_recursive(b, x, i - 1, j - 1)
        print(x[i])
    elif b[i, j] == 2:  # up
        print_lcs_recursive(b, x, i - 1, j)
    else:
        print_lcs_recursive(b, x, i, j - 1)


def print_lcs_iterative(b, x):
    i = np.size(b, 0)
    j = np.size(b, 1)
    sequence = []
    while i != 0 and j != 0:
        if b[i - 1, j - 1] == 'diag':  # diag
            i -= 1
            j -= 1
            sequence.append(x[i])
        elif b[i - 1, j - 1] == 'up':  # up
            i -= 1
        else:
            j -= 1
    return sequence[::-1]


def insertion_sort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        k = i - 1
        while k >= 0 and key < ar[k]:
            ar[k + 1] = ar[k]
            k -= 1
        ar[k + 1] = key
    return ar


# a is a sorted list
# a1 is a mandatory start to the intervals
# if a number ai is greater than the start of the last interval end, start a new interval
# once all of the n digits have been tested end the loop
# return the list of interval starts, by which each interval is [intervals[i], intervals[i] + 1]
def smallest_closed_interval_set(a):
    n = len(a)
    intervals = [a[0]]
    starting_interval = a[0]
    for i in range(1, n):
        if a[i] > starting_interval + 1:
            intervals.append(a[i])
            starting_interval = a[i]
    return intervals


if __name__ == '__main__':
    x = [1,1,5,2,0,35,21,1,2,1,2,4,0,1,4,5,1,2,5,1,3,13,1,34,21,125]
    index_list, amount_left, starting_index = longest_subsequence(x)
    print(index_list)
    print_ls_recursive(index_list, amount_left, starting_index, x)

