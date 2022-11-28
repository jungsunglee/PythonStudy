# import module 시 ModuleNotFoundError 발생 시 sys.path에 해당결로 추가필요
import sys
print(sys.path)
sys.path.append('C:\\Project\\pythonStudy\\basicPython\\moduleTest')

import importModule


print(importModule.version)
importModule.printAuth()

print(importModule.__name__)