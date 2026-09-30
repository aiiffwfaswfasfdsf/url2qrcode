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
def h1(t): return [CondPageBreak(6*cm),Paragraph(t,H1)]
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
    c.drawString(2.2*cm,H*0.62-2.4*cm,"Umfassende Lernzusammenfassung: Das musst du wissen")
    from reportlab.lib.utils import ImageReader
    c.drawImage(ImageReader(IMG+"bohr.png"),1.5*cm,H*0.12,width=W-3*cm,height=(W-3*cm)*0.19,mask="auto")
def later(c,d):
    W,H=A4; c.setFont("DV",8); c.setFillColor(colors.HexColor("#5d6778"))
    c.drawString(2*cm,1.2*cm,"Chemie – Lernzusammenfassung"); c.drawRightString(W-2*cm,1.2*cm,f"Seite {d.page}")
    c.setStrokeColor(colors.HexColor("#c9d3e3")); c.line(2*cm,1.7*cm,W-2*cm,1.7*cm)


def P(t): return Paragraph(t,B)
s=[PageBreak(),Paragraph("Inhaltsverzeichnis",H1)]
toc=["1. Materie, Stoffe &amp; Trennverfahren","2. Geschichte der Atommodelle","3. Der Atombau, Isotope &amp; Ionen","4. Elektronenkonfiguration &amp; Orbitale","5. Das Periodensystem &amp; seine Trends","6. Die ersten 20 Elemente im Detail","7. Chemische Bindungen, Lewis-Formeln &amp; Molekülgeometrie","8. Zwischenmolekulare Kräfte","9. Nomenklatur: Formeln &amp; Namen","10. Chemische Reaktionen &amp; Gleichungen","11. Stöchiometrie: Mol &amp; Rechnen","12. Gase &amp; Gasgesetze","13. Lösungen &amp; Konzentrationen","14. Energie &amp; Reaktionsgeschwindigkeit","15. Chemisches Gleichgewicht","16. Säuren, Basen &amp; pH-Wert","17. Redoxreaktionen &amp; Elektrochemie","18. Organische Chemie","19. Kernchemie &amp; Radioaktivität","20. Laborpraxis &amp; Sicherheit","21. Übungsaufgaben mit Lösungen","22. Lernplan, Merksätze &amp; Glossar"]
s+=bl(toc)+[Spacer(1,10)]
s+=box("Hinweis zur Quelle","Das Video des YouTubers „Wacky Science“ konnte in dieser Umgebung nicht abgerufen werden (YouTube war blockiert). Dieses Dokument basiert daher auf allgemeinem Schul- und Grundlagenwissen der Chemie, nicht auf dem Videoinhalt. Falls du das Transkript einfügst, gleiche ich beides ab.")

# 1
s+=h1("1. Materie, Stoffe &amp; Trennverfahren")
s+=[P("Chemie untersucht, woraus Stoffe bestehen, welche Eigenschaften sie haben und wie sie sich ineinander umwandeln. Alles Materielle besteht aus <b>Atomen</b>. Ein <b>Element</b> besteht nur aus einer Atomsorte (z. B. Gold, Sauerstoff). Eine <b>Verbindung</b> enthält verschiedene Atomsorten in festem Verhältnis (H<sub>2</sub>O, NaCl) und lässt sich nur chemisch zerlegen. Ein <b>Gemisch</b> ist nicht fest verbunden (Luft, Salzwasser) und lässt sich physikalisch trennen.")]
s+=table([["Begriff","Bedeutung","Beispiele"],["Reinstoff","einheitlich, feste Eigenschaften (Schmelz-/Siedepunkt, Dichte)","Wasser, Eisen, Zucker"],["Element","nur eine Atomsorte, chemisch nicht weiter zerlegbar","O<sub>2</sub>, Fe, Au"],["Verbindung","feste Zusammensetzung aus verschiedenen Elementen","H<sub>2</sub>O, CO<sub>2</sub>, NaCl"],["homogenes Gemisch","überall gleich, Bestandteile nicht sichtbar","Salzlösung, Luft, Legierung"],["heterogenes Gemisch","Bestandteile erkennbar","Sand + Wasser, Granit, Milch (Emulsion)"]],[3.5*cm,7.5*cm,6*cm])
s+=[Paragraph("Aggregatzustände",H2),
img("states.png",14*cm,"Abb. 1: Teilchenmodell – fest (geordnet), flüssig (beweglich, dicht), gasförmig (weit auseinander, schnell)."),
]+table([["Übergang","Name","Energie"],["fest → flüssig","Schmelzen","wird aufgenommen"],["flüssig → gasförmig","Verdampfen","wird aufgenommen"],["gasförmig → flüssig","Kondensieren","wird abgegeben"],["flüssig → fest","Erstarren","wird abgegeben"],["fest → gasförmig","Sublimieren","wird aufgenommen"],["gasförmig → fest","Resublimieren (Desublimation)","wird abgegeben"]],[5.5*cm,6*cm,5.5*cm])
s+=[P("Beim Schmelzen und Sieden bleibt die Temperatur konstant, obwohl Energie zugeführt wird: Die Energie wird zum Lösen der Anziehungskräfte zwischen den Teilchen gebraucht (latente Wärme). Wasser: Schmelzpunkt 0 °C, Siedepunkt 100 °C (bei 1013 hPa). Die <b>Dichte</b> ρ = m / V (Wasser: 1,00 g/cm³ bei 4 °C) ist eine typische Stoffeigenschaft. Wasser ist im festen Zustand weniger dicht als flüssig („Anomalie des Wassers“), deshalb schwimmt Eis."),
Paragraph("Trennverfahren für Gemische",H2)]
s+=table([["Verfahren","Prinzip","Beispiel"],["Filtrieren","unterschiedliche Teilchengröße","Sand aus Wasser entfernen"],["Sedimentieren / Dekantieren","unterschiedliche Dichte","Schlamm absetzen lassen"],["Eindampfen / Kristallisieren","unterschiedliche Siedepunkte, Feststoff bleibt","Salz aus Meerwasser"],["Destillieren","unterschiedliche Siedepunkte","Alkohol aus Wein, Trinkwasser aus Meerwasser"],["Chromatographie","unterschiedliche Wanderungsgeschwindigkeit","Farbstoffe in Filzstiften"],["Extrahieren","unterschiedliche Löslichkeit","Koffein aus Kaffee, Tee ziehen lassen"],["Magnetscheidung","magnetische Eigenschaften","Eisen aus Schrott"]],[4.5*cm,6*cm,6.5*cm])

# 2
s+=h1("2. Geschichte der Atommodelle")
s+=[P("Modelle sind vereinfachte Darstellungen der Wirklichkeit. Sie werden verworfen oder verfeinert, sobald neue Experimente sie widerlegen. Das Wort „Atom“ stammt vom griechischen <i>atomos</i> („unteilbar“). Heute wissen wir, dass Atome aus noch kleineren Teilchen bestehen."),
img("models.png",17*cm,"Abb. 2: Von der Kugel zur Wahrscheinlichkeitswolke – fünf Atommodelle im Überblick.")]
s+=table([["Modell","Forscher","Kernaussage / Experiment"],["Kugelmodell","John Dalton, 1803","Atome sind unteilbare, massive Kugeln; jedes Element hat eigene Atome."],["Rosinenkuchenmodell","J. J. Thomson, 1904","Entdeckung des Elektrons (Kathodenstrahlen): negative Teilchen in positiver Masse."],["Kern-Hülle-Modell","Ernest Rutherford, 1911","Goldfolien-Streuversuch: fast alle α-Teilchen fliegen durch, wenige werden stark abgelenkt → winziger, positiver, schwerer Kern; Atom fast leer."],["Schalenmodell","Niels Bohr, 1913","Elektronen kreisen auf festen Bahnen (Schalen) mit bestimmten Energien."],["Orbitalmodell","E. Schrödinger u. a., 1926","Elektronen werden durch Aufenthaltswahrscheinlichkeiten (Orbitale) beschrieben."]],[3.6*cm,3.6*cm,9.8*cm])
s+=box("Wusstest du?","Wäre der Atomkern so groß wie eine Erbse, hätte das gesamte Atom einen Durchmesser von etwa 100 Metern. Der Kern ist ca. 10 000- bis 100 000-mal kleiner als das Atom.")

