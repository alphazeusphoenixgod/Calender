import math

date = input("enter the date: ")
month = input("enter the month: ")
year = input("enter the last two digits of the year: ")
centuryyear = input("enter the century year (for example if your year is 1947 the century year will be 1900): ")

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

if (month == months[0]):
    if ( int(year) % 4 == 0 ):
        jan123 = 5
    else:
        jan123 = 6
    
if ( month == months[1]):
    if ( int(year) % 4 == 0 ):
        feb123 = 4
    else:
        feb123 = 2

if ( month == months[2]):
    mar123 = 2

if ( month == months[3]):
    apr123 = 5

if ( month == months[4]):
    may123 = 0

if ( month == months[5]):
    jun123 = 3

if ( month == months[6]):
    jul123 = 5

if ( month == months[7]):
    aug123 = 1

if ( month == months[8]):
    sep123 = 4

if ( month == months[9]):
    october123 = 6

if ( month == months[10]):
    nov123 = 2

if ( month == months[11]):
    dec123 = 4



k1 = (math.floor(5 * int(year)/4)) % 7 
dummy = int(centuryyear) % 400
dummy1 = dummy / 100
dummy3 = dummy1 * 5
k2 = dummy3 % 7


if (month == months[0]):
    dummyresult = (int(date)  + jan123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[1]):
    dummyresult = (int(date)  + feb123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[2]):
    dummyresult = (int(date)  + mar123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[3]):
    dummyresult = (int(date)  + apr123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[4]):
    dummyresult = (int(date)  + may123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[5]):
    dummyresult = (int(date)  + jun123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[6]):
    dummyresult = (int(date)  + jul123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[7]):
    dummyresult = (int(date)  + aug123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[8]):
    dummyresult = (int(date)  + sep123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[9]):
    dummyresult = (int(date)  + october123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[10]):
    dummyresult = (int(date)  + nov123 + k1 + k2) % 7
    result = str(dummyresult)

if (month == months[11]):
    dummyresult = (int(date)  + dec123 + k1 + k2) % 7
    result = str(dummyresult)


if (result == 0):
    print("The day on the given date was Sunday")

elif (result == 1):
    print("The day on the given date was Monday")

elif (result == 2):
    print("The day on the given date was Tuesday")

elif (result == 3):
    print("The day on the given date was Wednesday")

elif (result == 4):
    print("The day on the given date was Thursday")

elif (result == 5):
    print("The day on the given date was Friday")

elif (result == 6):
    print("The day on the given date was Saturday")




















# if (month == "jan") or (month == "january") or (month == "Jan") or (month == "January") or (month == "JANUARY"):
#     mj = int(month) / 4
#     if ( float(mj) == True ):
#         jan = 6
#     else:
#         jan = 5

# if (month == "feb") or (month == "february") or (month == "Feb") or (month == "February") or (month == "FEBRUARY"):
#     mf = int(month) / 4
#     if ( float(mf) == True ):
#         feb = 2
#     else:
#         feb = 1

# if (month == "march") or (month == "March") or (month == "MARCH"):
#     march = 2

# if (month == "april") or (month == "April") or (month == "APRIl"):
#     april = 5

# if (month == "may") or (month == "May") or (month == "MAY"):
#     may = 0

# if (month == "june") or (month == "June") or (month == "JUNE"):
#     june = 3

# if (month == "july") or (month == "July") or (month == "JULY"):
#     july = 5

# if (month == "august") or (month == "August") or (month == "AUGUST"):
#     august = 1

# if (month == "sept") or (month == "september") or (month == "Sept") or (month == "September") or (month == "SEPTEMBER"):
#     sept = 4

# if (month == "oct") or (month == "october") or (month == "Oct") or (month == "October") or (month == "OCTOBER"):
#     october = 6

# if (month == "november") or (month == "November") or (month == "NOVEMBER"):
#     nov = 2

# if (month == "dec") or (month == "december") or (month == "Dec") or (month == "December") or (month == "DECEMBER"):
#     dec = 4