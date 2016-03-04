#coding=utf-8

def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

a=calc_sum(1,3,5,7,9)
print a

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax=ax+n
        return ax
    return sum

a=lazy_sum(1,3,5,7,9)
print a
print a()

def make_adder(addend):
    def adder(augend):
        return augend+addend
    return adder
	
p=make_adder(23)
q=make_adder(44)
print p
print p(100)
print q(100)

def hellocounter(name):
    count=[0] 
    def counter():
        count[0]+=1
        print name,':',str(count[0])
    return counter

a=hellocounter('hello')
a()
a()
a()