# 3
s+=h1("3. Der Atombau, Isotope &amp; Ionen")
s+=[P("Ein Atom besteht aus einem winzigen, schweren <b>Kern</b> (Protonen und Neutronen, zusammen <b>Nukleonen</b>) und einer <b>Hülle</b> aus Elektronen. Fast die gesamte Masse steckt im Kern, fast das gesamte Volumen ist Hülle. Zusammengehalten wird der Kern durch die starke Kernkraft, die Elektronen durch die elektrische Anziehung zum Kern."),
img("atom.png",9.5*cm,"Abb. 3: Aufbau eines Atoms (schematisch, nicht maßstabsgetreu)."),
]+table([["Teilchen","Ladung","Masse","Ort"],["Proton (p<super>+</super>)","+1","1 u","Kern"],["Neutron (n)","0","1 u","Kern"],["Elektron (e<super>−</super>)","−1","≈ 1/1836 u","Hülle"]],[5*cm,3*cm,4*cm,5*cm])
s+=[Paragraph("Wichtige Begriffe",H2)]+bl(["<b>Ordnungszahl Z</b> = Zahl der Protonen. Sie bestimmt das Element.","<b>Massenzahl A</b> = Protonen + Neutronen. Neutronenzahl N = A − Z.","<b>Nuklidschreibweise</b>: <super>A</super><sub>Z</sub>X, z. B. <super>12</super><sub>6</sub>C.","<b>Atomare Masseneinheit</b>: 1 u = 1/12 der Masse eines C-12-Atoms ≈ 1,66 · 10<super>−27</super> kg.","<b>Isotope</b>: gleiche Protonenzahl, unterschiedliche Neutronenzahl. Die relative Atommasse im Periodensystem ist der Durchschnitt der natürlichen Isotopengemische.","<b>Ion</b>: geladenes Atom. Elektronen abgegeben → Kation (+), aufgenommen → Anion (−).","<b>Schalenmodell</b>: Schalen K, L, M … fassen max. 2, 8, 18 … Elektronen (2n²)."])
s+=[Spacer(1,4),img("bohr.png",17*cm,"Abb. 4: Bohr-Modelle ausgewählter Elemente. Die Valenzelektronen der äußersten Schale bestimmen das Verhalten.")]
s+=[Paragraph("Beispiele für Isotope",H2)]
s+=table([["Nuklid","Protonen","Neutronen","Besonderheit"],["<super>1</super>H (Protium)","1","0","99,98 % des Wasserstoffs"],["<super>2</super>H (Deuterium)","1","1","„schwerer Wasserstoff“, D<sub>2</sub>O = schweres Wasser"],["<super>3</super>H (Tritium)","1","2","radioaktiv (T<sub>1/2</sub> ≈ 12,3 a)"],["<super>12</super>C","6","6","98,9 %, Basis der Atommasseneinheit"],["<super>14</super>C","6","8","radioaktiv, Altersbestimmung (C-14-Methode)"],["<super>235</super>U / <super>238</super>U","92","143 / 146","Kernbrennstoff / häufigstes Uran-Isotop"]],[3.7*cm,2.3*cm,2.7*cm,8.3*cm])
s+=box("Rechenbeispiel: Ion","Chlorid-Ion <super>35</super>Cl<super>−</super>: Z = 17 → 17 Protonen; N = 35 − 17 = 18 Neutronen; da das Ion einfach negativ geladen ist, hat es 17 + 1 = 18 Elektronen.")
s+=box("Merke","Die äußerste Schale will voll sein (Edelgaskonfiguration, „Oktettregel“, bei H und He „Duett“). Deshalb geben Atome Elektronen ab, nehmen sie auf oder teilen sie.")

# 4
s+=h1("4. Elektronenkonfiguration &amp; Orbitale")
s+=[P("Das Orbitalmodell verfeinert das Schalenmodell: Jede Schale (Hauptquantenzahl n = 1, 2, 3 …) besteht aus Unterschalen <b>s, p, d, f</b>. Ein <b>Orbital</b> ist der Raum, in dem sich ein Elektron mit hoher Wahrscheinlichkeit (ca. 90 %) aufhält. Jedes Orbital fasst maximal zwei Elektronen."),
img("orbitals.png",17*cm,"Abb. 5: Form der s- und p-Orbitale und das Aufbauprinzip (Füllreihenfolge der Unterschalen).")]
s+=table([["Unterschale","Anzahl Orbitale","max. Elektronen","Form"],["s","1","2","kugelförmig"],["p","3","6","hantelförmig (p<sub>x</sub>, p<sub>y</sub>, p<sub>z</sub>)"],["d","5","10","kleeblattförmig"],["f","7","14","komplexer"]],[3.5*cm,4*cm,4*cm,5.5*cm])
s+=[Paragraph("Die drei Füllregeln",H2)]+bl(["<b>Aufbauprinzip</b>: Elektronen besetzen zuerst die energieärmsten Orbitale (1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p …).","<b>Pauli-Prinzip</b>: In einem Orbital sitzen höchstens 2 Elektronen, und zwar mit entgegengesetztem Spin (↑↓).","<b>Hundsche Regel</b>: Gleichwertige Orbitale (z. B. die drei p-Orbitale) werden erst einzeln mit parallelem Spin besetzt, dann gepaart."])
s+=[Spacer(1,4),img("cfg.png",15*cm,"Abb. 6: Orbitalbesetzung (Kästchenschema) bei C, O und Ne. Beachte die Hundsche Regel beim Kohlenstoff und Sauerstoff.")]
s+=table([["Element","Z","Elektronenkonfiguration","Kurzschreibweise"],["H","1","1s<super>1</super>","1s<super>1</super>"],["C","6","1s<super>2</super> 2s<super>2</super> 2p<super>2</super>","[He] 2s<super>2</super> 2p<super>2</super>"],["O","8","1s<super>2</super> 2s<super>2</super> 2p<super>4</super>","[He] 2s<super>2</super> 2p<super>4</super>"],["Ne","10","1s<super>2</super> 2s<super>2</super> 2p<super>6</super>","[He] 2s<super>2</super> 2p<super>6</super>"],["Na","11","1s<super>2</super> 2s<super>2</super> 2p<super>6</super> 3s<super>1</super>","[Ne] 3s<super>1</super>"],["Cl","17","1s<super>2</super> 2s<super>2</super> 2p<super>6</super> 3s<super>2</super> 3p<super>5</super>","[Ne] 3s<super>2</super> 3p<super>5</super>"],["Fe","26","… 4s<super>2</super> 3d<super>6</super>","[Ar] 4s<super>2</super> 3d<super>6</super>"],["Cu","29","… 4s<super>1</super> 3d<super>10</super> (Ausnahme)","[Ar] 4s<super>1</super> 3d<super>10</super>"]],[2.5*cm,1.5*cm,7.3*cm,5.7*cm])
s+=box("Merke","Die Zahl der Valenzelektronen entspricht bei den Hauptgruppen der Gruppennummer (1, 2, 13–18 → 1, 2, 3–8). Chrom ([Ar] 4s<super>1</super> 3d<super>5</super>) und Kupfer sind Ausnahmen: Halb- und vollbesetzte d-Unterschalen sind besonders stabil.")

# 5
s+=h1("5. Das Periodensystem &amp; seine Trends")
s+=[P("Das Periodensystem (Mendelejew 1869, Meyer) ordnet alle bekannten Elemente nach steigender Ordnungszahl. <b>Perioden</b> (7 Zeilen) entsprechen der Zahl der besetzten Schalen. <b>Gruppen</b> (18 Spalten) enthalten Elemente mit gleich vielen Valenzelektronen und daher ähnlichen Eigenschaften. Mendelejew ließ Lücken für damals noch unbekannte Elemente (z. B. Gallium, Germanium) und sagte deren Eigenschaften voraus."),
img("pt.png",17*cm,"Abb. 7: Periodensystem, farbig nach Elementfamilien.")]
s+=table([["Gruppe","Name","Valenz-e⁻","Eigenschaften"],["1","Alkalimetalle","1","weich, sehr reaktiv mit Wasser (Li, Na, K): 2 Na + 2 H<sub>2</sub>O → 2 NaOH + H<sub>2</sub>"],["2","Erdalkalimetalle","2","reaktiv, Mg brennt hell, Ca in Knochen"],["3–12","Übergangsmetalle","–","hart, gute Leiter, oft farbige Verbindungen, Katalysatoren (Fe, Cu, Au)"],["13–16","Bor-, Kohlenstoff-, Stickstoff-, Sauerstoffgruppe","3–6","Übergang von Metallen zu Nichtmetallen"],["17","Halogene („Salzbildner“)","7","sehr reaktive Nichtmetalle (F, Cl, Br, I), bilden Salze"],["18","Edelgase","8 (He: 2)","praktisch reaktionsträge (He, Ne, Ar)"]],[1.8*cm,4.2*cm,2.2*cm,8.8*cm])
s+=[Paragraph("Trends im Periodensystem",H2),img("trends.png",16*cm,"Abb. 8: Periodische Trends (dunkler = größerer Wert). Atomradius sinkt nach rechts, EN und Ionisierungsenergie steigen nach rechts.")]
s+=bl(["<b>Atomradius</b>: wächst in einer Gruppe nach unten (mehr Schalen), sinkt in einer Periode nach rechts (stärkere Kernladung zieht die Hülle enger).","<b>Ionisierungsenergie</b>: Energie zum Entfernen des äußersten Elektrons. Edelgase haben die höchsten Werte, Alkalimetalle die niedrigsten.","<b>Elektronegativität (EN)</b>: Maß für die Fähigkeit, Bindungselektronen anzuziehen. Skala nach Pauling von ca. 0,7 (Fr) bis 4,0 (F).","<b>Metallcharakter</b>: wächst nach links und unten."])
s+=table([["Element","Na","Mg","Al","Si","P","S","Cl","O","F","H","C","N"],["EN","0,9","1,3","1,6","1,9","2,2","2,6","3,2","3,5","4,0","2,2","2,5","3,0"]],[2.2*cm]+[1.2*cm]*12+[0]*0 if False else [2.0*cm]+[1.25*cm]*12)

