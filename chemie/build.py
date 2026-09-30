from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import *
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
F="/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV",F+"DejaVuSans.ttf")); pdfmetrics.registerFont(TTFont("DVB",F+"DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI","/usr/local/lib/python3.11/dist-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFontFamily("DV",normal="DV",bold="DVB",italic="DVI",boldItalic="DVB")
IMG="/tmp/claude-0/-home-user-url2qrcode/03f1d59f-cc33-51a3-9ad1-9b1c8fb90f86/scratchpad/img/"
NAVY=colors.HexColor("#1b2a49"); ACC=colors.HexColor("#2a6fdb"); LIGHT=colors.HexColor("#eef3fb")
B=ParagraphStyle("b",fontName="DV",fontSize=9.5,leading=14.5,alignment=TA_JUSTIFY,spaceAfter=6)
H1=ParagraphStyle("h1",fontName="DVB",fontSize=17,leading=21,textColor=NAVY,spaceBefore=6,spaceAfter=8)
H2=ParagraphStyle("h2",fontName="DVB",fontSize=11.5,leading=15,textColor=ACC,spaceBefore=8,spaceAfter=4)
CAP=ParagraphStyle("c",fontName="DVI",fontSize=8,leading=10,textColor=colors.HexColor("#5d6778"),spaceAfter=10)
CELL=ParagraphStyle("cell",fontName="DV",fontSize=8.5,leading=13)
CELLB=ParagraphStyle("cellb",parent=CELL,fontName="DVB",textColor=colors.white)
BUL=ParagraphStyle("bul",parent=B,leftIndent=14,bulletIndent=3,spaceAfter=2,alignment=0)
def bl(items): return [Paragraph(t,BUL,bulletText="•") for t in items]
def img(n,w,cap):
    from PIL import Image
    iw,ih=Image.open(IMG+n).size
    return KeepTogether([Image_(IMG+n,w,w*ih/iw),Paragraph(cap,CAP)])
def Image_(p,w,h):
    from reportlab.platypus import Image as I
    return I(p,width=w,height=h)
def box(title,text):
    t=Table([[Paragraph(f"<b>{title}</b><br/>{text}",CELL)]],colWidths=[17*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),("LINEBEFORE",(0,0),(0,-1),3,ACC),("LEFTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return [t,Spacer(1,8)]
def table(rows,widths):
    data=[[Paragraph(c,CELLB) for c in rows[0]]]+[[Paragraph(c,CELL) for c in r] for r in rows[1:]]
    t=Table(data,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,LIGHT]),("GRID",(0,0),(-1,-1),.4,colors.HexColor("#c9d3e3")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    return [t,Spacer(1,10)]

def cover(c,d):
    W,H=A4; c.setFillColor(NAVY); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(ACC); c.rect(0,H*0.42,W,6,fill=1,stroke=0)
    c.setFillColor(colors.white); c.setFont("DVB",38); c.drawString(2.2*cm,H*0.62,"Chemie")
    c.setFont("DVB",20); c.drawString(2.2*cm,H*0.62-1.3*cm,"Elemente, Atome & Grundlagen")
    c.setFont("DV",11); c.setFillColor(colors.HexColor("#b8c6e0"))
    c.drawString(2.2*cm,H*0.62-2.4*cm,"Lernzusammenfassung: Das musst du wissen")
    from reportlab.lib.utils import ImageReader
    c.drawImage(ImageReader(IMG+"bohr.png"),1.5*cm,H*0.12,width=W-3*cm,height=(W-3*cm)*0.19,mask="auto")
def later(c,d):
    W,H=A4; c.setFont("DV",8); c.setFillColor(colors.HexColor("#5d6778"))
    c.drawString(2*cm,1.2*cm,"Chemie – Lernzusammenfassung"); c.drawRightString(W-2*cm,1.2*cm,f"Seite {d.page}")
    c.setStrokeColor(colors.HexColor("#c9d3e3")); c.line(2*cm,1.7*cm,W-2*cm,1.7*cm)

s=[PageBreak()]
s+=[Paragraph("Inhalt",H1)]
s+=bl(["1. Was ist Chemie? Stoffe &amp; Aggregatzustände","2. Der Atombau","3. Das Periodensystem &amp; die Gruppen","4. Wichtige Elemente auf einen Blick","5. Chemische Bindungen","6. Reaktionen &amp; Reaktionsgleichungen","7. Säuren, Basen &amp; der pH-Wert","8. Mol &amp; Rechnen in der Chemie","9. Lernplan &amp; Merksätze"])
s+=[Spacer(1,10)]
s+=box("Hinweis zur Quelle","Das Video des YouTubers „Wacky Science“ konnte in dieser Umgebung nicht abgerufen werden (YouTube war blockiert). Dieses Dokument basiert daher auf allgemeinem Schul- und Grundlagenwissen der Chemie, nicht auf dem Videoinhalt. Falls du das Transkript einfügst, gleiche ich beides ab.")
s+=[Paragraph("1. Was ist Chemie?",H1),
Paragraph("Chemie untersucht, woraus Stoffe bestehen, welche Eigenschaften sie haben und wie sie sich ineinander umwandeln. Alles Materielle besteht aus <b>Atomen</b>. Ein <b>Element</b> besteht nur aus einer Atomsorte (z. B. Gold, Sauerstoff). Eine <b>Verbindung</b> enthält verschiedene Atomsorten in festem Verhältnis (H<sub>2</sub>O, NaCl). Ein <b>Gemisch</b> ist nicht fest verbunden (Luft, Salzwasser) und lässt sich physikalisch trennen.",B),
Paragraph("Aggregatzustände",H2),
img("states.png",15*cm,"Abb. 1: Teilchenmodell – fest (geordnet), flüssig (beweglich, dicht), gasförmig (weit auseinander, schnell)."),
]+table([["Übergang","Name","Energie"],["fest → flüssig","Schmelzen","wird aufgenommen"],["flüssig → gasförmig","Verdampfen","wird aufgenommen"],["gasförmig → flüssig","Kondensieren","wird abgegeben"],["flüssig → fest","Erstarren","wird abgegeben"],["fest → gasförmig","Sublimieren","wird aufgenommen"]],[5.5*cm,5.5*cm,6*cm])
s+=[PageBreak(),Paragraph("2. Der Atombau",H1),
Paragraph("Ein Atom besteht aus einem winzigen, schweren <b>Kern</b> (Protonen und Neutronen) und einer <b>Hülle</b> aus Elektronen. Fast die gesamte Masse steckt im Kern, fast das gesamte Volumen ist Hülle.",B),
img("atom.png",10.5*cm,"Abb. 2: Aufbau eines Atoms (schematisch, nicht maßstabsgetreu)."),
]+table([["Teilchen","Ladung","Masse","Ort"],["Proton (p<super>+</super>)","+1","1 u","Kern"],["Neutron (n)","0","1 u","Kern"],["Elektron (e<super>−</super>)","−1","≈ 1/1836 u","Hülle"]],[5*cm,3*cm,4*cm,5*cm])
s+=[Paragraph("Wichtige Begriffe",H2)]+bl(["<b>Ordnungszahl Z</b> = Zahl der Protonen. Sie bestimmt das Element.","<b>Massenzahl A</b> = Protonen + Neutronen.","<b>Isotope</b>: gleiche Protonenzahl, unterschiedliche Neutronenzahl (z. B. C-12 und C-14).","<b>Ion</b>: geladenes Atom. Elektronen abgegeben → Kation (+), aufgenommen → Anion (−).","<b>Schalenmodell</b>: Elektronen sitzen auf Schalen K, L, M … mit max. 2, 8, 18 … Elektronen (2n²)."])
s+=[Spacer(1,6),img("bohr.png",17*cm,"Abb. 3: Bohr-Modelle ausgewählter Elemente. Die Valenzelektronen der äußersten Schale bestimmen das Verhalten."),
]+box("Merke","Die äußerste Schale will voll sein (Edelgaskonfiguration, „Oktettregel“). Deshalb geben Atome Elektronen ab, nehmen sie auf oder teilen sie.")
s+=[PageBreak(),Paragraph("3. Das Periodensystem",H1),
Paragraph("Das Periodensystem ordnet alle bekannten Elemente nach steigender Ordnungszahl. <b>Perioden</b> (Zeilen) entsprechen der Zahl der besetzten Schalen. <b>Gruppen</b> (Spalten) enthalten Elemente mit gleich vielen Valenzelektronen und daher ähnlichen Eigenschaften.",B),
img("pt.png",17*cm,"Abb. 4: Periodensystem, farbig nach Elementfamilien."),
]+table([["Gruppe","Name","Valenz-e⁻","Eigenschaften"],
["1","Alkalimetalle","1","weich, sehr reaktiv mit Wasser (Li, Na, K)"],
["2","Erdalkalimetalle","2","reaktiv, Mg brennt hell, Ca in Knochen"],
["3–12","Übergangsmetalle","–","hart, gute Leiter, oft farbige Verbindungen (Fe, Cu, Au)"],
["17","Halogene","7","sehr reaktive Nichtmetalle (F, Cl, Br, I), bilden Salze"],
["18","Edelgase","8 (He: 2)","praktisch reaktionsträge (He, Ne, Ar)"]],[2*cm,3.6*cm,2.4*cm,9*cm])
s+=[Paragraph("Trends im Periodensystem",H2)]+bl(["<b>Atomradius</b>: nimmt in einer Gruppe nach unten zu, in einer Periode nach rechts ab.","<b>Elektronegativität</b> (EN): nimmt nach rechts und nach oben zu. Fluor hat die höchste EN.","<b>Metallcharakter</b>: nimmt nach links und unten zu."])
s+=[PageBreak(),Paragraph("4. Wichtige Elemente auf einen Blick",H1)]+table([
["Symbol","Name","Z","Wo begegnet es dir?"],
["H","Wasserstoff","1","häufigstes Element im Universum, Sonne, Wasser"],
["He","Helium","2","Ballons, Edelgas, nicht brennbar"],
["C","Kohlenstoff","6","Grundlage des Lebens, Diamant, Graphit"],
["N","Stickstoff","7","78 % der Luft, Dünger"],
["O","Sauerstoff","8","21 % der Luft, Atmung, Verbrennung"],
["Na","Natrium","11","Kochsalz (NaCl)"],
["Cl","Chlor","17","Schwimmbad, Salz"],
["Ca","Calcium","20","Knochen, Zähne, Kalk"],
["Fe","Eisen","26","Stahl, Blut (Hämoglobin)"],
["Cu","Kupfer","29","Kabel, Münzen"],
["Au","Gold","79","Schmuck, reagiert kaum"],
["U","Uran","92","Kernkraft, radioaktiv"]],[2*cm,3.5*cm,1.5*cm,10*cm])
s+=box("Wusstest du?","Der menschliche Körper besteht zu etwa 96 % aus nur vier Elementen: Sauerstoff, Kohlenstoff, Wasserstoff und Stickstoff.")
s+=[Paragraph("5. Chemische Bindungen",H1),
img("bonds.png",17*cm,"Abb. 5: Die drei Bindungstypen."),
]+table([["Typ","Zwischen","Prinzip","Beispiel"],["Ionenbindung","Metall + Nichtmetall","Elektronenübertragung, Anziehung der Ionen (Ionengitter)","NaCl, MgO"],["Kovalente Bindung","Nichtmetall + Nichtmetall","gemeinsame Elektronenpaare","H<sub>2</sub>O, CO<sub>2</sub>, O<sub>2</sub>"],["Metallbindung","Metall + Metall","Atomrümpfe im „Elektronengas“","Fe, Cu, Au"]],[3.3*cm,3.9*cm,6.3*cm,3.5*cm])
s+=bl(["Ionenverbindungen: hohe Schmelzpunkte, spröde, leiten als Schmelze/Lösung Strom.","Metalle: leiten Strom und Wärme, verformbar, glänzend.","Zwischenmolekulare Kräfte (z. B. Wasserstoffbrücken) erklären, warum Wasser bei 100 °C siedet."])
s+=[PageBreak(),Paragraph("6. Reaktionen &amp; Reaktionsgleichungen",H1),
Paragraph("Bei einer chemischen Reaktion werden Bindungen gelöst und neu geknüpft. Atome gehen dabei nicht verloren (<b>Massenerhaltung</b>). Deshalb muss jede Gleichung auf beiden Seiten gleich viele Atome jeder Sorte haben.",B)]
s+=box("Beispiel: Wasserbildung","2 H<sub>2</sub> + O<sub>2</sub> → 2 H<sub>2</sub>O")
s+=box("Beispiel: Verbrennung von Methan","CH<sub>4</sub> + 2 O<sub>2</sub> → CO<sub>2</sub> + 2 H<sub>2</sub>O")
s+=[Paragraph("Reaktionstypen",H2)]+bl(["<b>Synthese</b>: A + B → AB","<b>Zerlegung</b>: AB → A + B","<b>Austausch</b>: AB + C → AC + B","<b>Redoxreaktion</b>: Elektronenübertragung. Oxidation = Abgabe, Reduktion = Aufnahme („OIL RIG“).","<b>Exotherm</b>: gibt Energie ab. <b>Endotherm</b>: nimmt Energie auf."])
s+=[Paragraph("7. Säuren, Basen &amp; pH-Wert",H1),
Paragraph("Säuren geben H<super>+</super>-Ionen ab (z. B. HCl, Zitronensäure). Basen (Laugen) nehmen H<super>+</super> auf oder geben OH<super>−</super> ab (z. B. NaOH). Der pH-Wert misst die Konzentration der H<super>+</super>-Ionen: pH 7 ist neutral, darunter sauer, darüber basisch. Jeder Schritt bedeutet einen Faktor 10.",B),
img("ph.png",16*cm,"Abb. 6: pH-Skala mit Alltagsbeispielen."),
]+box("Neutralisation","HCl + NaOH → NaCl + H<sub>2</sub>O (Säure + Base → Salz + Wasser)")
s+=[Paragraph("8. Mol &amp; Rechnen",H1),
Paragraph("Ein <b>Mol</b> sind 6,022 · 10<super>23</super> Teilchen (Avogadro-Konstante N<sub>A</sub>). Die molare Masse M in g/mol steht (numerisch) im Periodensystem.",B)]
s+=box("Formeln","n = m / M &nbsp;&nbsp;|&nbsp;&nbsp; c = n / V &nbsp;&nbsp;|&nbsp;&nbsp; N = n · N<sub>A</sub><br/>Beispiel: 18 g Wasser (M = 18 g/mol) = 1 mol = 6,022 · 10<super>23</super> Moleküle.")
s+=[PageBreak(),Paragraph("9. Lernplan &amp; Merksätze",H1)]+bl(["Lerne zuerst die ersten 20 Elemente mit Symbol und Ordnungszahl.","Zeichne Bohr-Modelle selbst, das trainiert Schalen und Valenzelektronen.","Übe Reaktionsgleichungen täglich, 5 Stück reichen.","<b>Merksatz</b>: Ordnungszahl = Protonen = Elektronen (beim neutralen Atom).","<b>Merksatz</b>: Gruppe = Valenzelektronen, Periode = Schalen.","<b>Merksatz</b>: Metall + Nichtmetall = Ionen, Nichtmetall + Nichtmetall = Elektronenpaare.","Erkläre das Thema einem Freund. Wer erklären kann, hat es verstanden."])
doc=BaseDocTemplate("Chemie_Lernzusammenfassung.pdf",pagesize=A4,leftMargin=2*cm,rightMargin=2*cm,topMargin=2*cm,bottomMargin=2.3*cm,title="Chemie – Elemente & Grundlagen",author="Claude")
fr=Frame(2*cm,2.3*cm,17*cm,A4[1]-4.3*cm,id="f")
doc.addPageTemplates([PageTemplate("cover",[fr],onPage=cover),PageTemplate("body",[fr],onPage=later)])
from reportlab.platypus.doctemplate import NextPageTemplate
doc.build([NextPageTemplate("body")]+s)
