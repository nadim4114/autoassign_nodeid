# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import serial
#import pyserial


com = serial.Serial(port='COM8', baudrate=9600, timeout=.1)
def write_read(x):

    com.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    #data = com.readline()
    #return data



while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