# 6
s+=h1("6. Die ersten 20 Elemente im Detail")
rows=[["Z","Symbol","Name","rel. Atommasse (u)","Gruppe","Zustand (20 °C)","Wo begegnet es dir?"],
["1","H","Wasserstoff","1,008","1","gasförmig","häufigstes Element im Universum, Sonne, Wasser"],
["2","He","Helium","4,003","18","gasförmig","Ballons, Kühlmittel, Edelgas"],
["3","Li","Lithium","6,94","1","fest","Akkus, Handys"],
["4","Be","Beryllium","9,012","2","fest","Legierungen, Röntgenfenster"],
["5","B","Bor","10,81","13","fest","Borax, Glas (Pyrex)"],
["6","C","Kohlenstoff","12,011","14","fest","Leben, Diamant, Graphit, Kohle"],
["7","N","Stickstoff","14,007","15","gasförmig","78 % der Luft, Dünger, Proteine"],
["8","O","Sauerstoff","15,999","16","gasförmig","21 % der Luft, Atmung, Verbrennung"],
["9","F","Fluor","18,998","17","gasförmig","Zahnpasta (Fluorid), Teflon"],
["10","Ne","Neon","20,180","18","gasförmig","Leuchtreklame"],
["11","Na","Natrium","22,990","1","fest","Kochsalz NaCl"],
["12","Mg","Magnesium","24,305","2","fest","Chlorophyll, Leichtmetall, Feuerwerk"],
["13","Al","Aluminium","26,982","13","fest","Dosen, Flugzeuge, Folie"],
["14","Si","Silicium","28,085","14","fest","Sand, Glas, Chips, Solarzellen"],
["15","P","Phosphor","30,974","15","fest","DNA, Knochen, Dünger, Streichhölzer"],
["16","S","Schwefel","32,06","16","fest","Vulkane, Schwefelsäure, Gummi"],
["17","Cl","Chlor","35,45","17","gasförmig","Schwimmbad, Salz, PVC"],
["18","Ar","Argon","39,948","18","gasförmig","Schutzgas beim Schweißen, Glühbirnen"],
["19","K","Kalium","39,098","1","fest","Dünger, Bananen, Nervenfunktion"],
["20","Ca","Calcium","40,078","2","fest","Knochen, Zähne, Kalk, Gips"]]
s+=table(rows,[0.9*cm,1.4*cm,2.6*cm,2.3*cm,1.5*cm,2.3*cm,6*cm])
s+=[Paragraph("Ausgewählte weitere Elemente",H2)]
s+=table([["Symbol","Name","Z","Wo begegnet es dir?"],["Fe","Eisen","26","Stahl, Blut (Hämoglobin), rostet zu Fe<sub>2</sub>O<sub>3</sub>"],["Cu","Kupfer","29","Kabel, Münzen, Wasserrohre"],["Zn","Zink","30","Verzinkung, Batterien, Sonnencreme"],["Ag","Silber","47","Schmuck, Besteck, bester elektrischer Leiter"],["I","Iod","53","Schilddrüse, Desinfektion, violett-schwarz"],["Au","Gold","79","Schmuck, Elektronik, reagiert kaum"],["Hg","Quecksilber","80","einziges bei 20 °C flüssiges Metall, giftig"],["Pb","Blei","82","Akkus, Strahlenschutz, giftig"],["U","Uran","92","Kernkraft, radioaktiv"]],[2*cm,3.5*cm,1.5*cm,10*cm])
s+=box("Wusstest du?","Der menschliche Körper besteht zu etwa 96 % aus nur vier Elementen: Sauerstoff (ca. 65 %), Kohlenstoff (18 %), Wasserstoff (10 %) und Stickstoff (3 %). Brom und Quecksilber sind die einzigen bei Raumtemperatur flüssigen Elemente.")

# 7
s+=h1("7. Chemische Bindungen, Lewis-Formeln &amp; Molekülgeometrie")
s+=[img("bonds.png",16.5*cm,"Abb. 9: Die drei Bindungstypen.")]
s+=table([["Typ","Zwischen","Prinzip","Beispiel"],["Ionenbindung","Metall + Nichtmetall","Elektronenübertragung, Anziehung der Ionen (Ionengitter)","NaCl, MgO"],["Kovalente Bindung","Nichtmetall + Nichtmetall","gemeinsame Elektronenpaare","H<sub>2</sub>O, CO<sub>2</sub>, O<sub>2</sub>"],["Metallbindung","Metall + Metall","Atomrümpfe im „Elektronengas“","Fe, Cu, Au"]],[3.3*cm,3.9*cm,6.3*cm,3.5*cm])
s+=bl(["<b>Ionenverbindungen</b>: hohe Schmelzpunkte, spröde, leiten als Schmelze oder Lösung Strom (bewegliche Ionen), nicht als Feststoff.","<b>Metalle</b>: leiten Strom und Wärme (freie Elektronen), verformbar, glänzend.","<b>Molekülverbindungen</b>: niedrige Schmelz- und Siedepunkte, leiten meist keinen Strom."])
s+=[Paragraph("Polarität und Elektronegativitätsdifferenz",H2)]
s+=table([["ΔEN (Differenz)","Bindungsart","Beispiel"],["0 bis ca. 0,4","unpolare (reine) Atombindung","H–H, Cl–Cl, C–H"],["ca. 0,4 bis 1,7","polare Atombindung (Partialladungen δ+, δ−)","H–O, H–Cl, C–O"],["über ca. 1,7","Ionenbindung","Na–Cl (ΔEN = 2,3), Mg–O"]],[4*cm,7.5*cm,5.5*cm])
s+=[Paragraph("Lewis-Formeln (Valenzstrichformeln)",H2),P("In der Lewis-Formel werden Valenzelektronen als Punkte oder Striche gezeichnet. Ein Strich zwischen zwei Atomen ist ein <b>bindendes Elektronenpaar</b>, ein Strich an einem Atom ist ein <b>freies (nichtbindendes) Elektronenpaar</b>. Ziel ist, dass jedes Atom (außer H) ein Oktett erreicht.")]
s+=box("So zeichnest du eine Lewis-Formel","1) Valenzelektronen aller Atome addieren (bei Ionen Ladung berücksichtigen). 2) Zentralatom (meist das mit der niedrigsten EN, nie H) wählen und mit Einfachbindungen verbinden. 3) Restliche Elektronen als freie Paare auf die Außenatome, dann aufs Zentralatom verteilen. 4) Fehlt ein Oktett, Doppel- oder Dreifachbindungen bilden.<br/>Beispiel CO<sub>2</sub>: 4 + 2·6 = 16 Valenzelektronen → O=C=O mit je zwei freien Paaren an jedem O.")
s+=[Paragraph("Molekülgeometrie: das EPA-/VSEPR-Modell",H2),P("Elektronenpaare (bindend und frei) stoßen sich ab und ordnen sich so an, dass sie möglichst weit voneinander entfernt sind. Freie Elektronenpaare beanspruchen mehr Platz als bindende und drücken die Bindungswinkel etwas zusammen."),
img("vsepr.png",17*cm,"Abb. 10: Räumlicher Bau typischer Moleküle mit Bindungswinkeln.")]
s+=table([["Molekül","Bindende / freie Paare am Zentralatom","Geometrie","Winkel","Polar?"],["CO<sub>2</sub>","2 / 0","linear","180°","unpolar (Dipole heben sich auf)"],["H<sub>2</sub>O","2 / 2","gewinkelt","104,5°","stark polar (Dipolmolekül)"],["BF<sub>3</sub>","3 / 0","trigonal planar","120°","unpolar"],["NH<sub>3</sub>","3 / 1","trigonal pyramidal","107°","polar"],["CH<sub>4</sub>","4 / 0","tetraedrisch","109,5°","unpolar"]],[2.2*cm,5.3*cm,3.6*cm,2*cm,3.9*cm])
s+=box("Merke","Ob ein Molekül ein Dipol ist, hängt von <b>Polarität der Bindungen UND Geometrie</b> ab. CO<sub>2</sub> hat polare Bindungen, ist aber wegen der linearen Form insgesamt unpolar. Wasser ist gewinkelt und daher ein Dipol – das erklärt seine besonderen Eigenschaften.")

