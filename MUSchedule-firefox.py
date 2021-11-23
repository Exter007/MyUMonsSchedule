from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
import smtplib
from getpass import getpass
import imghdr
from email.message import EmailMessage
import tempfile
import sys
from datetime import datetime

import encrypt
from setup import path, login_file_name, retrieve_login

__author__ = "Pierre-Louis D'Agostino"
__email__ = "200197@umons.ac.be"

"""
VARIABLES GLOBALES
"""
# Adresse mail GMAIL envoyeur
Sender_Email = ""
# Adresse mail GMAIL receveur
Reciever_Email = ""

# Fichier config
config_file = open(f"{path}config/{login_file_name}.idd")
# Clé privée
private_key = encrypt.read_private_key("./keys/private_key.pem")
# Mot de passe et matricule encryptés
encrypted_mat, encrypted_pswd = retrieve_login("./config/login.idd")
# Matricule décrypté
mat = encrypt.decrypt(encrypted_mat, private_key).decode()
# Adresse mail UMons (matricule@umons.ac.be)
user = f"{mat}@umons.ac.be"
# Mot de passe UMons décrypté
passw = encrypt.decrypt(encrypted_pswd, private_key).decode()
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
if len(sys.argv) == 2 and sys.argv[1] == "daily":
    print("Daily Mode")
    driver.find_element(By.CLASS_NAME, "fc-agendaDay-button").click()
    checkday("daily")
else:
    print("Weekly Mode")
    driver.find_element(By.CLASS_NAME, "fc-agendaWeek-button").click()
    checkday("")
tmp = tempfile.NamedTemporaryFile(suffix=".png", mode='wb')
png = driver.get_screenshot_as_png()
tmp.write(png)

driver.quit()

print("Sending email...")

# Send Email (Be carefull to change your Google settings to allow less )
#Password = getpass()
newMessage = EmailMessage()
newMessage['Subject'] = "Horaire "+str(date.today())
newMessage['From'] = Sender_Email
newMessage['To'] = Reciever_Email
newMessage.set_content('Voici l\'horaire de la semaine !')
image_data = png
image_type = ".png"
image_name = "Horaire.png"

print("Sending email... GMail password needed.")

# Send Email (Be carefull to change your Google settings to allow less )
Password = getpass()
newMessage.add_attachment(image_data, maintype='image',
                          subtype=image_type, filename=image_name)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
except:
    print("Email not sent. Verify username, password and Gmail configuration.")
