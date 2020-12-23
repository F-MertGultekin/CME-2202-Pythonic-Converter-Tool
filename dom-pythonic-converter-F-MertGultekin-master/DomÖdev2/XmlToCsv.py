from xml.etree import ElementTree as ET 
import os
import csv

def XmlToCsv(inputFile,outputFile):
    tree=ET.parse(inputFile)

    outCsv=open(outputFile,'w',newline='',encoding='utf-8')
    csvwriter=csv.writer(outCsv)

    col_names=['ÜNİVERSİTE_TÜRÜ','ÜNİVERSİTE','FAKÜLTE;PROGRAM_KODU','PROGRAM;DİL','ÖĞRENİM_TÜRÜ','BURS;ÖĞRENİM_SÜRESİ','PUAN_TÜRÜ','KONTENJAN','OKUL_BİRİNCİSİ_KONTENJANI','GEÇEN_YIL_MİN_SIRALAMA','GEÇEN_YIL_MİN_PUAN']
    csvwriter.writerow(col_names)

    root=tree.getroot()

    for elem in root:
        deparment=[]
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

                deparment.append(utype)
                deparment.append(uniname)
                deparment.append(faculty)
                deparment.append(uniId)
                deparment.append(departmentName)
                deparment.append(lang)
                deparment.append(second)
                deparment.append(grant)
                deparment.append(period)
                deparment.append(field)
                deparment.append(quota)
                deparment.append(spec)
                deparment.append(order)
                deparment.append(last_min_score)

                csvwriter.writerow(deparment)

    outCsv.close()