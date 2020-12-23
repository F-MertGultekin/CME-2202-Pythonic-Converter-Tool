import json
import csv
import pandas
import numpy
def CsvToJson(inputFile,outputFile):
    #this is for the counting number of row
    count = len(open(inputFile).readlines(  ))
    count=count-1

    #read csv file by using panda library
    #seperator and encoding was announced
    df = pandas.read_csv(inputFile,sep=';',encoding='utf-8')
    outputJSON=open(outputFile,'w',newline='',encoding='utf-8')
    # to_numpy converts  to array
    arr = df.to_numpy() 
   
    i=0
    #first open braces after while loop ,there will be written close braces
    outputJSON.write("[")
    #i and count checks if program reach end of the file 
    while i != count: 
        #those if statements replace if element is NaN
        if arr[i][5] is numpy.nan:
            arr[i][5]='TR'
        if arr[i][6] is numpy.nan:
            arr[i][6]='No'

       
       
        if arr[i][11] is numpy.NaN:
            arr[i][11]=None
         
        if arr[i][12] is numpy.NaN:
            arr[i][12]=None
         
        if arr[i][13] is numpy.NaN:
            arr[i][13]=None
       
        if arr[i][7] is numpy.NaN:
            arr[i][7]=None

        #json dump puts this key value pairs into json file
        #for pretty printing indent=4,separators=(',', ': '),sort_keys=False are used
        # To encode turkish characters ensure_ascii=False are used
        json.dump({"university name":arr[i][1],"uType": arr[i][0],"items":[{"faculty":arr[i][2],"department":[{"id":arr[i][3],"name":arr[i][4],"lang":arr[i][5],"second":arr[i][6],"period":arr[i][8],"spec":arr[i][11],"quota":arr[i][10],"field":arr[i][9],"last_min_score":arr[i][13],"last_min_order":arr[i][12],"grant":arr[i][7]}] }]},outputJSON,indent=4,separators=(',', ': '),sort_keys=False,ensure_ascii=False)
        if count-1!=i:
            outputJSON.write(",")
        i=i+1


    outputJSON.write("]")

