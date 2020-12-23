import json
from lxml import etree as ET
def JsonToXml(inputFile,outputFile):

    with open(inputFile,encoding='utf-8') as fileJSON:
        data = json.load(fileJSON,)


    root = ET.Element('departments')

    for dep in data:
        
        utype=dep.get('uType')
        uniname=dep.get('university name') 
        faculty=dep.get('items')[0].get('faculty')
        uniId=dep.get('items')[0].get('department')[0].get('id')
        departmentName=dep.get('items')[0].get('department')[0].get('name')
        lang=dep.get('items')[0].get('department')[0].get('lang')
        second=dep.get('items')[0].get('department')[0].get('second')
        Grant=dep.get('items')[0].get('department')[0].get('grant')
        Period=dep.get('items')[0].get('department')[0].get('period')
        field=dep.get('items')[0].get('department')[0].get('field')
        Quota=dep.get('items')[0].get('department')[0].get('quota')
        spec=dep.get('items')[0].get('department')[0].get('spec')
        order=dep.get('items')[0].get('department')[0].get('last_min_order')
        lastMinScore=dep.get('items')[0].get('department')[0].get('last_min_score')


        universityRoot=ET.SubElement(root,'university',name=uniname,uType=utype)

        item=ET.SubElement(universityRoot,'item',id=str(uniId),faculty=(faculty))    


        if  lang =="":
            language='TR'
        else:
            language = lang
        if second  =="":
            SecondType='No'
        else: 
            SecondType=second

        name=ET.SubElement(item,'name',lang=language,second=SecondType)
        name.text=departmentName

        period=ET.SubElement(item,'period')
        period.text=str(Period)

        if Quota  =="":
            quota=ET.SubElement(item,'quota')
            quota.text=str(Quota)
        else:
            quota=ET.SubElement(item,'quota',spec=str(spec))
            quota.text=str(Quota)

        fieldforXML=ET.SubElement(item,'field')
        fieldforXML.text=field

        if order  =="":
            last_min_score=ET.SubElement(item,'last_min_score')
        else:
            last_min_score=ET.SubElement(item,'last_min_score',order=str(order))

        if not lastMinScore  =="":    
            last_min_score.text=str(lastMinScore)

        if  Grant  == "":
            grant=ET.SubElement(item,'grant')
                
        else:
            grant=ET.SubElement(item,'grant')
            grant.text=Grant

    mydata = ET.tostring(root,pretty_print=True,encoding='utf-8')

    fo = open(outputFile, "w",encoding='utf-8')

    fo.write(mydata.decode("utf-8"))
