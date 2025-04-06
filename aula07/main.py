import flet as ft
from custom_checkbox import Checkbox

def main(page: ft.Page):

    # Configurações da página
    page.title = 'Minhas Tarefas'
    page.window.width = 500
    page.window.height = 650
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)


    def add_task(e):
        listas_task_coluna.controls.append(Checkbox(new_task.value))
        new_task.value = ''
        page.update()
        new_task.focus()


    new_task = ft.TextField(hint_text='Insira uma tarefa', expand=True, autofocus=True)
    button_add_task = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    listas_task_coluna = ft.Column()


    # isso aqui é columa de dentro dela tem cada linha
    # a coluna coloca todas as linhas em uma unica linha
    barra_coluna = ft.Column(
        width=400,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    button_add_task
                ]
            ),
            listas_task_coluna
        ]
    )

    page.add(barra_coluna)

ft.app(target=main)