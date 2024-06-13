class Volumes:
    def __init__(self):
        self.ssh_login = "login"
        self.ssh_password = "password"

        self.port = 22

        self.user_containers_file = 'user_containers/user_containers.json'  # Пользовательские контейнеры
        self.script_containers_base_file = 'script_containers/script_containers.json'  # Контейнеры, которые создает скрипт
