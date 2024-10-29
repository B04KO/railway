class User:
    def __init__(self, username):
        self.username = username
        self.role = 'user'

    def view_documents(self):
        # Логика для просмотра документов
        return "Просмотр документов"

    def add_document(self, document):
        # Логика для добавления документа
        return f"Документ '{document}' добавлен пользователем {self.username}"

    def edit_own_document(self, document_id, new_content):
        # Логика для редактирования своего документа
        return f"Документ {document_id} обновлен пользователем {self.username}"


class Manager(User):
    def __init__(self, username):
        super().__init__(username)
        self.role = 'manager'

    def edit_document(self, document_id, new_content):
        # Логика для редактирования любого документа
        return f"Документ {document_id} обновлен менеджером {self.username}"

    def delete_document(self, document_id):
        # Логика для удаления любого документа
        return f"Документ {document_id} удален менеджером {self.username}"


class Admin(Manager):
    def __init__(self, username):
        super().__init__(username)
        self.role = 'admin'

    def edit_document(self, document_id, new_content):
        # Логика для редактирования любого документа
        return f"Документ {document_id} обновлен админом {self.username}"

    def delete_document(self, document_id):
        # Логика для удаления любого документа
        return f"Документ {document_id} удален админом {self.username}"

    def add_user(self, username, password, role):
        # Логика для добавления нового пользователя
        return f"Пользователь '{username}' добавлен с ролью '{role}'"

    def delete_user(self, username):
        # Логика для удаления пользователя
        return f"Пользователь '{username}' удален администратором {self.username}"

    def update_user_profile(self, username, new_name=None, new_password=None):
        # Логика для обновления имени или пароля пользователя
        return f"Профиль пользователя '{username}' обновлен администратором {self.username}"
