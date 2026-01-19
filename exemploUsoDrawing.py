from reportlab.graphics.shapes import Image,Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

guion = []

imagen = Image(50,20,148,148,"img1.jpeg")

dibujo = Drawing(300,12)
dibujo.add(imagen)

dibujo2 = Drawing()
dibujo2.add(imagen)
dibujo2.translate(150,350)

dibujo3 = Drawing()
dibujo3.add(imagen)
dibujo3.rotate(45)
dibujo3.translate(150,50)


guion.append(dibujo)
guion.append(dibujo2)
guion.append(dibujo3)

folla = Drawing(A4[0],A4[1])
print(folla)

for elemento in guion:
    folla.add(elemento)

renderPDF.drawToFile(folla,"prueba1.pdf")