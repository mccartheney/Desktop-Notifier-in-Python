# import desktopNotifier, for notification
from desktop_notifier import DesktopNotifier

# import sleep from time
from time import sleep

# create notification creator 
class notificationCreator :
    def __init__ (self) :
        #  initialize desktopNotifier
        self.notifier = DesktopNotifier ()

    def createNotification (self, title, message) :
        # create notification
        self.notifier.send_sync (title = title, message = message)
    
    def notificationFromArray (self, array, time) :
        # loop through news
        for news in array :
            # news title
            title = news["author"]
            # news content
            description = news["description"]
            
            # show notification
            self.createNotification(title, description)

            # wait
            sleep (time*60) #in minutes minutes