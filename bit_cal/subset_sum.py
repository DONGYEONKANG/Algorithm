# 1 ~ 12
# A 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램


from itertools import combinations

A = [1,2,3,4,5,6,7,8,9,10,11,12]

l = list(combinations(A,3))
print(l)
K = 6

cnt = 0
for li in l:
    if sum(li) == K:
        cnt += 1

print(cnt)
