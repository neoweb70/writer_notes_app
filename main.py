from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
import json
import os


class WriterNotesApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.notes = {}
        self.current_note_id = None
        self.data_file = 'notes_data.json'
        self.load_notes()

    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # Main layout
        main_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)
        
        # Left panel - Notes list
        left_panel = BoxLayout(orientation='vertical', size_hint=(0.3, 1), spacing=5)
        
        # Header with "New Note" button
        header = BoxLayout(size_hint=(1, 0.08))
        new_note_btn = Button(
            text='+ New Note',
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        new_note_btn.bind(on_press=self.create_new_note)
        header.add_widget(new_note_btn)
        left_panel.add_widget(header)
        
        # Notes list
        scroll = ScrollView(size_hint=(1, 0.92))
        self.notes_list = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.notes_list.bind(minimum_height=self.notes_list.setter('height'))
        scroll.add_widget(self.notes_list)
        left_panel.add_widget(scroll)
        
        # Right panel - Note editor
        right_panel = BoxLayout(orientation='vertical', size_hint=(0.7, 1), spacing=5)
        
        # Title input
        self.title_input = TextInput(
            hint_text='Note Title',
            size_hint=(1, 0.08),
            multiline=False,
            font_size=20,
            background_color=(1, 1, 1, 1)
        )
        self.title_input.bind(text=self.on_title_change)
        right_panel.add_widget(self.title_input)
        
        # Content input
        self.content_input = TextInput(
            hint_text='Start writing your note here...',
            size_hint=(1, 0.82),
            background_color=(1, 1, 1, 1),
            font_size=16
        )
        self.content_input.bind(text=self.on_content_change)
        right_panel.add_widget(self.content_input)
        
        # Bottom buttons
        bottom_buttons = BoxLayout(size_hint=(1, 0.08), spacing=5)
        
        save_btn = Button(
            text='Save',
            background_color=(0.2, 0.7, 0.3, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        save_btn.bind(on_press=self.save_current_note)
        
        delete_btn = Button(
            text='Delete',
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        delete_btn.bind(on_press=self.delete_current_note)
        
        bottom_buttons.add_widget(save_btn)
        bottom_buttons.add_widget(delete_btn)
        right_panel.add_widget(bottom_buttons)
        
        # Add panels to main layout
        main_layout.add_widget(left_panel)
        main_layout.add_widget(right_panel)
        
        # Refresh notes list
        self.refresh_notes_list()
        
        return main_layout

    def create_new_note(self, instance):
        note_id = str(len(self.notes) + 1)
        self.notes[note_id] = {
            'title': 'Untitled Note',
            'content': ''
        }
        self.current_note_id = note_id
        self.title_input.text = 'Untitled Note'
        self.content_input.text = ''
        self.refresh_notes_list()
        self.save_notes()

    def load_note(self, note_id):
        self.current_note_id = note_id
        note = self.notes.get(note_id, {})
        self.title_input.text = note.get('title', '')
        self.content_input.text = note.get('content', '')

    def on_title_change(self, instance, value):
        if self.current_note_id and self.current_note_id in self.notes:
            self.notes[self.current_note_id]['title'] = value

    def on_content_change(self, instance, value):
        if self.current_note_id and self.current_note_id in self.notes:
            self.notes[self.current_note_id]['content'] = value

    def save_current_note(self, instance):
        if self.current_note_id:
            self.save_notes()
            self.refresh_notes_list()
            self.show_popup('Success', 'Note saved successfully!')

    def delete_current_note(self, instance):
        if self.current_note_id and self.current_note_id in self.notes:
            del self.notes[self.current_note_id]
            self.save_notes()
            self.current_note_id = None
            self.title_input.text = ''
            self.content_input.text = ''
            self.refresh_notes_list()
            self.show_popup('Deleted', 'Note deleted successfully!')

    def refresh_notes_list(self):
        self.notes_list.clear_widgets()
        for note_id, note in self.notes.items():
            btn = Button(
                text=note['title'][:30] + ('...' if len(note['title']) > 30 else ''),
                size_hint_y=None,
                height=50,
                background_color=(1, 1, 1, 1),
                color=(0.2, 0.2, 0.2, 1)
            )
            btn.bind(on_press=lambda x, nid=note_id: self.load_note(nid))
            self.notes_list.add_widget(btn)

    def save_notes(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.notes, f, indent=2)
        except Exception as e:
            print(f"Error saving notes: {e}")

    def load_notes(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.notes = json.load(f)
            except Exception as e:
                print(f"Error loading notes: {e}")
                self.notes = {}

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        close_btn = Button(text='OK', size_hint=(1, 0.3))
        popup_layout.add_widget(close_btn)
        
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.6, 0.3)
        )
        close_btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    WriterNotesApp().run()
