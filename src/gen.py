from random import randint
from random import uniform

ex_add = []
ex_add_decimal = []
ex_sub = []

def gen_add(qnt):
    for ex in range(qnt):
        temp_ex = f"{ex+1}-     {randint(0,9000)} + {randint(0,9000)}"
        ex_add.append(temp_ex)
    return ex_add

def gen_add_decimal(qnt):
    for ex in range(qnt):
        temp_ex = f"{ex+1}-     {uniform(0,9000):.2f} + {uniform(0,9000):.2f}"
        ex_add_decimal.append(temp_ex)
    return ex_add_decimal

def gen_sub(qnt):
    print("=-"*50)
    for ex in range(qnt):
        temp_ex = f"{ex+1}-     {randint(0,9000):>5} - {randint(0,9000)}"
        ex_sub.append(temp_ex)
    return ex_sub

gen_sub(5)
print(ex_sub)



