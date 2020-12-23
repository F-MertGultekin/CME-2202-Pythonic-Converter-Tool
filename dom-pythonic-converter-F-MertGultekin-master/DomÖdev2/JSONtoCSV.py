import json
import csv
def JsonToCsv(inputFile,outputFile):
  #open output file with write mod
  outCsv=open(outputFile,'w',newline='',encoding='utf-8')
  csvwriter=csv.writer(outCsv)
  #col_names represent columns and this written in firstline 
  col_names=['ÜNİVERSİTE_TÜRÜ','ÜNİVERSİTE','FAKÜLTE;PROGRAM_KODU','PROGRAM;DİL','ÖĞRENİM_TÜRÜ','BURS;ÖĞRENİM_SÜRESİ','PUAN_TÜRÜ','KONTENJAN','OKUL_BİRİNCİSİ_KONTENJANI','GEÇEN_YIL_MİN_SIRALAMA','GEÇEN_YIL_MİN_PUAN']
  csvwriter.writerow(col_names)
  #open input file 
  #json load func loads json data variable 
  with open(inputFile,encoding='utf-8') as fileJSON:
    data = json.load(fileJSON)

  #dep = departments

  #keys and values can be reachable by using get() function
  for dep in data:
    deparment=[]
    utype=dep.get('uType')
    uniname=dep.get('university name') 
    faculty=dep.get('items')[0].get('faculty')
    uniId=dep.get('items')[0].get('department')[0].get('id')
    departmentName=dep.get('items')[0].get('department')[0].get('name')
    lang=dep.get('items')[0].get('department')[0].get('lang')
    second=dep.get('items')[0].get('department')[0].get('second')
    grant=dep.get('items')[0].get('department')[0].get('grant')
    period=dep.get('items')[0].get('department')[0].get('period')
    field=dep.get('items')[0].get('department')[0].get('field')
    quota=dep.get('items')[0].get('department')[0].get('quota')
    spec=dep.get('items')[0].get('department')[0].get('spec')
    order=dep.get('items')[0].get('department')[0].get('last_min_order')
    last_min_score=dep.get('items')[0].get('department')[0].get('last_min_score')

    #this function merge all the variables
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


 