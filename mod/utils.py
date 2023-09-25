import math
import random
from datetime import datetime as dt
import os

def ut_sqrt(x) :
    return math.sqrt(x)

def ut_sinpi(x) :
    return math.sin(math.pi/2)

def ut_elog(x) :
    return math.elog(math.e)

def ut_exp(x) :
    return math.exp(x)

def ut_pi() :
    return math.pi

def rd_int(x, y) :
    return random.randint(x,y)

def rd_list(this) :
    return random.choice(this)

def rd_rd() :
    return random.random()

def rd_nmvar() :
    return random.normalvariate(0,1)

def get_dtnow():
    return dt.now()
    
def cvt_time2str(objtime):
    return dt.strptime(objtime, "%Y-%n-%d")

def cvt_time2time():
    obj = dt.now()
    return obj.strftime("%Y-%n-%d")

def get_curdir() :
    return os.getcwd()

def os_mkdir(pname) :
    return os.mkdir(pname)