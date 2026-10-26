import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from database.database import connect_database


class CustomerForm:

    def __init__(self, parent):

        self.parent = parent

        self.create_interface()

        self.load_customers()

    # TẠO GIAO DIỆN

    def create_interface(self):

        # ==========================================
        # MÀU SẮC GIAO DIỆN
        # ==========================================

        bg_color = "#F1F2F7"
        card_color = "#FFFFFF"
        text_color = "#202044"
        purple_color = "#6500F5"
        hover_color = "#4D00C4"
        border_color = "#E5E7F0"
        muted_color = "#85859B"

        self.parent.configure(fg_color=bg_color)

        # ==========================================
        # TIÊU ĐỀ
        # ==========================================

        header_frame = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color
        )
        header_frame.pack(
            fill="x",
            padx=25,
            pady=(18, 10)
        )

        ctk.CTkLabel(
            header_frame,
            text="Quản lý khách hàng",
            font=("Arial", 27, "bold"),
            text_color=text_color
        ).pack(side="left")

        ctk.CTkLabel(
            header_frame,
            text="PET SHOP  /  CUSTOMERS",
            font=("Arial", 11),
            text_color=muted_color
        ).pack(side="right", padx=5)

        # ==========================================
        # KHUNG NHẬP THÔNG TIN
        # ==========================================

        input_frame = ctk.CTkFrame(
            self.parent,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )
        input_frame.pack(
            fill="x",
            padx=25,
            pady=7
        )

        ctk.CTkLabel(
            input_frame,
            text="Thông tin khách hàng",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=18,
            pady=(14, 8),
            sticky="w"
        )

        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # ==========================================
        # TÊN KHÁCH HÀNG
        # ==========================================

        ctk.CTkLabel(
            input_frame,
            text="Tên khách hàng:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=0,
            padx=18,
            pady=10,
            sticky="w"
        )

        self.name_entry = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập tên khách hàng"
        )
        self.name_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # ==========================================
        # ĐỊA CHỈ
        # ==========================================

        ctk.CTkLabel(
            input_frame,
            text="Địa chỉ:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=2,
            padx=18,
            pady=10,
            sticky="w"
        )

        self.address_entry = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập địa chỉ"
        )
        self.address_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # ==========================================
        # SỐ ĐIỆN THOẠI
        # ==========================================

        ctk.CTkLabel(
            input_frame,
            text="Số điện thoại:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=0,
            padx=18,
            pady=10,
            sticky="w"
        )

        self.phone_entry = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập số điện thoại"
        )
        self.phone_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        # ==========================================
        # MÃ KHÁCH HÀNG
        # ==========================================

        ctk.CTkLabel(
            input_frame,
            text="Mã khách hàng:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=2,
            padx=18,
            pady=10,
            sticky="w"
        )

        self.id_label = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            font=("Arial", 13, "bold"),
            text_color=purple_color
        )
        self.id_label.grid(
            row=2,
            column=3,
            padx=10,
            pady=10,
            sticky="w"
        )

        # Khoảng cách cuối khung nhập
        ctk.CTkLabel(
            input_frame,
            text=""
        ).grid(
            row=3,
            column=0,
            pady=3
        )

        # ==========================================
        # THANH CHỨC NĂNG
        # ==========================================

        button_frame = ctk.CTkFrame(
            self.parent,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 10)
        )

        # ==========================================
        # NÚT THÊM
        # ==========================================

        self.btn_add = ctk.CTkButton(
            button_frame,
            text="＋  Thêm",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#6500F5",
            hover_color="#4D00C4",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.add_customer
        )

        self.btn_add.pack(
            side="left",
            padx=(0, 8)
        )
        # ==========================================
        # NÚT SỬA
        # ==========================================

        self.btn_update = ctk.CTkButton(
            button_frame,
            text="✎  Sửa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color="#6500F5",
            font=("Arial", 12, "bold"),
            command=self.update_customer
        )

        self.btn_update.pack(
            side="left",
            padx=8
        )

        # ==========================================
        # NÚT XÓA
        # ==========================================

        self.btn_delete = ctk.CTkButton(
            button_frame,
            text="✕  Xóa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E5484D",
            hover_color="#C92A32",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_customer
        )

        self.btn_delete.pack(
            side="left",
            padx=8
        )

        # ==========================================
        # NÚT LÀM MỚI
        # ==========================================

        self.btn_clear = ctk.CTkButton(
            button_frame,
            text="↻  Làm mới",
            width=120,
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
            padx=8
        )

        # ==========================================
        # TÌM KIẾM
        # ==========================================

        ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Arial", 12),
            text_color=text_color
        ).pack(
            side="left",
            padx=(20, 5)
        )

        self.search_entry = ctk.CTkEntry(
            button_frame,
            width=230,
            height=35,
            corner_radius=8,
            border_color=border_color,
            fg_color=card_color,
            text_color="#000000",
            placeholder_text="Tên khách hàng hoặc SĐT..."
        )
        self.search_entry.pack(
            side="left",
            padx=5,
            pady=10
        )

        self.btn_search = ctk.CTkButton(
            button_frame,
            text="Tìm",
            width=75,
            height=36,
            corner_radius=8,
            fg_color="#6500F5",
            hover_color="#4D00C4",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.search_customer
        )

        self.btn_search.pack(
            side="left",
            padx=8
        )

        # ==========================================
        # KHUNG BẢNG DỮ LIỆU
        # ==========================================

        table_frame = ctk.CTkFrame(
            self.parent,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 18)
        )

        ctk.CTkLabel(
            table_frame,
            text="Danh sách khách hàng",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).pack(
            anchor="w",
            padx=16,
            pady=(14, 8)
        )

        # ==========================================
        # ĐỊNH DẠNG BẢNG
        # ==========================================

        tree_style = ttk.Style()

        tree_style.configure(
            "Customer.Treeview",
            background="#FFFFFF",
            foreground=text_color,
            fieldbackground="#FFFFFF",
            rowheight=34,
            font=("Arial", 10)
        )

        tree_style.configure(
            "Customer.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            padding=(8, 10)
        )

        tree_style.map(
            "Customer.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        # ==========================================
        # BẢNG KHÁCH HÀNG
        # ==========================================

        tree_container = ctk.CTkFrame(
            table_frame,
            fg_color=card_color
        )
        tree_container.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        columns = (
            "id",
            "name",
            "address",
            "phone"
        )

        self.customer_table = ttk.Treeview(
            tree_container,
            columns=columns,
            show="headings",
            style="Customer.Treeview"
        )

        self.customer_table.heading(
            "id",
            text="Mã khách hàng"
        )

        self.customer_table.heading(
            "name",
            text="Tên khách hàng"
        )

        self.customer_table.heading(
            "address",
            text="Địa chỉ"
        )

        self.customer_table.heading(
            "phone",
            text="Số điện thoại"
        )

        self.customer_table.column(
            "id",
            width=120,
            minwidth=90,
            anchor="center"
        )

        self.customer_table.column(
            "name",
            width=250,
            minwidth=160
        )

        self.customer_table.column(
            "address",
            width=350,
            minwidth=180
        )

        self.customer_table.column(
            "phone",
            width=180,
            minwidth=130,
            anchor="center"
        )

        # ==========================================
        # THANH CUỘN
        # ==========================================

        vertical_scrollbar = ttk.Scrollbar(
            tree_container,
            orient="vertical",
            command=self.customer_table.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            tree_container,
            orient="horizontal",
            command=self.customer_table.xview
        )

        self.customer_table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)

        self.customer_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        # ==========================================
        # CHỌN KHÁCH HÀNG TRONG BẢNG
        # ==========================================

        self.customer_table.bind(
            "<ButtonRelease-1>",
            self.select_customer
        )

    # LOAD KHÁCH HÀNG

    def load_customers(self):

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT id, name, address, phone
                FROM tbCustomer
                ORDER BY id
            """

            cursor.execute(sql)

            rows = cursor.fetchall()

            cursor.close()
            connection.close()

            # Xóa dữ liệu cũ trên bảng
            for item in self.customer_table.get_children():

                self.customer_table.delete(item)

            # Thêm dữ liệu mới
            for row in rows:

                self.customer_table.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách khách hàng!\n\n" + str(e)
            )

    # CHỌN KHÁCH HÀNG

    def select_customer(self, event=None):

        selected = self.customer_table.selection()

        if len(selected) == 0:

            return

        item = self.customer_table.item(
            selected[0]
        )

        values = item["values"]

        if len(values) == 0:

            return

        self.id_label.configure(
            text=str(values[0])
        )

        self.name_entry.delete(
            0,
            "end"
        )

        self.name_entry.insert(
            0,
            values[1]
        )

        self.address_entry.delete(
            0,
            "end"
        )

        self.address_entry.insert(
            0,
            values[2]
        )

        self.phone_entry.delete(
            0,
            "end"
        )

        self.phone_entry.insert(
            0,
            values[3]
        )

    # THÊM KHÁCH HÀNG

    def add_customer(self):

        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên khách hàng!"
            )

            return

        if phone == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập số điện thoại!"
            )

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                INSERT INTO tbCustomer
                (name, address, phone)
                VALUES (?, ?, ?)
            """

            cursor.execute(
                sql,
                (
                    name,
                    address,
                    phone
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Thêm khách hàng thành công!"
            )

            self.clear_form()
            self.load_customers()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể thêm khách hàng!\n\n" + str(e)
            )

    # SỬA KHÁCH HÀNG

    def update_customer(self):

        customer_id = self.id_label.cget("text")

        if customer_id == "Tự động":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng cần sửa!"
            )

            return

        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên khách hàng!"
            )

            return

        if phone == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập số điện thoại!"
            )

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                UPDATE tbCustomer
                SET name = ?,
                    address = ?,
                    phone = ?
                WHERE id = ?
            """

            cursor.execute(
                sql,
                (
                    name,
                    address,
                    phone,
                    customer_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật khách hàng thành công!"
            )

            self.clear_form()
            self.load_customers()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật khách hàng!\n\n" + str(e)
            )

    # XÓA KHÁCH HÀNG

    def delete_customer(self):

        customer_id = self.id_label.cget("text")

        if customer_id == "Tự động":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng cần xóa!"
            )

            return

        result = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa khách hàng này không?"
        )

        if not result:

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                DELETE FROM tbCustomer
                WHERE id = ?
            """

            cursor.execute(
                sql,
                (customer_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Xóa khách hàng thành công!"
            )

            self.clear_form()
            self.load_customers()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa khách hàng!\n\n" + str(e)
            )

    # TÌM KIẾM

    def search_customer(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_customers()

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT id, name, address, phone
                FROM tbCustomer
                WHERE name LIKE ?
                OR phone LIKE ?
                ORDER BY id
            """

            search_value = "%" + keyword + "%"

            cursor.execute(
                sql,
                (
                    search_value,
                    search_value
                )
            )

            rows = cursor.fetchall()

            cursor.close()
            connection.close()

            for item in self.customer_table.get_children():

                self.customer_table.delete(item)

            for row in rows:

                self.customer_table.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3]
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tìm kiếm khách hàng!\n\n" + str(e)
            )

    # LÀM MỚI FORM

    def clear_form(self):

        self.id_label.configure(
            text="Tự động"
        )

        self.name_entry.delete(
            0,
            "end"
        )

        self.address_entry.delete(
            0,
            "end"
        )

        self.phone_entry.delete(
            0,
            "end"
        )

        self.search_entry.delete(
            0,
            "end"
        )

        selected = self.customer_table.selection()

        for item in selected:

            self.customer_table.selection_remove(item)

        self.load_customers()