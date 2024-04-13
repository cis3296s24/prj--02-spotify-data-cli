import os
import json

class Credentials():
    #function initializes credentials, once they are created they are stored to a json file for that instance
    def __init__(self):
        #retrieve credentials
        if os.path.exists('credentials.json'):
            with open('credentials.json', 'r') as file:
                credentials = json.load(file)
                self.client_id = credentials['client_id']
                self.client_secret = credentials['client_secret']
                self.username = credentials['username']
        #input credentials
        else:
            self.client_id = input("Provide Client ID: ")
            self.client_secret = input("Provide Client SECRET: ")
            self.username = input("Provide Username: ")

            with open('credentials.json', 'w') as file:
                json.dump({
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'username': self.username
                }, file)

        self.redirect_uri = "http://localhost:3000"
        #Scope must correspond to the features required for reading library, tracks, and playlist creation
        self.scope = "user-library-read user-top-read"

cred = Credentials()