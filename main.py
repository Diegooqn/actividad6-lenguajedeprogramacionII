# Clase que representa una tarea (Modelo)
class Task:
    def __init__(self, title, description):
        self.title = title  # Título de la tarea
        self.description = description  # Descripción de la tarea
        self.completed = False  # Estado: si la tarea está completada o no, empieza como no completada

    def mark_as_completed(self):
        self.completed = True  # Cambia el estado a completada

    def edit_task(self, title, description):
        self.title = title  # Permite cambiar el título
        self.description = description  # Permite cambiar la descripción

    def __str__(self):
        status = "Completada" if self.completed else "No Completada"
        return f"Tarea: {self.title}, Descripción: {self.description}, Estado: {status}"

# Clase que muestra las tareas al usuario (Vista)
class View:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("No hay tareas disponibles.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    @staticmethod
    def prompt_for_task_info():
        title = input("Ingresa el título de la tarea: ")
        description = input("Ingresa la descripción de la tarea: ")
        return title, description

    @staticmethod
    def prompt_for_task_number():
        return int(input("Ingresa el número de la tarea: ")) - 1

# Clase que controla la lógica de la aplicacion (Controlador)
class Controller:
    def __init__(self, model, view):
        self.model = model  # Recibe la lista de tareas (modelo)
        self.view = view  # Recibe la vista para mostrar al usuario

    def add_task(self):
        title, description = self.view.prompt_for_task_info()  # Pide al usuario la información de la tarea
        task = Task(title, description)  # Crea una nueva tarea
        self.model.append(task)  # Añade la tarea a la lista

    def edit_task(self):
        self.view.show_tasks(self.model)  # Muestra las tareas
        task_index = self.view.prompt_for_task_number()  # Pide el número de la tarea a editar
        title, description = self.view.prompt_for_task_info()  # Pide nueva información
        self.model[task_index].edit_task(title, description)  # Edita la tarea seleccionada

    def delete_task(self):
        self.view.show_tasks(self.model)  # Muestra las tareas
        task_index = self.view.prompt_for_task_number()  # Pide el número de la tarea a eliminar
        del self.model[task_index]  # Elimina la tarea

    def mark_task_completed(self):
        self.view.show_tasks(self.model)  # Muestra las tareas
        task_index = self.view.prompt_for_task_number()  # Pide el número de la tarea a marcar como completada
        self.model[task_index].mark_as_completed()  # Marca la tarea como completada

    def show_tasks(self):
        self.view.show_tasks(self.model)  # Muestra las tareas

    def run(self):
        while True:
            print("\n1. Agregar tarea\n2. Editar tarea\n3. Eliminar tarea\n4. Marcar tarea como completada\n5. Ver tareas\n6. Salir")
            choice = input("Elige una opción: ")
            if choice == "1":
                self.add_task()  # Añadir tarea
            elif choice == "2":
                self.edit_task()  # Editar tarea
            elif choice == "3":
                self.delete_task()  # Eliminar tarea
            elif choice == "4":
                self.mark_task_completed()  # Marcar tarea como completada
            elif choice == "5":
                self.show_tasks()  # Mostrar tareas
            elif choice == "6":
                break  # Salir del programa
            else:
                print("Opción no válida.")

# Ejecución del programa
if __name__ == "__main__":
    tasks = []  # Lista donde se guardarán las tareas
    view = View()  # Instancia de la vista
    controller = Controller(tasks, view)  # Instancia del controlador con el modelo (lista) y la vista
    controller.run()  # Iniciar el programa