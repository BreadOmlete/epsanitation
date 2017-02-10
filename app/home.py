from framework.request_handler import EpscontrolRequestHandler

class Home(EpscontrolRequestHandler):
    def get(self):

        self.render('home/home.html')