# 8
s+=h1("8. Zwischenmolekulare Kräfte")
s+=[P("Zwischen Molekülen wirken Anziehungskräfte, die viel schwächer sind als Atombindungen, aber Siedepunkt, Löslichkeit und Aggregatzustand bestimmen. Je stärker die Kräfte, desto höher der Siedepunkt."),
img("hbond.png",9*cm,"Abb. 11: Wasserstoffbrücke zwischen zwei Wassermolekülen.")]
s+=table([["Kraft","Wirkt zwischen","Stärke","Beispiel"],["Van-der-Waals-Kräfte (London-Dispersion)","allen Molekülen, durch kurzzeitige Ladungsverschiebungen","schwach, wächst mit Molekülgröße","N<sub>2</sub>, CH<sub>4</sub>, Edelgase"],["Dipol-Dipol-Kräfte","polaren Molekülen","mittel","HCl, Aceton"],["Wasserstoffbrücken","H (gebunden an N, O, F) und freiem Elektronenpaar von N, O, F","stark (unter den zwischenmolekularen Kräften)","H<sub>2</sub>O, NH<sub>3</sub>, DNA-Basenpaare"]],[4.2*cm,5.2*cm,3.6*cm,4*cm])
s+=bl(["<b>Siedepunkte</b>: Wasser (100 °C) siedet viel höher als H<sub>2</sub>S (−60 °C), obwohl H<sub>2</sub>S schwerer ist – wegen der Wasserstoffbrücken.","<b>Löslichkeit</b>: „Gleiches löst sich in Gleichem.“ Polare Stoffe (Zucker, Salz) lösen sich in Wasser, unpolare (Öl, Benzin) in unpolaren Lösungsmitteln.","<b>Tenside</b> (Seife) haben einen polaren Kopf und einen unpolaren Schwanz und vermitteln zwischen Fett und Wasser."])

# 9
s+=h1("9. Nomenklatur: Formeln &amp; Namen")
s+=[P("Ionenverbindungen sind nach außen elektrisch neutral: Die Summe der positiven Ladungen muss gleich der Summe der negativen sein. Die <b>Verhältnisformel</b> gibt das kleinste ganzzahlige Verhältnis der Ionen an.")]
s+=table([["Kationen","Anionen"],["Na<super>+</super>, K<super>+</super>, Ag<super>+</super>, NH<sub>4</sub><super>+</super> (Ammonium)","F<super>−</super>, Cl<super>−</super>, Br<super>−</super>, I<super>−</super>, OH<super>−</super> (Hydroxid), NO<sub>3</sub><super>−</super> (Nitrat)"],["Mg<super>2+</super>, Ca<super>2+</super>, Zn<super>2+</super>, Cu<super>2+</super>, Fe<super>2+</super>","O<super>2−</super> (Oxid), S<super>2−</super> (Sulfid), SO<sub>4</sub><super>2−</super> (Sulfat), CO<sub>3</sub><super>2−</super> (Carbonat)"],["Al<super>3+</super>, Fe<super>3+</super>","PO<sub>4</sub><super>3−</super> (Phosphat)"]],[8.5*cm,8.5*cm])
s+=box("Formel aufstellen: Kreuzregel","Beispiel Aluminiumoxid: Al<super>3+</super> und O<super>2−</super>. Ladungszahlen „über Kreuz“ als Indizes: Al<sub>2</sub>O<sub>3</sub> (2·3+ = 6+, 3·2− = 6−). <br/>Beispiel Calciumchlorid: Ca<super>2+</super> + 2 Cl<super>−</super> → CaCl<sub>2</sub>. <br/>Bei Elementen mit mehreren Ladungen steht die Wertigkeit in römischen Ziffern: Eisen(II)-oxid FeO, Eisen(III)-oxid Fe<sub>2</sub>O<sub>3</sub>.")
s+=[Paragraph("Molekülverbindungen",H2),P("Bei Verbindungen aus Nichtmetallen zeigen griechische Zahlwörter die Atomzahl: <b>mono</b> (1), <b>di</b> (2), <b>tri</b> (3), <b>tetra</b> (4), <b>penta</b> (5), <b>hexa</b> (6). Beispiele: CO = Kohlenstoffmonoxid, CO<sub>2</sub> = Kohlenstoffdioxid, N<sub>2</sub>O<sub>5</sub> = Distickstoffpentoxid, SO<sub>3</sub> = Schwefeltrioxid.")]
s+=table([["Formel","Trivialname","Systematischer Name"],["H<sub>2</sub>O","Wasser","Wasserstoffoxid / Dihydrogenmonoxid"],["NaCl","Kochsalz","Natriumchlorid"],["CaCO<sub>3</sub>","Kalk, Kreide, Marmor","Calciumcarbonat"],["NaHCO<sub>3</sub>","Natron, Backsoda","Natriumhydrogencarbonat"],["HCl (aq)","Salzsäure","Chlorwasserstoff-Lösung"],["H<sub>2</sub>SO<sub>4</sub>","Schwefelsäure","Schwefelsäure"],["NH<sub>3</sub>","Ammoniak","Ammoniak (Stickstofftrihydrid)"],["CH<sub>4</sub>","Erdgas","Methan"]],[3.5*cm,5.5*cm,8*cm])

# 10
s+=h1("10. Chemische Reaktionen &amp; Gleichungen")
s+=[P("Bei einer chemischen Reaktion werden Bindungen gelöst und neu geknüpft; aus <b>Edukten</b> entstehen <b>Produkte</b> mit neuen Eigenschaften. Atome gehen dabei nicht verloren (<b>Gesetz der Massenerhaltung</b>, Lavoisier). Deshalb muss jede Gleichung auf beiden Seiten gleich viele Atome jeder Sorte haben. Außerdem gilt das <b>Gesetz der konstanten Proportionen</b>: Elemente verbinden sich stets im gleichen Massenverhältnis (Wasser: 1 g H zu 8 g O).")]
s+=box("Reaktionsgleichung in 4 Schritten aufstellen","1) Edukte und Produkte mit Formeln hinschreiben (Wasserstoff, Sauerstoff, Stickstoff, Halogene liegen als zweiatomige Moleküle H<sub>2</sub>, O<sub>2</sub>, N<sub>2</sub>, F<sub>2</sub>, Cl<sub>2</sub>, Br<sub>2</sub>, I<sub>2</sub> vor). 2) Atome je Element zählen. 3) Mit Koeffizienten (Faktoren vor den Formeln) ausgleichen – Indizes nie ändern! 4) Kontrolle: Atome links = rechts.<br/><b>Beispiel Rosten</b>: Fe + O<sub>2</sub> → Fe<sub>2</sub>O<sub>3</sub> → 4 Fe + 3 O<sub>2</sub> → 2 Fe<sub>2</sub>O<sub>3</sub>")
s+=table([["Reaktion","Gleichung"],["Wasserbildung (Knallgasreaktion)","2 H<sub>2</sub> + O<sub>2</sub> → 2 H<sub>2</sub>O"],["Verbrennung von Methan","CH<sub>4</sub> + 2 O<sub>2</sub> → CO<sub>2</sub> + 2 H<sub>2</sub>O"],["Photosynthese","6 CO<sub>2</sub> + 6 H<sub>2</sub>O → C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub>"],["Zellatmung","C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub> → 6 CO<sub>2</sub> + 6 H<sub>2</sub>O"],["Magnesium verbrennen","2 Mg + O<sub>2</sub> → 2 MgO"],["Kalkbrennen","CaCO<sub>3</sub> → CaO + CO<sub>2</sub>"]],[6*cm,11*cm])
s+=[Paragraph("Reaktionstypen",H2)]+bl(["<b>Synthese</b>: A + B → AB (2 Mg + O<sub>2</sub> → 2 MgO)","<b>Analyse / Zerlegung</b>: AB → A + B (2 H<sub>2</sub>O → 2 H<sub>2</sub> + O<sub>2</sub>, Elektrolyse)","<b>Einfache Substitution</b>: AB + C → AC + B (Zn + 2 HCl → ZnCl<sub>2</sub> + H<sub>2</sub>)","<b>Doppelte Umsetzung / Fällung</b>: AB + CD → AD + CB (AgNO<sub>3</sub> + NaCl → AgCl↓ + NaNO<sub>3</sub>)","<b>Säure-Base-Reaktion</b>: Protonenübertragung (siehe Kapitel 16)","<b>Redoxreaktion</b>: Elektronenübertragung (siehe Kapitel 17)","<b>Exotherm</b>: gibt Energie ab. <b>Endotherm</b>: nimmt Energie auf."])
s+=box("Nachweisreaktionen","Sauerstoff: Glimmspanprobe (glimmender Span flammt auf). Wasserstoff: Knallgasprobe (pfeifender/„knallender“ Ton). Kohlenstoffdioxid: Kalkwasser trübt sich (CaCO<sub>3</sub>). Wasser: weißes Kupfersulfat färbt sich blau. Stärke: Iod-Kaliumiodid-Lösung färbt sich blauviolett.")

