def thingsidid():
        
    dictionary = {1:{"Terrorists": ["sadan hussein","Jhon pork"]},2:{"Axis": ["germany","hungary","italy","slovakia","Japan"]}}
    print(dictionary[1]["Terrorists"]) #wil print only terrorists 
    dictionary[1]["Terrorists"][0] = "niga"
    print(dictionary)

    del dictionary[1]["Terrorists"]
    print(dictionary)



#SETS NOOOOOO I'M BAD AT MATH

    bbc = {1:"a",2:"b"} #thats a key tingy
    bbc = set()
    print(type(bbc))

    natural = {1,2,3,4,5,6,7}
    steroidusers = {"Károly","Lakatos","nagyfero",8,9,0}
    print(natural)
    print(steroidusers)
    print(type(natural),(type(steroidusers))) #prints that this is a set


    days = {"monday-left-me-broken","Tuesday-i-was-trought-the-hoppen?","Wendsday-my-arms-tututut","Thursday","Friday","Saturday","Sunday"}
    print(days)

    for x in days:
        if x == ("Friday"):
            print(x)

    #for days in days:
        #print(days)

    for i in days:
        if i == ("Sunday"):
            print(i)
            for days in days:
                if days == ("Sunday"):
                    print(days,"Hiii")

    #Operations with sets 
    set1 = {1,2,3,4,5}
    set2 = {2,4,6,8,7}
    set3 = {9,1,5,7}
    print(set1|set2) #ass i see it prints all of them combined 
    print(set1.union(set2)) #does the same so its union
    print(set1.intersection(set2)) #the intersection the indise both of them the gray one
    print(set1 & set2) #DOES THE SAMETHING AND SAVES TIME AND CHARACTERS USEE THIS this one ia a must use 
    print(set1 - set2) #set difrence
    print(set1.difference(set2)) #set difence but longer 
    print(set3 - set2 - set1)
    print(set3 & set2 , set3|set1)


#built in function sets

    set01 = {"Bbcteamvarmostrad",2,3,4,5,6}
    set02 = {1,2,3,4,5,6,7,8,0,11,12,13}
    print(len(set01))  #prtins the lengts  of each element the "bbcteamvarmostrad" counts as 1
    #print(max(set01)) #This will get you an error becasue "" is in the set 01
    print(max(set02)) #prints higest number in the set can be usefull for highscores or latency highest ping etc highest spending
    print(min(set02)) #prints the lowest number in the set can be usefull for fastes time speedrun or cheapest thing lowest povertyrate
    print(sorted(set02)) #sorts it  from smallest all the way to highest nuzmber in the  set
    set03 = {"A","B","C","E","D","G","F"}
    print(sorted(set03)) #sorts it acccording to alphabetic order
    set04 = {1,5,10}
    print(sum(set04)) #adds all the numbers together  with sum 

    set04.add(4) #adds 4
    set04.update([8, 9]) #TO add multiple elemetns iinstead of doing add and add because this is time saving for single operatioons use .add
    print(sum(set04))

    age = {23,22,34,36,24,41}
    print(max(age),len(age))
    print(max(age))
    print(len(age))

    for x in age:
        max(age) == x
        print(x) #doe sthe same thing as print(max(age),len(age)) would do

    for i in age:
        if "24" in age:
            len(age) == i
            print(i) #idk wtf i wanted to do here 

    age = {23,22,34,36,24,41}
    print(max(age),len(age))
    print(max(age))
    print(len(age))

    for x in age:
        if x == max(age):
            print(len(str(x))) #converts the age into a string and checks the digits 
            int(x) #converts back it into a integer int 

        print(x)

    #Set methods
        asdsd = {1:"sad"}
        bbc = {1,3,4}

        print(type(asdsd))
        print(type(bbc))

    zazausers = {1,2,3,4,7.3}
    cocoausers = {4,6,7.3,0}

    print(zazausers.intersection(cocoausers)) #prints the thing thats in both of them at the same time
    zazausers.add(4) #adds one
    zazausers.update([8, 3, 7])
    print(zazausers)
    print(zazausers.intersection(cocoausers))
    #POLICE RAIDED ZAZA USERSS HHAHA THEY GOT ARRESTed
    zazausers.clear()
    print(zazausers)
    zazausers.update([2,4,5,6,7,])
    print(zazausers)
    zazausers.copy()
    bb = {}
    print(zazausers.copy()) #returns a copy of a set

    print(zazausers - cocoausers) #or
    print("hi")
    print(zazausers)
    print(zazausers.difference(cocoausers))
    print(zazausers.discard(5)) #removes a specific thing from set if its a member = if its inside the set 
    print(zazausers)
    age = {23,22,34,24,41}
    age.add(56)
    print(age)

    age.remove(22)
    print(age)

    age.pop() #removes first thing accours in a set example {23,24,25} it rmves 23
    print(age)

    a = {1,2,4,5}
    b = {2,4,6,8,5,1}
    c = {100,101,102}
    print(a.issubset(b)) #run this part and udnerstand logic (részhalmaz) subset
    print(b.issuperset(a)) #run this part and udnerstand logic (nagyhalmaz) uperset

    print(a.isdisjoint(b)) #returns fasle beacuse there are common elements betwen a and c  and they are in intercetion(metszetbe vannak)
    print(b.isdisjoint(c)) #returns true due to no comon elements in a and c

    Whitenation = {"W","H","I","T","P","E","O","P","L","e",}
    Whitenation.discard("Z") #no error but it can't remove any z since its not found pretty cool 
    print(Whitenation) #gives it to be but scrambled shuffled
    #Whitenation.remove("z") #keyerror since there isn't a z 
