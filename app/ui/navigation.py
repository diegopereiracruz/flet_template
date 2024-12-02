from flet import *

def nav_button(page, text, icon, go_to):
    def on_hover(e):
        if e.data == "true":
            e.control.bgcolor = colors.with_opacity(0.1, colors.WHITE)
        else:
            e.control.bgcolor = "transparent"
        e.control.update()
    
    return Container(
        content=Row(
            controls=[
                Icon(
                    icon,
                    color=colors.WHITE,
                    size=20,
                ),
                
                Text(
                    text,
                    style=TextStyle(
                        color=colors.WHITE,
                        height=0.0,
                        weight=FontWeight.W_500,
                    ),
                ),
            ],
            expand=True,
        ),
        padding=padding.symmetric(horizontal=10, vertical=2),

        border_radius=50,
        height=40,
        expand=True,
        on_click=lambda _: page.go(go_to),
        on_hover=on_hover,
    )

def navigation_bar(page, ft):
    navbar = Container(
        content=Row(
            controls=[
                Row(
                    controls=[
                        Icon(icons.HOME, color='white'),
                        Text("App name",
                            weight=FontWeight.BOLD,
                            style=TextStyle(
                                height=0,
                            ),
                        ),
                    ],
                    width=200,
                    alignment=MainAxisAlignment.START,
                ),
                
                Row(
                    controls=[
                        nav_button(
                            page=page,
                            text="Home",
                            icon=icons.HOME,
                            go_to="/",
                        ),
                        nav_button(
                            page=page,
                            text="Library",
                            icon=icons.LIBRARY_BOOKS,
                            go_to="/library",
                        ),
                        nav_button(
                            page=page,
                            text="Settings",
                            icon=icons.SETTINGS,
                            go_to="/settings",
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                
                Row(
                    controls=[
                        Icon(icons.VERIFIED_USER, color='white'),
                    ],
                    width=200,
                    alignment=MainAxisAlignment.END,
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=padding.symmetric(horizontal=20, vertical=0),
        bgcolor=colors.BLUE_900,
        expand=True,
        border=border.only(bottom=border.BorderSide(1, colors.GREY_900))
    )
    
    return Column(
            [
                navbar
            ],
            expand=True,
            alignment="start",
            height=50,
        )