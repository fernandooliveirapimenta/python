from __future__ import annotations
from abc import ABC, abstractmethod


class Window:
    __toolkit: str = ''
    __purpose: str = ''

    def __init__(self, tookit: str, purpose: str):
        self.__toolkit = tookit
        self.__purpose = purpose

    def get_tolkit(self) -> str:
        return self.__toolkit

    def get_purpose(self) -> str:
        return self.__purpose


class GtkToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, 'Gtk', 'ToolboxWindow')


class GtkLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, 'Gtk', 'LayersWindow')


class GtkMainWindow(Window):
    def __init__(self):
        Window.__init__(self, 'Gtk', 'MainWindow')


class QtToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, 'Qt', 'ToolboxWindow')


class QtLayerWindow(Window):
    def __init__(self):
        Window.__init__(self, 'Qt', 'LayersWindow')


class QtMainWindow(Window):
    def __init__(self):
        Window.__init__(self, 'Qt', 'MainWindow')


class UIFactory(ABC):
    @abstractmethod
    def get_tool_box_window(self): pass

    @abstractmethod
    def get_layers_window(self): pass

    @abstractmethod
    def get_main_window(self): pass


class GtkUIFactory(UIFactory):
    def get_tool_box_window(self):
        return GtkToolboxWindow()

    def get_layers_window(self):
        return GtkLayersWindow()

    def get_main_window(self):
        return GtkMainWindow()


class QtUIFactory(UIFactory):
    def get_tool_box_window(self):
        return QtToolboxWindow()

    def get_layers_window(self):
        return QtLayerWindow()

    def get_main_window(self):
        return QtMainWindow()


if __name__ == '__main__':
    gnome = True
    kde = not gnome

    if gnome:
        ui = GtkUIFactory()
    else:
        ui = QtUIFactory()

    toolbox = ui.get_tool_box_window()
    layers = ui.get_layers_window()
    main = ui.get_main_window()

    print(f'{toolbox.get_tolkit()}:{toolbox.get_purpose()}')
    print(f'{layers.get_tolkit()}:{layers.get_purpose()}')
    print(f'{main.get_tolkit()}:{main.get_purpose()}')
