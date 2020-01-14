import datetime
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

exportedFilePath = 'WhatsApp Chat with Nisarg 07Jan2020.txt'
fullName1 = 'Nisarg'
fullName2 = 'Kunjal'
prevName = None
prevTime = None
color1 = '#0095B6'
color2 = '#F47789'
endDate = date.today()
with open(exportedFilePath, encoding="utf8") as fp:
    line = fp.readline()
    startDate = datetime.date(int(line[6:10]), int(line[3:5]), int(line[0:2]))
days = endDate - startDate
name1frequency = np.zeros(days.days+1, dtype=int)
name2frequency = np.zeros(days.days+1, dtype=int)
time1frequency = [datetime.timedelta()] * (days.days+1)
time2frequency = [datetime.timedelta()] * (days.days+1)
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

            """hour = line[12:line.index(':')]
            min = line[(line.index(':')+1):(line.index(':')+3)]
            if line[17] == 'p' and int(line[12:line.index(':')]) != 12:
                hour = str(int(line[12:line.index(':')]) + 12)
            if line[17] == 'a' and int(line[12:line.index(':')]) == 12:
                hour = '00'"""

            FMT = '%d/%m/%Y, %I:%M %p'

            endIndex = line.index(':', 14)
            name = line[22:endIndex]

            if name == fullName1 and (prevName == fullName2 or prevName == None):
                name1frequency[delta.days] += 1
                prevName = fullName1

                currentTime = datetime.datetime.strptime(line[:line.index('-')-1], FMT)
                if prevTime != None:
                    time1frequency[delta.days] = time1frequency[delta.days] + (currentTime - prevTime)
                    #print((currentTime - prevTime))
                prevTime = currentTime
            elif name == fullName2 and (prevName == fullName1 or prevName == None):
                name2frequency[delta.days] += 1
                prevName = fullName2

                currentTime = datetime.datetime.strptime(line[:line.index('-')-1], FMT)
                if prevTime != None:
                    time2frequency[delta.days] = time1frequency[delta.days] + (currentTime - prevTime)
                    #print((currentTime - prevTime))
                prevTime = currentTime

        except ValueError:
            print('Exception')

        line = fp.readline()

print(name1frequency)
print(name2frequency)
print(time1frequency)
print(time2frequency[-7].seconds)

#avg1 = np.divide(time1frequency, name1frequency)
avg1 = [time1frequency[i].seconds/(60*name1frequency[i]) for i in range(len(time1frequency))]
#avg2 = np.divide(time2frequency, name2frequency)
avg2 = [time2frequency[i].seconds/(60*name2frequency[i]) for i in range(len(time2frequency))]

print(avg1)
print(avg2)

plt.rc('font',family='Bahnschrift')
fig, ax1 = plt.subplots()
ax2 = ax1.twiny()

ax1.bar(range(1, len(avg1)+1), np.nan_to_num(np.array(avg1)), alpha=0.6, label=fullName1, color=color1, width=2)
ax1.bar(range(1, len(avg2)+1), -np.nan_to_num(np.array(avg2)), alpha=0.6, label=fullName2, color=color2, width=2)

bottom = -30
top = 30
ax1.set_ylim(bottom, top)
#ax2.set_ylim(-top, bottom)

ax2.set_xticks(range(len(months)))
ax2.set_xticklabels(months)

ax1.legend(loc='upper right', fontsize=18, frameon=False)

plt.show()
