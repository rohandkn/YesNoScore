prefOrder = [["Montana"]]
locs = ["Montana",
"Seattle, WA",
"Redding, CA",
"Oregon",
"South Carolina",
"Las Vegas, NV",
"Georgia",
"New Orleans, LA",
"UK",
"Canada",
"Grand Canyon",
"Yellowstone",
"LA, CA",
"Yosemite",
"NYC, NY",
"Salt/Zion Lake (Utah)",
"Boston, MA",
"Colorado",
"Washington DC",
"San Diego, CA",
"Great Lakes",
"Hawaii",
"Philadelphia",
"Orlando",
"Texas",
"Chicago"]

print("1 for first option, 2 for second option, 3 for tie")
for i in range(1, len(locs)):
	done = False
	for j in range(0, len(prefOrder)):
		inputR = input(locs[i] + " or "+ prefOrder[j][0]+"? ")
		if inputR == "1":
			prefOrder.insert(j, [locs[i]])
			done = True
			break
		if inputR == "3":
			prefOrder[j].append(locs[i])
			done = True
			break
	if done == False:
		prefOrder.append([locs[i]])

if len(prefOrder) < 10:
	print("be more decisive")
if len(prefOrder) == 10:
	print("Wrote to placeScores.csv")
else:
	while(len(prefOrder)!=10):
		minLen = 99999
		saveMin = -1
		for i in range(1, len(prefOrder)):
			if(len(prefOrder[i])+len(prefOrder[i-1]) < minLen):
				minLen = len(prefOrder[i])+len(prefOrder[i-1])
				saveMin = i
		stuffToAdd = prefOrder[saveMin-1]
		prefOrder[saveMin] += (stuffToAdd)
		prefOrder.pop(saveMin-1)
	print("Wrote to placeScores.csv")

import csv
with open('placeScores.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(locs)):
    	foundIndex = -1
    	for j in range(0, len(prefOrder)):
    		if locs[i] in prefOrder[j]:
    			foundIndex = j
    			break
    	csvwriter.writerow([locs[i], (10-foundIndex)])





