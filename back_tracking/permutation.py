

NMAX = 100
MAXCADIDATES = 100

def construct_candidiates(a, k, input, c):
    global NMAX
    in_perm = [False] * NMAX

    for i in range(1,k):
        in_perm[a[i]] = True

    ncadidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncadidates] = i
            ncadidates += 1
    return ncadidates


def backtrack(a,k,input):
    global MAXCADIDATES
    c = [0] * MAXCADIDATES


    if k == input:
        for i in range(1, k+1):
            print(a[i], end="")
        print()

    else:
        k += 1
        ncandidates = construct_candidiates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)