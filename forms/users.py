import customtkinter as ctk
from tkinter import ttk, messagebox

from database.database import connect_database
from models.session import Session


class UserForm:

    def __init__(self, parent):

        self.parent = parent

        self.selected_id = 0

        # =========================
        # TẠO GIAO DIỆN
        # =========================

        self.create_interface()

        # =========================
        # LOAD DỮ LIỆU
        # =========================

        self.load_users()

    # TẠO GIAO DIỆN


    def create_interface(self):

        # =========================
        # CẤU HÌNH GIAO DIỆN
        # =========================

        bg_color = "#F1F2F7"
        card_color = "#FFFFFF"
        primary_color = "#6500F5"
        hover_color = "#4D00C4"
        text_color = "#202044"
        muted_color = "#85859B"
        border_color = "#E5E7F0"

        self.parent.configure(fg_color=bg_color)

        # =========================
        # STYLE BẢNG DỮ LIỆU
        # =========================

        style = ttk.Style()

        style.configure(
            "User.Treeview",
            background=card_color,
            foreground=text_color,
            fieldbackground=card_color,
            rowheight=35,
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "User.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            padding=(8, 10),
            relief="flat"
        )

        style.map(
            "User.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        style.map(
            "User.Treeview.Heading",
            background=[("active", "#E4D6FF")]
        )

        # =========================
        # KHUNG CHÍNH
        # =========================

        main_frame = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color,
            corner_radius=0
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # =========================
        # TIÊU ĐỀ
        # =========================

        header_frame = ctk.CTkFrame(
            main_frame,
            fg_color=bg_color,
            corner_radius=0
        )

        header_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        title = ctk.CTkLabel(
            header_frame,
            text="QUẢN LÝ TÀI KHOẢN",
            font=("Arial", 25, "bold"),
            text_color=text_color
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Quản lý thông tin đăng nhập và phân quyền người dùng",
            font=("Arial", 12),
            text_color=muted_color
        )

        subtitle.pack(
            anchor="w",
            pady=(5, 0)
        )

        # =========================
        # KHUNG NHẬP THÔNG TIN
        # =========================

        input_frame = ctk.CTkFrame(
            main_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        input_frame.pack(
            fill="x",
            pady=(0, 12)
        )

        input_title = ctk.CTkLabel(
            input_frame,
            text="THÔNG TIN TÀI KHOẢN",
            font=("Arial", 15, "bold"),
            text_color=text_color
        )

        input_title.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(18, 10),
            sticky="w"
        )

        # Cho các cột co giãn đều
        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # Tên đăng nhập
        ctk.CTkLabel(
            input_frame,
            text="Tên đăng nhập:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_username = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            placeholder_text="Nhập tên đăng nhập"
        )

        self.txt_username.grid(
            row=1,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Họ tên
        ctk.CTkLabel(
            input_frame,
            text="Họ tên:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.txt_name = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            placeholder_text="Nhập họ tên"
        )

        self.txt_name.grid(
            row=1,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Địa chỉ
        ctk.CTkLabel(
            input_frame,
            text="Địa chỉ:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_address = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            placeholder_text="Nhập địa chỉ"
        )

        self.txt_address.grid(
            row=2,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Số điện thoại
        ctk.CTkLabel(
            input_frame,
            text="Số điện thoại:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.txt_phone = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            placeholder_text="Nhập số điện thoại"
        )

        self.txt_phone.grid(
            row=2,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Quyền
        ctk.CTkLabel(
            input_frame,
            text="Quyền:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.cbo_role = ctk.CTkComboBox(
            input_frame,
            values=[
                "Administrator",
                "Cashier",
                "Employee",
                "Staff"
            ],
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color
        )

        self.cbo_role.grid(
            row=3,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        self.cbo_role.set("Employee")

        # Ngày sinh
        ctk.CTkLabel(
            input_frame,
            text="Ngày sinh:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=3,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.txt_dob = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            placeholder_text="YYYY-MM-DD"
        )

        self.txt_dob.grid(
            row=3,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Mật khẩu
        ctk.CTkLabel(
            input_frame,
            text="Mật khẩu:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=4,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_password = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            show="*",
            placeholder_text="Nhập mật khẩu"
        )

        self.txt_password.grid(
            row=4,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # ID
        ctk.CTkLabel(
            input_frame,
            text="ID:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=4,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.lbl_id = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            height=36,
            font=("Arial", 13, "bold"),
            text_color=primary_color,
            corner_radius=8
        )

        self.lbl_id.grid(
            row=4,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Khoảng trống cuối khung
        ctk.CTkLabel(
            input_frame,
            text="",
            height=5
        ).grid(
            row=5,
            column=0,
            columnspan=4
        )

        # =========================
        # KHUNG NÚT CHỨC NĂNG
        # =========================

        button_frame = ctk.CTkFrame(
            main_frame,
            fg_color=card_color,
            corner_radius=12,
            border_width=1,
            border_color=border_color
        )

        button_frame.pack(
            fill="x",
            pady=(0, 12)
        )

        action_frame = ctk.CTkFrame(
            button_frame,
            fg_color="transparent"
        )

        action_frame.pack(
            fill="x",
            padx=12,
            pady=10
        )

        # NÚT THÊM
        self.btn_add = ctk.CTkButton(
            action_frame,
            text="＋  Thêm",
            width=105,
            height=36,
            corner_radius=8,
            fg_color="#6500F5",
            hover_color="#4D00C4",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.add_user
        )

        self.btn_add.pack(
            side="left",
            padx=(4, 5)
        )

        # NÚT SỬA
        self.btn_update = ctk.CTkButton(
            action_frame,
            text="✎  Sửa",
            width=105,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color="#6500F5",
            font=("Arial", 12, "bold"),
            command=self.update_user
        )

        self.btn_update.pack(
            side="left",
            padx=5
        )

        # NÚT XÓA
        self.btn_delete = ctk.CTkButton(
            action_frame,
            text="✕  Xóa",
            width=105,
            height=36,
            corner_radius=8,
            fg_color="#E5484D",
            hover_color="#C92A32",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_user
        )

        self.btn_delete.pack(
            side="left",
            padx=5
        )

        # NÚT LÀM MỚI
        self.btn_clear = ctk.CTkButton(
            action_frame,
            text="↻  Làm mới",
            width=115,
            height=36,
            corner_radius=8,
            fg_color="#E9ECF3",
            hover_color="#DDE1EB",
            text_color="#202044",
            font=("Arial", 12, "bold"),
            command=self.clear_form
        )

        self.btn_clear.pack(
            side="left",
            padx=5
        )

        # ĐƯỜNG PHÂN CÁCH
        ctk.CTkFrame(
            action_frame,
            width=1,
            height=28,
            fg_color="#E5E7F0"
        ).pack(
            side="left",
            padx=12
        )

        # NHÃN TÌM KIẾM
        ctk.CTkLabel(
            action_frame,
            text="Tìm kiếm:",
            font=("Arial", 12),
            text_color="#202044"
        ).pack(
            side="left",
            padx=(5, 5)
        )

        # Ô TÌM KIẾM
        self.txt_search = ctk.CTkEntry(
            action_frame,
            height=36,
            corner_radius=8,
            border_width=1,
            border_color="#E5E7F0",
            fg_color="#FFFFFF",
            text_color="#202044",
            placeholder_text="Tên đăng nhập, họ tên, SĐT...",
            placeholder_text_color="#85859B",
            font=("Arial", 12)
        )

        self.txt_search.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        # NÚT TÌM
        self.btn_search = ctk.CTkButton(
            action_frame,
            text="Tìm",
            width=75,
            height=36,
            corner_radius=8,
            fg_color="#6500F5",
            hover_color="#4D00C4",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.search_user
        )

        self.btn_search.pack(
            side="left",
            padx=(5, 4)
        )

        # =========================
        # KHUNG BẢNG DỮ LIỆU
        # =========================

        table_frame = ctk.CTkFrame(
            main_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        # Tiêu đề bảng
        table_header = ctk.CTkFrame(
            table_frame,
            fg_color="transparent"
        )

        table_header.pack(
            fill="x",
            padx=18,
            pady=(15, 10)
        )

        ctk.CTkLabel(
            table_header,
            text="DANH SÁCH TÀI KHOẢN",
            font=("Arial", 15, "bold"),
            text_color=text_color
        ).pack(side="left")

        ctk.CTkLabel(
            table_header,
            text="Chọn một dòng để xem hoặc chỉnh sửa",
            font=("Arial", 11),
            text_color=muted_color
        ).pack(side="right")

        # Khung chứa Treeview và scrollbar
        tree_frame = ctk.CTkFrame(
            table_frame,
            fg_color=card_color,
            corner_radius=8
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        columns = (
            "id",
            "username",
            "name",
            "address",
            "phone",
            "role",
            "dob"
        )

        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            style="User.Treeview"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("username", text="Tên đăng nhập")
        self.tree.heading("name", text="Họ tên")
        self.tree.heading("address", text="Địa chỉ")
        self.tree.heading("phone", text="Số điện thoại")
        self.tree.heading("role", text="Quyền")
        self.tree.heading("dob", text="Ngày sinh")

        self.tree.column(
            "id",
            width=55,
            minwidth=45,
            anchor="center",
            stretch=False
        )

        self.tree.column(
            "username",
            width=140,
            minwidth=110,
            anchor="w"
        )

        self.tree.column(
            "name",
            width=180,
            minwidth=130,
            anchor="w"
        )

        self.tree.column(
            "address",
            width=220,
            minwidth=150,
            anchor="w"
        )

        self.tree.column(
            "phone",
            width=135,
            minwidth=110,
            anchor="center"
        )

        self.tree.column(
            "role",
            width=130,
            minwidth=100,
            anchor="center"
        )

        self.tree.column(
            "dob",
            width=110,
            minwidth=95,
            anchor="center"
        )

        # Thanh cuộn dọc
        scrollbar_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.tree.yview
        )

        # Thanh cuộn ngang
        scrollbar_x = ttk.Scrollbar(
            tree_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # =========================
        # SỰ KIỆN CHỌN DÒNG
        # =========================

        self.tree.bind(
            "<ButtonRelease-1>",
            self.select_user
        )

    # HIỂN THỊ DANH SÁCH

    def load_users(self):

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT id, username, name, address,
                       phone, role, dob
                FROM tbUser
                ORDER BY id
            """

            cursor.execute(sql)

            rows = cursor.fetchall()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in rows:

                dob = row[6]

                if dob is not None:
                    dob = dob.strftime("%Y-%m-%d")
                else:
                    dob = ""

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        dob
                    )
                )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách tài khoản.\n" + str(e)
            )

    # CHỌN TÀI KHOẢN

    def select_user(self, event):

        selected = self.tree.selection()

        if len(selected) == 0:
            return

        item = self.tree.item(selected[0])

        values = item["values"]

        self.selected_id = values[0]

        self.lbl_id.configure(
            text=str(self.selected_id)
        )

        self.txt_username.delete(0, "end")
        self.txt_username.insert(0, values[1])

        self.txt_name.delete(0, "end")
        self.txt_name.insert(0, values[2])

        self.txt_address.delete(0, "end")

        if values[3] is not None:
            self.txt_address.insert(0, values[3])

        self.txt_phone.delete(0, "end")

        if values[4] is not None:
            self.txt_phone.insert(0, values[4])

        self.cbo_role.set(values[5])

        self.txt_dob.delete(0, "end")

        if values[6] is not None:
            self.txt_dob.insert(0, values[6])

        # Lấy mật khẩu
        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT password
                FROM tbUser
                WHERE id = ?
            """

            cursor.execute(
                sql,
                (self.selected_id,)
            )

            row = cursor.fetchone()

            self.txt_password.delete(0, "end")

            if row is not None and row[0] is not None:

                self.txt_password.insert(
                    0,
                    row[0]
                )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể lấy mật khẩu.\n" + str(e)
            )

    # THÊM TÀI KHOẢN

    def add_user(self):

        username = self.txt_username.get().strip()
        name = self.txt_name.get().strip()
        address = self.txt_address.get().strip()
        phone = self.txt_phone.get().strip()
        role = self.cbo_role.get().strip()
        dob = self.txt_dob.get().strip()
        password = self.txt_password.get().strip()

        if username == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập."
            )
            return

        if name == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập họ tên."
            )
            return

        if password == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mật khẩu."
            )
            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql_check = """
                SELECT id
                FROM tbUser
                WHERE username = ?
            """

            cursor.execute(
                sql_check,
                (username,)
            )

            existing = cursor.fetchone()

            if existing is not None:

                messagebox.showwarning(
                    "Thông báo",
                    "Tên đăng nhập đã tồn tại."
                )

                cursor.close()
                connection.close()

                return

            sql = """
                INSERT INTO tbUser
                (
                    username,
                    name,
                    address,
                    phone,
                    role,
                    dob,
                    password
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(
                sql,
                (
                    username,
                    name,
                    address,
                    phone,
                    role,
                    dob if dob != "" else None,
                    password
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Thêm tài khoản thành công."
            )

            self.clear_form()
            self.load_users()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể thêm tài khoản.\n" + str(e)
            )

    # SỬA TÀI KHOẢN

    def update_user(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tài khoản cần sửa."
            )

            return

        username = self.txt_username.get().strip()
        name = self.txt_name.get().strip()
        address = self.txt_address.get().strip()
        phone = self.txt_phone.get().strip()
        role = self.cbo_role.get().strip()
        dob = self.txt_dob.get().strip()
        password = self.txt_password.get().strip()

        if username == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên đăng nhập."
            )
            return

        if name == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập họ tên."
            )
            return

        if password == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mật khẩu."
            )
            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql_check = """
                SELECT id
                FROM tbUser
                WHERE username = ?
                AND id <> ?
            """

            cursor.execute(
                sql_check,
                (
                    username,
                    self.selected_id
                )
            )

            existing = cursor.fetchone()

            if existing is not None:

                messagebox.showwarning(
                    "Thông báo",
                    "Tên đăng nhập đã được sử dụng."
                )

                cursor.close()
                connection.close()

                return

            sql = """
                UPDATE tbUser
                SET username = ?,
                    name = ?,
                    address = ?,
                    phone = ?,
                    role = ?,
                    dob = ?,
                    password = ?
                WHERE id = ?
            """

            cursor.execute(
                sql,
                (
                    username,
                    name,
                    address,
                    phone,
                    role,
                    dob if dob != "" else None,
                    password,
                    self.selected_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật tài khoản thành công."
            )

            self.clear_form()
            self.load_users()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật tài khoản.\n" + str(e)
            )

    # XÓA TÀI KHOẢN

    def delete_user(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn tài khoản cần xóa."
            )

            return

        # Không cho xóa tài khoản đang đăng nhập
        if self.selected_id == Session.user_id:

            messagebox.showwarning(
                "Thông báo",
                "Bạn không thể xóa tài khoản đang đăng nhập."
            )

            return

        answer = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa tài khoản này không?"
        )

        if answer is False:
            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                DELETE FROM tbUser
                WHERE id = ?
            """

            cursor.execute(
                sql,
                (self.selected_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Xóa tài khoản thành công."
            )

            self.clear_form()
            self.load_users()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa tài khoản.\n" + str(e)
            )

    # TÌM KIẾM

    def search_user(self):

        keyword = self.txt_search.get().strip()

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT id, username, name, address,
                       phone, role, dob
                FROM tbUser
                WHERE username LIKE ?
                   OR name LIKE ?
                   OR phone LIKE ?
                ORDER BY id
            """

            search_value = "%" + keyword + "%"

            cursor.execute(
                sql,
                (
                    search_value,
                    search_value,
                    search_value
                )
            )

            rows = cursor.fetchall()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in rows:

                dob = row[6]

                if dob is not None:
                    dob = dob.strftime("%Y-%m-%d")
                else:
                    dob = ""

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        dob
                    )
                )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tìm kiếm.\n" + str(e)
            )

    # LÀM MỚI FORM

    def clear_form(self):

        self.selected_id = 0

        self.lbl_id.configure(
            text="Tự động"
        )

        self.txt_username.delete(0, "end")
        self.txt_name.delete(0, "end")
        self.txt_address.delete(0, "end")
        self.txt_phone.delete(0, "end")
        self.txt_dob.delete(0, "end")
        self.txt_password.delete(0, "end")

        self.cbo_role.set("Employee")

        self.txt_search.delete(0, "end")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.load_users()