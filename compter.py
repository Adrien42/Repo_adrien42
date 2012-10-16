"""Code pour compter le nombre de lettre d'un site web"""
import httplib
import sys
from datetime import datetime
import pdb

SAVE = sys.stdout
LOGFILE = open('compter.log', 'w')
sys.stdout = LOGFILE

ADRESS = sys.argv[1]
print datetime.now().strftime("[%d/%m/%y %H:%M]") + \
    "Adresse indiquee : " + ADRESS

#pdb.set_trace()
H1 = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
H1.request("GET", ADRESS)
R1 = H1.getresponse()
PAGE = R1.read()
print datetime.now().strftime("[%d/%m/%y %H:%M]") + \
    "Nombre de lettres: " + str(PAGE.count(' '))

sys.stdout = SAVE
LOGFILE.close()
print file('compter.log').read()

# c veut dire continuer, s rentre dans la fonction, n pour next
