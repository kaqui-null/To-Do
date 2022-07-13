import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango


class Janela(Gtk.Window):

      def __init__(self):
            Gtk.Window.__init__(self, title="To-Do List")
            
            self.grid = Gtk.Grid()
            self.add(self.grid)

            self.buttons()
            self.adicionar_stack()      


      def criar_textview(self):
            janela_com_scroll = Gtk.ScrolledWindow()
            janela_com_scroll.set_hexpand(True)
            janela_com_scroll.set_vexpand(True)

            self.textview = Gtk.TextView()
            self.textbuffer = self.textview.get_buffer()
            self.textbuffer.set_text(
                  "Texto teste"
            )
            janela_com_scroll.add(self.textview)

            return janela_com_scroll

      def adicionar_stack(self):
            
            stack = Gtk.Stack()
            stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
            stack.set_transition_duration(1000) # 1s

            stack.add_titled(self.criar_textview(), "texto 1", "Texto")

            stack_switcher = Gtk.StackSwitcher()
            stack_switcher.set_stack(stack)
            self.grid.attach(stack_switcher, 0, 1, 1, 1)
            self.grid.attach(stack, 0, 2, 1, 1)

      def buttons(self):
            pass
      
















