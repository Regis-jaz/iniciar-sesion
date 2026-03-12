import flet as ft

def main(page: ft.Page):
    page.title = "inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text(
            "Iniciar Sesion",
            bgcolor="pink50",
            size=30,
            weight="bold", 
        )
    
    

    nombre = ft.TextField(
            label="Nombre",
            hint_text="",
            border_color="pink200",
            bgcolor="pink50",
            color="white",
            width=300
        )

    conraseña = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            border_color="pink200",
            bgcolor="pink50",
            color="white",
            width=300
        )

    
    boton = ft.Button(
            content="Ingresar",
            bgcolor="pink200",
            color="white",
            width=300
        )


ft.app(target=main)
