#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep
import sys
import requests
import paramiko
import subprocess

__author__ = "Pierre-Louis D'Agostino"
__email__ = "200197@umons.ac.be"

"""
VARIABLES GLOBALES
"""
# Adresse mail UMons (matricule@umons.ac.be)
user = ""
# Mot de passe UMons
passw = ""
"""
FIN DES VARS
"""

# Opening selenium webdriver
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Connection to gestac
try:
    driver.get("https://gestacumons.umons.ac.be/login_ad.php?destination=student")
    print("Connection...")
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(passw)
    driver.find_element(By.ID, "SubmitCreds").click()
except:
    print("Username/password incorrect or geckodriver not installed")
    sys.exit(1)

print("Finding schedule...")

try:
    # Find schedule and download iCalendar
    driver.get("https://gestacumons.umons.ac.be/MyUmons/mon_horaire.php")
    driver.find_element(By.ID, "menu").click()
    driver.find_elements(
        By.PARTIAL_LINK_TEXT, "Télécharger")[0].click()
    sleep(1)
    matricule = user.split("@")[0]
    url = "https://gestacumons.umons.ac.be/MyUmons/module_horaire/monIcalendar.php?fichier=" + matricule + ".ics"
    cookies = driver.get_cookies()
    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
except:
    print("Schedule not found...")
    sys.exit(1)
try:
    print("Downloading...")
    #fo = open(str(matricule)+'horaire.ics', 'wb')
    fo = open('horaire.ics', 'wb')
    fo.write(requests.get(url, cookies=s.cookies).content)
    fo.close()
    s.close()
    driver.quit()
except:
    print("Cannot download schedule...")
    sys.exit(1)

print("Done !")
