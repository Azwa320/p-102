import csv
import dropbox
import random 
import cv2
import time

start_time= time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = csv.videoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img" + str(number)+ ".png"
        cv2.inwrite(image_name, frame)
        start_time=time.time
        result= False
    return image_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.distroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token='sl.BQFWE9uSM1uanK2aOF8dzS5s6jmEKqKo55sXyLBwtehm_lwCI4RYYKgQEzg4d4IErSZPpUScvUq2ItaBABUso014HO3SQBRgiCAwfynxTwF3LuexJaWoo4hCnChOKoLiVz7XcA0'
    file= image_name
    file_from= file
    file_to= "/newfolder1" +(image_name)
    dbx= dropbox.Dropbox(access_token)

    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time()- start_time) >= 3):
            name= take_snapshot()
            upload_file(name)
    
main()