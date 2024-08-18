import sys

def count_subthreengs(S):
    # 3으로 나눴을 때 나머지가 0인 prefix의 수를 셀 딕셔너리
    prefix_count = {0: 1}  # 처음부터 3의 배수인 경우를 고려
    prefix_sum = 0
    count = 0

    for char in S:
        if char.isdigit():
            # 현재 숫자를 더해 누적합을 갱신
            prefix_sum = (prefix_sum + int(char)) % 3

            # 현재 prefix_sum 값이 이전에 몇 번 나타났는지를 count에 추가
            if prefix_sum in prefix_count:
                count += prefix_count[prefix_sum]
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1
        else:
            # 숫자가 아닌 문자가 나오면 초기화
            prefix_sum = 0
            prefix_count = {0: 1}

    return count


S = sys.stdin.readline().rstrip('\n')

print(count_subthreengs(S))
