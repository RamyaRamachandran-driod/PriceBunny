from plyer import notification
import time

def notifyme(title,message):
    notification.notify(
       title=title,
       message=message,
       app_icon = "C:\\Users\\Admin\\Downloads\\Jommans-Mushroom-Clock.ico",
       timeout = 10,)


  # while True:
notifyme("HEY USER!!! Have you done any shopping today?","If YES, don't forget to enter your expenses in PriceBunny :) ")

   # time.sleep(10)
