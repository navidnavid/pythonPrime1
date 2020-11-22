from model.prim import primMethod

def main():
 
    prm=[ 2, 2, 2]
    wn=3
    wnComb = 2**wn
    priObj = primMethod(0,[])
    convRes = []    
    
    for fn in range(wnComb) :
        #convRes.append([])
        temp = priObj.conv(fn,prm)
        temp= deleteDub(temp)
        convRes.append(matchQ(temp.append(prm)))
        #convRes[n].append(temp)
    
    print(convRes)

if __name__ == "__main__":
    main()