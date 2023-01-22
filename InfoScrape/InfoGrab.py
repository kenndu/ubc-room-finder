
def combineTime(first,second):
    test = first[:]
    test2 = second[:]

    count1 = len(test)
    count2 = len(test2)

    if ":" not in test or ":" not in test2:
        return test + test2

    if count2 == 0 or count1 == 0:
        return test + test2

    endtime = test[count1-1]
    start2 = test2[0]
    (h,m) = endtime.split(':')
    (h2,m2) = start2.split(':')

    t1 =  int(h) * 3600 + int(m)*60
    t2 = int(h2) * 3600 + int(m2)*60

    if t2 <= t1:
        z = test.pop(count1-1)
        g = test2.pop(0)
    
    return test + test2


f = open('test.txt')

result = open('result.txt','w')

current_day = ""
room = ""
time_range = []
final_ranges = []



for i in range(20):
    line = f.readline()
while f:
    line = f.readline()
    if "<p><span class='labelone'>" in line:
        #print(final_ranges)
        num = len("<p><span class='labelone'>")
        current_day = line[num:num+3]
        #print(current_day)
    if "<tr>" in line and len(line) == 5:
        time_range = []
        for i in range(6):  
            line = f.readline()
        room = line[4:-6]
        #print(room)
        for i in range(4):  
            line = f.readline()
        time_range.append(line[4:-6])
        line = f.readline()
        time_range.append(line[4:-6])    
        finalStr = room + '.'+ current_day + '.' + '["' + '","'.join(time_range) + '"]'
        result.write(finalStr + "\n")
        f.flush()
        result.flush()

f.close()
result.close()

print("done!")
       




            
        







