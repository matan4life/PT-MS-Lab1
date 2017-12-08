import math
import random
def Randomchik():
    length=random.randint(2, 40)
    list=[]
    for i in range (0, length):
        list.append(random.randint(0, 100))
    return list
def BubbleSort(collection):
    for i in range (0, len(collection)):
        for j in range (i, len(collection)):
            if (collection[i]>collection[j]):
                t=collection[i]
                collection[i]=collection[j]
                collection[j]=t
    return collection
def EmpiricalMean(collection):
    sum=0
    for i in range(0, len(collection)):
        sum+=collection[i]
    return sum/len(collection)
def SampleVariance(collection):
    sum=0
    for i in range (0, len(collection)):
        sum+=pow(collection[i]-EmpiricalMean(collection), 2)
    return sum/(len(collection)-1)
def StandartDeviation(collection):
    return SampleVariance(collection) ** 0.5
def Median(collection):
    temp=BubbleSort(collection)
    if (len(temp)%2==1):
        return temp[int((len(temp)-1))//2]
    else:
        return ((temp[int(len(temp)/2)]+temp[int(len(temp)/2-1)])/2)
def Mode(collection):
    temp=BubbleSort(collection)
    max=0
    counter=1
    mod=[]
    for i in range(0, len(temp)-1):
        if (i==len(temp)-2 and temp[i]==temp[i+1] and counter+1>max):
            max=counter+1
            counter=1
        if (temp[i]==temp[i+1]):
            counter+=1
        else:
            if (counter>max):
                max=counter
            counter=1
    c1=1
    if (max==1):
        return "No mode here"
    else:
        for i in range (0, len(temp)-1):
            if (i==len(temp)-2 and temp[i]==temp[i+1] and c1+1==max):
                mod.append(str(temp[i]))
            if (temp[i]==temp[i+1]):
                c1+=1
            else:
                if (c1==max):
                    mod.append(str(temp[i]))
                c1=1
        return mod
def MaxandMin(collection):
    temp=BubbleSort(collection)
    res=[str(temp[0]), str(temp[len(temp)-1])]
    return res
def Range(collection):
    return (int(MaxandMin(collection)[1])-int(MaxandMin(collection)[0]))
def Quantile(collection, value):
    temp=BubbleSort(collection)
    K=math.floor(value*(len(temp)-1))
    if (K+1<(value*len(temp))):
        return temp[K+1]
    elif (K+1==(value*len(temp))):
        return ((temp[K]+temp[K+1])/2)
    else:
        return temp[K]
def Console():
    list=[]
    while (1):
        s=input()
        if (s=="exit"):
            break
        elif (s=="newcol"):
            print("Enter values of the list in one line")
            list=[int(i) for i in input().split(" ")]
        elif (s=="gen"):
            print ("Generating your sequence....")
            list=Randomchik()
        elif (s=="help"):
            print ("Enter some commands from the list below")
            print ("newcol - create new collection")
            print ("emean - find empirical mean")
            print ("svar - find sample variance")
            print ("sdev - find standart deviation")
            print ("med - find median")
            print ("mod - find mode")
            print ("mam - find maximum and minimum value")
            print ("ran - find range")
            print ("qua - find some determined quantiles")
            print ("out - print your variance")
            print ("gen - generate your sequence by random generator")
            print ("exit - close program")
        else:
            if (len(list)==0):
                print ("Your list is empty! Add some elements")
            else:
                if (s=="emean"):
                    print (str(EmpiricalMean(list)))
                elif (s=="svar"):
                    print(str(SampleVariance(list)))
                elif (s=="sdev"):
                    print(str(StandartDeviation(list)))
                elif (s=="med"):
                    print(str(Median(list)))
                elif (s=="mod"):
                    print(' '.join(Mode(list)))
                elif (s=="mam"):
                    print(' '.join(MaxandMin(list)))
                elif (s=="ran"):
                    print (str(Range(list)))
                elif (s=="qua"):
                    print("Quantile of 0.1 equals "+str(Quantile(list, 0.1)))
                    print("Quantile of 0.25 equals "+str(Quantile(list, 0.25)))
                    print("Quantile of 0.5 equals "+str(Quantile(list, 0.5)))
                    print("Quantile of 0.75 equals "+str(Quantile(list, 0.75)))
                elif (s=="out"):
                    s=""
                    for i in range (0, len(list)):
                        s+=str(list[i])+" "
                    print("Your variance is: ["+s+"]")
                else:
                    print("You've entered wrong command. Try again")
Console()
