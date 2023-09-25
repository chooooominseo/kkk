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