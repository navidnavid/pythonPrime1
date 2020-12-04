from model.prim import primMethod
import numpy

def main():
 
    prm=[ 2, 3, 5]
    wn=3
    wnComb = 2**wn
    priObj = primMethod(0,[])
    convRes = []    
    
    for fn in range(wnComb) :
        #convRes.append([])
        temp = priObj.convfiltd(fn,prm)
        #temp= priObj.deleteDub(temp)
        convRes.append(priObj.matchQ(numpy.append(temp, prm)))# add prime then see matches
        #convRes[n].append(temp)
    
    print(convRes)

if __name__ == "__main__":
    main()