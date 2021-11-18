from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
import smtplib
from getpass import getpass
import imghdr
import sys
from datetime import datetime

from discordwebhook import Discord
import requests
import json
import feedparser
import subprocess

__author__ = "Pierre-Louis D'Agostino"
__email__ = "200197@umons.ac.be"

"""
VARIABLES GLOBALES
"""
# URL discord webhook (à créer via les param. d'un channel discord)
discord = Discord(url="")

# Adresse mail UMons (matricule@umons.ac.be)
user = ""
# Mot de passe UMons
passw = ""
"""
FIN DES VARS
"""


def checkday(moment):
    j = datetime.today().weekday()
    if moment == "daily":
        if j == 7:
            driver.find_element(
                By.CLASS_NAME, "fc-icon-right-single-arrow").click()
        elif j == 6:
            driver.find_element(
                By.CLASS_NAME, "fc-icon-right-single-arrow").click()
            driver.find_element(
                By.CLASS_NAME, "fc-icon-right-single-arrow").click()
    else:
        if j == 6 or j == 7:
            driver.find_element(
                By.CLASS_NAME, "fc-icon-right-single-arrow").click()


# Opening selenium webdriver
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Connection to gestac
driver.get("https://gestacumons.umons.ac.be/login_ad.php?destination=student")
print("Connection...")
driver.find_element(By.ID, "username").send_keys(user)
driver.find_element(By.ID, "password").send_keys(passw)
driver.find_element(By.ID, "SubmitCreds").click()

print("Finding schedule...")

# Find schedule and take screenshot
driver.get("https://gestacumons.umons.ac.be/MyUmons/mon_horaire.php")
driver.set_window_size(1920, 1080)
if sys.argv[1] == "daily":
    print("Daily Mode")
    driver.find_element(By.CLASS_NAME, "fc-agendaDay-button").click()
    checkday("daily")
else:
    print("Weekly Mode")
    driver.find_element(By.CLASS_NAME, "fc-agendaWeek-button").click()
    checkday("")
driver.get_screenshot_as_file("./screenshot.png")
driver.quit()

print("Sending to discord ...")

newMessage = "Horaire "+str(date.today()) + " " + str(user)

cmd = subprocess.Popen(
    "curl --upload-file ./screenshot.png https://transfer.sh/screenshot.png", stdout=subprocess.PIPE, shell=True)
out = cmd.communicate()[0].decode("utf-8")

try:
    discord.post(
        embeds=[
            {
                "title": newMessage,
                "image": {"url": out},
            },
        ],
    )
except:
    print("Message not sent.")
