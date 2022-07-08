import multiprocessing
import time
from lanes import *
import numpy as np
from threading import Timer
import os
import shutil
from laneSchedule import *

def main_module(path1,path2,path3,path4):
    global ttime
    fold1 = path1.split('.',1)
    fold1 = fold1[0]
    if(os.path.isdir(fold1)):
        shutil.rmtree(fold1)
    fold2 = path2.split('.',1)
    fold2 = fold2[0]
    if(os.path.isdir(fold2)):
        shutil.rmtree(fold2)
    fold3 = path3.split('.',1)
    fold3 = fold3[0]
    if(os.path.isdir(fold3)):
        shutil.rmtree(fold3)
    fold4 = path4.split('.',1)
    fold4 = fold4[0]
    if(os.path.isdir(fold4)):
        shutil.rmtree(fold4)
    outputs = [[]*2]*4
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4)
    inputs = [path1,path2,path3,path4]
    outputs = pool.map(lane_gst,inputs)
    print("\nInput: {}".format(inputs))
    print("\nOutput: [Green Signal Time, Ambulance count]",outputs)   
    schedule,ttime = scheduling(outputs)
    print("\nSchedule: ",schedule)
    print("\nTotal time to complete the schedule: ",ttime)
    
if __name__ == '__main__':
    waiting_time = 0
    input_list = ['video/sample.mp4','video/cars.mp4','video/cars_Trim.mp4','video/amb.mp4']
    for i in range(1):
        t = Timer(waiting_time,main_module,input_list)
        t.start()
        t.join()
        waiting_time = ttime - 15
        print("\nWaiting time for next detection to start: ",waiting_time)
