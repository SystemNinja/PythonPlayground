"""
https://codereview.stackexchange.com/questions/75574/ping-function-in-python
"""

import os 

hostname="www.google.com"
response=os.system("ping "+hostname+" -n 2")
#test=os.system("dir")
print(type(response))