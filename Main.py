# -*- coding: utf-8 -*-

"""
Main.py

Script principal de la MARCONEO.
Lance l'application.
"""

#-------------------------------------------------------------------#

from PACKAGES.MarcoNeo import *
from PACKAGES.INTERFACE.MenuPrincipal import MenuPrincipal

#-------------------------------------------------------------------#

if __name__ == "__main__":
    print("Lancement de la MARCONEO...")
    app = MarcoNeo()
    app.setView(MenuPrincipal)
    #print(dir(app)) enumere tous les attributs de la classe MarcoNeo
    app.start()
    app.refreshLog()
    