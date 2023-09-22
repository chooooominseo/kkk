"""
#콜백함수

def prt_func(n) :
    print("hello",n)
    
def callfunc(fx) :
    for i in range(5):
        fx(i)
    
callfunc(prt_func)
"""
"""
#타입힌트

def add(a, b):
    return a + b
def add(a : int, b : int) -> int:
    return a + b

def update_msg(name: str) -> list:
    msg = []
    msg.append("Hello" + name)
    msg.append("Bye" + name)
    return msg 

def greeting(in_name: str) ->list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg 

res = greeting("python")

for message in res:
    print(message)
"""
"""
def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1)

"""
"""
#팩토리얼

def ploop(n) :
    if n == 0:
        print("end")
        return 1
    
    else :
        print(n, n-1, "=", n + n-1)
        return n * ploop(n-1)
    
print(ploop(5))

"""
"""
#피보나치
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4) 
print("res = ", res)    
"""
"""
#사용 가능 메소드

import calc
print(dir(calc))

import calc
add_res = calc.add(3,4)
sub_res = calc.sub(3,4)
mul_res = calc.mul(3,4)
div_res = calc.div(3,4)

import calc as cl
# 수정확인
add_res = cl.add(3,4)
"""
"""
import mod.circle_mod as cm

print(cm. pi)

print(cm.cc_area(4))
print(cm.cc_len(5))
"""
"""
# 문자열 자르기

def cutstr(st, wd, idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res
url ="http://www.notion.so/test/4-1"
rs = cutstr(url, "/", 3)
print(rs)
"""
"""
import mod.str_util as smod

url = "http://www.notion.so/test/4-1"
res = smod.cutstr(url, "/", 3)
print(res)
"""
"""
#표준라이브러리, 내장모듈 모듈

import math

sq_res = math.sqrt(6)
print(sq_res)

sp_res = math.sin(math.pi/2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fc_math = math.factorial(4)
print(fc_math)
"""
"""
import mod.utils as mu

res = mu.ut_sqrt(7)
print(res)

sin = mu.ut_sinpi()
print(sin)

el = mu.ut_elod()
print(el)

ep = mu.ut_exp(3)
print(ep)

pi = mu.ut_pi()
print(pi)
"""

import random as rd

res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random() #0에서 1.0까지 랜덤 실수 출력
print(fres)

nvres = rd.normalvariate()
print(nvres)

#모듈화

import mod.utils as mu

my_list = ["apple", "banana", "cherry"]
print(mu.rd_int(1,100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar())