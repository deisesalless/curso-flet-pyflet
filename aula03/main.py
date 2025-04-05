import flet as ft

def main(page: ft.Page):

    def add_task(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()

    title = ft.Text(value='Hello world')
    new_task = ft.TextField(hint_text='Insira uma tarefa')
    button_add_task = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    page.add(title, new_task, button_add_task)

ft.app(target=main)