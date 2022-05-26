
import pyodbc 
import config
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

class Database:
    
    connection = None
    cursor = None

    def __init__(self) -> None:
        self.connect()

    def connect(self):
        self.connection = pyodbc.connect('DRIVER='+config.DB_DRIVER+';SERVER='+config.DB_SERVER+';DATABASE='+config.DB_NAME+';')
        self.cursor = self.connection.cursor()