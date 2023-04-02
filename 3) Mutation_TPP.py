from colorama import *
import random

def mutation():
    mutableBit = 5 #math.trunc(probOfMutation * totalBit)
    listofMutate = [[5, 2, 4, 1, 8], [3, 5, 6], [3, 6, 5], [5, 8, 1, 9], [5, 8, 1, 9], [1, 7, 2, 4, 6], [1, 7, 6, 2], [9, 4, 2, 5, 6], [9, 2, 4, 5, 8]]
    print(Style.BRIGHT,Fore.BLUE,mutableBit,"\n",listofMutate)
    
    def swap(swap,choice1,choice2):
        swap[choice1] , swap[choice2] = swap[choice2] ,swap[choice1]
        return swap
    
    mutatedList, selectedList, i, count = [], [], 0, 0
    position = []
    while 1:
        for i in range(len(listofMutate)):
            rnd_no =float(input("Enter no :")) #"{:.1f}".format(random.uniform(0.08, 0.11)) 
            index = [] 
            if float(rnd_no) < 0.1: 
                if i not in selectedList:
                    count += 1
                    for j in range(len(listofMutate[i])):
                        index.append(j)
                    while 1:
                        choice1 = random.choice(index)
                        choice2 = random.choice(index)
                        if choice1 != choice2:
                            break
                    mutatedList.append(swap(listofMutate[i], choice1-1, choice2-1))
                    selectedList.append(i)
                    listofMutate[i] = mutatedList[i]
                    position.append(i)
                    if count == mutableBit:
                        break
                else:
                    continue
            else:
                if i not in position:
                    position.append(i) 
                    mutatedList.append(listofMutate[i])
                    if count == mutableBit:
                        break 
                    continue
                else:
                    continue
            if count == mutableBit :
                break
            else:
                continue
        if count == mutableBit :
            break
        else:
            continue
        
    print(Style.BRIGHT,Fore.GREEN,"\nMutated List : ",listofMutate)
    
mutation()