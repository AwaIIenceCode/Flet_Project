import flet as ft

def main(page: ft.Page):
    page.title = "To-Do List"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "dark"

    def add_clicked(e):
        if new_task.value.strip():
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()

    def toggle_theme(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
            theme_button.icon = ft.icons.DARK_MODE
        else:
            page.theme_mode = "light"
            theme_button.icon = ft.icons.LIGHT_MODE
        page.update()

    new_task = ft.TextField(hint_text="What needs to be done?", width=350)
    add_button = ft.ElevatedButton("Add", on_click=add_clicked)
    theme_button = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        on_click=toggle_theme,
        tooltip="Toggle day/night mode"
    )

    page.add(
        ft.Row(
            [theme_button, new_task, add_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