# 11
s+=h1("11. Stöchiometrie: Mol &amp; Rechnen")
s+=[P("Ein <b>Mol</b> ist die Stoffmenge, die genau 6,022 · 10<super>23</super> Teilchen enthält (Avogadro-Konstante N<sub>A</sub>). Die <b>molare Masse</b> M in g/mol entspricht zahlenmäßig der relativen Atom- bzw. Molekülmasse im Periodensystem. Das Mol verbindet die unsichtbare Teilchenwelt mit der wägbaren Masse.")]
s+=box("Wichtige Formeln","n = m / M &nbsp;&nbsp;|&nbsp;&nbsp; N = n · N<sub>A</sub> &nbsp;&nbsp;|&nbsp;&nbsp; c = n / V &nbsp;&nbsp;|&nbsp;&nbsp; V = n · V<sub>m</sub><br/>(n Stoffmenge in mol, m Masse in g, M molare Masse in g/mol, V<sub>m</sub> molares Volumen eines Gases)")
s+=[Paragraph("Beispiel 1: Molare Masse",H2),P("M(CaCO<sub>3</sub>) = 40,08 + 12,01 + 3 · 16,00 = <b>100,09 g/mol</b>. Wie viel Mol sind 25 g? n = 25 g / 100,09 g/mol ≈ <b>0,25 mol</b>."),
Paragraph("Beispiel 2: Masse eines Produkts",H2),P("Wie viel Gramm Wasser entstehen aus 4 g Wasserstoff? Gleichung: 2 H<sub>2</sub> + O<sub>2</sub> → 2 H<sub>2</sub>O. n(H<sub>2</sub>) = 4 g / 2,016 g/mol ≈ 2 mol. Verhältnis H<sub>2</sub> : H<sub>2</sub>O = 2 : 2 → n(H<sub>2</sub>O) = 2 mol. m = 2 mol · 18 g/mol = <b>36 g</b>."),
Paragraph("Beispiel 3: Begrenzender Reaktand",H2),P("Reagieren 3 mol H<sub>2</sub> mit 1 mol O<sub>2</sub>, ist O<sub>2</sub> der <b>limitierende Reaktand</b>: Nach der Gleichung reichen 1 mol O<sub>2</sub> nur für 2 mol H<sub>2</sub>. Es entstehen 2 mol H<sub>2</sub>O, 1 mol H<sub>2</sub> bleibt übrig."),
Paragraph("Ausbeute und Massenanteil",H2)]
s+=bl(["<b>Ausbeute</b> = tatsächlich erhaltene Menge / theoretisch mögliche Menge · 100 %.","<b>Massenanteil</b> w(X) = m(X) / m(gesamt). Beispiel: w(O) in H<sub>2</sub>O = 16 / 18 ≈ 89 %.","<b>Summenformel aus Massenverhältnis</b>: Massen durch molare Massen teilen und das kleinste ganzzahlige Verhältnis bilden."])

# 12
s+=h1("12. Gase &amp; Gasgesetze")
s+=[P("Gase füllen jeden verfügbaren Raum aus und sind stark komprimierbar. Im Teilchenmodell bewegen sich die Teilchen schnell und ungeordnet und stoßen gegen die Gefäßwand – das ergibt den <b>Druck</b>. Die Temperatur ist ein Maß für die mittlere Bewegungsenergie der Teilchen."),
img("gas.png",16*cm,"Abb. 12: Die drei klassischen Gasgesetze.")]
s+=table([["Gesetz","Formel","Bedingung"],["Boyle-Mariotte","p · V = konstant","T und n konstant"],["Gay-Lussac (Charles)","V / T = konstant","p und n konstant, T in Kelvin"],["Amontons","p / T = konstant","V und n konstant, T in Kelvin"],["Allgemeine Gasgleichung","p · V = n · R · T","ideales Gas, R = 8,314 J/(mol·K)"],["Avogadro","gleiche Volumina enthalten bei gleichem p, T gleich viele Teilchen","Molvolumen V<sub>m</sub> ≈ 22,4 L/mol (0 °C, 1013 hPa), ≈ 24,5 L/mol (25 °C)"]],[4*cm,6.5*cm,6.5*cm])
s+=box("Kelvin-Skala","T (K) = ϑ (°C) + 273,15. Bei 0 K (−273,15 °C, absoluter Nullpunkt) stünde die Teilchenbewegung praktisch still. Bei Gasgesetzen immer in Kelvin rechnen!<br/>Beispiel: Ein Gas hat bei 300 K das Volumen 2 L. Bei 600 K (p konstant) hat es 4 L.")
s+=[P("<b>Dalton-Gesetz der Partialdrücke</b>: Der Gesamtdruck eines Gasgemischs ist die Summe der Einzeldrücke. <b>Luft</b> besteht aus ca. 78 % N<sub>2</sub>, 21 % O<sub>2</sub>, 0,93 % Ar und 0,04 % CO<sub>2</sub> (Volumenanteile).")]

# 13
s+=h1("13. Lösungen &amp; Konzentrationen")
s+=[P("Eine Lösung besteht aus <b>Lösungsmittel</b> (meist Wasser) und <b>gelöstem Stoff</b>. Beim Lösen von Salz umgeben polare Wassermoleküle die Ionen (<b>Hydratation</b>) und lösen sie aus dem Gitter. Ist keine weitere Menge mehr löslich, ist die Lösung <b>gesättigt</b>. Die Löslichkeit der meisten Feststoffe steigt mit der Temperatur, die von Gasen sinkt (warme Cola verliert schneller Kohlensäure).")]
s+=table([["Größe","Definition","Einheit"],["Stoffmengenkonzentration c","c = n / V","mol/L"],["Massenkonzentration β","β = m / V","g/L"],["Massenanteil w","w = m(Stoff) / m(Lösung)","% oder 1"],["Volumenanteil φ","φ = V(Stoff) / V(Gemisch)","% (z. B. Alkohol im Bier)"],["Verdünnung","c<sub>1</sub> · V<sub>1</sub> = c<sub>2</sub> · V<sub>2</sub>","–"]],[5*cm,7*cm,5*cm])
s+=box("Rechenbeispiel","5,85 g NaCl (M = 58,44 g/mol) werden zu 500 mL Lösung aufgefüllt. n = 5,85 / 58,44 = 0,100 mol; c = 0,100 mol / 0,500 L = <b>0,20 mol/L</b>.<br/>Verdünnen: Aus 100 mL einer 2 mol/L-Lösung sollen 500 mL werden → c<sub>2</sub> = 2 · 100 / 500 = 0,4 mol/L.")

# 14
s+=h1("14. Energie &amp; Reaktionsgeschwindigkeit")
s+=[P("Jede Reaktion ist mit einem Energieumsatz verbunden. Die <b>Reaktionsenthalpie ΔH</b> (bei konstantem Druck) gibt die Wärme an: <b>ΔH &lt; 0</b> bei exothermen Reaktionen (Energie wird frei), <b>ΔH &gt; 0</b> bei endothermen Reaktionen (Energie wird aufgenommen). Damit eine Reaktion startet, müssen die Teilchen die <b>Aktivierungsenergie E<sub>a</sub></b> überwinden – deshalb entzündet sich Holz nicht von selbst."),
img("energy.png",16*cm,"Abb. 13: Energieprofil einer exothermen und einer endothermen Reaktion. Ein Katalysator senkt die Aktivierungsenergie.")]
s+=[Paragraph("Was beeinflusst die Reaktionsgeschwindigkeit?",H2)]
s+=table([["Faktor","Wirkung","Erklärung (Stoßtheorie)"],["Temperatur ↑","schneller (Faustregel RGT-Regel: +10 K ≈ doppelte bis dreifache Geschwindigkeit)","mehr Teilchen erreichen die nötige Energie, mehr Zusammenstöße"],["Konzentration / Druck ↑","schneller","mehr Zusammenstöße pro Zeit"],["Zerteilungsgrad ↑","schneller (Mehl explodiert, ein Holzscheit nicht)","größere Oberfläche"],["Katalysator","schneller, wird nicht verbraucht","niedrigere Aktivierungsenergie, Gleichgewichtslage unverändert"]],[4*cm,6.3*cm,6.7*cm])
s+=box("Katalysatoren im Alltag","Auto-Katalysator (Pt, Rh, Pd wandelt CO, NO<sub>x</sub> in CO<sub>2</sub>, N<sub>2</sub>), Enzyme im Körper (Biokatalysatoren, z. B. Amylase im Speichel), Eisenkatalysator bei der Ammoniaksynthese.")

