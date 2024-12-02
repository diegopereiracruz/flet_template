import flet as ft

# Pages
from app.pages.home import home_page
# from pages.library_page import LibraryPage
# from pages.settings_page import SettingsPage
# from pages.loading_page import LoadingPage
# from pages.game_page import GameDetailPage  # Importe a página de detalhes do jogo

class Router:
    
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": home_page(page),
            # Remova o conteúdo estático da biblioteca para garantir que ela seja recriada
            # "/settings": SettingsPage(page),
            # "/loading": LoadingPage(page),
            # "/game_details": None,  # Este será atualizado dinamicamente com o ID do jogo
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        if route.route.startswith("/game_details"):
            # Extraia o ID do jogo da rota e gere a página correspondente
            # game_id = route.route.split("/")[-1]
            # self.body.content = GameDetailPage(self.page, game_id)
            ...
            
        elif route.route == "/library":
            # Recrie a página da biblioteca sempre que a rota for /library
            # self.body.content = LibraryPage(self.page)
            ...
            
        else:
            self.body.content = self.routes.get(route.route, self.routes["/"])
        self.body.update()