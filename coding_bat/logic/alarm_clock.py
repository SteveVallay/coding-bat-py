def alarm_clock(day,vacation):
    if vacation:
        if 0 < day < 6:
            return "10:00"
        else:
            return "off"
    else:
        if 0 < day < 6:
            return "7:00"
        else:
            return "10:00"


print alarm_clock(1,False)
print alarm_clock(5,False)
print alarm_clock(0,False)