# 15
s+=h1("15. Chemisches Gleichgewicht")
s+=[P("Viele Reaktionen laufen in beide Richtungen (⇌). Im <b>chemischen Gleichgewicht</b> sind Hin- und Rückreaktion gleich schnell: Die Konzentrationen bleiben konstant, obwohl ständig Teilchen reagieren (dynamisches Gleichgewicht). Für a A + b B ⇌ c C + d D gilt das <b>Massenwirkungsgesetz</b>:"),
Paragraph("K = ([C]<super>c</super> · [D]<super>d</super>) / ([A]<super>a</super> · [B]<super>b</super>)",ParagraphStyle("f",parent=B,alignment=1,fontName="DVB",fontSize=11,spaceAfter=8)),
P("K &gt; 1: Gleichgewicht liegt auf der Produktseite; K &lt; 1: auf der Eduktseite. K hängt nur von der Temperatur ab."),
Paragraph("Prinzip von Le Chatelier (Prinzip vom kleinsten Zwang)",H2),P("Wird ein System im Gleichgewicht gestört, weicht es so aus, dass die Störung teilweise ausgeglichen wird.")]
s+=table([["Störung","Reaktion des Gleichgewichts"],["Konzentration eines Edukts ↑","Verschiebung Richtung Produkte"],["Konzentration eines Produkts ↓ (Entfernen)","Verschiebung Richtung Produkte"],["Druck ↑ (bei Gasen)","Richtung der Seite mit weniger Gasmolekülen"],["Temperatur ↑","Richtung der endothermen Reaktion"],["Katalysator","keine Verschiebung, nur schnellere Einstellung"]],[7.5*cm,9.5*cm])
s+=box("Beispiel: Haber-Bosch-Verfahren","N<sub>2</sub> + 3 H<sub>2</sub> ⇌ 2 NH<sub>3</sub> &nbsp; (ΔH = −92 kJ/mol). Hoher Druck (150–300 bar) begünstigt Ammoniak (4 → 2 Gasmoleküle). Niedrige Temperatur würde die Ausbeute erhöhen (exotherm), ist aber zu langsam; Kompromiss: ca. 400–500 °C mit Eisenkatalysator. Ammoniak ist Grundstoff für Düngemittel und ernährt einen großen Teil der Weltbevölkerung.")

# 16
s+=h1("16. Säuren, Basen &amp; pH-Wert")
s+=[P("Nach Brønsted ist eine <b>Säure</b> ein Protonendonator (gibt H<super>+</super> ab), eine <b>Base</b> ein Protonenakzeptor. In Wasser bilden Säuren Oxonium-Ionen H<sub>3</sub>O<super>+</super>, Basen (Laugen) Hydroxid-Ionen OH<super>−</super>. Der <b>pH-Wert</b> ist der negative dekadische Logarithmus der H<sub>3</sub>O<super>+</super>-Konzentration: <b>pH = −log c(H<sub>3</sub>O<super>+</super>)</b>. Bei 25 °C gilt pH + pOH = 14. Jeder Schritt auf der Skala bedeutet einen Faktor 10 in der Konzentration."),
img("ph.png",16*cm,"Abb. 14: pH-Skala mit Alltagsbeispielen.")]
s+=table([["Säure","Formel","Stärke","Vorkommen"],["Salzsäure","HCl","stark","Magensäure (ca. 0,5 %)"],["Schwefelsäure","H<sub>2</sub>SO<sub>4</sub>","stark","Autobatterie, Industrie"],["Salpetersäure","HNO<sub>3</sub>","stark","Dünger, Sprengstoffe"],["Essigsäure","CH<sub>3</sub>COOH","schwach","Essig"],["Kohlensäure","H<sub>2</sub>CO<sub>3</sub>","schwach","Sprudelwasser"],["Zitronensäure","C<sub>6</sub>H<sub>8</sub>O<sub>7</sub>","schwach","Zitrusfrüchte"]],[3.5*cm,3.5*cm,3*cm,7*cm])
s+=table([["Base / Lauge","Formel","Verwendung"],["Natronlauge","NaOH","Seifenherstellung, Rohrreiniger"],["Kalilauge","KOH","Batterien, Seifen"],["Kalkwasser","Ca(OH)<sub>2</sub>","CO<sub>2</sub>-Nachweis, Bauwesen"],["Ammoniak-Lösung","NH<sub>3</sub> (aq)","Reiniger, Dünger"]],[4*cm,4*cm,9*cm])
s+=box("Rechenbeispiele","0,01 mol/L HCl (starke Säure, vollständig dissoziiert): c(H<sub>3</sub>O<super>+</super>) = 10<super>−2</super> mol/L → <b>pH = 2</b>. <br/>0,001 mol/L NaOH: c(OH<super>−</super>) = 10<super>−3</super> → pOH = 3 → <b>pH = 11</b>.<br/><b>Neutralisation</b>: HCl + NaOH → NaCl + H<sub>2</sub>O (Säure + Base → Salz + Wasser). Die Titration bestimmt so die unbekannte Konzentration einer Lösung (Äquivalenzpunkt).")
s+=table([["Indikator","Farbe sauer","Umschlagbereich","Farbe basisch"],["Universalindikator","rot – orange","gesamte Skala 1–14","grün (neutral) – blau – violett"],["Lackmus","rot","pH 5–8","blau"],["Bromthymolblau","gelb","pH 6,0–7,6","blau (neutral: grün)"],["Phenolphthalein","farblos","pH 8,2–10","pink/violett"]],[4*cm,3.5*cm,4.5*cm,5*cm])
s+=[P("<b>Puffer</b> halten den pH-Wert nahezu konstant, auch wenn Säure oder Base zugegeben wird (z. B. Hydrogencarbonat-Puffer im Blut, pH ≈ 7,4). Säuren + unedle Metalle → Salz + Wasserstoff; Säuren + Carbonate → Salz + Wasser + CO<sub>2</sub> (Aufbrausen).")]

# 17
s+=h1("17. Redoxreaktionen &amp; Elektrochemie")
s+=[P("Eine <b>Redoxreaktion</b> ist eine Reaktion mit Elektronenübertragung. <b>Oxidation</b> = Elektronenabgabe (Oxidationszahl steigt), <b>Reduktion</b> = Elektronenaufnahme (Oxidationszahl sinkt). Beides läuft immer gemeinsam ab. Merkhilfe: <b>OIL RIG</b> – Oxidation Is Loss, Reduction Is Gain. Das Reduktionsmittel wird oxidiert (es gibt Elektronen ab), das Oxidationsmittel wird reduziert.")]
s+=box("Regeln für Oxidationszahlen","1) Atome in Elementen: 0 (Fe, O<sub>2</sub>, H<sub>2</sub>). 2) Einatomige Ionen: Ionenladung (Na<super>+</super> → +I). 3) Fluor immer −I. 4) Sauerstoff meist −II (Peroxide −I). 5) Wasserstoff meist +I (Metallhydride −I). 6) Summe der Oxidationszahlen = Gesamtladung des Teilchens.<br/>Beispiel Mn in KMnO<sub>4</sub>: +I + x + 4·(−II) = 0 → x = <b>+VII</b>.")
s+=box("Beispiel: Zink in Kupfersulfat","Zn + Cu<super>2+</super> → Zn<super>2+</super> + Cu<br/>Oxidation: Zn → Zn<super>2+</super> + 2 e<super>−</super> (Zn ist Reduktionsmittel). Reduktion: Cu<super>2+</super> + 2 e<super>−</super> → Cu (Cu<super>2+</super> ist Oxidationsmittel). Das unedlere Metall geht in Lösung, das edlere scheidet sich ab.")
s+=[Paragraph("Elektrochemische Spannungsreihe",H2)]
s+=table([["Redoxpaar","Standardpotenzial E° (V)","Charakter"],["Li / Li<super>+</super>","−3,04","sehr unedel, starkes Reduktionsmittel"],["Na / Na<super>+</super>","−2,71","unedel"],["Mg / Mg<super>2+</super>","−2,37","unedel"],["Al / Al<super>3+</super>","−1,66","unedel"],["Zn / Zn<super>2+</super>","−0,76","unedel"],["Fe / Fe<super>2+</super>","−0,44","unedel"],["H<sub>2</sub> / 2 H<super>+</super>","0,00","Bezugselektrode"],["Cu / Cu<super>2+</super>","+0,34","edel"],["Ag / Ag<super>+</super>","+0,80","edel"],["Au / Au<super>3+</super>","+1,50","sehr edel"]],[5*cm,5.5*cm,6.5*cm])
s+=[Paragraph("Galvanische Zelle und Elektrolyse",H2),P("In einer <b>galvanischen Zelle</b> (Batterie) laufen Oxidation und Reduktion räumlich getrennt ab; die Elektronen fließen über einen Leiter, Ionen über die Salzbrücke. An der <b>Anode</b> findet Oxidation statt, an der <b>Kathode</b> Reduktion (bei galvanischen Zellen ist die Anode der Minuspol). Die Zellspannung ist die Differenz der Standardpotenziale: U = E°(Kathode) − E°(Anode) = 0,34 V − (−0,76 V) = <b>1,10 V</b>."),
img("daniell.png",13*cm,"Abb. 15: Daniell-Element (Zink-Kupfer-Zelle).")]
s+=bl(["<b>Elektrolyse</b>: Mit elektrischer Energie wird eine nicht freiwillig ablaufende Reaktion erzwungen (2 H<sub>2</sub>O → 2 H<sub>2</sub> + O<sub>2</sub>; Aluminiumgewinnung aus Al<sub>2</sub>O<sub>3</sub>; Vergolden, Verchromen).","<b>Korrosion</b>: Rosten ist eine Redoxreaktion von Eisen mit Sauerstoff und Wasser. Schutz durch Lack, Verzinken (Opferanode Zn), Legieren (Edelstahl).","<b>Batterien</b> sind nicht wiederaufladbar, <b>Akkus</b> (Blei-, Li-Ionen) sind durch Elektrolyse wieder ladbar."])

