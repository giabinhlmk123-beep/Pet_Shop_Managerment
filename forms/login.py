import customtkinter as ctk
from tkinter import messagebox

from database.database import connect_database
from models.session import Session
from forms.mainform import MainForm


class LoginForm:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("Pet Shop Management System")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Đưa cửa sổ Login ra giữa màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 500
        window_height = 500

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(
            "{}x{}+{}+{}".format(
                window_width,
                window_height,
                x,
                y
            )
        )

        self.main_form = None

        self.create_interface()

        self.root.mainloop()

    def create_interface(self):

        title = ctk.CTkLabel(
            self.root,
            text="PET SHOP",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=(50, 10))

        subtitle = ctk.CTkLabel(
            self.root,
            text="HỆ THỐNG QUẢN LÝ CỬA HÀNG THÚ CƯNG",
            font=("Arial", 14)
        )

        subtitle.pack(pady=(0, 30))

        username_label = ctk.CTkLabel(
            self.root,
            text="Tên đăng nhập",
            font=("Arial", 14)
        )

        username_label.pack(anchor="w", padx=80)

        self.username_entry = ctk.CTkEntry(
            self.root,
            width=340,
            height=40,
            placeholder_text="Nhập tên đăng nhập"
        )

        self.username_entry.pack(pady=(5, 15))

        password_label = ctk.CTkLabel(
            self.root,
            text="Mật khẩu",
            font=("Arial", 14)
        )

        password_label.pack(anchor="w", padx=80)

        self.password_entry = ctk.CTkEntry(
            self.root,
            width=340,
            height=40,
            placeholder_text="Nhập mật khẩu",
            show="*"
        )

        self.password_entry.pack(pady=(5, 5))

        self.show_password = ctk.BooleanVar(value=False)

        show_password_checkbox = ctk.CTkCheckBox(
            self.root,
            text="Hiện mật khẩu",
            variable=self.show_password,
            command=self.change_password_visibility
        )

        show_password_checkbox.pack(pady=10)

        login_button = ctk.CTkButton(
            self.root,
            text="ĐĂNG NHẬP",
            width=340,
            height=45,
            font=("Arial", 15, "bold"),
            command=self.login
        )

        login_button.pack(pady=20)

        self.username_entry.bind(
            "<Return>",
            self.login
        )

        self.password_entry.bind(
            "<Return>",
            self.login
        )

    def change_password_visibility(self):

        if self.show_password.get():

            self.password_entry.configure(show="")

        else:

            self.password_entry.configure(show="*")

    def login(self, event=None):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if username == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập!"
            )

            return

        if password == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mật khẩu!"
            )

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT id, username, name, role
                FROM tbUser
                WHERE username = ?
                AND password = ?
            """

            cursor.execute(
                sql,
                (username, password)
            )

            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user is None:

                messagebox.showerror(
                    "Đăng nhập thất bại",
                    "Tên đăng nhập hoặc mật khẩu không đúng!"
                )

                return

            user_id = user[0]
            username = user[1]
            full_name = user[2]
            role = user[3]

            Session.login(
                user_id,
                username,
                full_name,
                role
            )

            # Ẩn cửa sổ Login
            self.root.withdraw()

            # Mở MainForm
            self.main_form = MainForm(
                self.root,
                self
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể đăng nhập!\n\n" + str(e)
            )

    def show_login(self):

        self.root.deiconify()

        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

        self.username_entry.focus()