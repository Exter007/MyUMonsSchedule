# MyUMonsSchedule
### Use MyUMonsSchedule python script to send a screenshot (by email (Gmail) or on Discord) of your MyUMons schedule.
#### If you use it on Windows, take care to download geckodriver (and add it to PATH*) : https://github.com/mozilla/geckodriver/releases
1) You must modify the script to **CHANGE** the global vars.
2) **DON'T FORGET** to change your Gmail/Google config only for the **SENDER**. There are only 2 easy steps to do.
3) You are prompted for your Gmail password (*sender only*) while running the script.
4) Use "python /path-to-file.py ["daily"]" -> Daily is an optionnal argument if you want to show the daily-view of your schedule (instead of weekly by default).

PS : If you want to change from Gmail to another provider, don't forget to change the SMTP servers.

\* Just run it in the MyUMonsSchedule folder. You can close the window right after.

(**WORKS** on Linux distributions, if you use the Firefox/Discord module, you need to add Geckodriver to path)

Update 29/10 : Working on Fedora (geckodriver needed too)

Update 29/10 : Discord module is working.

Update 03/11 : Temp files added instead of "screenshot.png" (not for Discord module)

Update 18/11 :
  - Website creation (coming soon) including connection with your UMons account.
  - Creating database (alwaysdata) of users using MUSchedule to send them screenshots by email (with cron)
  - Trying to download ics for each user (difficult due to authentification)
  - If we can download ics for each user, the next step is to sync with Google Calendar (cron?/auto?/...?)

### In the next versions (outdated)
1) Cron ?
2) Directly download ICS file and add it to google calendar ?
