"""
# 1번
for i in range(1,6):
    print("*"*(6-i))

# 1번 교수님 풀이

for i in range(5,0,-1):
    print("*"*i)
    
# 2번

for i in range(1,6):
    print("*"*i)
    
# 3번
for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2*i-1)
    print(spaces + stars)
    
"""
"""
# 4번

for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2*i-1)
    print(spaces + stars)
    
# 5X5 츨력

# 1번
num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = []
"""
"""
# 2번

num = 0
line = []
for i in range(1,6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = []
"""
""" 
# 3번

num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []
"""
"""
# 가위바위보

import random

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2') 
    ):
        print("승")
        return
    else:
        print("패")
        return
    
print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")

chnum = input()
pcnum = get_computer_choice()

determine_winner(chnum)

"""
"""
# 파일 쓰기

f = open("temp.txt", "w")
f.write("hello\n")
f.write("world")
f.close()
"""
"""
# 0 ~ 100
file = open("temp.txt", "w")

for i in range(100):
    file.write(f"{i}\n")
file.close()
"""
"""
# “c:/User/Catholic/temp.txt” 경로

file = open("C:\\Users\\Catholic\\temp.txt", "w")
for i in range(100):
    file.write(f"{i}\n")
    
file.close()
"""
"""
# “hello\n”, “world” 추가

file = open("C:\\Users\\Catholic\\temp.txt", "a")

file.write("hello\n")
file.write("world")
    
file.close()
"""
"""
file = open("C:\\Users\\Catholic\\temp.txt", "r")
res = file.read()
print(res)

file.close()
"""
"""
# readline

file = open("C:\\Users\\Catholic\\temp.txt", "r")

res = file.readline()

print(res)
for i in range(110):
    res = file.readline()
    print(res)
    
file.close()
"""
"""
# readlines

file = open("C:\\Users\\Catholic\\temp.txt", "r")
res = file.readlines()
print(res)

file.close()
"""
"""
# 라인별 처리

file = open("C:\\Users\\Catholic\\temp.txt", "r")
line = file.readlines()
for l in line :
	print(l)
 
file.close()
"""
file = open("C:\\Users\\Catholic\\temp.txt", "r")
for line in file :
	print(line)

file.close()