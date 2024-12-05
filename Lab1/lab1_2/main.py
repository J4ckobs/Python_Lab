import random
import string

chain = "".join(random.choices(string.ascii_letters,k=1000000))

def replaceString(_chain, _oldKey, _newKey=""):
    count = 0
    while(_chain.find(_oldKey) != -1):
        _chain = _chain.replace(_oldKey,_newKey,1)
        count += 1
    return [count, _chain ]

[cnt, res] = replaceString(chain, "Lab", "KOŚĆ")

print("Amount of replaced words: ", cnt)

print(res)
