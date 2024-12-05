import random
import string

chain = "".join(random.choices(string.ascii_letters, k=1000000))

def delString(_chain, _oldKey):
    count = 0
    while(_chain.find(_oldKey) != -1):
        _chain = _chain.replace(_oldKey, '', 1)
        count += 1
    return [count, _chain ]

[cnt, res] = delString(chain, "Lab")

print("Amount of deleted words: ", cnt)

print(res)
