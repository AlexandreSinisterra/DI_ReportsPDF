from reportlab.pdfgen import canvas

texto = ["EL DIABLO MAMI", "no se que quiere", "a cadea", " estoy hasta el pene"]

obxcanvas = canvas.Canvas("obxcanvas.pdf")

obxtexto = obxcanvas.beginText()
obxtexto.setTextOrigin(100,500)
obxtexto.setFont("Courier", 12)

for linea in texto:
    obxtexto.textLine(linea)
    print("Linea creada = " + str(linea))

obxtexto.setFillGray(0.5)

textoLongo = ("""TEXTO CON VARIANTE
                 raro
                 no se""")

obxtexto.textLines(textoLongo)

obxtexto.setTextOrigin(20,850)

for tipo_letra in obxcanvas.getAvailableFonts():
    obxtexto.setFont(tipo_letra, 15)
    obxtexto.textLine("Texto de exemplo coa fonte " + tipo_letra)

obxtexto.setFillColorRGB(0.9,0,0.6)

obxtexto.setFont("Times-BoldItalic",20)

for linea in texto:
    obxtexto.moveCursor(20,15)
    obxtexto.textOut(linea)

obxtexto.moveCursor(-60,15)
espazoCaracteres = 0

for linea in texto:
    obxtexto.setCharSpace(espazoCaracteres)
    obxtexto.textLine("Espazo %s:%s " % (espazoCaracteres, linea))
    espazoCaracteres = espazoCaracteres + 1

obxtexto.setFillColorRGB(0.9,0.4,1.2)
obxtexto.setTextOrigin(20,150)
obxtexto.setCharSpace(1)
obxtexto.setWordSpace(0)
obxtexto.textLines(textoLongo)




obxcanvas.drawText(obxtexto)

obxcanvas.showPage()
obxcanvas.save()