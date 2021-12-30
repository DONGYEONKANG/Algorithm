# K = 3 / N = 10 / M = 5

# Greedy 탐색
# 예외 처리
# 앞 뒤 위치의 차이를 계산해 , K 보다 크다면 0 반환

# 현재 위치부터 K(최대) 만큼 이동한다.
# 만약 K 지점에 주유소가 있다면 cnt = 1 / 없다면 K - 1 지점 확인 ... 현재 위치 + 1 지점 까지 확인
# 주유소가 위치한 지점을 현재위치로 한 후에 N까지 반복



def elec_bus(K,N,M_list):

    pre = 0 # 현재 위치
    cnt = 0 # 카운트
    while True:
        p = pre + K

        if p >= N:
            return cnt

        for i in range(0, K + 1):
            pp = p - i

            if pp in M_list:
                cnt += 1
                pre = pp
                break

        if pp == p - K:
            return 0

if __name__ == "__main__":

    print(elec_bus(3,10,[1,3,7,8,9]))


