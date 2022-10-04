# python program to check oracle alert log file for error in past 48 hours

#!/usr/bin/env python

import io
import datetime
import traceback

DayList=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
KeyWordList=['ORA-','Error','alter']
# KeyWordList=['ORA-','Error','Starting ORACLE instance','Shutting down instance']
OutputList=[]

# customize hours to look for 
SkipOldEventHours=48

# customize name of alert.log
AlertLogFile=r'alert_cisdbc.log'

SkipOldEventDateTimeDelta=datetime.timedelta(hours=SkipOldEventHours)
EventDate=datetime.datetime(1, 1, 1, 0, 0)

try:
    with io.open(AlertLogFile,mode='r') as f:
        for line in f:
           if len(line)>3 and line[0:3] in DayList:
                # OutputList.append(line)              
                EventDate=datetime.datetime.strptime(line.rstrip('\n'), '%a %b %d %H:%M:%S %Y')
                if EventDate < datetime.datetime.now()-SkipOldEventDateTimeDelta :
                    continue        
           elif len(line)>3:
                if EventDate < datetime.datetime.now()-SkipOldEventDateTimeDelta :
                    continue              
                for w in KeyWordList:
                    if w in line:
                        OutputList.append([EventDate,line.rstrip('\n')])
           else:
                continue
except:
    print(traceback.format_exc())

for o in OutputList:
    # use o[0].strftime('%a %b %d %H:%M:%S %Y') to get original Oracle style Format  
    print('[%s] %s' % (o[0],o[1]))

# the end