#imports
import random as r
import sys
import kivy
from kivy.app import App
from kivy.event import EventDispatcher
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
	ListProperty, ObjectProperty
import Jumbalaya

class JumbalayaMenu(Screen):
	pass

class BowlScreen(Screen):
	def art(self):
		gs = sm.current_screen
		gs.set_bowl('ArtLiterature')
	def ent(self):
		gs = sm.current_screen
		gs.set_bowl('Entertainment')
	def geo(self):
		gs = sm.current_screen
		gs.set_bowl('Geography')
	def his(self):
		gs = sm.current_screen
		gs.set_bowl('History')
	def sci(self):
		gs = sm.current_screen
		gs.set_bowl('ScienceNature')
	def msc(self):
		gs = sm.current_screen
		gs.set_bowl('Misc')

class GameScreen(Screen):
	bowl = StringProperty()
	hint = StringProperty()
	word = StringProperty()
	jumble = ListProperty()
	j_rows = NumericProperty()
	jumble_y_hint = NumericProperty()
	tile_selected = BooleanProperty()
	letter_selected = StringProperty()

	def set_bowl(self, bowl):
		jb = Jumbalaya.Jumbalaya(bowl)
		self.bowl = self.display_bowl(bowl)
		self.hint = jb.return_data()[0]
		self.word = jb.return_data()[1]
		self.jumble = jb.return_data()[2]
		if len(self.jumble) == 10:
			self.j_rows = 1
			self.jumble_y_hint = 0.4
		else:
			self.j_rows = 2
			self.jumble_y_hint = 1
		self.load_slots()
		self.load_jumble()

	def load_slots(self):
		remainder = 20 - len(self.word)
		for letter in self.word:
			slot_button = Button(background_normal=('Art/Tiles/slot.png'), background_down=('Art/Tiles/slot.png'))
			if not letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				self.ids.slot_grid.add_widget(Label(text=letter, font_size=24))
			else:
				self.ids.slot_grid.add_widget(slot_button)
		for num in range(remainder):
			self.ids.slot_grid.add_widget(Label(text=''))

	def load_jumble(self):
		jumble_index = 0
		for letter in self.jumble:
			tile_button = TileButton(background_normal=('Art/Tiles/' + letter + '.png'), background_down=('Art/Tiles/Selected/' + letter + '.png'))
			tile_button.letter = letter
			tile_button.jumble_index = jumble_index
			self.ids.jumble_grid.add_widget(tile_button)
			jumble_index += 1

	def update_jumble(self):
		pass

	def tile_pressed(self):
		self.tile_selected = True
		print('button pressed')


	def slot_pressed(self):
		if self.tile_selected:
			pass

	def display_bowl(self, bowl):
		bowl = bowl.replace('ArtLiterature','Art & Literature')
		bowl = bowl.replace('ScienceNature','Science & Nature')
		bowl = bowl.replace('Misc','Miscellaneous')
		return bowl

class TileButton(ToggleButton):
	letter = StringProperty()
	jumble_index = NumericProperty()
	def on_press(self):
		pass

Builder.load_string("""
#:kivy 1.8.0
<Jumbalaya>:
	canvas:
		Color:
			rgb: 0, 1, 1
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size

<JumbalayaMenu>:
	canvas:
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size
	BoxLayout:
		orientation: 'vertical'
		Image:
			source: 'Art/Title.png'
		BoxLayout:
			spacing: 20
			orientation: 'vertical'
			BoxLayout:
				Label:
				Button:
					background_normal: 'Art/Buttons/new_bowl.png'
					on_press: root.manager.current = 'bowls'
				Label:
			BoxLayout:
				Label:
				Button:
					background_normal: 'Art/Buttons/about.png'
				Label:
			BoxLayout:
				Label:
				Button:
					background_normal: 'Art/Buttons/quit.png'
					on_press: exit()
				Label:
		Label:
			size_hint_y: 0.2

<BowlScreen>:
	canvas:
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size

	BoxLayout:
		orientation: 'vertical'
		padding: 50
		Button:
			text: 'Art & Literature'
			on_press: root.manager.current = 'game'; root.art()
		Button:
			text: 'Entertainment'
			on_press: root.manager.current = 'game'; root.ent()
		Button:
			text: 'Geography'
			on_press: root.manager.current = 'game'; root.geo()
		Button:
			text: 'History'
			on_press: root.manager.current = 'game'; root.his()
		Button:
			text: 'Science & Nature'
			on_press: root.manager.current = 'game'; root.sci()
		Button:
			text: 'Misc'
			on_press: root.manager.current = 'game'; root.msc()
		Button:
			text: 'Back to menu'
			on_press: root.manager.current = 'menu';

<GameScreen>:
	canvas:
		Rectangle:
			source: 'Art/bg1.png'
			size: self.size

	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			size_hint:(1, 0.3)
			orientation: 'horizontal'
			Button:
				text: 'Back'
				on_press: root.clear_widgets();root.manager.current = 'bowls'
			Label:
				font_size: 24
				text: root.bowl
			Button:
				text: 'Give Up'
				on_press: root.manager.current = 'game'
		Label:
			multiline: True
			text: root.hint
			font_size: 24
		GridLayout:
			id: slot_grid
			cols: 10
			rows: 2
			minimum_width: 34
		GridLayout:
			id: jumble_grid
			cols: 10
			rows: root.j_rows
			size_hint:(1,root.jumble_y_hint)			
""")

sm = ScreenManager(transition = FadeTransition())
sm.add_widget(JumbalayaMenu(name='menu'))
sm.add_widget(BowlScreen(name='bowls'))
sm.add_widget(GameScreen(name='game'))

class JumbalayaApp(App):
	def build(self):
		return sm
	
if __name__ == '__main__':
	JumbalayaApp().run()
