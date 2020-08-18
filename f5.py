#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.client

conn = http.client.HTTPSConnection("covid-19-coronavirus-statistics.p.rapidapi.com")


headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "---"
}

conn.request("GET", "/v1/stats?country=", headers=headers)

res = conn.getresponse()
data = res.read()

master
master
master
master
master
master
master
master
master
master
master
master
master
master
master
master
master
master

s = data.decode()s = data.decode()
print(s)
s = data.decode()s = data.decode()
print(s)
s = data.decode()s = data.decode()
print(s)s = data.decode()s = data.decode()
print(s)s = data.decode()s = data.decode()
print(s)
s = data.decode()s = data.decode()
print(s)s = data.decode()s = data.decode()
print(s)

s = data.decode()s = data.decode()
print(s)s = data.decode()s = data.decode()
print(s)s = data.decode()s = data.decode()
print(s)s = data.decode()s = data.decode()
print(s)


spis = s.split('country')
for i in range(len(spis)):
    s = spis[i]
    spis[i] = s.split(',')
print(len(spis))
for i in range(len(spis)):
    print(len(spis[i]))

myfile0 = open('eggs3.txt', 'w')
#with myfile0:

myfile0.write('":"Country"'+ '\n')
myfile0.write('"lastUpdatee":"2020-03-15T18:20:18"'+ '\n')
myfile0.write('"c-onfirmed":'+ '\n')
myfile0.write('"d-eeathss":'+ '\n')
myfile0.write('"r-eccovereds":'+ '\n')
myfile0.write('"p-roovinces":"'+ '\n')
myfile0.write('"'+ '\n')
myfile0.write('==================0'+ '\n')


for i in range(len(spis)):
    if i!=0:
        for ii in range(len(spis[i])):
            myfile0.write(spis[i][ii]+ '\n')
        myfile0.write('==================0'+ '\n')
#myfile0.write(data.decode("utf-8"))
#print((data.decode("utf-8")))
