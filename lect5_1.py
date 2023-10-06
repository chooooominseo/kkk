# datetime
"""
from datetime import datetime as dt

# 현재 시간 출력
print(dt.now())

# 특정 시간대의 현재 시간 출력
# from pytz import timezone

# tz = timezone('Asia/Seoul')
# tz = timezone('UTC')
# print("timezne : ", dt.now(tz))

# 문자열을 날짜로 변환
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%n-%d')

# 날짜를 문자열로 변환 
date_object = dt.now()
date_string = date_object.strftime("%Y-%n-%d")
print(date_string)
"""
"""
import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

"""
"""
import os

# 현재 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')

# 파일 목록 출력
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

"""
"""
import mod.utils as mu
import os


print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir("python")
print(os.listdir())
"""
"""
import sys

print(sys.version)
print(sys.argv)
"""
"""
# stack
st = []

st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

top = st.pop()
print(top)
print(st)
print(len(st))
"""
"""
# Q
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

front = queue.pop(0)
print(front)
print(queue)
print(len(queue))
"""
"""
# qlist

qlist = []

def enqueue(qlist, data):
    qlist.append(data)
    
def dequeue(qlist):
    data = qlist[0]
    del qlist[0]
    return data

enqueue(qlist, 1)
print(qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

dequeue(qlist)
print(qlist)

dequeue(qlist)
print(qlist)
"""
"""
#O(1)
import time

arr = [1,2,3,4,5]

def ret_O1(idx) :
    return arr[idx]

start = time.time()
print(ret_O1(2))
end = time.time()
print(f"{end-start : 5f}sec")
"""
"""
# O(n)

import time
arr = [1,2,3,4,5]

def print_elements(arr):
    for elen in arr:
        print(elen)

start = time.time()
print_elements(arr)
end = time.time()

print(f"{end-start : 5f}sec")
"""
"""
# O(logn)

import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

start = time.time()
result = binary_search(my_list, 4)
end = time.time()

print(f"{end-start : 5f}sec") # 시간 측정

if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")
"""

#O(n2)

import time

def mul_for() :
    for i in range(5) :
        for j in range(5) :
            print(i, j)
            
start = time.time()     
mul_for()
end = time.time()

print(f"{end-start : 5f}sec")



