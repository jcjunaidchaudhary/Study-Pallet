def convert_days(timetables,time):
    timetables_days = []
    for i in timetables:
        timetable=[]
        for idx,j in enumerate(i):
            days={}
            days.update({'time':time[idx],'M': j[0],"T": j[1],'W': j[2],"Th": j[3],"F": j[4]})
            timetable.append(days)
        timetables_days.append(timetable)

    return timetables_days


def am_pm(time):
    if int(time)<12:
        time=time+".00am"
    else:
        time=time+".00pm"
    return time