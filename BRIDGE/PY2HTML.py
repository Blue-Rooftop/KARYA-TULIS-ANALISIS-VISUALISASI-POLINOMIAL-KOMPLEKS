from flask import Flask, render_template, request
from calculateMath import funcDiscriminant, midX, midY, route1Roots, route1Equation, onlyResults, route2Equation, route2Roots
from switch import switch
from visualize import visualizeY, visualizeX

app = Flask(__name__, template_folder="../WEB-DESIGN")

def get_float(value):
    if value is None or value.strip() == "":
        return None
    return float(value)

def get_int(value):
    if value is None or value.strip() == "":
        return None
    return int(value)

@app.route("/")
def index():
    return render_template("The-Title.html")

@app.route("/roots", methods=["GET", "POST"])
def ROUTE1():
    result = None
    visImagY = None
    visImagX = None

    if request.method == "POST":

        switches = request.form.get("switch")
        if not switches:
            return render_template("ROOTS.html", error="Pilih mode kalkulasi.")

        minX = get_int(request.form.get("minX"))
        maxX = get_int(request.form.get("maxX"))
        root1Real = get_float(request.form.get("realRoot1"))
        root1Imag = get_float(request.form.get("imagRoot1"))
        root2Real = get_float(request.form.get("realRoot2"))
        root2Imag = get_float(request.form.get("imagRoot2"))

        if None in (minX, maxX, root1Real, root1Imag, root2Real, root2Imag):
            return render_template(
                "ROOTS.html",
                error="Semua input numerik wajib diisi."
            )

        root1, root2 = route1Roots(root1Real, root1Imag, root2Real, root2Imag)
        hypA, hypB, hypC = route1Equation(root1, root2)

        discriminant = funcDiscriminant(hypB, hypA, hypC)
        productsOfRoots = hypC/hypA
        sumOfRoots = 2*midX(hypB, hypA)
        midx = midX(hypB, hypA)
        midy = midY(hypB, hypA, hypC)

        switches = request.form.get("switch")

        d = e = None

        if switches in ("constantImag", "constantReal"):
            d = get_float(request.form.get("D"))
            e = get_float(request.form.get("E"))

            if d is None or e is None:
                return render_template(
                    "ROOTS.html",
                    error="Mode konstanta membutuhkan nilai d dan e."
                )


        resultXY = switch(minX,maxX,hypB,hypA,hypC,switches,d,e) 
        if not resultXY:
            return render_template(
            "ROOTS.html",
            error="Tidak ada data untuk divisualisasikan."
            )

        resultX,resultNewX,resultY = onlyResults(resultXY)

        visImagY = visualizeY(resultNewX,resultY)
        visImagX = visualizeX(resultNewX,resultY)

        result = {
            "r1": str(root1),
            "r2": str(root2),
            "standardForm": f"(x - {root1}) (x - {root2})",
            "extendedForm": f"x² + {hypB}x + {hypC}",
            "domain": f"{minX} ≤ x ≤ {maxX}",
            "productsRoots" : str(productsOfRoots),
            "sORoots" : str(sumOfRoots),
            "disc": str(discriminant),
            "vertex": f"({midx},{midy})",
        }

    return render_template("ROOTS.html", result=result, visualizeIY = visImagY, visualizeIX = visImagX)

@app.route("/coefficients", methods=["GET", "POST"])
def ROUTE2():
    result = None
    visImagY = None
    visImagX = None

    if request.method == "POST":

        switches = request.form.get("switch")
        if not switches:
            return render_template("COEFFICIENT.html", error="Pilih mode kalkulasi.")

        minX = get_int(request.form.get("minX"))
        maxX = get_int(request.form.get("maxX"))
        A = get_float(request.form.get("AR"))
        a = get_float(request.form.get("aI"))
        B = get_float(request.form.get("BR"))
        b = get_float(request.form.get("bI"))
        C = get_float(request.form.get("CR"))
        c = get_float(request.form.get("cI"))


        if None in (minX, maxX, A, a, B, b, C, c):
            return render_template(
                "COEFFICIENT.html",
                error="Semua input numerik wajib diisi."
            )

        hypA, hypB, hypC = route2Equation(A,a,B,b,C,c)
        root1, root2 = route2Roots(hypB,hypA,hypC)

        discriminant = funcDiscriminant(hypB, hypA, hypC)
        productsOfRoots = hypC/hypA
        sumOfRoots = 2*midX(hypB, hypA)
        midx = midX(hypB, hypA)
        midy = midY(hypB, hypA, hypC)

        switches = request.form.get("switch")

        d = e = None

        if switches in ("constantImag", "constantReal"):
            d = get_float(request.form.get("D"))
            e = get_float(request.form.get("E"))

            if d is None or e is None:
                return render_template(
                    "COEFFICIENT.html",
                    error="Mode konstanta membutuhkan nilai d dan e."
                )


        resultXY = switch(minX,maxX,hypB,hypA,hypC,switches,d,e) 
        if not resultXY:
            return render_template(
            "COEFFICIENT.html",
            error="Tidak ada data untuk divisualisasikan."
            )

        resultX,resultNewX,resultY = onlyResults(resultXY)

        visImagY = visualizeY(resultNewX,resultY)
        visImagX = visualizeX(resultNewX,resultY)

        result = {
            "r1": str(root1),
            "r2": str(root2),
            "standardForm": f"({A}+{a}i)x² + ({B}+{b}i)x + ({C}+{c}i)",
            "extendedForm": f"{hypA}x² + {hypB}x + {hypC}",
            "domain": f"{minX} ≤ x ≤ {maxX}",
            "productsRoots" : str(productsOfRoots),
            "sORoots" : str(sumOfRoots),
            "disc": str(discriminant),
            "vertex": f"({midx},{midy})",
        }

    return render_template("COEFFICIENT.html", result=result, visualizeIY = visImagY, visualizeIX = visImagX)

if __name__ == "__main__":
    app.run(debug=True)
