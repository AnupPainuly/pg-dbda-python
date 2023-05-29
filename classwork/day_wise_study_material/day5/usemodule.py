#application level path setting
import sys
sys.path.append("c:\mydata")
'''import myfunctions

print("in usemodule")
myfunctions.f11()
myfunctions.f12()
'''
'''
import myfunctions as mf

print("in usemodule")
mf.f11()
mf.f12()
'''

from myfunctions import *
f11()
f12()
