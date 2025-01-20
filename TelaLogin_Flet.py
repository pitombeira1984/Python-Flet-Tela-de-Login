import flet as ft

def main(page: ft.Page):
    page.title = "Login"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE

    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", width=300, password=True, can_reveal_password=True)
    button = ft.ElevatedButton("Login", width=300)
    forgot_password = ft.Text("Forgot password?", size=12)

    container = ft.Container(
        content=ft.Column([
            username,
            password
        ]),
        bgcolor=ft.colors.WHITE,
        padding=10,
        border_radius=5
    )

    page.add(
        ft.Column(
            [
                ft.Text("Login", size=30),
                container,
                button,
                forgot_password
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )



ft.app(target=main)