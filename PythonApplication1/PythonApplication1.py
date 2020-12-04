from model.prim import primMethod
import numpy

def main():
 
    prm=[ 2, 3, 5]
    prm1 =[0, 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77, 92,
         100, 117, 126, 145, 155, 176, 187, 210, 222, 247, 260, 287, 301,
        330, 345, 376, 392, 425, 442, 477, 495, 532, 551, 590, 610, 651, 672,
       715, 737, 782, 805, 852, 876, 925, 950, 1001, 1027, 1080, 1107,
      1162, 1190, 1247, 1276, 1335 ]

    wn=5
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