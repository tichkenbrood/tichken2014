#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
from web import form




from Adafruit_PWM_Servo_Driver import PWM

import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)
pwm2 =PWM(0x40, debug=True)

servoMin = 300  # Min pulse length out of 4096
servoMax = 580  # Max pulse length out of 4096
servoMoy = 360

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)
  pwm2.setPWM(channel, 1, pulse)	

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz













# definit la page de nom index pour le site web
urls = ('/', 'index')
dossier_web = web.template.render('templates')

app = web.application(urls, globals())

# definit les boutons a afficher
ma_forme = form.Form(
form.Button("btn", id = "btnon", value = "action", html = "action", class_ = "bouton_on"),

)

# definit l action a effectuer quand la page index est appele
class index:
    # utilise quand la page est demande
    def GET(self):
        forme = ma_forme()
        return dossier_web.index(forme, "action du servo")
   
    # utilise quand une forme web est soumise
    def POST(self):
        userdata = web.input()
        if userdata.btn == "action":
	    pwm.setPWM(1, 1, servoMoy)
	    time.sleep(0.5)
            pwm.setPWM(1, 1, servoMax)
        
        # recharge la page web
        raise web.seeother('/')

# programme
if __name__ == '__main__':
    app.run()