import flet as ft

class Checkbox(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)

        # botoes salvar, editar e deletar
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=self.save, visible=False, icon_color='green')
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete, icon_color='red')

        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.delete_button.visible = False
        self.text_view.visible = False
        self.save_button.visible = True
        self.text_edit.visible = True
        self.update()
        
    def save(self, e):
        self.save_button.visible = False
        self.text_edit.visible = False
        self.edit_button.visible = True
        self.text_view.visible = True

        # se tentar salvar uma tarefa em branco, ele pega o texto anterior nao deixando uma tarefa em branco
        if self.text_edit.value == '':
            self.text_edit.value = self.text_view.value
            # ou usar só 'return' na linha 39 para não deixar salvar nada vazia

        self.delete_button.visible = True
        self.text_view.value = self.text_edit.value
        self.update()

    def delete(self, e):
        self.visible = False
        self.update()