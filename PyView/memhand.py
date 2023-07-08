from functools import lru_cache
from pyautogui import size

globalMemory = 200

def setMaxMemory(newAmount):
    global globalMemory
    globalMemory = newAmount

@lru_cache(globalMemory)
def getMaxMemory():
    global globalMemory
    return globalMemory
