import numpy as np
import pandas as pd
def file_access():
    count_array = np.loadtxt('static-data.txt', delimiter=',', dtype = int)
    return (count_array)
def GreenSignalTime(count_array, avg_time):
    vehicle_class = np.multiply(count_array, avg_time)
    #print(vehicle_class)
    summation = np.sum(vehicle_class)
    gst = summation #Green signal Time
    return(gst)
def main():
    avg_time = np.array([2,2.5,2.25,2.5,1,2.2]) #average time for each class of vehicle to cross the intersection
    count = file_access() #vehicle count of each class - array
    #print (count)
    gst = GreenSignalTime(count, avg_time)
    minimum_gst = 10
    maximum_gst = 40
    #print(gst)
    return gst
    #Green Signal time in seconds