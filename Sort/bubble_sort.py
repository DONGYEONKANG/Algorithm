# 버블 정렬
# 순차적으로 비교
# 한 단계가 끝나면 가장 큰 원소 또는 작은 원소가 마지막 정렬로..


li = [1,3,5,6,8,9]


def BubbleSort(li): #
    for i in range(len(li) -1 , 0, -1):
        for j in range(0,i):

            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li

if __name__ == "__main__":
    print(BubbleSort(li))


