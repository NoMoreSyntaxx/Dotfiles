#!/usr/bin/env python3

import tkinter
import os

def BlackWhiteMode():
    os.system("killall waybar &")
    
    os.system("rm ~/.config/waybar/style.css")
    os.system("ln -sf ~/.config/waybar/styles/BlackWhiteMode.css ~/.config/waybar/style.css")
    os.system("swaybg -i ~/me/blackandwhitewallpaper.jpg &")

    os.system("waybar &")
    
def DarkBlueMode():
    os.system("killall waybar &")

    os.system("swaybg -i ~/me/DarkModeBlueWallpaper.jpg &")
    os.system("rm ~/.config/waybar/style.css")
    os.system("ln -sf ~/.config/waybar/styles/DarkBlueMode.css ~/.config/waybar/style.css")
    os.system("waybar &")

def DarkRedMode():
    os.system("killall waybar &")
    
    os.system("swaybg -i ~/me/DarkModeRedWallpaper.jpg &")
    os.system("rm ~/.config/waybar/style.css")
    os.system("ln -sf ~/.config/waybar/styles/DarkRedMode.css ~/.config/waybar/style.css")
    os.system("waybar &")
    
def BrightBlueMode():
    os.system("killall waybar &")
    
    os.system("swaybg -i ~/me/anime-wallpaper1.jpg &")
    os.system("rm ~/.config/waybar/style.css")
    os.system("ln -sf ~/.config/waybar/styles/BrightBlueMode.css ~/.config/waybar/style.css")
    os.system("waybar &")


def KillWaybar():
    os.system("killall waybar &")

def StartWaybar():
    os.system("waybar &")


root = tkinter.Tk()
root.geometry("250x420")


SwitchToBlackWhite = tkinter.Button(root, text="Black & White Mode", command=BlackWhiteMode)
SwitchToBlackWhite.pack(pady=20)

SwitchToDarkBlue = tkinter.Button(root, text="Blue Dark Mode", command=DarkBlueMode)
SwitchToDarkBlue.pack(pady=20)

SwitchToBrightBlue = tkinter.Button(root, text="Blue Bright Mode", command=BrightBlueMode)
SwitchToBrightBlue.pack(pady=20)

SwitchToDarkBlue = tkinter.Button(root, text="Red Dark Mode", command=DarkRedMode)
SwitchToDarkBlue.pack(pady=20)

KillWaybarButton = tkinter.Button(root, text="Kill Waybar", command=KillWaybar).pack(pady=10)
StartWaybarButton = tkinter.Button(root, text="Start Wayber", command=StartWaybar).pack(pady=10)

root.mainloop()

