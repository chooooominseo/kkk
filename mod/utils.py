import math
import random

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
