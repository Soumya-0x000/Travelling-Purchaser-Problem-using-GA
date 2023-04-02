import random,time

count = 0
while True:
    if not count == 20 :
        shop_count=int(random.randint(10, 90))
        print("\n\n\033[91m\033[4m\033[1m(",count+1,") shop_count = ",shop_count,"\033[0m")
        print("\033[92m")
        position=[]
        j=0
        for i in range(shop_count): 
            position.append(j)
            j+=1
        print("\n\n",position)
        
        availability=[]
        for i in range(shop_count):
            availability.append(random.randint(1, 7) * 100)
        print("\n\n",availability) 

        require = 1000

        listoflist=[]
        for i in range(shop_count):
            list1=[]  
            list1.append(0)
            check=0 
            random.shuffle(position)
            while check <= require:
                no = random.choice(position)
                if no not in list1:
                    avail = availability[no]
                    list1.append(no)
                    check+=avail
                    if check >= require :
                        list1.append(0)
                        break           
            listoflist.append(list1)
        print("\n\n",listoflist)  
    print("\033[0m")  
    time.sleep(2)
    if count == 20 :
        exit()
    count+=1
