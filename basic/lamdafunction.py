adder= lambda a,b:a+b
adder (69,225)
 
def exp(power):
    return lambda l : [a**power for a in l ]
four= exp(4)
four([2,4,6,8,10])


