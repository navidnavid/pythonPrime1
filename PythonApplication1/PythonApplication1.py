from model.prim import primMethod
import numpy
import os

def main():

# read db file and change str to int 
    cur_path = os.path.dirname(__file__)
    new_path =  cur_path + '\\db\\db.txt' 
    prm=[ 2, 3, 5]# for test 
    file1 = open(new_path,"r") 
    dbtxt= file1.read()
    dbPrim= dbtxt.split(',')
    prm= []
    try:
        for prNum in dbPrim:
            prm.append(int( prNum ))
    except:
        prNum

    #print(prm)

# do algorithm
    wn=8
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
    print("-----------------------------")
    print(maxP)

if __name__ == "__main__":
    main()