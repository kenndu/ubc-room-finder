
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
        if len(room) != 0:    
            finalStr = room + '.'+ current_day + '.' + '["' + '","'.join(time_range) + '"]'
            result.write(finalStr + "\n")
        f.flush()
        result.flush()
    if len(line) == 0:
        break

f.close()
result.close()

print("done!")
       




            
        







