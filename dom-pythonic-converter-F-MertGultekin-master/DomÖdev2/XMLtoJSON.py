import json
from lxml import etree as ET

def XmlToJson(inputFile,outputFile):
    #parse xml file 
    tree=ET.parse(inputFile)
  #open output file 
    XMLtoJSON=open(outputFile,'w',newline='',encoding='utf-8')
    #get root reach root object of the tree
    root=tree.getroot()

    XMLtoJSON.write("[")
    elemCount=0
    for elem in root:
        elemCount=elemCount+1
    i=0
    for elem in root:
        
        
        uniname=elem.attrib.get('name')
        utype=elem.attrib.get('uType')
    
        for subelem in elem:

                uniId=subelem.attrib.get('id')
                faculty=subelem.attrib.get('faculty')
                lang=subelem[0].attrib.get('lang')
                second=subelem[0].attrib.get('second')
                departmentName=subelem[0].text
                period=subelem[1].text
                spec=subelem[2].attrib.get('spec')
                quota=subelem[2].text
                field=subelem[3].text
                order=subelem[4].attrib.get('order')
                last_min_score=subelem[4].text
                grant=subelem[5].text

                json.dump({"university name":uniname,
                "uType": utype,
                "items":[{"faculty":faculty,
                "department":[{"id":uniId,"name":departmentName,"lang":lang,"second":second,
                "period":period,"spec":spec,"quota":quota,"field":field,
                "last_min_score":last_min_score,"last_min_order":order,
                "grant":grant}] }]},XMLtoJSON,indent=4,separators=(',', ': '),sort_keys=False,ensure_ascii=False)
                if elemCount-1!=i:
                    XMLtoJSON.write(",")
                i=i+1
    XMLtoJSON.write("]")