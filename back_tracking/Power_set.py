# 부분 집합의 합


MAXCADIDATES = 100
NMAX = 100
a = [0] * NMAX


def procees_solution(a, k):
    print("(", end=" ")
    for i in range(k+1):
        if a[i]:
            print(i, end=" ")
    print(")")


def construct_candidiates(a, k, input, c):

    c[0] = True
    c[1] = False
    return 2


def backtrack(a,k,input):
    global MAXCADIDATES
    c = [0] * MAXCADIDATES


    if k == input:
        procees_solution(a,k)

    else:
        k += 1
        ncandidates = construct_candidiates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)
