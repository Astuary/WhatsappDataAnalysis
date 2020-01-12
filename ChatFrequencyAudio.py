import datetime
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

exportedFilePath = 'WhatsApp Chat with Nisarg 07Jan2020.txt'
fullName1 = 'Nisarg'
fullName2 = 'Kunjal'
color1 = '#0095B6'
color2 = '#F47789'
endDate = date.today()
with open(exportedFilePath, encoding="utf8") as fp:
    line = fp.readline()
    startDate = datetime.date(int(line[6:10]), int(line[3:5]), int(line[0:2]))
days = endDate - startDate
name1frequency = np.zeros(days.days+1, dtype=int)
name2frequency = np.zeros(days.days+1, dtype=int)
months = [''] * (days.days+1)
currentMonth = startDate.strftime("%b")+" "+startDate.strftime("%y")
months[0] = currentMonth

with open(exportedFilePath, encoding="utf8") as fp:
    line = fp.readline()

    while line:
        try:
            currentDate = datetime.date(int(line[6:10]), int(line[3:5]), int(line[0:2]))
            delta = currentDate - startDate
            print(delta.days)

            if currentMonth != currentDate.strftime("%b")+" "+currentDate.strftime("%y"):
                currentMonth = currentDate.strftime("%b")+" "+currentDate.strftime("%y")
                print(months)
                print(delta.days)
                months[delta.days] = currentMonth

            endIndex = line.index(':', 14)
            name = line[22:endIndex]

            if name == fullName1:
                name1frequency[delta.days] += 1
            elif name == fullName2:
                name2frequency[delta.days] += 1

        except ValueError:
            print('Exception')

        line = fp.readline()

print(name1frequency)
print(name2frequency)
print(months)

# Normalised [-1,1]
norm_name1frequency = 2.*(name1frequency - np.min(name1frequency))/np.ptp(name1frequency)-1
norm_name2frequency = 2.*(name2frequency - np.min(name2frequency))/np.ptp(name2frequency)-1

#data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
scaled = np.int16(norm_name1frequency/np.max(np.abs(norm_name1frequency)) * 32767)
write('test.wav', len(name1frequency), scaled)
