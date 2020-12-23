import pandas
import numpy
from lxml import etree as ET

def CsvToXml(input,output):
     #this is for the counting number of row
    count = len(open(input).readlines(  ))
    count=count-1
     #read csv file by using panda library
    #seperator and encoding was announced
    df = pandas.read_csv(input,sep=';',encoding='utf-8')

    # to_numpy converts  to array
    arr = df.to_numpy() 
    #departments is root

    data = ET.Element('departments')
    i=0
     #i and count checks if program reach end of the file 
    while i != count:
        #adding sub elements to root
        # name and uType are attributes
        university=ET.SubElement(data,'university',name=arr[i][1],uType=arr[i][0])

        item=ET.SubElement(university,'item',id=str(arr[i][3]),faculty=(arr[i][2]))    


        if  arr[i][5] is numpy.nan:
            language='TR'
        else:
            language = arr[i][5]

        if arr[i][6] is numpy.nan:
            SecondType='No'
        else: 
            SecondType=arr[i][6]
        #after here thoso elements are connected to item element.
        #for ex name is a child of item

        name=ET.SubElement(item,'name',lang=language,second=SecondType)
        name.text=arr[i][4]

        period=ET.SubElement(item,'period')
        #text must be string
        period.text=str(arr[i][8])
        #checks if NaN (NOT A NUMBER)
        if arr[i][11] is numpy.nan:
            quota=ET.SubElement(item,'quota')
            quota.text=str(arr[i][10])
        else:
            quota=ET.SubElement(item,'quota',spec=str(arr[i][11]))
            quota.text=str(arr[i][10])

        field=ET.SubElement(item,'field')
        field.text=arr[i][9]

        if arr[i][12] is numpy.nan:
            last_min_score=ET.SubElement(item,'last_min_score')
        else:
            last_min_score=ET.SubElement(item,'last_min_score',order=str(arr[i][12]))

        if not arr[i][13] is numpy.nan:    
            last_min_score.text=str(arr[i][13])

        if  arr[i][7] is numpy.nan:
            grant=ET.SubElement(item,'grant')
            
        else:
            grant=ET.SubElement(item,'grant')
            grant.text=None
        i=i+1
    #tree has converted to string with tostring method
    #to pretty print pretty_print attribute is true
    #to write turkish characters to xml file string must be encoded utf-8 
    #file also must be encoded utf8 
    mydata = ET.tostring(data,pretty_print=True,encoding='utf-8')

    fo = open(output, "w",encoding='utf-8')

    fo.write(mydata.decode("utf-8"))












