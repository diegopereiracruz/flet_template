from flet import *

# Barra de informações no rodapé
def footer_bar(page, ft):
    footer = Container(
        content=Row(
            controls=[
                Row(
                    controls=[
                        Text("Left data",
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
                        Text("Center data",
                            style=TextStyle(
                                height=0,
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                
                Row(
                    controls=[
                        TextButton(
                            text="Button",
                            icon=icons.CHECK_CIRCLE,
                            icon_color="green",
                            style=ButtonStyle(
                                icon_size=12,
                            ),
                            tooltip=Tooltip(
                                message="Tooltip info",
                                wait_duration=0,
                            ),
                            
                        ),
                    ],
                    width=200,
                    alignment=MainAxisAlignment.END,
                ),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=padding.symmetric(horizontal=10),
        bgcolor=colors.BACKGROUND,
        height=30,
        border=border.only(top=border.BorderSide(1, colors.GREY_900))
    )
    
    # Configurando layout geral com a barra de informações no final
    return Column(
            [
                footer  # barra de informações no rodapé
            ],
            expand=True,  # permite que o conteúdo principal se expanda
            alignment="end",  # mantém o footer no final da página
        )