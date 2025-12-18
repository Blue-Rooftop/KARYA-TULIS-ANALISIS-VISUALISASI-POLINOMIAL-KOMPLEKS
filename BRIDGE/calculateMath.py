import cmath

#Discriminant
def funcDiscriminant(hypB,hypA,hypC):
    return (hypB**2)-(4*hypA*hypC)

#Exe's
def midX(hypB,hypA):
    return (hypB*-1)/(2*hypA)

def midY(hypB,hypA,hypC):
    return hypA*(midX(hypB,hypA))**2 +  hypB*(midX(hypB,hypA)) + hypC

#Roots
#=== ROUTE 1 ===
def route1Roots(root1Real,root1Imag,root2Real,root2Imag):
    root1 = root1Real + (root1Imag*1j)
    root2 = root2Real + (root2Imag*1j)
    return root1,root2

#=== ROUTE 2 ===
def route2Roots(hypB,hypA,hypC):
    root1 = (-hypB+cmath.sqrt(funcDiscriminant(hypB,hypA,hypC)))/(2*hypA)
    root2 = (-hypB-cmath.sqrt(funcDiscriminant(hypB,hypA,hypC)))/(2*hypA)
    return root1,root2

#=== EQUATION ===

def route1Equation(root1,root2):
    hypA = 1
    hypB = (root1+root2)*-1
    hypC = (root1*root2)
    return hypA,hypB,hypC

def route2Equation(A,a,B,b,C,c):
    hypA = complex(A,a)
    if hypA == 0:
        raise ValueError("no.")
    hypB = complex(B,b)
    hypC = complex(C,c)
    return hypA,hypB,hypC

def onlyResults(resultXY):
    resultXTuple,resultNewXTuple,resultYTuple = zip(*resultXY)
    resultX = list(resultXTuple)
    resultNewX = list(resultNewXTuple)
    resultY = list(resultYTuple)
    return resultX,resultNewX,resultY