#=== FAIS COOL EXES ===
def complexNewXCImag(minX,maxX,hypB,hypA,hypC,d,e):
    result = []
    #this is complex
    for x in range(minX, maxX+1):
        newX = d*x + (e*1j)
        y = hypA*(newX)**2 + hypB*(newX) + hypC

        result.append((x,newX,y))
    return result

def complexNewXCReal(minX,maxX,hypB,hypA,hypC,d,e):
    result = []
    #this is complex
    for x in range(minX, maxX+1):
        newX = d + (e*x*1j)
        y = hypA*(newX)**2 + hypB*(newX) + hypC

        result.append((x,newX,y))
    return result

def realNewX(minX,maxX,hypB,hypA,hypC):
    result = []
    #This is real
    for x in range(minX, maxX+1):
        newX = x
        y = hypA*(newX)**2 + hypB*(newX) + hypC

        result.append((x,newX,y))
    return result

def imagNewX(minX,maxX,hypB,hypA,hypC):
    result = []
    #This is... imaginary
    for x in range(minX, maxX+1):
        newX = x * 1j
        y = hypA*(newX)**2 + hypB*(newX) + hypC

        result.append((x,newX,y))
    return result