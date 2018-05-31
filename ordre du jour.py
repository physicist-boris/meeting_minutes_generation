from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Code qui permet de générer un  ordre du jour sous format pdf selon certaines instructions définissant le contenu


c = canvas.Canvas("Ordre_du_jour.pdf", pagesize=letter)
c.setLineWidth(.3)
c.setFont('Helvetica', 12)
c.setFillColorRGB(0, 0, 256)

c.rect(0, 730, 620, 710, fill=1)


# titre"ordre du jour" manipulé
def Title(canvas):
    textobject = c.beginText()
    textobject.setTextOrigin(250, 700)
    textobject.setFont("Helvetica-Bold", 20)
    textobject.setFillColorRGB(256, 0, 0)
    textobject.textOut("Ordre Du Jour")
    c.drawText(textobject)


Title(c)
c.setFont('Helvetica', 12)
c.setFillColorRGB(0, 0, 0)

c.line(25, 620, 595, 620)

# lieu
c.drawString(50, 590, "Lieu :")
lieu_meeting = input("Entrez le nom du Lieu de la prochaine rencontre:")
c.drawString(100, 590, lieu_meeting)

# date
c.drawString(50, 550, "Date :")
date_meeting = input("Entrez la date de la prochaine rencontre:")
c.drawString(100, 550, date_meeting)

# heure
c.drawString(50, 510, "Heure :")
heure_meeting = input("Entrez l'heure de la prochaine rencontre:")
c.drawString(100, 510, heure_meeting)

c.line(25, 485, 595, 485)

c.setFont('Helvetica', 12)
c.setFillColorRGB(256, 0, 0)
c.drawRightString(50, 450, "Détails:")

# Présentations
c.setFont('Helvetica-Bold', 14)
c.setFillColorRGB(0, 0, 256)
c.drawString(40, 410, "1- Présentation de l'ordre du jour:")

# points ordre du jour
c.setFont('Helvetica-Bold', 14)
c.setFillColorRGB(0, 0, 256)
c.drawString(40, 330, "2- Points à l'ordre du jour:")
liste_points = []
réponse = "non"
while réponse != "oui":
    point_ordre_du_jour = input("Entrez un point d'ordre du jour à traiter: ")
    liste_points.append(point_ordre_du_jour)
    réponse = input("Avez vous finis de nommer les points d'ordre du jour(oui/non):")
c.setFont('Helvetica', 12)
c.setFillColorRGB(0, 0, 0)
b = 310
for i in range(0, len(liste_points)):
    c.drawString(144, b, "-")
    c.drawString(150, b, liste_points[i])
    b -= 25

c.save()
