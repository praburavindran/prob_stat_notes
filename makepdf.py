from __future__ import print_function
import os

filename = "notes" 
bib = False

latexcmd = " ".join(["latex", filename + ".tex"])
bibtexcmd = " ".join(["bibtex", filename])
dvipdfcmd = " ".join(["dvipdf", filename + ".dvi"])
evincecmd = " ".join(["evince", filename + ".pdf"])
rmlogcmd = " ".join(["rm -f", filename + ".log"])
rmdvicmd = " ".join(["rm -f", filename + ".dvi"])
rmauxcmd = " ".join(["rm -f", filename + ".aux"])
rmbblcmd = " ".join(["rm -f", filename + ".bbl"])
rmblgcmd = " ".join(["rm -f", filename + ".blg"])

fullcmd = ""
if bib:
    fullcmd = " ".join([latexcmd, "&&",
                        latexcmd, "&&",
                        bibtexcmd, "&&",
                        bibtexcmd, "&&",
                        latexcmd, "&&",
                        latexcmd, "&&",
                        dvipdfcmd, "&&",
                        rmlogcmd, "&&",
                        rmdvicmd, "&&",
                        rmauxcmd, "&&",
                        rmbblcmd, "&&",
                        rmblgcmd, "&&",
                        evincecmd, "&"])
else:
    fullcmd = " ".join([latexcmd, "&&",
                        latexcmd, "&&",
                        dvipdfcmd, "&&",
                        rmlogcmd, "&&",
                        rmdvicmd, "&&",
                        rmauxcmd, "&&",
                        evincecmd, "&"])
    
print("Running the command = {}".format(fullcmd))
os.system(fullcmd)

