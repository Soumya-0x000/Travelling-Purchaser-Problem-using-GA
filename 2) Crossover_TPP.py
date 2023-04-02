list1 =  [[0.0, 26.25, 58.14, 58.05, 53.91, 32.76, 42.8], [26.25, 0.0, 80.78, 81.93, 63.6, 57.27, 69.03], [58.14, 80.78, 0.0, 7.07, 42.54, 26.17, 32.56], 
        [58.05, 81.93, 7.07, 0.0, 48.7, 25.32, 27.46], [53.91, 63.6, 42.54, 48.7, 0.0, 42.95, 61.4], [32.76, 57.27, 26.17, 25.32, 42.95, 0.0, 19.1], 
        [42.8, 69.03, 32.56, 27.46, 61.4, 19.1, 0.0]]

cost1 = [34, 35, 85, 92, 16]
cost2 = [53, 62, 86, 66, 25]

list2 = [0,3,2,1,4,6,0]
list3 = [0,4,5,2,3,1,0]
 
list4 = []
len2 = len(list2)
len3 = len(list3)
 
i , j , point = 1, 1, 0
sum = 0
list4.append(point)
while i < len2 or j < len3:
    if i < len2 and j < len3:
        if list1[point][list2[i]] < list1[point][list3[j]]:
            point = list2[i]
            print(point)
            sum += point
            print(sum)
            if list2[i] not in list4:
                list4.append(list2[i])
                i+=1
            else:
                i += 1
        elif list1[point][list2[i]] == list1[point][list3[j]]:
            point = list2[i]
            sum += point
            if list2[i] not in list4:
                list4.append(list2[i])
                i+=1
                j+=1
            else:
                i += 1
                j += 1
        else:
            point = list3[j]
            sum += point
            if list3[j] not in list4:
                list4.append(list3[j])
                j += 1
            else:
                j+=1
    elif i < len2 :
        point = list2[i]
        sum += point
        if point not in list4:
            list4.append(point) 
            i += 1
        else:
            i+=1
    elif j < len3:
        point = list3[j]
        sum += point
        if list3[j] not in list4:
            list4.append(list3[j])
            j += 1
        else:
            j+=1
    # if point == 0 or sum > 1000:
        # break
list4.append(0)
print(list4)