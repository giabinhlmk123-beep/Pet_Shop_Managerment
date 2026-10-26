class Session:

    user_id = 0
    username = ""
    full_name = ""
    role = ""

    @classmethod
    def login(cls, user_id, username, full_name, role):

        cls.user_id = user_id
        cls.username = username
        cls.full_name = full_name
        cls.role = role

    @classmethod
    def logout(cls):

        cls.user_id = 0
        cls.username = ""
        cls.full_name = ""
        cls.role = ""

    @classmethod
    def is_admin(cls):

        if cls.role == "Administrator":
            return True

        return False

    @classmethod
    def is_cashier(cls):

        if cls.role == "Cashier":
            return True

        return False

    @classmethod
    def is_employee(cls):

        if cls.role == "Employee":
            return True

        return False

    @classmethod
    def is_staff(cls):

        if cls.role == "Staff":
            return True

        return False