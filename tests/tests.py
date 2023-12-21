import timeit


new_setup = '''from PIL import Image
from time import time
import sys'''

new_code = open('new_code.txt', 'r').read()


old_setup = '''from PIL import Image
import sys'''

old_code = open('old_code.txt','r').read()


# 10k iterations
new_time = timeit.timeit(setup=new_setup,  stmt=new_code, number=10000)
old_time = timeit.timeit(setup=old_setup, stmt=old_code, number=10000)


print("NEW-CODE Lapsed: ",  new_time*1000," ms")
print("OLD-CODE Lapsed: ",old_time*1000," ms")


print("Winner:", min(new_time,old_time)*1000)
