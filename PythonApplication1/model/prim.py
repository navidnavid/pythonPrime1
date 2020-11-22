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
            
    def conv(self,n , pAry):
        x=list(bin(n).format(8))
        del x[0]
        del x[0]
        
        x = map(int, x)
        nState =list( x)
        res = numpy.convolve(nState, pAry)
        return res

    def matchQ(self, resAry):
        resAry.sort() 
        resAryNp =numpy.array(resAry)
        index = numpy.where((resAryNp == 0))
        resAryNp= numpy.delete(resAryNp, index)
        resAryMOd= numpy.diff(resAryNp)
        pMatchFind = numpy.where(resAryMOd == 0)
        return len(pMatchFind)
        
    def deleteDub(self,ary):
        arySortd= numpy.unique(arySortd)


    
    
