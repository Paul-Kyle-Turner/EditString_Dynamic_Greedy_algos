import numpy as np
import sys

# BRUTE FORCE
# this does not give a min
# this does however run at a linear time
def edit_string_naive(a, b):
    z = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < n or j < m:
        if i >= m:
            z.append('I')
            i += 1
            j += 1
        elif j >= n:
            z.append('D')
            i += 1
            j += 1
        elif a[i] == b[i]:
            z.append('C')
            i += 1
            j += 1
        elif i + 1 > n and a[i] == b[i+1] and a[i+1] == b[i]:
            z.append('T')
            i += 2
            j += 2
        else:
            z.append('R')
            i += 1
            j += 1
    return z


# THIS ALGORITHM ASSUMES COPY WILL ALWAYS BE SMALLEST
# this algorithm runs at a O(nm) time
def edit_string_iterative(x, y, copy_cost=0, delete_cost=1, insert_cost=1, twiddl_cost=1, replace_cost=1):
    n = len(y) + 1
    m = len(x) + 1
    c = np.zeros((m, n))
    z = np.ndarray((m, n), dtype=object)
    for i in range(m):
        c[i][0] = i * delete_cost
        z[i][0] = 'd'
    for j in range(n):
        c[0][j] = j * insert_cost
        z[0][j] = 'i'
    z[0][0] = 'end'
    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:  # copy
                c[i][j] = c[i - 1][j - 1] + copy_cost
                z[i][j] = 'c'
            elif x[i - 1] != y[j - 1]:  # NOT EQUAL CHECK ALL 4 CLOSEST VALUES AND
                if c[i - 1][j] < c[i-1][j-1] and c[i - 1][j] < c[i][j - 1]:  # delete
                    c[i][j] = c[i - 1][j] + delete_cost
                    z[i][j] = 'd'
                elif c[i][j - 1] < c[i - 1][j - 1] and c[i][j - 1] < c[i - 1][j]:  # insert
                    c[i][j] = c[i][j - 1] + insert_cost
                    z[i][j] = 'i'
                elif i >= 2 and j >= 2 and x[i - 1] == y[j - 2] and y[j - 1] == x[i - 2]:  # twiddle
                    c[i][j] = c[i - 2][j - 2] + twiddl_cost
                    z[i][j] = 't'
                else:
                    c[i][j] = c[i - 1][j - 1] + replace_cost
                    z[i][j] = 'r'
    return c, z


def opt_string_change(c, z):
    b = list()
    start = c.shape
    something = z.shape
    print(start)
    print(something)
    i = start[0] - 1
    j = start[1] - 1
    while i > 0 and j > 0:
        b.append(z[i][j])
        # copy or replace
        if z[i][j] == 'c' or z[i][j] == 'r':
            i -= 1
            j -= 1
        # twiddle
        elif z[i][j] == 't':
            i -= 2
            j -= 2
        # up
        elif z[i][j] == 'd':
            i -= 1
        # left
        else:
            j -= 1
    return b[::-1]


if __name__ == '__main__':
    np.set_printoptions(threshold=sys.maxsize)

    rowan = list('rowan')
    rowana = list('rowana')
    romance = list('romance')
    rowantimestory = list('rowantimestory')
    romanticstory = list('romanticstory')
    myrowanuniversity = list('myrowanuniversity')
    rowanuniversitymy = list('ROWANUNIVERSITYMY'.lower())
    bacon = list('bacon')
    steakon = list('steakon')
    repair = list('repair')
    ressair = list('ressair')
    tacos = list('tacos')
    french = list('french')

    all_strings = [rowan, rowana, romance, rowantimestory, romanticstory, myrowanuniversity, rowanuniversitymy,
                   bacon, steakon, repair, ressair, tacos, french]

    with open('output.txt', 'w+') as file:
        c, z = edit_string_iterative(rowan, rowana)
        b = opt_string_change(c, z)
        file.write(f'First string {rowan}, Second string {rowana}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(rowana, rowan)
        b = opt_string_change(c, z)
        file.write(f'First string {rowana}, Second string {rowan}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(rowan, romance)
        b = opt_string_change(c, z)
        file.write(f'First string {rowan}, Second string {romance}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(romance, rowan)
        b = opt_string_change(c, z)
        file.write(f'First string {romance}, Second string {rowan}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(rowantimestory, romanticstory)
        b = opt_string_change(c, z)
        file.write(f'First string {rowantimestory}, Second string {romanticstory}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(romanticstory, rowantimestory)
        b = opt_string_change(c, z)
        file.write(f'First string {romanticstory}, Second string {rowantimestory}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(myrowanuniversity, rowanuniversitymy)
        b = opt_string_change(c, z)
        file.write(f'First string {myrowanuniversity}, Second string {rowanuniversitymy}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        c, z = edit_string_iterative(rowanuniversitymy, myrowanuniversity)
        b = opt_string_change(c, z)
        file.write(f'First string {rowanuniversitymy}, Second string {myrowanuniversity}.\n')
        file.write('Cost Matrix\n')
        file.write(np.array2string(c) + '\n')
        file.write('Function Matrix\n')
        file.write(np.array2string(z) + '\n')
        file.write('List of opt functions : \n')
        file.write(str(b) + '\n\n')

        long_one = 'Studentsinthiscoursewillstudyefficientalgorithmsforsortingsearchinggraphssets' \
                   'matricesandotherapplicationsandwilllearntodesignandanalyzenewalgorithms'.lower()
        long_two = 'Studentsthiscourseinwillstudyefficientalgorithmssortingsearchinggraphssets' \
                   'matricesforandotherapplicationswilllearntodesignandanalyzeandnewalgorithms'.lower()

        c, z = edit_string_iterative(long_one, long_two)
        file.write('Long strings given on problem 5\n')
        file.write(np.array2string(c, max_line_width=sys.maxsize))
        file.write(np.array2string(z, max_line_width=sys.maxsize))
        b = opt_string_change(c, z)
        file.write('\n' + str(b))

    with open('fulloutput.txt', 'a+') as file:
        for string in all_strings:
            for string_second in all_strings:
                c, z = edit_string_iterative(string, string_second)
                file.write(f'First string {string}, Second string {string_second}.\n')
                file.write('Cost Matrix\n')
                file.write(np.array2string(c) + '\n')
                file.write('Function Matrix\n')
                file.write(np.array2string(z) + '\n')
                b = opt_string_change(c, z)
                file.write('List of opt functions : \n')
                file.write(str(b) + '\n\n')

        long_one = 'Studentsinthiscoursewillstudyefficientalgorithmsforsortingsearchinggraphssets' \
                   'matricesandotherapplicationsandwilllearntodesignandanalyzenewalgorithms'.lower()
        long_two = 'Studentsthiscourseinwillstudyefficientalgorithmssortingsearchinggraphssets' \
                   'matricesforandotherapplicationswilllearntodesignandanalyzeandnewalgorithms'.lower()

        c, z = edit_string_iterative(long_one, long_two)
        file.write('Long strings given on problem 5\n')
        file.write(np.array2string(c, max_line_width=sys.maxsize))
        file.write(np.array2string(z, max_line_width=sys.maxsize))
        b = opt_string_change(c, z)
        file.write('\n' + str(b))
