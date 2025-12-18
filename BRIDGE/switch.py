from transform import complexNewXCImag,complexNewXCReal,realNewX,imagNewX

def switch(minX,maxX,hypB,hypA,hypC,switches,d,e):
    if switches == "constantImag":
        return complexNewXCImag(minX,maxX,hypB,hypA,hypC,d,e)
    elif switches == "constantReal":
        return complexNewXCReal(minX,maxX,hypB,hypA,hypC,d,e)
    elif switches == "onlyReal":
        return realNewX(minX,maxX,hypB,hypA,hypC)
    elif switches == "onlyImag":
        return imagNewX(minX,maxX,hypB,hypA,hypC) 