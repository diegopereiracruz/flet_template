import pystray
import flet as ft
from flet import Page
from PIL import Image

from app.system.FletRouter import Router
from app.ui.footer import footer_bar
from app.ui.navigation import navigation_bar

enable_tray = False
enable_navbar = False
enable_footer = False

if __name__ == "__main__":
    app_name = "App name"
    app_icon = "app/assets/tray_icon/icon.png"

    # Load the image to be displayed in the tray
    if enable_tray:
        tray_image = Image.open(app_icon)
    
    p: ft.Page  # Global variable for the Flet page

    def exit_app(icon, query):
        """Handle exit action from the tray icon."""
        # button_clicked(None)  # Trigger a button click event for feedback
        
        # Execute here some functions before the program close

        if enable_tray:
            icon.stop()  # Stop the tray icon loop/display
        p.window.destroy()  # Close the Flet window
        print("The App was closed/exited successfully!")

    def other_item_clicked(icon, query):
        """Handle clicks on non-default tray menu items."""
        # button_clicked(None)  # Trigger a button click event for feedback
        print("A tray option button was pressed.")

    def default_item_clicked(icon, query):
        """Show the Flet window when the default tray item is clicked."""
        icon.visible = True
        p.window.skip_task_bar = False  # Ensure the window shows on the taskbar
        p.window.visible = True  # Make the window visible
        p.window.focused = True  # Bring the window to focus
        p.window.minimized = False  # Restore window if minimized
        p.update()  # Update the page to reflect changes
        print("Tray button was pressed.")

    def menu_item_clicked(icon, query):
        """Handle menu item clicks from the tray icon."""
        if str(query) == "Open App":
            default_item_clicked(icon, query)  # Reuse logic to show the app
        elif str(query) == "Close App":
            exit_app(icon, query)  # Reuse logic to exit the app
        else:
            print("A Non-Default button was pressed.")

    def my_setup(icon):
        """Initial setup for the tray icon."""
        icon.visible = True  # Ensure the tray icon is visible at startup

    # Define the tray icon with its menu and actions
    if enable_tray:
        tray_icon = pystray.Icon(
            name=app_name,
            icon=tray_image,
            title=f"{app_name} Tray",
            menu=pystray.Menu(
                pystray.MenuItem("Open", default_item_clicked, default=True),  # Default menu item
                pystray.Menu.SEPARATOR,
                pystray.MenuItem("Option 1", other_item_clicked),
                pystray.MenuItem("Option 2", other_item_clicked),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem("Exit", exit_app)
            ),
            visible=True,
        )

    # def button_clicked(e): # Flet interaction example. put it in a button on_click event (on_click=button_clicked)
    #     """Handle button click events in the Flet app."""
    #     p.add(ft.Text("Button event handler was triggered!"))  # Feedback to user

    if enable_tray:
        def on_window_event(e):
            """Handle window events (minimize, restore, close)."""
            if e.data == "minimize":
                p.window.minimized = True  # Minimize the window
            elif e.data == "restore":
                p.window.skip_task_bar = False  # Show on taskbar
                p.window.visible = True  # Restore visibility
                p.window.focused = True  # Bring window to focus
            elif e.data == "close":
                p.window.skip_task_bar = True  # Remove from taskbar
                p.window.visible = False  # Hide the window

            p.update()  # Update the page to reflect changes


    def main(page):
        global p  # Make the page variable accessible globally
        p = page
        
        # Configurações da janela
        page.window.width = 1000
        page.window.min_width = 1000
        page.window.height = 600
        page.window.min_height = 600
        page.window.center()
        page.scroll = ft.ScrollMode.ADAPTIVE
        
        if enable_tray:
            page.window.on_event = on_window_event  # Set up window event handling
            page.window.prevent_close = True  # Prevent direct window closing
        
        page.title = app_name  # Set window title
        page.window.icon = app_icon

        # Definindo as barras fixa no topo e na parte inferior
        # page.appbar = NavBar(page, ft)
        
        myRouter = Router(page, ft)

        padding_top = 1
        padding_bottom = 1

        if enable_navbar:
            padding_top = 50
        
        if enable_footer:
            padding_bottom = 30
        
        # Adicionando o conteúdo principal e o footer fixo
        page.add(
            ft.Container(
                content=myRouter.body,
                expand=True,
                padding=ft.padding.only(top=padding_top, bottom=padding_bottom)  # Espaço para o footer
            )
        )
        
        # Adicionar o footer no layout como barra inferior fixa
        if enable_navbar:
            navBar = navigation_bar(page, ft)
            page.overlay.append(navBar)

        if enable_footer:
            footer = footer_bar(page, ft)
            page.overlay.append(footer)

        page.on_route_change = myRouter.route_change
        page.go('/')

    # Start the tray icon in a detached mode to integrate with the Flet app
    if enable_tray:
        tray_icon.run_detached(setup=my_setup)

    ft.app(target=main, assets_dir="assets")