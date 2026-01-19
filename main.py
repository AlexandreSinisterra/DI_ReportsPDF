from reportlab.pdfgen import canvas


folla = canvas.Canvas ("primerDocPdf.pdf")

folla.drawString(0,0,"Posicion inicial (x,y) = (0,0)")

folla.drawString(50,100,"Posicion 2 (x,y) = (50,100)")

folla.drawString(150,20,"Posicion 3 (x,y) = (150,20)")

folla.drawImage(image="img1.jpeg",x=200,y=600)

folla.showPage()

folla.save()

