"""
   watch.py

   MediaWiki API Demos
   Demo of `Watch` module: Add a page to your watchlist
   MIT license

   for creating bots: https://en.wikipedia.org/wiki/Special:BotPasswords

   https://www.mediawiki.org/wiki/API:Watch


"""

import requests


class WikipediaApi:
    api_url = "https://en.wikipedia.org/w/api.php"
    session = requests.Session()

    def retrieve_login_token(self):
        params = {
            "action": "query",
            "meta": "tokens",
            "type": "login",
            "format": "json"
        }
        request = self.session.get(url=self.api_url, params=params)
        data = request.json()
        login_token = data["query"]["tokens"]["logintoken"]
        return login_token

    def send_post_to_log_in(self):
        """
        # method, Obtain credentials by first visiting
        https://www.en.wikipedia.org/wiki/Special:BotPasswords
        See https://www.mediawiki.org/wiki/API:Login for more
        information on log in methods.
        """
        params = {
            "action": "login",
            'lgname': "Testusername1090@educationmailru",
            'lgpassword': "6m387r983fof7l706m082vl5l9posqat",
            "format": "json",
            "lgtoken": self.retrieve_login_token()
        }
        self.session.post(url=self.api_url, data=params)

    def get_csrf_token(self):
        self.send_post_to_log_in()
        params = {
            "action": "query",
            "meta": "tokens",
            "type": "watch",
            "format": "json"
        }
        request = self.session.get(url=self.api_url, params=params)
        data = request.json()
        csrf_token = data["query"]["tokens"]["watchtoken"]
        return csrf_token

    def send_request_delete_watchlist(self):
        params = {
            "action": "watch",
            "titles": "Parkway Drive" + "|" + "Judas Priest",
            "unwatch": "",
            "format": "json",
            "token": self.get_csrf_token(),
        }
        session = self.session.post(url=self.api_url, data=params)
        return session.status_code