# 18
s+=h1("18. Organische Chemie")
s+=[P("Die organische Chemie ist die Chemie der Kohlenstoffverbindungen. Kohlenstoff ist vierbindig, kann stabile Ketten, Ringe und Verzweigungen bilden und Einfach-, Doppel- und Dreifachbindungen eingehen. Deshalb gibt es Millionen organischer Verbindungen – Grundlage von Erdöl, Kunststoffen, Medikamenten und allen Lebewesen (Zucker, Fette, Proteine, DNA)."),
img("organic.png",16*cm,"Abb. 16: Strukturformeln einiger einfacher organischer Moleküle.")]
s+=[Paragraph("Kohlenwasserstoffe",H2)]
s+=table([["Stoffklasse","Allg. Formel","Bindung","Beispiel"],["Alkane (gesättigt)","C<sub>n</sub>H<sub>2n+2</sub>","nur Einfachbindungen","Methan CH<sub>4</sub>, Ethan C<sub>2</sub>H<sub>6</sub>"],["Alkene (ungesättigt)","C<sub>n</sub>H<sub>2n</sub>","eine C=C-Doppelbindung","Ethen C<sub>2</sub>H<sub>4</sub>"],["Alkine (ungesättigt)","C<sub>n</sub>H<sub>2n−2</sub>","eine C≡C-Dreifachbindung","Ethin C<sub>2</sub>H<sub>2</sub>"],["Aromaten","–","Ring mit delokalisierten e⁻","Benzol C<sub>6</sub>H<sub>6</sub>"]],[4*cm,3.3*cm,4.8*cm,4.9*cm])
s+=table([["n","Name","Formel","n","Name","Formel"],["1","Methan","CH<sub>4</sub>","6","Hexan","C<sub>6</sub>H<sub>14</sub>"],["2","Ethan","C<sub>2</sub>H<sub>6</sub>","7","Heptan","C<sub>7</sub>H<sub>16</sub>"],["3","Propan","C<sub>3</sub>H<sub>8</sub>","8","Octan","C<sub>8</sub>H<sub>18</sub>"],["4","Butan","C<sub>4</sub>H<sub>10</sub>","9","Nonan","C<sub>9</sub>H<sub>20</sub>"],["5","Pentan","C<sub>5</sub>H<sub>12</sub>","10","Decan","C<sub>10</sub>H<sub>22</sub>"]],[1.5*cm,3.5*cm,3.5*cm,1.5*cm,3.5*cm,3.5*cm])
s+=[P("Merkhilfe für die ersten vier Alkane: <b>„Method Eating Propane Butter“</b> – Methan, Ethan, Propan, Butan. Mit steigender Kettenlänge steigen Siedepunkt und Viskosität (Gas → Flüssigkeit → Wachs). Alkane reagieren durch <b>Verbrennung</b> und mit Halogenen (radikalische Substitution), Alkene und Alkine durch <b>Addition</b> (z. B. Bromwasser wird entfärbt – Nachweis der Doppelbindung)."),
Paragraph("Funktionelle Gruppen",H2)]
s+=table([["Gruppe","Struktur","Stoffklasse","Beispiel"],["Hydroxy","–OH","Alkohole","Ethanol C<sub>2</sub>H<sub>5</sub>OH (Getränke, Desinfektion)"],["Aldehyd","–CHO","Aldehyde","Formaldehyd, Acetaldehyd"],["Carbonyl (Keto)","C=O in der Kette","Ketone","Aceton (Nagellackentferner)"],["Carboxy","–COOH","Carbonsäuren","Essigsäure, Ameisensäure"],["Amino","–NH<sub>2</sub>","Amine","Aminosäuren, Proteine"],["Ester","–COO–","Ester","Fruchtaromen, Fette"]],[3*cm,3*cm,3.5*cm,7.5*cm])
s+=bl(["<b>Isomerie</b>: Gleiche Summenformel, verschiedene Struktur (Butan C<sub>4</sub>H<sub>10</sub> und Isobutan).","<b>Polymere</b>: Riesenmoleküle aus vielen Monomeren (Polyethylen aus Ethen, PVC, Nylon, Proteine, Stärke, Cellulose). Reaktionsarten: Polymerisation, Polykondensation, Polyaddition.","<b>Biomoleküle</b>: Kohlenhydrate (Glucose C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>, Stärke), Lipide (Fette, Öle), Proteine (Aminosäureketten), Nukleinsäuren (DNA, RNA).","<b>Erdöl</b> wird durch fraktionierte Destillation in Benzin, Diesel, Heizöl, Bitumen getrennt; durch <b>Cracken</b> werden lange Ketten in kürzere gespalten."])

# 19
s+=h1("19. Kernchemie &amp; Radioaktivität")
s+=[P("Manche Atomkerne sind instabil und zerfallen unter Aussendung von Strahlung. Die Kernumwandlung ist unabhängig von chemischen Bedingungen (Temperatur, Druck, Bindung). Die Aktivität wird in Becquerel (Bq, Zerfälle pro Sekunde) gemessen, die Strahlendosis in Sievert (Sv)."),
img("radiation.png",14*cm,"Abb. 17: Reichweite und Abschirmung der drei Strahlungsarten (schematisch).")]
s+=table([["Strahlung","Teilchen","Kern-Änderung","Reichweite in Luft"],["α (Alpha)","<super>4</super><sub>2</sub>He-Kern (2 p + 2 n)","Z −2, A −4","wenige cm"],["β<super>−</super> (Beta)","Elektron (aus n → p + e<super>−</super>)","Z +1, A gleich","einige Meter"],["γ (Gamma)","energiereiche elektromagnetische Strahlung","keine","sehr weit, durchdringend"]],[3*cm,6.3*cm,3.7*cm,4*cm])
s+=box("Beispiele für Zerfallsgleichungen","α-Zerfall: <super>238</super><sub>92</sub>U → <super>234</super><sub>90</sub>Th + <super>4</super><sub>2</sub>He<br/>β<super>−</super>-Zerfall: <super>14</super><sub>6</sub>C → <super>14</super><sub>7</sub>N + e<super>−</super> (Basis der C-14-Datierung)")
s+=[Paragraph("Halbwertszeit",H2),P("Die <b>Halbwertszeit T<sub>1/2</sub></b> ist die Zeit, in der die Hälfte der vorhandenen Kerne zerfallen ist. Nach n Halbwertszeiten sind noch (1/2)<super>n</super> der Kerne übrig."),
img("decay.png",9.5*cm,"Abb. 18: Exponentieller Zerfall – nach jeder Halbwertszeit halbiert sich die Menge.")]
s+=table([["Nuklid","Halbwertszeit","Verwendung"],["I-131","ca. 8 Tage","Schilddrüsentherapie"],["Tc-99m","ca. 6 Stunden","medizinische Diagnostik"],["C-14","5730 Jahre","Altersbestimmung organischer Funde"],["U-238","4,47 Mrd. Jahre","Uran-Blei-Datierung, Erdalter"]],[3*cm,5*cm,9*cm])
s+=bl(["<b>Kernspaltung (Fission)</b>: Ein schwerer Kern (U-235) wird durch ein Neutron gespalten, dabei werden weitere Neutronen frei → Kettenreaktion; genutzt in Kernkraftwerken.","<b>Kernfusion</b>: Leichte Kerne verschmelzen (Wasserstoff → Helium) – die Energiequelle der Sonne. Sie braucht extrem hohe Temperaturen (Millionen °C).","<b>Massendefekt</b>: Kernmasse ist kleiner als die Summe der Nukleonen; die Differenz wird als Energie frei (E = m·c²).","<b>Strahlenschutz</b>: Abstand, Abschirmung, kurze Aufenthaltsdauer."])

