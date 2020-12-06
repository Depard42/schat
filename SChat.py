import wx
import time
from client import Client
from threading import Thread
import random

newClient=Client()

def connect(event):
    if nameBox.GetValue()=='':
        messageBox.SetValue('Name!')
    elif addressBox.GetValue()=='':
        messageBox.SetValue('Adress!')
    else:
        newClient.done()
        messageBox.SetValue('Connecting...')
        time.sleep(1)
        newClient.start(addressBox.GetValue(),portBox.GetValue(),nameBox.GetValue())
def create(event):
    print("hi")
    pass
def send(event):
    s=writeBox.GetValue()
    writeBox.SetValue('')
    newClient.send(s)
def OnKeyPress(event):
    keyCode = event.GetKeyCode()
    if keyCode==13:
        send(event)
app = wx.App()
win = wx.Frame(None, title="Secret Chat", size=(410,335))

bkg=wx.Panel(win)
connectButton = wx.Button(bkg, label="connect")
connectButton.Bind(wx.EVT_BUTTON, connect)
createButton = wx.Button(bkg, label="create")
createButton.Bind(wx.EVT_BUTTON, create)
sendButton = wx.Button(bkg, label="^_^_^")
sendButton.Bind(wx.EVT_BUTTON, send)
writeBox = wx.TextCtrl(bkg)
writeBox.Bind(wx.EVT_KEY_UP, OnKeyPress)
usersBox = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
messageBox = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
nameBox = wx.TextCtrl(bkg, value="NickName_"+str(random.randrange(99999)))
addressBox = wx.TextCtrl(bkg, value="91.192.71.197") #91.192.71.197
portBox = wx.TextCtrl(bkg, value="5555")

topName = wx.BoxSizer()
topName.Add(nameBox, proportion=0,border=5)
topServer = wx.BoxSizer()
topServer.Add(addressBox, proportion=1, flag=wx.EXPAND, border=5)
topServer.Add(portBox, proportion=0, flag=wx.EXPAND, border=5)
topServer.Add(connectButton, proportion=0, flag=wx.LEFT, border=5)
topServer.Add(createButton, proportion=0, flag=wx.LEFT, border=5)
infoBox = wx.BoxSizer()
infoBox.Add(messageBox, proportion=1, flag=wx.EXPAND, border=5)
infoBox.Add(usersBox, proportion=0, flag=wx.EXPAND|wx.LEFT, border=5)
sendingBox = wx.BoxSizer()
sendingBox.Add(writeBox, proportion=1, flag=wx.EXPAND|wx.LEFT, border=5)
sendingBox.Add(sendButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(topName, proportion=0, flag=wx.ALL, border=5)
vbox.Add(topServer, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vbox.Add(infoBox, proportion=1, flag=wx.EXPAND|wx.TOP, border=5)
vbox.Add(sendingBox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)

newClient.set(messageBox,usersBox)

bkg.SetSizer(vbox)
win.Show()

newClient.set(messageBox,usersBox)
app.MainLoop()

newClient.end()
newClient.done()
input("Press ENTER...")