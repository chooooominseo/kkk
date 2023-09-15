"""
#식별 연산

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)
print(x is z)
print(x is not y)

# 식별

a = 5
b = 5
print(a is b)
print(a is not b)
"""
"""
a = 3
b = 3.0
print( 3 == 3.0 )
print( 3 is 5.0 )
"""
"""
# 특성

a = [3, 5, 1]
b = a
print(a is b)

a[0] = 2
print(a,b)
print(a is b)
"""
"""
# 연산자 결합 순서

x = 2 ** 3 ** 2
print(x)

# a = 2 + 3 * 4
# a = 10 / 5 / 2
# a = 2 ** 3 ** 2
# a = 2 ** (3 ** 2)
# a = 10 % 3 % 2
# a = 1 + 2 > 3 and 4 - 1 < 2
# a = not False and True
# a = not True or False and True
# a = 1 & 2 | 3 ^ 4
# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# a = 2 * -3 // 2
# a = 1 == 2 != 3
# print(a)
"""
"""
# 조건문

x = 0

if x > 0:
    print("x is positive")
    
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
"""
"""
# 1
a = 7

if a%2 == 0:
    print("짝수")
    
else:
    print("홀수")
"""
"""
# 2
a = 3
b = 6
if a != b:
    print("a is not b")

else:
    print("a is b")
"""
"""
# 3
a = 8
b = 4
char = a
if char == "a" or char == "b"
    print("a 또는 b 입니다")
else: 
    print("adhk b 둘 다 아닙니다")
"""
"""
# for문

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
"""
"""
# 1. 이중 For문
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
"""
"""
# 0부터 9까지 출력
for i in range(10) :
    print(i)
"""
"""
# 문자열 출력
for char in "Phython" :
    print(char)
"""    
#리스트 요소 반대로 출력
fruits = ["apple", "banana", "cherry"]
"""
for fruit in reversed(fruits):
    print(fruit)
"""    
"""
#리스트 요소 역순 출력

for fruit in sorted(fruits, reverse = True):
    print(fruit)
    
#구구단 출력

for i in range(1, 10):
    for k in range(1, 10):
        print(i, "x", k, "=", i*k) 
        
"""
"""
#for ~ else 문

rang = [5, 8, 3, 1, 6]
    
for i in rang:
    print("element :", i)
else :
    print("end process")

# 반복문 제어

for i in range(10):
    if i == 7:
        break
    elif i == 1:
        continue
    else:
        pass # 그냥 실행

    print(i)
"""
"""
#while문

i = 1

while i <= 5:
    print(i)
    i += 1
"""
"""
# 1. 0부터 9까지

i = 0

while i <= 9:
    print(i)
    i += 1
"""
"""
# 2. 문자열을 한글자씩 출력

str_word = "python"
idx = 0

while idx < len(str_word):
    print(str_word[idx])
    idx += 1
"""
"""
# 3. 1부터 10까지의 총합 출력

sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1 
    print(sum)
"""
"""
# 4. 1에서 100까지의 짝수, 홀수 출력

i = 1

while i <= 100:
    if i%2 == 0:
        print("짝수", i)
    else:
        print("홀수", i)
    i += 1
"""
# 5. 1에서 100까지의 7의 배수만 출력

i = 1

while i <= 100:
    if i%7 == 0:
        print(i)
    else:
        pass
    
    i += 1