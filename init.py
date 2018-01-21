import requests
import os
import json

api_key="AIzaSyCwSBqoHbF8m3Vt8PmLmdDtfACP4gByz7E"
query_term = input("Please Enter the search string: ")
max_per_page=int(input("Enter the maxnumber search reults required (between 0-50) : "))
if(not (max_per_page >0 and max_per_page <51)):
    max_per_page=5
stri = 'https://www.googleapis.com/youtube/v3/search?part=snippet,id&key='+api_key+'&q='+query_term+'&type=video&maxResults='+str(max_per_page)
r = requests.get(stri)
data =r.json()
with open('data.json', 'w+',encoding='utf-8') as outfile:
    json.dump(data, outfile)
cmd = "python "+".\lib\json_to_csv.py "+ "items "+"data.json "+"channel.csv"
os.system(cmd)