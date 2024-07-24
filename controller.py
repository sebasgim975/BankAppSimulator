from view import *

#Controller class for managing interactions between the model and view in an MVC framework.
class Controller:
    def __init__(self, master):
        self.view = View(master)
