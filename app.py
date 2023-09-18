# -*- coding: utf-8 -*-
from importlib import import_module
from falcon import App


class APP(App):

    def __init__(self, url_list=None, **kwargs):
        super().__init__(**kwargs)
        self.url_list = url_list
        self.auto_route()

    def auto_route(self):
        for path, version in self.url_list:
            urls = import_module(path + '.url').urls
            for route, instance in urls:
                self.add_route(f'/{route}', instance)
