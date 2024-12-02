import flet as ft

# Pages
from app.pages.home import home_page

class Router:
    
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            # Add pages here
            # 1. Create the page file in app/pages/   | Ex.: app/pages/settings.py
            # 2. Import the page in this file         | Ex.: from app.pages.settings import settings_page
            # 2. Put the path name of the page here   | Ex.: "/settings": settings_page(page),
            "/": home_page(page),
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        if route.route.startswith("/example"):
            # If the page's path starts with some name, do something.
            ...
            
        elif route.route == "/example":
            # If the page's path is equal some name, do something.
            ...
            
        else:
            self.body.content = self.routes.get(route.route, self.routes["/"])
        self.body.update()
