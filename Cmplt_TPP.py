import random, math, datetime, shutil
from math import sqrt
from colorama import *

now = datetime.datetime.now()
random.seed(0)

def main():
    
    print(Style.BRIGHT+Fore.YELLOW,"\n1) Gen : ")
    def initital_pop(shop_count, require):
        print(" Initial Population ".center(shutil.get_terminal_size().columns,'='))
        position = [i for i in range(shop_count)]

        print("\033[96m","\nAvailability : ",availability)  
        
        listofInitial_pop , total_quantity, quantity_per_shop = [], [], []
        for i in range(initital_popSize):
            list1, quantity, charge = [], [], []  
            list1.append(0)
            check=0 
            while check <= require:
                no = random.choice(position)
                if no not in list1:
                    avail = float("{:.2f}".format(random.uniform(0.5, 1))) * availability[no]
                    quantity.append(avail)
                    list1.append(no)
                    check+=avail
                    if check >= require :
                        list1.append(0)
                        quantity.append(0)
                        quantity_per_shop.append(quantity)
                        break          
            listofInitial_pop.append(list1)
        
        print(Style.BRIGHT+Fore.BLUE,"\nInitial Population : ",listofInitial_pop)              # According to availability 
        print("\nPurchasing cost : ", costPerUnit)
        
        shopList = []
        for i in range(shop_count):
            list1= []
            for j in range(2):
                list1.append(int(random.random() * 100))
            shopList.append(list1)
            
        print("Coordinates of each shop :",shopList)

        print(Style.BRIGHT+"\033[92m","\nDistance Matrix : \n")
        def f(city, i, j):
            k = sqrt((city[i][0]-city[j][0])**2 + (city[i][1] - city[j][1])**2)
            # print(abs(k))
            return abs(k)

        def main(city):
            matrx = [[ 9999 if i==j else f(city,i,j) for i in range(len(city))] for j in range(len(city))]
            return matrx

        if __name__ == "__main__":
            city = shopList
            k = main(city)
            global listofrow
            listofrow = []
            for i in range(len(k)):
                row=[]
                for j in range(len(k)):
                    dist_mat = "{:.2f}".format(k[i][j])
                    print(dist_mat,end="\t")
                    row.append(dist_mat)
                listofrow.append(row)
                print()   
        
        global listofdistance
        listofdistance, access_list = [], []
        for i in range (len(listofInitial_pop)) :    
            x=0
            apnd=[]  
            for j in range (len(listofInitial_pop[i]) - 1):
                access_list = listofInitial_pop[i]        
                for k in access_list :
                    x+=1
                    a=listofrow[k][access_list[x]]
                    apnd.append(a)               
                    if(len(apnd)==(len(access_list)-1)):
                        listofdistance.append(apnd)
                        break
                break
        
        global LIST
        LIST = []
        for i in range(len(listofrow)):
            fltlistofrow = []
            for j in range(len(listofrow[i])):
                fltlistofrow.append(float(listofrow[i][j]))
                if len(fltlistofrow) == len(listofrow[i]):               
                    LIST.append(fltlistofrow)
                    break      
        
        fitness,  listOfCost, charge_per_shop, quantity_per_shop = fitness_calculate(listofInitial_pop, quantity_per_shop)
        print("\033[91m","\nFitness : ",fitness)                 # Calculate fitness by adding elements of UnorganisedDistMat[]
      
        OrganisedlistofInitial_pop = organise(fitness, listofInitial_pop, listOfCost)
        Organised_quantity_per_shop = organise(fitness, quantity_per_shop, listOfCost)
        
        global mating_pool, Ordered_quantity
        mating_pool, listx, mpool, Rest_Charge, Ordered_quantity  = [], [], [], [], []
        same = math.trunc(len(OrganisedlistofInitial_pop) * eliteRate)
        for i in range(2):
            if len(mating_pool) < same:        
                for j in range(same):
                    mating_pool.append(OrganisedlistofInitial_pop[j])
                    Ordered_quantity.append(Organised_quantity_per_shop[j])
                    if len(mating_pool) == same :                   
                        for k in range(len(mating_pool) , len(OrganisedlistofInitial_pop)):
                            listx.append(OrganisedlistofInitial_pop[k])
                            Rest_Charge.append(Organised_quantity_per_shop[k])
                        break
            elif len(mating_pool) == same:
                for k in range(len(listx)):
                    while 1:
                        chosenList = random.choice(listx)
                        if chosenList not in mating_pool:
                            mating_pool.append(chosenList)
                            Ordered_quantity.append(Organised_quantity_per_shop[OrganisedlistofInitial_pop.index(chosenList)])
                            break      
        print("\nOrdered quantity : ",mating_pool)   
        
        
    global Crossover
    def Crossover(population, probOfCrossOver):
        print(Fore.CYAN)
        print(" Crossover ".center(shutil.get_terminal_size().columns,'='))
        print("\nParent for gen ",Fore.RED, gen_no , Fore.CYAN," CROSSOVER : ", population,Fore.GREEN,"\n")

        def generateChild(index):
            offspring, mpool_quantity = [], []
            # for i in index:
            #     print("\nparents : ",i,"\t",population[i])
            for x in range(len(index)):
                parent1, parent2 = population[index[x]], population[index[x+1]]
                quantity1, quantity2 = Ordered_quantity[index[x]], Ordered_quantity[index[x+1]]
                # print(parent1, "\t", quantity1,"\t", parent2, "\t", quantity2)
                child,  store = [], []
                len2, len3  = len(parent1), len(parent2)
                i, j, point, x, y = 1, 1, 0, 0, 0
                sum = 0
                child.append(point)
                while i < len2 or j < len3 :
                    if i < len2 and j < len3 :
                        if (LIST[point][parent1[i]]*travelling_cost)+(quantity1[x]*costPerUnit[parent1[i]]) < (LIST[point][parent2[j]]*travelling_cost)+(quantity2[y]*costPerUnit[parent2[j]]):
                            point = parent1[i]
                            sum += point
                            if parent1[i] not in child:
                                child.append(parent1[i])
                                store.append(quantity1[x])
                                x += 1
                                i += 1
                            else:
                                x += 1
                                i += 1
                        elif (LIST[point][parent1[i]]*travelling_cost)+(quantity1[x]*costPerUnit[parent1[i]]) == (LIST[point][parent2[j]] * travelling_cost)+(quantity2[y]*costPerUnit[parent2[j]]):
                            point = parent1[i]
                            sum += point
                            if parent1[i] not in child:
                                child.append(parent1[i])
                                store.append(quantity1[x])
                                x += 1
                                y += 1
                                i += 1
                                j += 1
                            else:
                                x += 1
                                y += 1
                                i += 1
                                j += 1
                        else:
                            point = parent2[j]
                            sum += point
                            if parent2[j] not in child:
                                child.append(parent2[j])
                                store.append(quantity2[y])
                                y += 1
                                j += 1
                            else:
                                y += 1
                                j += 1
                    elif i < len2 :
                        point = parent1[i]  
                        sum += point
                        if point not in child:
                            child.append(point) 
                            store.append(quantity1[x])
                            x += 1
                            i += 1
                        else:
                            x += 1
                            i += 1
                    elif j < len3:
                        point = parent2[j]
                        sum += point
                        if parent2[j] not in child:
                            child.append(parent2[j])
                            store.append(quantity2[y])
                            y += 1
                            j += 1
                        else:
                            y += 1
                            j += 1
                child.append(0)
                store.append(0)
                offspring.append(child)
                mpool_quantity.append(store)
                if len(offspring) == len(index)-1:
                    break
            # print("\nChildren: ",offspring, "\t",len(offspring),"\t",mpool_quantity,"\t", len(mpool_quantity),"\t") 
            return offspring, mpool_quantity
        
        CrossoverRate = math.trunc(probOfCrossOver * shop_count) 
        xoverindex, count , sublist = [], 0, []
        while 1:
            for i in range(len(population)):
                rnd_no = "{:.2f}".format(random.uniform(0.30, 0.70))
                if(float(rnd_no)) < 0.5:
                    if i not in xoverindex:
                        xoverindex.append(i)
                        if len(xoverindex) == 3:
                            #print("\n",xoverindex)
                            sublist.extend(xoverindex)
                            offspring = []
                            offspring, mpool_quantity = generateChild(xoverindex)
                            # print(Fore.GREEN, "\npopulation: ",population,"\n")
                            for i in range(len(offspring)):
                                population[xoverindex[i]] = offspring[i]
                                Ordered_quantity[xoverindex[i]] = mpool_quantity[i]
                            # for i in xoverindex:
                            #     print("\nparents : population [",i,"]\t",population[i])
                            # print("\n", Fore.CYAN)
                            # print(" xover ".center(shutil.get_terminal_size().columns,"."))
                            xoverindex = []
                            count+=1
                            break
                else:
                    continue 
            if count == CrossoverRate:
                break
            else:
                continue
        
        print("Selected parents for crossover: ", *sublist, sep=' ')
        for i in range(initital_popSize):
            if (i == 0):
                print("Non-Selected parents for crossover: ", end= ' ')
            if i not in sublist:
                print(i,end=' ')

        print("\n\nMating Pool : ",population)
        [x.insert(0, 0) for x in Ordered_quantity]
        # [print(len(population[i]),"\t",len(Ordered_quantity[i]),"\t",sum(Ordered_quantity[i]),"\t",population[i],"\t",Ordered_quantity[i]) for i in range(len(population))]
        global children, charge_per_child
        children, charge_per_child  = [], []
        for i in range(len(population)):
            list1, list2 = [], []
            list1.append(0)
            list2.append(0)
            total = 0
            for j in range(1,len(population[i])+1):
                total += Ordered_quantity[i][j]
                if  total < require:
                    list1.append(population[i][j])
                    list2.append(Ordered_quantity[i][j])
                elif total >= require:
                    list1.append(population[i][j])
                    list2.append(Ordered_quantity[i][j])
                    list1.append(0)
                    list2.append(0)
                    break
            children.append(list1)
            charge_per_child.append(list2)
        print(Style.BRIGHT+Fore.MAGENTA,"\nChildren : ",children,"\n")
                    
    
    global Mutation
    def Mutation(chromosome, gen_no):
        print(" Mutation ".center(shutil.get_terminal_size().columns,'='))
        mutableBit = math.trunc(mutationRate * len(chromosome))
        print("\nMutable child : ",mutableBit)

        global listofMutate, listofPrice
        listofMutate, listofPrice = [], []
        for i in range(len(chromosome)):
            mutate, price = [], []
            for j in range(1,len(chromosome[i])-1):
                mutate.append(chromosome[i][j])
                price.append(charge_per_child[i][j])
                if len(mutate) == len(price) == len(chromosome[i])-2:
                    listofMutate.append(mutate)
                    listofPrice.append(price)
                    break

        def swap(swap,choice1,choice2):
            swap[choice1] , swap[choice2] = swap[choice2] ,swap[choice1]
            return swap
        
        mutatedList, mutated_Charge, selectedList, position, i, count = [], [], [], [], 0, 0
        while 1:
            for i in range(len(listofMutate)):
                rnd_no ="{:.2f}".format(random.uniform(0.08, 0.11)) 
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
                        mutated_Charge.append(swap(listofPrice[i], choice1-1, choice2-1))
                        listofMutate[i] = mutatedList[i]
                        listofPrice[i] = mutated_Charge[i] 
                        selectedList.append(i)
                        position.append(i)
                        if count == mutableBit:
                            break
                    else:
                        continue
                else:
                    if i not in position:
                        position.append(i) 
                        mutatedList.append(listofMutate[i])
                        mutated_Charge.append(listofPrice[i])
                        if count == mutableBit:
                            break 
                        continue
                    else:
                        continue
                if count == mutableBit:
                    break
                else:
                    continue
            if count == mutableBit:
                break
            else:
                continue
        
        for i in range(len(listofMutate)):
            listofMutate[i].insert(0 , 0)
            listofPrice[i].insert(0, 0)
            listofMutate[i].append(0)
            listofPrice[i].append(0)
        print(Style.BRIGHT,Fore.RED,"\nMutated List : ",listofMutate)
        
        global mutationFitness, organisedListOfMutate, order_quantity_per_shop
        mutationFitness, listofPrice, charge_per_shop, quantity_per_shop = fitness_calculate(listofMutate, listofPrice)
        organisedListOfMutate = organise(mutationFitness, listofMutate, listofPrice)
        order_quantity_per_shop = organise(mutationFitness, quantity_per_shop, listofPrice)
        
        print(Style.BRIGHT+Fore.YELLOW,"\n", gen_no ,"""\b) Gen best results : 
    Fitness : """,mutationFitness[0],"\t\t",
    """Child : """,organisedListOfMutate[0],"\n")
        
        print("\n\n",organisedListOfMutate)
        print(now.strftime("%H:%M:%S"),"\n")
        

    def fitness_calculate(chromosomes, quantity_per_shop):
        listOfCost, charge_per_shop = [], []
        #print("\n",quantity_per_shop)
        for i in range(len(quantity_per_shop)):
            TotalCost = []
            add = 0
            for j in range(len(quantity_per_shop[i])):  
                add += quantity_per_shop[i][j]
                if add > require:
                    greater = add - require
                    add -= quantity_per_shop[i][j]
                    smaller = quantity_per_shop[i][j] - greater
                    add += smaller
                    TotalCost.append(costPerUnit[chromosomes[i][j+1]] * smaller)
                    quantity_per_shop[i][j] = smaller
                    break
                elif add == require:
                    TotalCost.append(quantity_per_shop[i][j] * costPerUnit[chromosomes[i][j+1]])    
                    break
                TotalCost.append(quantity_per_shop[i][j] * costPerUnit[chromosomes[i][j+1]])
                charge_per_shop.append(TotalCost)
            listOfCost.append(sum(TotalCost))
    
        # Distance Matrix according to listofInitial_pop[]  -->UnorganisedDistMat[]
        global UnorganisedDistMat
        UnorganisedDistMat, fitness = [], []                 
        for i in range(len(listofdistance)) :
            UnorganisedDistMat.append(listofdistance[i])
            for j in range(len(UnorganisedDistMat)):
                add = 0
                for k in range(len(UnorganisedDistMat[j])):
                    UnorganisedDistMat[j][k] = float(UnorganisedDistMat[j][k]) 
                    add = UnorganisedDistMat[j][k]+float(add)   
            fitness.append("{:.2f}".format(add))
        # print(fitness)
        for i in range(len(fitness)):
            fitness[i] = float("{:.2f}".format(float(fitness[i]) + listOfCost[i]))
        fitness.sort()
    
        return fitness, listOfCost, charge_per_shop, quantity_per_shop


    def organise(fitness, chromosomes, listOfCost):
        UnorganisaedFitness=[]
        for i in range(len(UnorganisedDistMat)):
            UnorganisaedFitness.append(float("{:.2f}".format(sum(UnorganisedDistMat[i])+listOfCost[i])))                     

        OrganisedDistMat = []
        for i in range(len(UnorganisaedFitness)):
            OrganisedDistMat.append(UnorganisedDistMat[UnorganisaedFitness.index(fitness[i])])
        
        Organisedchromosomes = []
        for i in range(len(chromosomes)):
            Organisedchromosomes.append(chromosomes[UnorganisedDistMat.index(OrganisedDistMat[i])])

        return Organisedchromosomes

    initital_pop(shop_count, require)
    Crossover(mating_pool, probOfCrossOver)
    Mutation(children, gen_no)

      
