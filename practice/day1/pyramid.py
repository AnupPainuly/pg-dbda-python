
"""
#half pyramid
rows=5
for i in range(0,rows+1,1):
    for j in range(0,rows+1,1):
        print("* "*j)
"""

"""
#full pyramid
#adding two space around star makes it equvilateral.
rows=5
for i in range(0,rows+1):
    space=" "*(rows - i)
    star="* "*i
    print(space+star)
"""

#left pyramid
rows=5
v=5
for i in range(0,rows+1):
    space=" "*(rows-i+v)
    star=" *"*i
    print(space+star)
    v=v-1
