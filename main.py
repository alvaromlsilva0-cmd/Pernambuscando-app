import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    # Cores principais
    cor_fundo_azul = "#131b4d"
    cor_texto_verde = "#00c87c"

    # Função para criar cartões
    def criar_cartao(icone, titulo, subtitulo, cor_fundo, cor_texto):
        return ft.Container(
            bgcolor=cor_fundo,
            border_radius=15,
            padding=15,
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Icon(icone, color=cor_texto, size=35),
                    ft.Text(
                        titulo,
                        color=cor_texto,
                        weight=ft.FontWeight.BOLD,
                        size=16
                    ),
                    ft.Text(
                        subtitulo,
                        color=cor_texto,
                        size=10,
                        weight=ft.FontWeight.W_500
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            )
        )

    # Cabeçalho
    cabecalho = ft.Container(
        padding=ft.Padding.only(
            top=50,
            left=20,
            right=20,
            bottom=20
        ),
        bgcolor=cor_fundo_azul,
        content=ft.Text(
            spans=[
                ft.TextSpan(
                    "Bora descobrir\n",
                    style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=28,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.TextSpan(
                    "Pernambuco ",
                    style=ft.TextStyle(
                        color=cor_texto_verde,
                        size=28,
                        weight=ft.FontWeight.BOLD
                    )
                ),
                ft.TextSpan(
                    "hoje?",
                    style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=28,
                        weight=ft.FontWeight.BOLD
                    )
                ),
            ],
            height=80
        )
    )

    # Área principal branca
    area_branca = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=ft.BorderRadius.only(
            top_left=20,
            top_right=20
        ),
        expand=True,
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=20,
            controls=[

                # Barra de pesquisa
                ft.Container(
                    bgcolor="#f0f0f0",
                    border_radius=30,
                    padding=ft.Padding.symmetric(
                        horizontal=15,
                        vertical=12
                    ),
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                ft.Icons.SEARCH,
                                color=ft.Colors.GREY_600,
                                size=20
                            ),
                            ft.Text(
                                "Jet ski, tapioca, museu",
                                color=ft.Colors.GREY_500,
                                size=14
                            )
                        ]
                    )
                ),

                # Ícones de navegação
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Icon(ft.Icons.ARROW_DROP_DOWN, color=cor_fundo_azul, size=40),
                        ft.Icon(ft.Icons.ARROW_DROP_DOWN, color="#e91e63", size=40),
                        ft.Icon(ft.Icons.ARROW_DROP_DOWN, color="#ffc107", size=40),
                        ft.Icon(ft.Icons.ARROW_DROP_DOWN, color="#2196f3", size=40),
                        ft.Icon(ft.Icons.ARROW_DROP_DOWN, color="#4caf50", size=40),
                        ft.Icon(ft.Icons.ARROW_DROP_DOWN, color=cor_fundo_azul, size=40),
                    ]
                ),

                # Título das categorias
                ft.Text(
                    "Categorias",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK
                ),

                # Cartões de categorias
                ft.Column(
                    spacing=15,
                    controls=[
                        ft.Row(
                            spacing=15,
                            controls=[
                                criar_cartao(
                                    ft.Icons.POOL,
                                    "Aquático",
                                    "Praia, rios, jet ski",
                                    "#7a9df5",
                                    "#13317c"
                                ),
                                criar_cartao(
                                    ft.Icons.PARK,
                                    "Natureza",
                                    "Trilha e ecoturismo",
                                    "#95df9c",
                                    "#176931"
                                ),
                            ]
                        ),

                        ft.Row(
                            spacing=15,
                            controls=[
                                criar_cartao(
                                    ft.Icons.ACCOUNT_BALANCE,
                                    "Cultura",
                                    "Museu e patrimônio",
                                    "#f0cf6a",
                                    "#815e0a"
                                ),
                                criar_cartao(
                                    ft.Icons.RESTAURANT,
                                    "Gastronomia",
                                    "Restaurante",
                                    "#ef8a9d",
                                    "#aa193a"
                                ),
                            ]
                        )
                    ]
                ),

                # Perto de você agora
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            "Perto de você agora",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK
                        ),
                        ft.Text(
                            "Ver tudo",
                            size=13,
                            color=ft.Colors.BLUE_500
                        )
                    ]
                ),

                # Estabelecimento próximo
                ft.Row(
                    controls=[
                        ft.Container(
                            bgcolor="#ef8a9d",
                            width=45,
                            height=45,
                            border_radius=10
                        ),
                        ft.Text(
                            "Tapioca Rosa da Joana",
                            weight=ft.FontWeight.BOLD,
                            italic=True,
                            size=14,
                            color=ft.Colors.BLACK,
                            expand=True
                        ),
                        ft.Text(
                            "450m",
                            size=13,
                            color=ft.Colors.BLACK_87
                        )
                    ]
                ),

                ft.Container(height=10)
            ]
        )
    )

    # Barra de navegação inferior
    barra_navegacao = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=ft.Padding.only(
            top=10,
            bottom=20,
            left=20,
            right=20
        ),
        border=ft.Border.all(
            1,
            ft.Colors.GREY_200
        ),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            width=30,
                            height=2,
                            bgcolor=ft.Colors.CYAN_600
                        ),
                        ft.Icon(
                            ft.Icons.HOME_OUTLINED,
                            color=ft.Colors.CYAN_600,
                            size=28
                        )
                    ],
                    spacing=4,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),

                ft.Icon(
                    ft.Icons.ARTICLE_OUTLINED,
                    color=ft.Colors.BLACK_87,
                    size=28
                ),

                ft.Icon(
                    ft.Icons.SEARCH,
                    color=ft.Colors.BLACK_87,
                    size=28
                ),

                ft.Icon(
                    ft.Icons.VIDEOCAM_OUTLINED,
                    color=ft.Colors.BLACK_87,
                    size=28
                ),

                ft.Icon(
                    ft.Icons.ACCOUNT_CIRCLE_OUTLINED,
                    color=ft.Colors.BLACK_87,
                    size=29
                ),
            ]
        )
    )

    # Layout principal
    layout_principal = ft.Column(
        spacing=0,
        expand=True,
        controls=[
            cabecalho,
            area_branca,
            barra_navegacao
        ]
    )

    # Adiciona à página
    page.add(
        ft.Container(
            bgcolor=cor_fundo_azul,
            expand=True,
            content=layout_principal
        )
    )


if __name__ == "__main__":
    ft.run(
        main,
        view=ft.AppView.WEB_BROWSER
    )
