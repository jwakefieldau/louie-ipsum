import sys

from louie_ipsum import LouieIpsum

keyword = None
if len(sys.argv) == 2:
    keyword = sys.argv[1]    

li = LouieIpsum()

print(li.get(keyword=keyword))
