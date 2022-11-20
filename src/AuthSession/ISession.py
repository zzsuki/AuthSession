from abc import ABC, abstractmethod
from typing import Union
from urllib.parse import urljoin

import requests
from requests import Session, Response, Request
from requests.auth import AuthBase


# 关闭证书警告
requests.packages.urllib3.disable_warnings()




class ISession(Session, ABC):
    def __init__(self, host):
        super().__init__()
        self.host = host
        self.token = None
        self.timeout = 10
    
    @abstractmethod
    def authorize(self):
        """负责处理每个请求的鉴权问题,，负责根据token更新加salt的token"""
        pass

    @abstractmethod
    def login(self):
        """登录并设置token(未加salt的原始token)"""
        pass

    @abstractmethod
    def logout(self):
        pass


    def _fill_url(self, url: str, scheme: str = 'https'):
        """拼凑完整url"""
        # enclosed_url = self._enclose_url(url)
        return urljoin(f'{scheme}://{self.host}', url)

    def request(self, method: str, url: str, is_login=False, *args, **kwargs):
        """请求接口"""
        url = self._fill_url(url)
        if is_login:
            return super().request(method=method.upper(), url=url, verify=False, *args, **kwargs)
        if self.token is not None:
            self.authorize()
        else:
            self.login()
        return super().request(method=method.upper(), url=url, verify=False, timeout=self.timeout, *args, **kwargs)

    def get(self, url=None, *args, **kwargs):
        return self.request(method='GET', url=url, *args, **kwargs)

    def post(self, url=None, *args, **kwargs):
        return self.request(method='POST', url=url, *args, **kwargs)

    def put(self, url=None, *args, **kwargs):
        return self.request(method='PUT', url=url, *args, **kwargs)

    def delete(self, url=None, *args, **kwargs):
        return self.request(method='DELETE', url=url, *args, **kwargs)

    def patch(self, url=None, *args, **kwargs):
        return self.request(method='PATCH', url=url, *args, **kwargs)

    