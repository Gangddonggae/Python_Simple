# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = input("단수 :")
# for i in range(1,10):
#     print(f"{dan}x{i}={i*int(dan)}")

# 문제2) 2단부터 9단까지 출력(중첩 for문)
for i in range(2,10):
    for j in range(1,10):
        print(f"{j}x{i} = {i*j}")

# 문제3) list a 의 평균값을 계산하세요.
a = [1,2,3,4,5,99,87,54,2,5,4]
# a길이 => len(a)
b = len(a)
sum = 0
for i in a:
    sum += i #sum = sum + i
result = sum/len(a)

#round(값, 자리수): 자리수만큼 반올림
print(round(result, 2))  #평균값

# 문제4) list b에서 최소값 찾기
b = [22,1,4,7,98]
num_min = b[0] #22
for x in b:
    if x < num_min:
        num_min = x
print(f"최소값: {num_min}")
#오름차순 만들기

#문제 5) list c의 최소값, 최대값 찾기
c = [2,5,7,1,8]
num_min = c[0]
num_max = c[0]
for x in c:
    if x < num_min:
        num_min = x
    if x > num_max:
        num_max = x
print(f"최소값 {num_min}")
print(f"최대값 {num_max}")