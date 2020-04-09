import requests
import json
import configparser as cfg


class Chatbot():

    def __init__(self, token):
        self.token = self.readToken(token)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def getUpdates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def sendMessage(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def readToken(self, token):
        parser = cfg.ConfigParser()
        parser.read(token)
        return parser.get('creds', 'token')