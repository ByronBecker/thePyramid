import OSC
import subprocess

carrie = OSC.OSCClient()
carrie.connect(('192.168.2.102', 8675)) #connect to carrie

water_comp = 0
light_comp = 0
rot_comp = 0
slide_comp = 0
ultra_comp = 0
c_comp = 0


def button(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)
    global water_comp, light_comp, rot_comp, slide_comp, ultra_comp
    #reset all
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/lightsoff")
    carrie.send(oscmsg)

    light_comp = 0
    rot_comp = 0
    slide_comp = 0
    ultra_comp = 0
    if water_comp == 0:
        subprocess.call('say "Welcome, to the pyramid. First you must solve the water!"', shell=True)
    else:
        subprocess.call('say "You must return to the waters you came from!"', shell=True)
    water_comp = 0

def water(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)
    global water_comp
    water_comp = 1
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/waton")
    carrie.send(oscmsg)
    subprocess.call('say "Ah, fresh water! You must now seek the light"', shell=True)

def light(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

    global water_comp, light_comp, rot_comp, slide_comp, ultra_comp
    if water_comp == 1:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/lighton")
        carrie.send(oscmsg)

        light_comp = 1
        subprocess.call('say "I feel... Illuminated! You may now seek the path of the hand!"', shell=True)
    else:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/lightsoff")
        carrie.send(oscmsg)
        light_comp = 0
        water_comp = 0
        subprocess.call('say "You must return to the waters you came from!"', shell=True)

def rot(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

    global water_comp, light_comp, rot_comp, slide_comp, ultra_comp
    if water_comp == 1 and  light_comp == 1 and  slide_comp == 1 and ultra_comp == 1:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/handon")
        carrie.send(oscmsg)
        subprocess.call('say "Congratulations, you have bested the Pyramid!"', shell=True)
        rot_comp = 1
    elif water_comp == 1 and light_comp == 1:
        rot_comp = 1
        print("rot " + str(rot_comp) + " ultra " + str(ultra_comp) + " slide " + str(slide_comp))
        subprocess.call('say "Ouch, you twisted me!"', shell=True)
    else:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/lightsoff")
        carrie.send(oscmsg)
        light_comp = 0
        water_comp = 0
        slide_comp = 0
        ultra_comp = 0
        rot_comp = 0
        subprocess.call('say "You must return to the waters you came from!"', shell=True)

def slide(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

    global water_comp, light_comp, rot_comp, slide_comp, ultra_comp
    if water_comp == 1 and  light_comp == 1 and  rot_comp == 1  and ultra_comp == 1:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/handon")
        carrie.send(oscmsg)
        subprocess.call('say "Congratulations, you have bested the Pyramid!"', shell=True)
        slide_comp = 1
    elif water_comp == 1 and light_comp == 1:
        print("rot " + str(rot_comp) + " ultra " + str(ultra_comp) + " slide " + str(slide_comp))
        subprocess.call('say "Nice slide!"', shell=True)
        slide_comp = 1
    else:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/lightsoff")
        carrie.send(oscmsg)
        light_comp = 0
        water_comp = 0
        slide_comp = 0
        ultra_comp = 0
        rot_comp = 0
        subprocess.call('say "You must return to the waters you came from!"', shell=True)

def ultra(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

    global water_comp, light_comp, rot_comp, slide_comp, ultra_comp
    if water_comp == 1 and  light_comp == 1 and  rot_comp == 1 and  slide_comp == 1:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/handon")
        carrie.send(oscmsg)
        subprocess.call('say "Congratulations, you have bested the Pyramid!"', shell=True)
        ultra_comp = 1
    elif water_comp == 1 and light_comp == 1:
        print("rot " + str(rot_comp) + " ultra " + str(ultra_comp) + " slide " + str(slide_comp))
        subprocess.call('say -v Fred "Your hand is close!"', shell=True)
        ultra_comp = 1
    else:
        oscmsg = OSC.OSCMessage()
        oscmsg.setAddress("/lightsoff")
        carrie.send(oscmsg)
        light_comp = 0
        water_comp = 0
        slide_comp = 0
        ultra_comp = 0
        rot_comp = 0
        subprocess.call('say "You must return to the waters you came from!"', shell=True)
        

if __name__ == "__main__":
    w = OSC.OSCServer(('0.0.0.0', 9555))  # listen on localhost, port 12000
    w.addMsgHandler('/water', water)     # call handler() for received OSC w  /hello address
    w.addMsgHandler('/button', button)

    w.addMsgHandler('/light', light)     # call handler() for received OSC w  /hello address
    w.addMsgHandler('/rot', rot)     # call handler() for received OSC w  /hello address
    
    w.addMsgHandler('/slide', slide)     # call handler() for received OSC w  /hello address

    w.addMsgHandler('/ultra', ultra)     # call handler() for received OSC w  /hello address
    w.serve_forever()

