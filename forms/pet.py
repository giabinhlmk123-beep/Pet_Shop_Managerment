import customtkinter as ctk
from tkinter import ttk, messagebox

from database.database import connect_database


class PetForm:

    def __init__(self, parent):

        self.parent = parent

        self.selected_id = 0

        self.customer_data = []

        self.create_interface()

        self.load_customers()

        self.load_pets()

    # TẠO GIAO DIỆN

    def create_interface(self):

        # =========================
        # MÀU SẮC GIAO DIỆN
        # =========================

        bg_color = "#F1F2F7"
        card_color = "#FFFFFF"
        primary_color = "#6500F5"
        hover_color = "#4D00C4"
        text_color = "#202044"
        muted_color = "#85859B"
        border_color = "#E5E7F0"
        danger_color = "#E5484D"
        danger_hover = "#C92A32"

        self.parent.configure(fg_color=bg_color)

        # =========================
        # CẤU HÌNH STYLE BẢNG
        # =========================

        style = ttk.Style()

        style.configure(
            "Pet.Treeview",
            background=card_color,
            foreground=text_color,
            rowheight=34,
            fieldbackground=card_color,
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "Pet.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=(8, 10)
        )

        style.map(
            "Pet.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        style.map(
            "Pet.Treeview.Heading",
            background=[("active", "#E4D6FF")]
        )

        # =========================
        # TIÊU ĐỀ
        # =========================

        header_frame = ctk.CTkFrame(
            self.parent,
            fg_color="transparent"
        )

        header_frame.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        title = ctk.CTkLabel(
            header_frame,
            text="QUẢN LÝ THÚ CƯNG",
            font=("Arial", 25, "bold"),
            text_color=text_color
        )

        title.pack(
            side="left",
            padx=5
        )

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Quản lý thông tin thú cưng và chủ sở hữu",
            font=("Arial", 12),
            text_color=muted_color
        )

        subtitle.pack(
            side="left",
            padx=(15, 0),
            pady=(8, 0)
        )

        # =========================
        # KHUNG NHẬP THÔNG TIN
        # =========================

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
            pady=(5, 10)
        )

        # Tiêu đề khung thông tin

        input_title = ctk.CTkLabel(
            input_frame,
            text="Thông tin thú cưng",
            font=("Arial", 16, "bold"),
            text_color=text_color
        )

        input_title.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(15, 5),
            sticky="w"
        )

        # Cấu hình cột

        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # =========================
        # TÊN THÚ CƯNG
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Tên thú cưng:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_pet_name = ctk.CTkEntry(
            input_frame,
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập tên thú cưng"
        )

        self.txt_pet_name.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # LOẠI THÚ CƯNG
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Loại:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.cbo_pet_type = ctk.CTkComboBox(
            input_frame,
            values=["Chó", "Mèo", "Chim", "Cá", "Khác"],
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color
        )

        self.cbo_pet_type.grid(
            row=1,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        self.cbo_pet_type.set("Chó")

        # =========================
        # GIỐNG
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Giống:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_breed = ctk.CTkEntry(
            input_frame,
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập giống thú cưng"
        )

        self.txt_breed.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # GIỚI TÍNH
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Giới tính:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.cbo_gender = ctk.CTkComboBox(
            input_frame,
            values=["Đực", "Cái"],
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color
        )

        self.cbo_gender.grid(
            row=2,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        self.cbo_gender.set("Đực")

        # =========================
        # TUỔI
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Tuổi:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_age = ctk.CTkEntry(
            input_frame,
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập tuổi"
        )

        self.txt_age.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # CÂN NẶNG
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Cân nặng (kg):",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=3,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.txt_weight = ctk.CTkEntry(
            input_frame,
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Ví dụ: 5.5"
        )

        self.txt_weight.grid(
            row=3,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # =========================
        # KHÁCH HÀNG
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Khách hàng:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=4,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.cbo_customer = ctk.CTkComboBox(
            input_frame,
            values=[],
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color,
            command=self.customer_selected
        )

        self.cbo_customer.grid(
            row=4,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # SỐ ĐIỆN THOẠI
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Số điện thoại:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=4,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.txt_phone = ctk.CTkEntry(
            input_frame,
            height=35,
            width=220,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập số điện thoại"
        )

        self.txt_phone.grid(
            row=4,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # =========================
        # GHI CHÚ
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Ghi chú:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=5,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_note = ctk.CTkEntry(
            input_frame,
            height=35,
            width=500,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Thông tin bổ sung (nếu có)"
        )

        self.txt_note.grid(
            row=5,
            column=1,
            columnspan=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # ID
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Mã thú cưng:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=6,
            column=0,
            padx=(20, 10),
            pady=(8, 15),
            sticky="w"
        )

        self.lbl_id = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            font=("Arial", 13, "bold"),
            text_color=primary_color
        )

        self.lbl_id.grid(
            row=6,
            column=1,
            padx=10,
            pady=(8, 15),
            sticky="w"
        )

        # =========================
        # KHUNG NÚT CHỨC NĂNG
        # =========================

        button_frame = ctk.CTkFrame(
            self.parent,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 10)
        )

        # NÚT THÊM

        self.btn_add = ctk.CTkButton(
            button_frame,
            text="＋  Thêm",
            width=110,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            font=("Arial", 12, "bold"),
            command=self.add_pet
        )

        self.btn_add.pack(
            side="left",
            padx=(0, 8)
        )

        # NÚT SỬA

        self.btn_update = ctk.CTkButton(
            button_frame,
            text="✎  Sửa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color=primary_color,
            font=("Arial", 12, "bold"),
            command=self.update_pet
        )

        self.btn_update.pack(
            side="left",
            padx=8
        )

        # NÚT XÓA

        self.btn_delete = ctk.CTkButton(
            button_frame,
            text="✕  Xóa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color=danger_color,
            hover_color=danger_hover,
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_pet
        )

        self.btn_delete.pack(
            side="left",
            padx=8
        )

        # NÚT LÀM MỚI

        self.btn_clear = ctk.CTkButton(
            button_frame,
            text="↻  Làm mới",
            width=120,
            height=36,
            corner_radius=8,
            fg_color="#E9ECF3",
            hover_color="#DDE1EB",
            text_color=text_color,
            font=("Arial", 12, "bold"),
            command=self.clear_form
        )

        self.btn_clear.pack(
            side="left",
            padx=8
        )

        # KHU VỰC TÌM KIẾM

        ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Arial", 12, "bold"),
            text_color=text_color
        ).pack(
            side="left",
            padx=(20, 8)
        )

        self.txt_search = ctk.CTkEntry(
            button_frame,
            width=210,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color=card_color,
            text_color="#000000",
            placeholder_text="Tên thú cưng, giống..."
        )

        self.txt_search.pack(
            side="left",
            padx=5
        )

        self.btn_search = ctk.CTkButton(
            button_frame,
            text="Tìm",
            width=75,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            font=("Arial", 12, "bold"),
            command=self.search_pet
        )

        self.btn_search.pack(
            side="left",
            padx=5
        )

        # =========================
        # KHUNG BẢNG DỮ LIỆU
        # =========================

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
            pady=(0, 20)
        )

        # TIÊU ĐỀ BẢNG

        table_title_frame = ctk.CTkFrame(
            table_frame,
            fg_color="transparent"
        )

        table_title_frame.pack(
            fill="x",
            padx=15,
            pady=(12, 8)
        )

        ctk.CTkLabel(
            table_title_frame,
            text="Danh sách thú cưng",
            font=("Arial", 16, "bold"),
            text_color=text_color
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            table_title_frame,
            text="Thông tin thú cưng và khách hàng sở hữu",
            font=("Arial", 11),
            text_color=muted_color
        ).pack(
            side="right"
        )

        # =========================
        # CẤU HÌNH CỘT
        # =========================

        columns = (
            "id",
            "petname",
            "pettype",
            "breed",
            "gender",
            "age",
            "weight",
            "customer",
            "phone",
            "note"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Pet.Treeview"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("petname", text="Tên thú cưng")
        self.tree.heading("pettype", text="Loại")
        self.tree.heading("breed", text="Giống")
        self.tree.heading("gender", text="Giới tính")
        self.tree.heading("age", text="Tuổi")
        self.tree.heading("weight", text="Cân nặng (kg)")
        self.tree.heading("customer", text="Khách hàng")
        self.tree.heading("phone", text="Số điện thoại")
        self.tree.heading("note", text="Ghi chú")

        # ĐỘ RỘNG CỘT

        self.tree.column(
            "id",
            width=55,
            minwidth=45,
            anchor="center",
            stretch=False
        )

        self.tree.column(
            "petname",
            width=140,
            minwidth=100,
            anchor="w"
        )

        self.tree.column(
            "pettype",
            width=80,
            minwidth=65,
            anchor="center",
            stretch=False
        )

        self.tree.column(
            "breed",
            width=130,
            minwidth=90,
            anchor="w"
        )

        self.tree.column(
            "gender",
            width=85,
            minwidth=70,
            anchor="center",
            stretch=False
        )

        self.tree.column(
            "age",
            width=60,
            minwidth=50,
            anchor="center",
            stretch=False
        )

        self.tree.column(
            "weight",
            width=100,
            minwidth=80,
            anchor="center",
            stretch=False
        )

        self.tree.column(
            "customer",
            width=160,
            minwidth=110,
            anchor="w"
        )

        self.tree.column(
            "phone",
            width=125,
            minwidth=100,
            anchor="w"
        )

        self.tree.column(
            "note",
            width=200,
            minwidth=120,
            anchor="w"
        )

        # =========================
        # THANH CUỘN
        # =========================

        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.tree.pack(
            side="top",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        scrollbar_y.pack(
            side="right",
            fill="y",
            pady=(0, 5)
        )

        scrollbar_x.pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=(0, 8)
        )

        # =========================
        # SỰ KIỆN CHỌN DÒNG
        # =========================

        self.tree.bind(
            "<ButtonRelease-1>",
            self.select_pet
        )

    # LOAD KHÁCH HÀNG

    def load_customers(self):

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT
                    id,
                    name,
                    phone
                FROM tbCustomer
                ORDER BY id
            """

            cursor.execute(
                sql
            )

            rows = cursor.fetchall()

            self.customer_data = []

            values = []

            for row in rows:

                customer_id = row[0]
                customer_name = row[1]
                phone = row[2]

                display_text = (
                    str(customer_id)
                    + " - "
                    + str(customer_name)
                )

                self.customer_data.append(
                    {
                        "id": customer_id,
                        "name": customer_name,
                        "phone": phone,
                        "display": display_text
                    }
                )

                values.append(
                    display_text
                )

            if len(values) > 0:

                self.cbo_customer.configure(
                    values=values
                )

                self.cbo_customer.set(
                    values[0]
                )

            else:

                self.cbo_customer.configure(
                    values=[
                        "Chưa có khách hàng"
                    ]
                )

                self.cbo_customer.set(
                    "Chưa có khách hàng"
                )

            cursor.close()

            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách khách hàng.\n\n"
                + str(e)
            )

    # LẤY CUSTOMER ID

    def get_customer_id(self):

        selected_customer = self.cbo_customer.get()

        for customer in self.customer_data:

            if customer["display"] == selected_customer:

                return customer["id"]

        return None

    # LOAD THÚ CƯNG

    def load_pets(self):

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT
                    p.PetID,
                    p.PetName,
                    p.PetType,
                    p.Breed,
                    p.Gender,
                    p.Age,
                    p.Weight,
                    c.name,
                    p.Phone,
                    p.Note
                FROM tbPet p
                LEFT JOIN tbCustomer c
                    ON p.CustomerID = c.id
                ORDER BY p.PetID
            """

            cursor.execute(
                sql
            )

            rows = cursor.fetchall()

            for item in self.tree.get_children():

                self.tree.delete(
                    item
                )

            for row in rows:

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
                        row[6],
                        row[7],
                        row[8],
                        row[9]
                    )
                )

            cursor.close()

            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách thú cưng.\n\n"
                + str(e)
            )

    # CHỌN THÚ CƯNG

    def select_pet(self, event=None):

        selected = self.tree.selection()

        if len(selected) == 0:

            return

        item = self.tree.item(
            selected[0]
        )

        values = item["values"]

        if len(values) == 0:

            return

        self.selected_id = values[0]

        self.lbl_id.configure(
            text=str(
                self.selected_id
            )
        )

        # Tên

        self.txt_pet_name.delete(
            0,
            "end"
        )

        self.txt_pet_name.insert(
            0,
            values[1]
        )

        # Loại

        self.cbo_pet_type.set(
            values[2]
        )

        # Giống

        self.txt_breed.delete(
            0,
            "end"
        )

        if values[3] is not None:

            self.txt_breed.insert(
                0,
                values[3]
            )

        # Giới tính

        self.cbo_gender.set(
            values[4]
        )

        # Tuổi

        self.txt_age.delete(
            0,
            "end"
        )

        if values[5] is not None:

            self.txt_age.insert(
                0,
                values[5]
            )

        # Cân nặng

        self.txt_weight.delete(
            0,
            "end"
        )

        if values[6] is not None:

            self.txt_weight.insert(
                0,
                values[6]
            )

        # Khách hàng

        customer_name = values[7]

        for customer in self.customer_data:

            if str(customer["name"]) == str(customer_name):

                self.cbo_customer.set(
                    customer["display"]
                )

                break

        # Số điện thoại

        self.txt_phone.delete(
            0,
            "end"
        )

        if values[8] is not None:

            self.txt_phone.insert(
                0,
                values[8]
            )

        # Ghi chú

        self.txt_note.delete(
            0,
            "end"
        )

        if values[9] is not None:

            self.txt_note.insert(
                0,
                values[9]
            )

    # THÊM THÚ CƯNG

    def add_pet(self):

        pet_name = self.txt_pet_name.get().strip()

        pet_type = self.cbo_pet_type.get().strip()

        breed = self.txt_breed.get().strip()

        gender = self.cbo_gender.get().strip()

        age = self.txt_age.get().strip()

        weight = self.txt_weight.get().strip()

        phone = self.txt_phone.get().strip()

        note = self.txt_note.get().strip()

        customer_id = self.get_customer_id()

        # Kiểm tra tên

        if pet_name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên thú cưng."
            )

            return

        # Kiểm tra khách hàng

        if customer_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng."
            )

            return

        # Kiểm tra tuổi

        try:

            if age == "":

                age_value = None

            else:

                age_value = int(
                    age
                )

                if age_value < 0:

                    messagebox.showwarning(
                        "Thông báo",
                        "Tuổi không được nhỏ hơn 0."
                    )

                    return

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Tuổi phải là số nguyên."
            )

            return

        # Kiểm tra cân nặng

        try:

            if weight == "":

                weight_value = None

            else:

                weight_value = float(
                    weight
                )

                if weight_value < 0:

                    messagebox.showwarning(
                        "Thông báo",
                        "Cân nặng không được nhỏ hơn 0."
                    )

                    return

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Cân nặng phải là số."
            )

            return

        # Thêm vào SQL Server

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                INSERT INTO tbPet
                (
                    PetName,
                    PetType,
                    Breed,
                    Gender,
                    Age,
                    Weight,
                    CustomerID,
                    Phone,
                    Note
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(
                sql,
                (
                    pet_name,
                    pet_type,
                    breed,
                    gender,
                    age_value,
                    weight_value,
                    customer_id,
                    phone,
                    note
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Thêm thú cưng thành công."
            )

            self.clear_form()

            self.load_pets()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể thêm thú cưng.\n\n"
                + str(e)
            )

    # SỬA THÚ CƯNG

    def update_pet(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thú cưng cần sửa."
            )

            return

        pet_name = self.txt_pet_name.get().strip()

        pet_type = self.cbo_pet_type.get().strip()

        breed = self.txt_breed.get().strip()

        gender = self.cbo_gender.get().strip()

        age = self.txt_age.get().strip()

        weight = self.txt_weight.get().strip()

        phone = self.txt_phone.get().strip()

        note = self.txt_note.get().strip()

        customer_id = self.get_customer_id()

        if pet_name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên thú cưng."
            )

            return

        if customer_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng."
            )

            return

        # Kiểm tra tuổi

        try:

            if age == "":

                age_value = None

            else:

                age_value = int(
                    age
                )

                if age_value < 0:

                    messagebox.showwarning(
                        "Thông báo",
                        "Tuổi không được nhỏ hơn 0."
                    )

                    return

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Tuổi phải là số nguyên."
            )

            return

        # Kiểm tra cân nặng

        try:

            if weight == "":

                weight_value = None

            else:

                weight_value = float(
                    weight
                )

                if weight_value < 0:

                    messagebox.showwarning(
                        "Thông báo",
                        "Cân nặng không được nhỏ hơn 0."
                    )

                    return

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Cân nặng phải là số."
            )

            return

        # UPDATE

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                UPDATE tbPet
                SET
                    PetName = ?,
                    PetType = ?,
                    Breed = ?,
                    Gender = ?,
                    Age = ?,
                    Weight = ?,
                    CustomerID = ?,
                    Phone = ?,
                    Note = ?
                WHERE PetID = ?
            """

            cursor.execute(
                sql,
                (
                    pet_name,
                    pet_type,
                    breed,
                    gender,
                    age_value,
                    weight_value,
                    customer_id,
                    phone,
                    note,
                    self.selected_id
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật thú cưng thành công."
            )

            self.clear_form()

            self.load_pets()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật thú cưng.\n\n"
                + str(e)
            )

    # XÓA THÚ CƯNG

    def delete_pet(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thú cưng cần xóa."
            )

            return

        answer = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa thú cưng này không?"
        )

        if answer is False:

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                DELETE FROM tbPet
                WHERE PetID = ?
            """

            cursor.execute(
                sql,
                (
                    self.selected_id,
                )
            )

            connection.commit()

            cursor.close()

            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Xóa thú cưng thành công."
            )

            self.clear_form()

            self.load_pets()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa thú cưng.\n\n"
                + str(e)
            )

    # TÌM KIẾM

    def search_pet(self):

        keyword = self.txt_search.get().strip()

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT
                    p.PetID,
                    p.PetName,
                    p.PetType,
                    p.Breed,
                    p.Gender,
                    p.Age,
                    p.Weight,
                    c.name,
                    p.Phone,
                    p.Note
                FROM tbPet p
                LEFT JOIN tbCustomer c
                    ON p.CustomerID = c.id
                WHERE p.PetName LIKE ?
                   OR p.PetType LIKE ?
                   OR p.Breed LIKE ?
                   OR c.name LIKE ?
                   OR p.Phone LIKE ?
                ORDER BY p.PetID
            """

            search_value = (
                "%"
                + keyword
                + "%"
            )

            cursor.execute(
                sql,
                (
                    search_value,
                    search_value,
                    search_value,
                    search_value,
                    search_value
                )
            )

            rows = cursor.fetchall()

            for item in self.tree.get_children():

                self.tree.delete(
                    item
                )

            for row in rows:

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
                        row[6],
                        row[7],
                        row[8],
                        row[9]
                    )
                )

            cursor.close()

            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tìm kiếm thú cưng.\n\n"
                + str(e)
            )

    # TỰ ĐỘNG HIỂN THỊ SỐ ĐIỆN THOẠI KHI CHỌN KHÁCH HÀNG

    def customer_selected(self, selected_value=None):
        # Lấy khách hàng đang được chọn trong Combobox
        selected_customer = self.cbo_customer.get().strip()

        # Xóa số điện thoại cũ
        self.txt_phone.configure(state="normal")
        self.txt_phone.delete(0, "end")

        # Tìm khách hàng trong danh sách đã tải
        for customer in self.customer_data:
            if customer["display"] == selected_customer:
                phone = customer["phone"]

                if phone is not None:
                    self.txt_phone.insert(0, str(phone))

                return

    # LÀM MỚI

    def clear_form(self):

        self.selected_id = 0

        self.lbl_id.configure(
            text="Tự động"
        )

        self.txt_pet_name.delete(
            0,
            "end"
        )

        self.txt_breed.delete(
            0,
            "end"
        )

        self.txt_age.delete(
            0,
            "end"
        )

        self.txt_weight.delete(
            0,
            "end"
        )

        self.txt_phone.delete(
            0,
            "end"
        )

        self.txt_note.delete(
            0,
            "end"
        )

        self.cbo_pet_type.set(
            "Chó"
        )

        self.cbo_gender.set(
            "Đực"
        )

        self.txt_note.delete(
            0,
            "end"
        )

        if len(self.customer_data) > 0:

            self.cbo_customer.set(
                self.customer_data[0]["display"]
            )

        else:

            self.cbo_customer.set(
                "Chưa có khách hàng"
            )

        self.txt_search.delete(
            0,
            "end"
        )

        for item in self.tree.selection():

            self.tree.selection_remove(
                item
            )

        self.load_pets()