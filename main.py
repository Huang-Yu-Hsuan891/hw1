# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061136.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.
data = list(filter(lambda item: item['PRES'] != '-99.000' and item['PRES'] != '-999.000', data))
target_id = ['C0A880','C0F9A0','C0G640','C0R190','C0X260']
target_data=[]
for ID in target_id:
    d = list(filter(lambda item: item['station_id']==ID, data))
    if d:
        target_data.append(d)
    else:
        target_data.append([{'station_id':ID, 'PRES':float('0')}])

print(target_data)
ans=[]
cnt=0
for this_data in target_data:
    l = [float(x['PRES']) if x['PRES']!='0' else '0' for x in this_data]
    l = sum(l)/len(l)
    ans.append([target_id[cnt], l])
    cnt+=1
ans = sorted(ans)
for i in range(len(ans)):
    if((ans[i][1]) == 0.0):
    	ans[i][1] = 'None'
#=======================================

# Part. 4
#=======================================
# Print result
print(ans)
#========================================