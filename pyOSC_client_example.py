import OSC

c = OSC.OSCClient()
c.connect(('127.0.0.1', 12000))   # localhost, port 57120
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/hello")
oscmsg.append('world')
c.send(oscmsg)