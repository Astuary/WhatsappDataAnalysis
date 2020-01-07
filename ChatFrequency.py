import datetime
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

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

plt.rc('font',family='Bahnschrift')
fig, ax1 = plt.subplots()
ax2 = ax1.twiny()

ax1.bar(range(1, len(name1frequency)+1), name1frequency, alpha=0.6, label=fullName1, color=color1, width=2)
ax1.bar(range(1, len(name2frequency)+1), -name2frequency, alpha=0.6, label=fullName2, color=color2, width=2)

ax2.set_xticks(range(len(months)))
ax2.set_xticklabels(months)

ax1.legend(loc='upper right', fontsize=18, frameon=False)
plt.show()
