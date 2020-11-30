import numpy

class primMethod(object):

    def __init__(self, fn, prmAry):
            self.fn = fn
            self.prmAry = prmAry

    def makeAry(self,fn):
        x=list(bin(fn).format(8))
        del x[0]
        del x[0]
        return x
            
    def convfiltd(self,n , pAry):
        x=list(bin(n).format(8))
        del x[0]
        del x[0]
        # find signle 1 which means no linear relatoin

        nState = list(map(int, x)) # converst to intiger
        x =numpy.array(nState)
        #ones_idx= numpy.where(x==1, )# remove single 1 relation
        if ( sum(x) < 2): #remove single ones 
            return 0
        
        res =( numpy.convolve(x, pAry))
        res = res[n:] # remove first n elemnet
        res= res[:len(res)-n] # remove last n element 
        return res

    def matchQ(self, resAry):
        resAry.sort() 
        resAryNp =numpy.array(resAry)
        index = numpy.where((resAryNp == 0)) #find zeroe
        resAryNp= numpy.delete(resAryNp, index) # delete zeros
        resAryMOd= numpy.diff(resAryNp) # compare to nearest
        pMatchFind_idx = numpy.where(resAryMOd == 0) # 0 = one found 
        return pMatchFind_idx 
        
    def deleteDub(self,ary):
        arySortd= numpy.unique(ary)
        return arySortd


    
    