# 20
s+=h1("20. Laborpraxis &amp; Sicherheit")
s+=[P("Sicheres Arbeiten im Labor ist Pflicht: Schutzbrille und Kittel tragen, nicht essen oder trinken, lange Haare zusammenbinden, keine Chemikalien probieren oder direkt riechen (Zufächeln), Chemikalien beschriften, Abfälle getrennt entsorgen und vor dem Experiment die Gefahrstoffkennzeichnung lesen.")]
s+=table([["GHS-Piktogramm","Bedeutung","Beispiel"],["Flamme","entzündbar","Ethanol, Benzin, Wasserstoff"],["Flamme über Kreis","brandfördernd (Oxidationsmittel)","Sauerstoff, Kaliumnitrat"],["Explodierende Bombe","explosiv","Feuerwerkskörper"],["Ätzwirkung","ätzend für Haut/Augen, metallkorrosiv","Salzsäure, Natronlauge"],["Totenkopf mit Knochen","akut giftig","Blausäure, Quecksilber"],["Ausrufezeichen","reizend, gesundheitsschädlich","verdünnte Säuren, Reiniger"],["Gesundheitsgefahr","krebserzeugend, organschädigend","Benzol, Asbest"],["Umwelt","umweltgefährlich","Schwermetalle, manche Pestizide"],["Gasflasche","Gas unter Druck","Sauerstoff-, Propanflasche"]],[4*cm,7*cm,6*cm])
s+=bl(["<b>Messen</b>: Volumen mit Messzylinder oder Pipette (Ablesen auf Augenhöhe am Meniskus), Masse mit der Waage, Temperatur mit dem Thermometer.","<b>Bunsenbrenner</b>: blaue (rauschende) Flamme = heiß, gelbe (leuchtende) Flamme = rußt, kühler (Luftzufuhr geschlossen).","<b>Säuren verdünnen</b>: immer die Säure ins Wasser gießen, nie umgekehrt („erst das Wasser, dann die Säure, sonst geschieht das Ungeheure“).","<b>Wissenschaftliche Methode</b>: Beobachtung → Fragestellung → Hypothese → Experiment (Kontrolle, nur eine Variable ändern) → Auswertung → Schlussfolgerung."])

# 21
s+=h1("21. Übungsaufgaben mit Lösungen")
s+=[P("Löse zuerst alle Aufgaben selbst, schau erst danach in die Lösungen.")]
tasks=[
("Wie viele Protonen, Neutronen und Elektronen hat das Ion <super>27</super>Al<super>3+</super> (Z = 13)?","13 Protonen, 27 − 13 = 14 Neutronen, 13 − 3 = 10 Elektronen."),
("Gib die Elektronenkonfiguration von Magnesium (Z = 12) an.","1s<super>2</super> 2s<super>2</super> 2p<super>6</super> 3s<super>2</super> (kurz: [Ne] 3s<super>2</super>). Zwei Valenzelektronen → bildet Mg<super>2+</super>."),
("Gleiche aus: Al + O<sub>2</sub> → Al<sub>2</sub>O<sub>3</sub>","4 Al + 3 O<sub>2</sub> → 2 Al<sub>2</sub>O<sub>3</sub>"),
("Bestimme Bindungstyp und Geometrie von CaCl<sub>2</sub> und CH<sub>4</sub>.","CaCl<sub>2</sub>: Ionenbindung (Metall + Nichtmetall, ΔEN = 2,2). CH<sub>4</sub>: unpolare Atombindung (ΔEN = 0,4), tetraedrisch, 109,5°, unpolares Molekül."),
("Berechne die Masse von 0,5 mol Wasser (M = 18 g/mol).","m = n · M = 0,5 mol · 18 g/mol = 9 g."),
("Welches Volumen nehmen 2 mol eines Gases bei 0 °C und 1013 hPa ein?","V = n · V<sub>m</sub> = 2 mol · 22,4 L/mol = 44,8 L."),
("Welchen pH-Wert hat eine 0,001 mol/L Salzsäure?","c(H<sub>3</sub>O<super>+</super>) = 10<super>−3</super> mol/L → pH = 3."),
("Bestimme die Oxidationszahl von Schwefel in H<sub>2</sub>SO<sub>4</sub>.","2·(+I) + x + 4·(−II) = 0 → x = +VI."),
("Von 80 g eines Nuklids (T<sub>1/2</sub> = 8 Tage) sind nach 24 Tagen noch wie viel vorhanden?","24 d = 3 Halbwertszeiten → 80 g · (1/2)<super>3</super> = 10 g."),
("Warum siedet Wasser höher als Schwefelwasserstoff (H<sub>2</sub>S)?","Wassermoleküle bilden Wasserstoffbrücken (O ist stark elektronegativ), H<sub>2</sub>S nur schwächere Dipol-/Van-der-Waals-Kräfte."),
("Wie verschiebt sich N<sub>2</sub> + 3 H<sub>2</sub> ⇌ 2 NH<sub>3</sub> (exotherm) bei Druckerhöhung und bei Temperaturerhöhung?","Druck ↑: Richtung NH<sub>3</sub> (weniger Gasmoleküle). Temperatur ↑: Richtung Edukte (endotherme Rückreaktion)."),
("Berechne die Spannung einer Zelle aus Mg/Mg<super>2+</super> und Ag/Ag<super>+</super>.","U = E°(Ag) − E°(Mg) = 0,80 V − (−2,37 V) = 3,17 V."),
]
rows=[["Nr.","Aufgabe","Lösung"]]+[[str(i+1),a,b] for i,(a,b) in enumerate(tasks)]
s+=table(rows,[1*cm,7.5*cm,8.5*cm])

# 22
s+=h1("22. Lernplan, Merksätze &amp; Glossar")
s+=[Paragraph("Vorschlag für einen Lernplan (4 Wochen)",H2)]
s+=table([["Woche","Schwerpunkt","Aufgabe"],["1","Atombau, Periodensystem, Elektronenkonfiguration","erste 20 Elemente, Bohr-Modelle und Kästchenschema zeichnen"],["2","Bindungen, Lewis-Formeln, Nomenklatur, Reaktionsgleichungen","täglich 5 Gleichungen ausgleichen, Formeln aufstellen"],["3","Mol, Gase, Lösungen, Energie, Gleichgewicht","Rechenaufgaben mit Formelblatt"],["4","Säuren/Basen, Redox, Organik, Kernchemie","Übungsaufgaben aus Kapitel 21, Lernkarten wiederholen"]],[2*cm,7.5*cm,7.5*cm])
s+=[Paragraph("Die wichtigsten Merksätze",H2)]+bl(["Ordnungszahl = Protonen = Elektronen (beim neutralen Atom).","Gruppe = Valenzelektronen, Periode = Schalen.","Metall + Nichtmetall = Ionen, Nichtmetall + Nichtmetall = Elektronenpaare.","Nur Koeffizienten ändern, nie Indizes.","Immer in Kelvin und mol rechnen.","Säure gibt H<super>+</super> ab, Base nimmt H<super>+</super> auf. OIL RIG: Oxidation = Elektronen abgeben.","Le Chatelier: Das System weicht dem Zwang aus.","Gleiches löst sich in Gleichem."])
s+=[Paragraph("Glossar",H2)]
s+=table([["Begriff","Erklärung"],["Atom","kleinstes chemisch nicht weiter teilbares Teilchen eines Elements"],["Molekül","Teilchen aus mindestens zwei durch Atombindung verbundenen Atomen"],["Ion","elektrisch geladenes Atom oder Molekül"],["Isotop","Atome eines Elements mit verschiedener Neutronenzahl"],["Valenzelektron","Elektron der äußersten Schale, bestimmt das Bindungsverhalten"],["Elektronegativität","Fähigkeit eines Atoms, Bindungselektronen anzuziehen"],["Stoffmenge","Zahl der Teilchen, gemessen in Mol"],["Katalysator","Stoff, der die Reaktion beschleunigt, ohne verbraucht zu werden"],["Enthalpie ΔH","Reaktionswärme bei konstantem Druck"],["Oxidation / Reduktion","Elektronenabgabe / Elektronenaufnahme"],["pH-Wert","Maß für die Konzentration der Oxonium-Ionen (sauer &lt; 7 &lt; basisch)"],["Halbwertszeit","Zeit, in der die Hälfte der Kerne zerfällt"],["Polymer","Makromolekül aus vielen gleichen Bausteinen (Monomeren)"]],[4*cm,13*cm])
s+=box("Tipp","Erkläre das Thema einem Freund oder zeichne es aus dem Kopf. Wer erklären kann, hat es verstanden. Zum Vertiefen eignen sich Schulbücher, die Lernplattformen von Kanälen wie „musstewissen Chemie“ und das Video von Wacky Science, sobald du das Transkript einfügst.")

doc=BaseDocTemplate("Chemie_Lernzusammenfassung.pdf",pagesize=A4,leftMargin=2*cm,rightMargin=2*cm,topMargin=2*cm,bottomMargin=2.3*cm,title="Chemie – Elemente & Grundlagen",author="Claude")
fr=Frame(2*cm,2.3*cm,17*cm,A4[1]-4.3*cm,id="f")
doc.addPageTemplates([PageTemplate("cover",[fr],onPage=cover),PageTemplate("body",[fr],onPage=later)])
from reportlab.platypus.doctemplate import NextPageTemplate
doc.build([NextPageTemplate("body")]+s)
