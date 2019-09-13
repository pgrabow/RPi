# File:      dict01.py
# Created:   9/11/19
# Author:    P. Grabow
# ===============================================
yours ={ 'white':0, 'blue':1, 'yellow':2, 'green':3, 'red':4}
print('yours: ', yours)

print( 'black in yours:', 'black' in yours)
print( 'red in yours:  ', 'red' in yours)

print( 'Value associated with white: ', yours.get('white', -1))
print( 'Value associated with gray:  ', yours.get('gray', -1))

if('black' in yours):
    print('deleting item where key = black')
    del( yours['black'])
else:
    print('black not in yours')
    
print('yours: ', yours)

if('blue' in yours):
    print('deleting item where key = blue')
    del( yours['blue'])
else:
    print('blue not in yours')
    
print('yours: ', yours)

print('Clearing yours')
yours.clear()
print('yours: ', yours)

    
    

       