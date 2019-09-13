# File:      list01.py
# Created:   9/11/19
# Author:    P. Grabow
# ===============================================
mine = [10, 'blue', 'A', 20.2]
tmp = mine
print(mine)

del(mine[2:3])
print(mine)

mine.append(40)
print(mine)

mine.insert(0, 'B')
print(mine)

mine.insert(2, 20)
print(mine)

mine.pop()
print(mine)

print(mine.count('B'))

mine.remove('B')
print(mine)

mine.reverse()
print(mine)

print(len(mine))

otherList = ['X', 'Y', 'Z']
mine.append(otherList)
print(mine)

mine.reverse()
print(mine)

print(len(mine))

print(tmp)
