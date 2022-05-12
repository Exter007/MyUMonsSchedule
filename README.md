# MyUMonsSchedule
## Use MyUMonsSchedule to sync your personalized calendar (MyUMons schedule) with Google Calendar !
### Or use MyUMonsSchedule python script to send a screenshot (by email (Gmail) or on Discord) of your MyUMons schedule.
#### If you use it on Windows, take care to download geckodriver (and add it to PATH*): https://github.com/mozilla/geckodriver/releases
\* Just run it in the folder where the main script is located. You can close the window right after.

---

## iCalendar (and Google Calendar)

To use the iCalendar feature, you must have Geckodriver in path (in /etc/bin for Linux distributions or in Windows Path like explained before)
1) You must modify the script to **CHANGE** the global vars. (UMons username and password)
2) Run the "main_calendar.py" script
After execution, a new file will be created "horaire.ics". This file contains all the events of your calendar. The default timezone is not correct if you want to use this ics.
3) Run the timezone.sh script to change the timezone in "horaire.ics".
After this step, your ics file will be correct.
4) You have now two options:
    * Option 1: Import this ics file directly in Google Calendar (or other calendar) but **event changes will not be shown in your calendar** to sync the events, go to Option 2. If you don't want to sync, don't follow the next steps.
    * Option 2: **Sync your ics with Google Calendar**. In Google Calendar, click on add new calendar from URL. In the URL section, you must provide a fixed link where your "horaire.ics" file is stored. It's recommended to use Dropbox (free) for this feature. So in your laptop you must store the ics file in your Dropbox folder and get the public **DOWNLOAD** link of it (get the public link and change the end to " **?dl=1** "). Copy/Paste this link in the url section of your new Google calendar. Now, everytime that you run the script, don't forget to replace the "horaire.ics" file in your Dropbox folder ! (You can easily create a bash script for doing that **automatically** and don't forget to make a cron for those steps if you want to use this feature everyday (or whenever you want) to refresh your calendar everyday). 
    * **Note:** Google Calendar sync the calendar with your URL every 24h in mean and it is not perfect everytime. To avoid this problem you can use this Github repository: https://github.com/derekantrican/GAS-ICS-Sync. That repository shows you how to easilly create a Google script that refresh your calendar "every x" minutes. It takes only **few seconds** to use this script and the Google Calendar sync will be perfect !

---

## Email folder

1) You must modify the script to **CHANGE** the global vars.
2) **DON'T FORGET** to change your Gmail/Google config only for the **SENDER**. There are only 2 easy steps to do.
3) You are prompted for your Gmail password (*sender only*) while running the script.
4) Use "python /path-to-file.py ["daily"]" -> Daily is an optionnal argument if you want to show the daily-view of your schedule (instead of weekly by default).
5) **Be carefull:** Please make sure that you installed all dependencies (easy with pip for python)

PS: If you want to change from Gmail to another provider, don't forget to change the SMTP servers.

(**WORKS** on Linux distributions, if you use the Firefox/Discord module, you need to add Geckodriver to path)

---

## Updates

Update 29/10 : Working on Fedora (geckodriver needed too)

Update 29/10 : Discord module is working.

Update 03/11 : Temp files added instead of "screenshot.png" (not for Discord module)

Update 18/11 :
  - Website creation (coming soon) including connection with your UMons account.
  - Creating database (alwaysdata) of users using MUSchedule to send them screenshots by email (with cron)
  - Trying to download ics for each user (difficult due to authentification)
  - If we can download ics for each user, the next step is to sync with Google Calendar (cron?/auto?/...?)

Update 14/02/22 : Setup changed (hiding the password during setup and during final_confirmation)

Update 12/05/22 : The iCalendar (ics) file is now available ! And there is a section associated with it to link this calendar with Google Calendar
