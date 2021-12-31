
if __name__ == "__main__":
    arr = [3, 6, 7, 1, 5, 4]

    n = len(arr) # n: 원소의 수

    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end=",")
        print()

################################################################

    N = 3
    K = 6
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(arr)

    cnt = 0
    for i in range(1 << n):
        # 부분 집합 리스트
        ar = []
        for j in range(n):
            if i & (1 << j):
                ar.append(arr[j])

        # 부분 집합 리스트에서 N과 K 가 일치한 것.
        if len(ar) == N and sum(ar) == K:
            cnt += 1

    print(cnt)



