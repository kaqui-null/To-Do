import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from janela import Janela


class Main():

      def main(self):
            janela = Janela()
            janela.connect("delete-event", Gtk.main_quit)
            janela.show_all()
            Gtk.main()


if __name__ == "__main__":
      Main().main()
