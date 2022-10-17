from urllib.parse import urljoin

import requests


class ApiClientException(Exception):
    ...


class ResponseStatusCodeException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ApiClient:
    BLOG_ID = 431

    def __init__(self, base_url: str, login: str, password: str):
        self.base_url = base_url

        self.login = login
        self.password = password

        self.session = requests.Session()

    def get_token(self):
        headers = requests.get(url=self.base_url).headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken']
        if not token_header:
            raise ApiClientException('Expected csrftoken in Set-Cookie')
        token_header = token_header[0].split('=')[-1]
        return token_header

    def post_login(self):
        token = self.get_token()
        headers = {
            'Cookie': f'csrftoken={token}',
            'X-CSRFToken': f'{token}'
        }

        data = {
            'login': self.login,
            'password': self.password
        }
        login_request = self._request(method='POST', location='login/', headers=headers, data=data)

        return login_request

    def _request(self, method, location, headers, data, params=None, allow_redirects=False, expected_status=200,
                 jsonify=True):
        url = urljoin(self.base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Expected {expected_status}, but got {response.status_code}')
        if jsonify:
            json_response: dict = response.json()
            if json_response.get('bStateError', False):
                error = json_response['sErrorMsg']
                raise RespondErrorException(f'Request {url} return error : "{error}"')

            return json_response
        return response

    def post_topic_create(self, title, text, publish=False):
        data = {
            'title': title,
            'text': text,
            'publish': 'on' if publish else 'false',
            'forbid_comment': 'false',
            'is_news': 'false',
            'important': 'false',
            'lessons': '',
            'blog': self.BLOG_ID,
        }

        headers = {
            'Cookie': f'sessionid_gtp={self.session.cookies["sessionid_gtp"]};'
                      f' csrftoken={self.session.cookies["csrftoken"]}',
            'X-CSRFToken': f'{self.session.cookies["csrftoken"]}'
        }

        location = urljoin(self.base_url, 'blog/topic/create/')
        return self._request(method='POST', location=location, data=data, headers=headers)

    def get_feed(self, feed_type=None):
        feed_type = feed_type if feed_type else 'all'
        params = {'type': feed_type}

        headers = {
            'Cookie': f'sessionid_gtp={self.session.cookies["sessionid_gtp"]};'
                      f' csrftoken={self.session.cookies["csrftoken"]}',
        }

        location = urljoin(self.base_url, 'feed/update/stream/')

        return self._request(method='GET', location=location, headers=headers, params=params, data=None)

    def post_topic_delete(self, topic_id):
        data = {
            'submit': 'Удалить',
        }
        headers = {
            'Cookie': f'sessionid_gtp={self.session.cookies["sessionid_gtp"]}; '
                      f'csrftoken={self.session.cookies["csrftoken"]};',
            'X-CSRFToken': f'{self.session.cookies["csrftoken"]}'
        }

        location = urljoin(self.base_url, f'blog/topic/delete/{topic_id}/')

        delete_request = self._request(method='POST', location=location, data=data, headers=headers,
                                       allow_redirects=True, jsonify=False)
        return delete_request
