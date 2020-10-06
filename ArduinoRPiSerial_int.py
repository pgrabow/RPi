# File: ArduinoRPiSeral_int.py @ 1:00 pm 10/6/20
# Arduino File: ArduinoRPiSeral_int.ino
# Date: 10/6/2020
# Reference: https://github.com/PowerBroker2/pySerialTransfer

import time
from pySerialTransfer import pySerialTransfer as txfer

INT_SIZE = 4
PORT = 'COM6'
# -----------------------------------------
def wait_for_available():
    while not link.available():
        if link.status < 0:
            if link.status == txfer.CRC_ERROR:
                print('ERROR: CRC_ERROR')
            elif link.status == txfer.PAYLOAD_ERROR:
                print('ERROR: PAYLOAD_ERROR')
            elif link.status == txfer.STOP_BYTE_ERROR:
                print('ERROR: STOP_BYTE_ERROR')
            else:
                print('ERROR: {}'.format(link.status))
    
# -----------------------------------------
def send_list(tmp_list):
    list_size = link.tx_obj(tmp_list)
    link.send(list_size)
    return list_size
    
# -----------------------------------------
def recv_list(count):
    position = 0

    tmp_list = []
    for val in range(count):     
        tmpStr  = link.rx_obj(obj_type=type(val),
                    obj_byte_size=INT_SIZE,
                    list_format='i',
                    start_pos=position*INT_SIZE)
        tmp_list.append(int(tmpStr))
        position = position + 1
    return tmp_list
 


# ================================================
if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer(PORT)
        # List will always have 10 elements
        outList = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

        link.open()
        time.sleep(2) # allow some time for the Arduino to completely reset
        
        for x in range(100):
            inList = []
            
            list_size = send_list(outList)          
            wait_for_available()
            
            inList = recv_list(10)
                              
            ###########################################
            # Display the received values
            ###########################################
            print('SENT: ', outList)
            print('RCVD: ', inList)
            print(' ')
            
            ###########################################
            # Reset the lists
            ###########################################            
            outList = inList
            inList = []
                
    except KeyboardInterrupt:
        try:
            link.close()
        except:
            pass
    
    except:
        import traceback
        traceback.print_exc()
        
        try:
            link.close()
        except:
            pass