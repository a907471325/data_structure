#
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

gas =[5,1,2,3,4]
cost = [4,4,1,5,1]

total_gas = 0
for i in range(len(gas)):
    total_gas += gas[i] - cost[i]
if total_gas < 0:
    print(-1)

start = 0

current_gas = 0
start_station = 0
for i in range(len(gas)):
    current_gas += gas[i] - cost[i]
    if current_gas >= 0:
        continue

    while current_gas < 0:
        start_station = start_station - 1 if start_station != 0 else len(gas) - 1
        current_gas += gas[start_station] - cost[start_station]

print (start_station + 1)