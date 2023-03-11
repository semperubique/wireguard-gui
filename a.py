#!/usr/bin/python3

import os

# Load Gtk
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def afunc(btn):
    # is wg on or off
    wg_output = os.popen("sudo wg").read()
    if(len(wg_output)>0):
    	state = 'up'
    else:
    	state = 'down'
    	
    if(state=='down'):
    	state='up'
    	os.system('wg-quick up ProtonVPN')
    elif(state=='up'):
    	state='down'
    	os.system('wg-quick down ProtonVPN')
    	
    btn.set_label('Wireguard is ' + state)

# When the application is launched…
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app, title='Wireguard')
        
    wg_output = os.popen("sudo wg").read()
    if(len(wg_output)>0):
    	state = 'up'
    else:
    	state = 'down'

    btn = Gtk.Button(label='Wireguard is ' + state)
    btn.connect('clicked', lambda x: afunc(btn))
    
    win.set_child(btn)
    win.present()

app = Gtk.Application(application_id='Wireguard')
app.connect('activate', on_activate)
app.run(None)

