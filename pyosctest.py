

import OSC
'''
c = OSC.OSCClient()
c.connect(('192.168.2.153', 8675))
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/oschello")
oscmsg.append(80)
c.send(oscmsg)
'''

c = OSC.OSCClient()
c.connect(('127.0.0.1', 12000))
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/hello")
oscmsg.append(80)
c.send(oscmsg)
