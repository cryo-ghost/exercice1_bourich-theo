from controllers.task_controller import taskManager

def show_menu():
    print("\n1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Marquer une tâche comme faite")
    print("4. Quitter")



def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Choix: ")
        if choice == "1":
            title = input("Nom de la tâche: ")
            manager.add_task(title)
        elif choice == "2":
            for i, task in enumerate(manager.list_tasks()):
                print(f"{i}. {task}")
        elif choice == "3":
            index = int(input("Numéro de la tâche: "))
            manager.complete_task(index)
        elif choice == "4":
            break
        else:
            print("Choix invalide.")



if __name__ == "__main__":
    main()
