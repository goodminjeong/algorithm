"""
두 정수 사이의 합

<문제 설명>
- 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
- 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

<제한 조건>
- a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
- a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
- a와 b의 대소관계는 정해져있지 않습니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 첫 번째 풀이
@func_speed
def solution1(a, b):
    answer = 0
    for n in range(min(a, b), max(a, b) + 1):
        answer += n
        n += 1
    return answer


# 두 번째 풀이
@func_speed
def solution2(a, b):
    answer = 0
    for n in range(min(a, b), max(a, b) + 1, 1):
        answer += n
    return answer


# 세 번째 풀이
@func_speed
def solution3(a, b):
    return sum(n for n in range(min(a, b), max(a, b) + 1, 1))


# 네 번째 풀이
@func_speed
def solution4(a, b):
    return sum(range(min(a, b), max(a, b) + 1, 1))


# 다섯 번째 풀이
@func_speed
def solution5(a, b):
    if max(abs(a), abs(b)) - min(abs(a), abs(b)) == 0:
        return 0
    else:
        return sum(range(min(a, b), max(a, b) + 1, 1))


solution1(1000000, -150000)
solution2(1000000, -150000)
solution3(1000000, -150000)
solution4(1000000, -150000)
solution5(1000000, -150000)

solution1(1000000, -1000000)
solution2(1000000, -1000000)
solution3(1000000, -1000000)
solution4(1000000, -1000000)
solution5(1000000, -1000000)
