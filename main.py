import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesión"
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

    boton = ft.Button(
        content="Ingresar", 
        bgcolor="pink200", 
        color="white", 
        width=300
    )

    page.add(
        icono,
        titulo,
        nombre,
        contrasena,
        boton
    )

ft.app(target=main)
