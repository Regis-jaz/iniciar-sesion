import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    icono = ft.Icon(
        icon=ft.Icons.AUTO_AWESOME,
        color="pink200",
        size=60
    )

    titulo = ft.Text(
        "Iniciar Sesión",
        size=30,
        weight="bold",
        color="pink200"
    )

    nombre = ft.TextField(
        label="Nombre",
        border_color="pink200",
        width=300
    )
    
    contrasena = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        border_color="pink200",
        width=300
    )

    mensaje = ft.Text()

    def pantalla_principal():

        page.controls.clear()

        titulo_panel = ft.Container(
        content=ft.Text(
            "Panel Principal",
            color="white",
            size=18,
            weight="bold"
        ),
        bgcolor="pink200",
        padding=10,
        width=300
    )

        bienvenida = ft.Text(
        "Bienvenido al Sistema",
        size=20,
        weight="bold",
        color="pink200"
    )

        subtexto = ft.Text(
        "Has iniciado sesión correctamente",
        size=12,
        color="pink100"
        )

        menu = ft.Row(
        [
            ft.Column(
                [
                    ft.Icon(ft.Icons.HOME, color="pink200"),
                    ft.Text("Inicio", color="pink200")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
                
                ft.Column(
                [
                    ft.Icon(ft.Icons.SEARCH, color="pink200"),
                    ft.Text("Explorar", color="pink200")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Column(
                [
                    ft.Icon(ft.Icons.PERSON, color="pink200"),
                    ft.Text("Perfil", color="pink200")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        width=300
    )

        page.add(
        ft.Column(
            [
                titulo_panel,
                ft.Container(height=40),
                bienvenida,
                subtexto,
                ft.Container(height=60),
                menu
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

        page.update()

    def login(e):
        if nombre.value == "admin" and contrasena.value == "123456":
            mensaje.value = "Bienvenido"
            mensaje.color = "pink200"
            page.update()
            pantalla_principal()
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "pink200"
            page.update()

    boton = ft.ElevatedButton(
        "Ingresar",
        bgcolor="pink200",
        color="white",
        on_click=login
    )

    page.add(
        ft.Column(
            [
                icono,
                titulo,
                nombre,
                contrasena,
                boton,
                mensaje,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main) 
