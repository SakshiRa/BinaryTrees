

#def maxFreq(l):
#    d = {}
#    for i in l:
#        if i in l:
#            d[i] = d.get(i,0)+1
#        Keymax = max(d, key=d.get) 
#    return Keymax
#         
#    
## Main
#n=int(input())
#l=list(int(i) for i in input().strip().split(' '))
#print(maxFreq(l))
#
##
#def pairsumzero(l):
#    for i in (l):
#        for j in (l):
#            if i + j == 0:
#                if i < j:
#                    print(i,j)
#                
#            
#    
#n=int(input())
#l=list(int(i) for i in input().strip().split(' '))
#pairsumzero(l)

#target =int(input())
#A = [7, 2, 11, 15,13]
#d = {}
#for i in A:
#    if target - i == d[i]:
#        d[i] +1
#    else:
#        i - 



def maxFreq(l):
    map = {}
    for i in l:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
        ans = l[0]
        for i in l:
            if map[i] > map[ans]:
                ans = i
            return ans
                

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))        
        
    
    


def freqmap(l):
    map = {}
    for i in l:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    return map

def pairSum0(l):
    m = freqmap(l)
    for i in m:
        if i >=0 and -i in m:
            for _ in range(0,m[i]*m[-i]):
                print(-i,i)
            
    
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)       
        
    
    
        


    
    

  
    

    
    
        

           
            


    