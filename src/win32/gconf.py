import ConfigParser

print "Using fake gconf (win32)"
CLIENT_PRELOAD_RECURSIVE = 'CLIENT_PRELOAD_RECURSIVE'

config = ConfigParser.RawConfigParser()
config.read('hamster.win.cfg')

class Client:
    def __init__(self):
        pass
    
    def add_dir(self, dir, preload):
        pass
    
    def notify_add(self, dir, preload):
        pass
    
    def get(self, key):
        pass
    
    def set_bool(self, key, value):
        pass
    
    def set_string(self, key, value):
        pass
    
    def set_int(self, key, value):
        pass
    
def client_get_default():
    return Client()
    