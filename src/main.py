"""
👁️ RetinaReset - Refresh Your Vision, Sharpen Your Focus

Welcome to RetinaReset — a simple tool built to protect your eyes from digital fatigue.

🔁 Based on the 20-20-20 rule:
   • Every 20 minutes,
   • Look at something 20 feet away,
   • For at least 20 seconds.

📲 This program runs in the background and sends you a gentle notification
named 'Screen Detox' every 20 minutes, reminding you to pause and refresh your eyes.

💡 Why use RetinaReset?
   • Reduce eye strain and dryness
   • Prevent screen fatigue and headaches
   • Improve focus and productivity
   • Build a healthy screen-time habit

Take control of your screen time. One glance away, one healthy habit at a time.

Your eyes will thank you! 😌
"""

import time
from plyer import notification

while True:
    print("Initiating")
    notification.notify(title= "Retina Rest",
                        message= "Successfully Initiated...")

    time.sleep(20*60)

    notification.notify(title= "Screen Detox",
                        message= "Your eyes need a breather. 20-20-20 rule to the rescue!")
    
    time.sleep(20)
    
    notification.notify(title= "Retina Rest Review",
                        message= "Your task was success! Now it's time to get back to work.")
    
    time.sleep(2*60)