if __name__ == "__main__":
    while True:    
        print(Style.BRIGHT+Fore.MAGENTA)
        shop_count = int(input("\nEnter number of shops : "))
        initital_popSize = 20
        
        availability = [(random.randint(1, 8) * 100) for i in range(shop_count-1)]
        availability.insert(0, 0)
        print("Availability : ",availability)
        print("Total available content : ",sum(availability))
        
        while 1:
            print("Requirement should be less than", sum(availability)/2)
            require =  int(input("Enter your requirement : "))
            if require < sum(availability)/2 :
                break
            else:
                continue
            
        eliteRate = 0.2             # first 20% from the initial population is taken in mating pool just the way it was
        probOfCrossOver = 0.5
        mutationRate = 0.1
        generation = int(input("\nUpto how many generations you want to run : "))
        bestFitness, unsortedBestFitness = [], []
        travelling_cost = 5
        
        for i in range(generation):
            gen_no = i+1
            costPerUnit = [random.randint(10, 15) for i in range(shop_count-1)]
            costPerUnit.insert(0, 0)
            if i == 0:
                main() 
            elif i > 0:
                print(Style.BRIGHT+Fore.YELLOW)
                print(str(i+1).center(shutil.get_terminal_size().columns,'_'))       
                print("\n", gen_no , "\b) Gen : ")     
                
                for i in range(len(order_quantity_per_shop)): 
                    order_quantity_per_shop[i].pop(0)
                Ordered_quantity = order_quantity_per_shop
                
                Crossover(organisedListOfMutate, probOfCrossOver)
                Mutation(children, gen_no)
                
                bestFitness.append(mutationFitness[0])
                unsortedBestFitness.append(mutationFitness[0])

        print("\nFitness List : ", Style.BRIGHT+Fore.MAGENTA, bestFitness)
        bestFitness.sort()
        overallBestFitness = bestFitness[0]
        bestGen = unsortedBestFitness.index(overallBestFitness)
        
        print(Style.BRIGHT,Fore.BLUE,"\nGeneration no",Fore.RED,bestGen+2,Style.BRIGHT,Fore.BLUE,"generates the optimal fitness value, that is :",Fore.RED, overallBestFitness)
        
        print(Fore.CYAN,"\033[1m","\n\n","\033[4m","HURRAH!!!!!!!!, Eureka Eureka, WE DID IT","\033[0m","😘😘😘😘😎😎😎😎🔥🔥🔥🔥🤩🤩🤩🤩")  
        print("\n\n")

        print(Style.BRIGHT+Fore.GREEN)
        user_input = input("Enter alphabet to continue or anything to exit: ")
        if user_input.isalpha():
            continue
        else:
            print("Exiting..........")
            break