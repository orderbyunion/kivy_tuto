import socket 
import gi
gi.require_version('Gst', '1.0')
import kivy

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.graphics.texture import Texture
from kivy.core.camera import Camera
from kivy.graphics import *
import time
import os 
from pathlib import Path 
#import cv2											
import struct
import threading
import pickle

class fscreen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def select_file(self):
		from plyer import filechooser
		filechooser.open_file(on_selection = self.selected)

	def selected(self, selection):
		print(selection[0])
		self.ids.bck.source = selection[0]



class theapp(App):
	def build(self):

		self.screenm = ScreenManager() 

		self.fscreen = fscreen()
		screen = Screen(name = "first screen")
		screen.add_widget(self.fscreen)
		self.screenm.add_widget(screen)

		return self.screenm

if __name__ == "__main__":
	theapp = theapp()										
	theapp.run() 