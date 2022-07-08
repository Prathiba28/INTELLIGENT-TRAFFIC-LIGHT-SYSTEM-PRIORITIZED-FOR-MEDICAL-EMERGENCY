import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Markdown
from glob import glob
from image_capturing import *
from vehicles.counter import *
from vehicles.tracker import *
from vehicles.GST import *
import multiprocessing
import threading
import time
def lane_gst(video_path):
    PATH = capturing(video_path)
    print(PATH)
    gst_list = []
    amb_list = []
    res = []
    for images in glob.iglob(f'{PATH}/*'):
        if (images.endswith(".jpg")):
            print("\nImage path:",images)
            amb_freq = from_static_image(images)
            #print("AMBULANCE COUNT:",amb_freq)
            amb_list.append(amb_freq)
            gst_list.append(main())
    print("\nGST LIST:",gst_list)
    gst = max(gst_list)
    amb_max = max(amb_list)
    print("\nMAX GREEN SIGNAL TIME: ",gst)
    print("MAX AMBULANCE FREQUENCY: ",amb_max)
    res.append([gst,amb_max])
    return res



