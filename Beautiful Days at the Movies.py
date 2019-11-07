def beautifulDays(i, j, k):
    count=0
    for l in range(i,j+1):
        n = (str(l)[::-1])
        if(abs(l-int(n))%k ==0):
            count+=1
    return count
