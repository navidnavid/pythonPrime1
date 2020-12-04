from model.prim import primMethod
import numpy
import os

def main():

    
    cur_path = os.path.dirname(__file__)
    new_path =  cur_path + '\\db\\db.txt'
 
    prm=[ 2, 3, 5]

    
    file1 = open(new_path,"r") 
    dbtxt= file1.read()
    

    wn=6
    wnComb = 2**wn
    priObj = primMethod(0,[])
    convRes = []    
    maxP =0
    for fn in range(wnComb) :
        #convRes.append([])
        temp = priObj.convfiltd(fn,prm)

        #temp= priObj.deleteDub(temp)
        foundPrim = priObj.matchQ(numpy.append(temp, prm))
        if(foundPrim >0 ):
            convRes.append([fn, foundPrim])# add prime then see matches
            maxP = max(foundPrim, maxP)

  
        #convRes[n].append(temp)
    
    print(convRes)
    print(maxP)

if __name__ == "__main__":
    main()