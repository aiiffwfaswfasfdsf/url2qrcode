import re, sys
sys.path.insert(0,"src")
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import *
from reportlab.platypus import Image as RLImage
from reportlab.platypus.doctemplate import NextPageTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
from c1 import C1
from c2 import C2
from c3 import C3, AN

M="/usr/local/lib/python3.11/dist-packages/matplotlib/mpl-data/fonts/ttf/"
F="/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV",F+"DejaVuSans.ttf")); pdfmetrics.registerFont(TTFont("DVB",F+"DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI",M+"DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFontFamily("DV",normal="DV",bold="DVB",italic="DVI",boldItalic="DVB")
IMG="/tmp/claude-0/-home-user-url2qrcode/03f1d59f-cc33-51a3-9ad1-9b1c8fb90f86/scratchpad/img/"
NAVY=colors.HexColor("#1b2a49"); ACC=colors.HexColor("#2a6fdb"); LIGHT=colors.HexColor("#eef3fb")
try:
    import pyphen; HY=dict(hyphenationLang="de_DE",hyphenationMinWordLength=6,uriWasteReduce=0.3)
except Exception: HY={}
B=ParagraphStyle("b",fontName="DV",fontSize=10,leading=16,alignment=TA_JUSTIFY,spaceAfter=8,allowWidows=0,**HY)
H1=ParagraphStyle("h1",fontName="DVB",fontSize=19,leading=24,textColor=NAVY,spaceBefore=4,spaceAfter=12)
H2=ParagraphStyle("h2",fontName="DVB",fontSize=12.5,leading=16,textColor=ACC,spaceBefore=10,spaceAfter=5)
CAP=ParagraphStyle("c",fontName="DVI",fontSize=8.3,leading=11,textColor=colors.HexColor("#5d6778"),spaceAfter=12,alignment=1)
BOXS=ParagraphStyle("box",fontName="DV",fontSize=9.4,leading=14,**HY)
QS=ParagraphStyle("q",parent=B,alignment=0,fontName="DVB",spaceAfter=2,spaceBefore=6)
AS=ParagraphStyle("a",parent=B,leftIndent=12,textColor=colors.HexColor("#33415c"),spaceAfter=6)
TOCS=ParagraphStyle("toc",fontName="DV",fontSize=10.5,leading=17)

def fmt(t):
    t=t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    mi=lambda s: s.replace("-","−")
    t=re.sub(r"\^\{([^}]*)\}",lambda m:"<super>"+mi(m.group(1))+"</super>",t)
    t=re.sub(r"_\{([^}]*)\}",lambda m:"<sub>"+mi(m.group(1))+"</sub>",t)
    t=re.sub(r"\^(\d*[+\-])",lambda m:"<super>"+mi(m.group(1))+"</super>",t)
    t=re.sub(r"_(\d+)",r"<sub>\1</sub>",t)
    t=re.sub(r"_([A-Za-z])(?![A-Za-z])",r"<sub>\1</sub>",t)
    t=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",t)
    t=re.sub(r"//(.+?)//",r"<i>\1</i>",t)
    return t

fig=[0]
def make(items):
    out=[]
    for it in items:
        k=it[0]
        if k=="h1": out+=[CondPageBreak(7*cm),Paragraph(fmt(it[1]),H1)]
        elif k=="h2": out+=[CondPageBreak(4*cm),Paragraph(fmt(it[1]),H2)]
        elif k=="p": out.append(Paragraph(fmt(it[1]),B))
        elif k=="img":
            fig[0]+=1
            w=it[2]*cm; iw,ih=PILImage.open(IMG+it[1]).size
            out.append(KeepTogether([RLImage(IMG+it[1],width=w,height=w*ih/iw),Paragraph(f"Abbildung {fig[0]}: "+fmt(it[3]),CAP)]))
        elif k=="box":
            t=Table([[Paragraph(f"<b>{fmt(it[1])}</b><br/>{fmt(it[2])}",BOXS)]],colWidths=[17*cm])
            t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),("LINEBEFORE",(0,0),(0,-1),3,ACC),("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
            out+=[t,Spacer(1,10)]
        elif k=="qa": out.append(KeepTogether([Paragraph(fmt(it[1]),QS),Paragraph(fmt(it[2]),AS)]))
        elif k=="gl": out.append(Paragraph(f"<b>{fmt(it[1])}:</b> {fmt(it[2])}",ParagraphStyle("g",parent=B,alignment=0,spaceAfter=4)))
    return out

body=C1+C2+C3+AN
heads=[i[1] for i in body if i[0]=="h1"]

def cover(c,d):
    W,H=A4; c.setFillColor(NAVY); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(ACC); c.rect(0,H*0.42,W,6,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("DVB",42); c.drawString(2.2*cm,H*0.62,"Chemie")
    c.setFont("DVB",19); c.drawString(2.2*cm,H*0.62-1.4*cm,"Von den Atomen bis zur Seife")
    c.setFont("DV",11); c.setFillColor(colors.HexColor("#b8c6e0"))
    c.drawString(2.2*cm,H*0.62-2.5*cm,"Ein Lernheft, das bei null anfängt und Schritt für Schritt aufbaut")
    c.drawImage(ImageReader(IMG+"bohr.png"),1.5*cm,H*0.12,width=W-3*cm,height=(W-3*cm)*0.19,mask="auto")
def later(c,d):
    W,H=A4; c.setFont("DV",8); c.setFillColor(colors.HexColor("#5d6778"))
    c.drawString(2*cm,1.2*cm,"Chemie: Von den Atomen bis zur Seife"); c.drawRightString(W-2*cm,1.2*cm,f"Seite {d.page}")
    c.setStrokeColor(colors.HexColor("#c9d3e3")); c.line(2*cm,1.7*cm,W-2*cm,1.7*cm)

story=[NextPageTemplate("body"),PageBreak(),Paragraph("Bevor es losgeht",H1)]
story+=make([("p","Dieses Heft ist für alle gedacht, die Chemie von Grund auf verstehen wollen, auch wenn sie noch nie etwas davon gehört haben. Es fängt ganz vorne an und baut Kapitel für Kapitel aufeinander auf. Am Anfang steht die Frage, was ein Stoff überhaupt ist, danach kommt das Atom, dann das Periodensystem, dann die Frage, wie sich Atome verbinden. Erst wenn das sitzt, geht es um Reaktionen, Rechnen, Säuren und Batterien und am Ende um Dinge, die man aus dem Alltag kennt, zum Beispiel wie Seife wirkt, warum Klebstoff hält und weshalb Zement hart wird."),
("p","Am besten liest du die Kapitel der Reihe nach, denn viele Erklärungen greifen auf früher Gelerntes zurück. Neue Fachbegriffe sind beim ersten Auftreten **fett** gedruckt und werden gleich erklärt. Am Ende findest du Übungsaufgaben mit Lösungen, ein kleines Glossar zum Nachschlagen und einen Vorschlag, wie man sich das Ganze über vier Wochen einteilen kann. Die Zeichnungen wurden für dieses Heft eigens angefertigt und sind teilweise stark vereinfacht. Sie sollen helfen, sich etwas vorzustellen, aber sie ersetzen nicht das Nachdenken."),
("p","Falls du das Heft für die Schule nutzt: Vergleiche die Formeln und Zahlen im Zweifel noch mit deinem Schulbuch, denn die Schwerpunkte unterscheiden sich von Bundesland zu Bundesland."),
("h2","Inhalt")])
story+=[Paragraph(h,TOCS) for h in map(fmt,heads)]
story+=make(body)
doc=BaseDocTemplate("Chemie_Lernzusammenfassung.pdf",pagesize=A4,leftMargin=2*cm,rightMargin=2*cm,topMargin=2*cm,bottomMargin=2.3*cm,title="Chemie: Von den Atomen bis zur Seife",author="")
fr=Frame(2*cm,2.3*cm,17*cm,A4[1]-4.3*cm,id="f")
doc.addPageTemplates([PageTemplate("cover",[fr],onPage=cover),PageTemplate("body",[fr],onPage=later)])
doc.build(story)
