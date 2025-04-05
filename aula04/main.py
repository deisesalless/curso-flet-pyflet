import flet as ft

def main(page: ft.Page):

    def add_task(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()

    title = ft.Text(value='Hello world')
    new_task = ft.TextField(hint_text='Insira uma tarefa', expand=True)
    button_add_task = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    # isso aqui é columa de dentro dela tem cada linha
    # a columa coloca todas as linhas em uma unica linha
    task_column = ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                title,
                                new_task,
                                button_add_task
                            ]
                        )
                    ]
                )

    page.add(task_column)

ft.app(target=main)