#drinking water reminder
import time
from plyer import notification
 
 
if __name__=="__main__":
 
        notification.notify(
            title ="Drink water",
            message=" You should drink water everyday" ,
           
            # displaying time
            timeout=10
)
        # waiting time
        time.sleep(3600)