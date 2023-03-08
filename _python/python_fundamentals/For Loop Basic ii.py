def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0 :
            arr[i]="big"

    return arr

def count_positives(arr):
    count=0
    for i in range(len(arr)):
        if arr[i] > 0 :
            count+=1

    arr.append(count)
    return arr

def sum_total(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    return total


def average(arr):
    total=sum_total(arr)
    return total/len(arr)

def  length(arr):
    length=0
    for i in range(len(arr)):
        length+=1
    return length

def minimum(arr):
    if len(arr)==0: return False
    min=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<min:
            min=arr[i]

    return min

def maximum(arr):
    if len(arr)==0: return False
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]

    return max

def ultimate_analysis(arr):
    return {'sumTotal': sum_total(arr), 'average': average(arr), 'minimum':minimum(arr), 'maximum':maximum(arr), 'length': length(arr) }


def  reverse_list(arr):
    
    for i in range(int(len(arr)/2)):
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]

    return arr

