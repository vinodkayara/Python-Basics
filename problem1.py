def highest_frequency_string(n,arr):
    frequency={}
    for string in arr:
        if string in frequency:
            frequency[string]+=1
        else:
            frequency[string]=1
    max_freq=0
    result=""
    for string in arr:
     if frequency[string]>max_freq:
        max_freq=frequency[string]
        result=string
    print(result)

n= int(input())
arr=input().split()
highest_frequency_string(n,arr)