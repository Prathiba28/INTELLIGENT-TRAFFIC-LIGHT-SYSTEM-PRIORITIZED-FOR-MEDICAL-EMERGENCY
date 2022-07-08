def laneScheduling(output_list):
    n = len(output_list)
    quantum = 40
    min_quantum = 10
    i=0
    results= []
    
    while(i < n):
        if output_list[i][1] > quantum:
            val = output_list[i][1] - quantum
            output_list.append([output_list[i][0],val,output_list[i][2]]) 
            results.append([output_list[i][0],quantum,output_list[i][2]])
            n=n+1
        else:
            if output_list[i][1] < min_quantum:
                results.append([output_list[i][0],min_quantum,output_list[i][2]])
            else:
                results.append(output_list[i])
        i=i+1            
    return results
#Round Robin Lane Scheduling
def scheduling(outputs):
    gst_amb_list = []
    n = len(outputs)
    for i in range(n):
        temp = i + 1
        val = 'lane' + str(temp)
        gst_amb_list.append([val,outputs[i][0][0],outputs[i][0][1]])
    #sorting
    gst_amb_list.sort(key = lambda x:x[1],reverse=True)
    gst_amb_list.sort(key = lambda x:x[2],reverse=True)
    
    i=0
    amb_list = []
    non_amb_list=[]
    n = len(gst_amb_list)
    while(i < n):
        if gst_amb_list[i][2] > 0:
            amb_list.append(gst_amb_list[i])
        else:
            non_amb_list.append(gst_amb_list[i])
        i = i+1
    
    #print("Ambulance list:",amb_list)
    res1 = laneScheduling(amb_list)
    #print("\nAmbulance Schedule:",res1)

    #print("\nNon Ambulance list:",non_amb_list)
    res2 = laneScheduling(non_amb_list)
    #print("\nNon Ambulance Schedule:",res2)

    res1 = res1 + res2
    #print("\nFinal Schedule:",res1)
    total_time = 0
    k = len(res1)
    
    for i in range(k):
        total_time = res1[i][1] + total_time
    #print("Total time: ",total_time)
    return res1,total_time