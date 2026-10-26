import datetime

import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import datetime

from database.database import connect_database


class BoardingForm:

    def __init__(self, parent):

        self.parent = parent

        self.selected_id = 0

        self.pet_data = []
        self.customer_data = []

        self.create_interface()
        self.start_boarding_reminder()
        self.load_pets()
        self.load_customers()
        self.load_boarding()

    # GIAO DIỆN

    def create_interface(self):

        # ======================================
        # MÀU SẮC GIAO DIỆN
        # ======================================

        bg_color = "#F1F2F7"
        card_color = "#FFFFFF"
        text_color = "#202044"
        purple_color = "#6500F5"
        hover_color = "#4D00C4"
        border_color = "#E5E7F0"
        primary_color = "#6500F5"
        muted_color = "#85859B"
        danger_color = "#E5484D"
        danger_hover = "#C92A32"

        self.parent.configure(fg_color=bg_color)

        # ======================================
        # TIÊU ĐỀ
        # ======================================

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
            text="Quản lý gửi thú cưng",
            font=("Arial", 27, "bold"),
            text_color=text_color
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            header_frame,
            text="PET BOARDING  /  QUẢN LÝ LƯU TRÚ",
            font=("Arial", 11),
            text_color="#85859B"
        ).pack(
            side="right",
            padx=5
        )

        # ======================================
        # KHUNG NHẬP THÔNG TIN
        # ======================================

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
            pady=8
        )

        ctk.CTkLabel(
            input_frame,
            text="Thông tin gửi thú cưng",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=18,
            pady=(15, 8),
            sticky="w"
        )

        # Các cột co giãn theo kích thước cửa sổ
        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # ======================================
        # THÚ CƯNG
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Thú cưng:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=1,
            column=0,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.cbo_pet = ctk.CTkComboBox(
            input_frame,
            width=230,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color
        )
        self.cbo_pet.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # KHÁCH HÀNG
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Khách hàng:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=1,
            column=2,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.cbo_customer = ctk.CTkComboBox(
            input_frame,
            width=230,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color
        )
        self.cbo_customer.grid(
            row=1,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )


        # Khi chọn thú cưng, tự động chọn chủ nuôi
        self.cbo_pet.configure(
            command=self.on_pet_selected
        )

        # Khi chọn khách hàng, tự động chọn thú cưng
        self.cbo_customer.configure(
            command=self.on_customer_selected
        )

        # ======================================
        # NGÀY GỬI
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Ngày gửi:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=2,
            column=0,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.txt_checkin_date = ctk.CTkEntry(
            input_frame,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="YYYY-MM-DD"
        )
        self.txt_checkin_date.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # GIỜ GỬI
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Giờ gửi:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=2,
            column=2,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.txt_checkin_time = ctk.CTkEntry(
            input_frame,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="HH:MM"
        )
        self.txt_checkin_time.grid(
            row=2,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # NGÀY NHẬN DỰ KIẾN
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Ngày nhận dự kiến:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=3,
            column=0,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.txt_expected_date = ctk.CTkEntry(
            input_frame,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="YYYY-MM-DD"
        )
        self.txt_expected_date.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # GIỜ NHẬN DỰ KIẾN
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Giờ nhận dự kiến:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=3,
            column=2,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.txt_expected_time = ctk.CTkEntry(
            input_frame,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="HH:MM"
        )
        self.txt_expected_time.grid(
            row=3,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # KHU VỰC
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Khu vực:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=4,
            column=0,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.txt_area = ctk.CTkEntry(
            input_frame,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Ví dụ: Khu A"
        )
        self.txt_area.grid(
            row=4,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # TRẠNG THÁI
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Trạng thái:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=4,
            column=2,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.cbo_status = ctk.CTkComboBox(
            input_frame,
            values=[
                "Đang gửi",
                "Đã trả"
            ],
            width=230,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color
        )
        self.cbo_status.grid(
            row=4,
            column=3,
            padx=10,
            pady=8,
            sticky="ew"
        )
        self.cbo_status.set("Đang gửi")

        # ======================================
        # GHI CHÚ
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Ghi chú:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=5,
            column=0,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.txt_note = ctk.CTkEntry(
            input_frame,
            height=34,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color="#000000",
            placeholder_text="Nhập ghi chú..."
        )
        self.txt_note.grid(
            row=5,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # ======================================
        # ID
        # ======================================

        ctk.CTkLabel(
            input_frame,
            text="Mã gửi:",
            text_color=text_color,
            font=("Arial", 12)
        ).grid(
            row=5,
            column=2,
            padx=18,
            pady=8,
            sticky="w"
        )

        self.lbl_id = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            text_color=purple_color,
            font=("Arial", 13, "bold")
        )
        self.lbl_id.grid(
            row=5,
            column=3,
            padx=10,
            pady=8,
            sticky="w"
        )

        # Khoảng trống cuối khung
        ctk.CTkLabel(
            input_frame,
            text=" "
        ).grid(
            row=6,
            column=0,
            pady=3
        )

        # ======================================
        # THANH CHỨC NĂNG VÀ TÌM KIẾM
        # ======================================

        button_frame = ctk.CTkFrame(
            self.parent,
            fg_color=card_color,
            corner_radius=12
        )
        button_frame.pack(
            fill="x",
            padx=25,
            pady=7
        )

        # NÚT THÊM
        self.btn_add_boarding = ctk.CTkButton(
            button_frame,
            text="＋  Thêm",
            width=105,
            height=36,
            corner_radius=8,
            fg_color="#6500F5",
            hover_color="#4D00C4",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.add_boarding
        )
        self.btn_add_boarding.pack(
            side="left",
            padx=(12, 5),
            pady=10
        )

        # NÚT SỬA
        self.btn_update_boarding = ctk.CTkButton(
            button_frame,
            text="✎  Sửa",
            width=105,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color="#6500F5",
            font=("Arial", 12, "bold"),
            command=self.update_boarding
        )
        self.btn_update_boarding.pack(
            side="left",
            padx=5,
            pady=10
        )

        # NÚT XÓA
        self.btn_delete_boarding = ctk.CTkButton(
            button_frame,
            text="✕  Xóa",
            width=105,
            height=36,
            corner_radius=8,
            fg_color="#E5484D",
            hover_color="#C92A32",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_boarding
        )
        self.btn_delete_boarding.pack(
            side="left",
            padx=5,
            pady=10
        )

        # NÚT LÀM MỚI
        self.btn_clear_boarding = ctk.CTkButton(
            button_frame,
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
        self.btn_clear_boarding.pack(
            side="left",
            padx=5,
            pady=10
        )

        # ĐƯỜNG PHÂN CÁCH
        ctk.CTkFrame(
            button_frame,
            width=1,
            height=28,
            fg_color="#E5E7F0"
        ).pack(
            side="left",
            padx=12,
            pady=10
        )

        # NHÃN TÌM KIẾM
        ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            text_color="#202044",
            font=("Arial", 12)
        ).pack(
            side="left",
            padx=(5, 5)
        )

        # Ô NHẬP TỪ KHÓA
        self.txt_search = ctk.CTkEntry(
            button_frame,
            width=210,
            height=36,
            corner_radius=8,
            border_width=1,
            border_color="#E5E7F0",
            fg_color="#FFFFFF",
            text_color="#202044",
            placeholder_text="Tên thú cưng...",
            placeholder_text_color="#85859B",
            font=("Arial", 12)
        )
        self.txt_search.pack(
            side="left",
            padx=5,
            pady=10
        )

        # NÚT TÌM KIẾM
        self.btn_search_boarding = ctk.CTkButton(
            button_frame,
            text="Tìm",
            width=70,
            height=36,
            corner_radius=8,
            fg_color="#6500F5",
            hover_color="#4D00C4",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.search_boarding
        )
        self.btn_search_boarding.pack(
            side="left",
            padx=(5, 12),
            pady=10
        )

        # ======================================
        # KHUNG BẢNG DỮ LIỆU
        # ======================================

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
            text="Danh sách gửi thú cưng",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).pack(
            anchor="w",
            padx=16,
            pady=(14, 8)
        )

        # ======================================
        # TREEVIEW
        # ======================================

        tree_style = ttk.Style()

        tree_style.configure(
            "Boarding.Treeview",
            background="#FFFFFF",
            foreground="#202044",
            fieldbackground="#FFFFFF",
            rowheight=32,
            font=("Arial", 10)
        )

        tree_style.configure(
            "Boarding.Treeview.Heading",
            background="#F0EBFF",
            foreground="#202044",
            font=("Arial", 10, "bold"),
            padding=(6, 9)
        )

        tree_style.map(
            "Boarding.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", "#202044")]
        )

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
            "pet",
            "customer",
            "checkin_date",
            "checkin_time",
            "expected_date",
            "expected_time",
            "area",
            "status",
            "note"
        )

        self.tree = ttk.Treeview(
            tree_container,
            columns=columns,
            show="headings",
            style="Boarding.Treeview"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("pet", text="Thú cưng")
        self.tree.heading("customer", text="Khách hàng")
        self.tree.heading("checkin_date", text="Ngày gửi")
        self.tree.heading("checkin_time", text="Giờ gửi")
        self.tree.heading("expected_date", text="Ngày nhận dự kiến")
        self.tree.heading("expected_time", text="Giờ nhận dự kiến")
        self.tree.heading("area", text="Khu vực")
        self.tree.heading("status", text="Trạng thái")
        self.tree.heading("note", text="Ghi chú")

        self.tree.column("id", width=55, minwidth=50, anchor="center")
        self.tree.column("pet", width=130, minwidth=100)
        self.tree.column("customer", width=145, minwidth=110)
        self.tree.column("checkin_date", width=110, minwidth=95, anchor="center")
        self.tree.column("checkin_time", width=90, minwidth=75, anchor="center")
        self.tree.column("expected_date", width=135, minwidth=110, anchor="center")
        self.tree.column("expected_time", width=135, minwidth=110, anchor="center")
        self.tree.column("area", width=100, minwidth=80, anchor="center")
        self.tree.column("status", width=105, minwidth=90, anchor="center")
        self.tree.column("note", width=180, minwidth=120)

        vertical_scrollbar = ttk.Scrollbar(
            tree_container,
            orient="vertical",
            command=self.tree.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            tree_container,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)

        self.tree.grid(
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

        # ======================================
        # CHỌN DÒNG TRONG BẢNG
        # ======================================

        self.tree.bind(
            "<ButtonRelease-1>",
            self.select_boarding
        )

    # LOAD THÚ CƯNG

    # LOAD THÚ CƯNG VÀ CHỦ NUÔI

    def load_pets(self):

        connection = None
        cursor = None

        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT PetID, PetName, PetType, CustomerID
                FROM tbPet
                ORDER BY PetID
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            self.pet_data = []
            values = []

            for row in rows:
                display = str(row[0]) + " - " + str(row[1])

                self.pet_data.append({
                    "id": row[0],
                    "name": row[1],
                    "type": row[2],
                    "customer_id": row[3],
                    "display": display
                })

                values.append(display)

            if len(values) > 0:
                self.cbo_pet.configure(values=values)
                self.cbo_pet.set(values[0])
            else:
                self.cbo_pet.configure(values=[])
                self.cbo_pet.set("Chưa có thú cưng")

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách thú cưng.\n\n" + str(e)
            )

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

    # LOAD KHÁCH HÀNG

    # LOAD KHÁCH HÀNG

    def load_customers(self):

        connection = None
        cursor = None

        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT id, name, phone
                FROM tbCustomer
                ORDER BY id
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            self.customer_data = []
            values = []

            for row in rows:
                display = str(row[0]) + " - " + str(row[1])

                self.customer_data.append({
                    "id": row[0],
                    "name": row[1],
                    "phone": row[2],
                    "display": display
                })

                values.append(display)

            if len(values) > 0:
                self.cbo_customer.configure(values=values)
                self.cbo_customer.set(values[0])
            else:
                self.cbo_customer.configure(values=[])
                self.cbo_customer.set("Chưa có khách hàng")

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách khách hàng.\n\n" + str(e)
            )

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

    # CHỌN THÚ CƯNG -> TỰ ĐỘNG CHỌN CHỦ NUÔI

    def on_pet_selected(self, selected_value=None):

        selected_pet = self.cbo_pet.get()

        for pet in self.pet_data:

            if pet["display"] == selected_pet:

                customer_id = pet["customer_id"]

                # Tìm chủ nuôi của thú cưng
                for customer in self.customer_data:

                    if customer["id"] == customer_id:
                        self.cbo_customer.set(
                            customer["display"]
                        )

                        return

                # Thú cưng chưa có chủ nuôi hợp lệ
                self.cbo_customer.set("Chưa xác định chủ nuôi")
                return

    # CHỌN KHÁCH HÀNG -> TỰ ĐỘNG CHỌN THÚ CƯNG

    def on_customer_selected(self, selected_value=None):

        selected_customer = self.cbo_customer.get()
        customer_id = None

        # Lấy ID khách hàng đang chọn
        for customer in self.customer_data:

            if customer["display"] == selected_customer:
                customer_id = customer["id"]
                break

        if customer_id is None:
            return

        # Tìm thú cưng đầu tiên thuộc khách hàng
        for pet in self.pet_data:

            if pet["customer_id"] == customer_id:
                self.cbo_pet.set(pet["display"])
                return

        # Khách hàng chưa có thú cưng
        self.cbo_pet.set("Chưa có thú cưng")

    # LẤY PET ID

    def get_pet_id(self):

        selected = self.cbo_pet.get()

        for pet in self.pet_data:

            if pet["display"] == selected:

                return pet["id"]

        return None

    # LẤY CUSTOMER ID

    def get_customer_id(self):

        selected = self.cbo_customer.get()

        for customer in self.customer_data:

            if customer["display"] == selected:

                return customer["id"]

        return None

    def start_boarding_reminder(self):
        self.notified_boardings = set()
        self.check_boarding_reminder()

    def check_boarding_reminder(self):
        connection = None
        cursor = None

        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT
                    b.BoardingID,
                    p.PetName,
                    b.ExpectedDate,
                    b.ExpectedTime
                FROM tbPetBoarding b
                INNER JOIN tbPet p
                    ON b.PetID = p.PetID
                WHERE b.Status = N'Đang gửi'
                  AND b.ExpectedDate IS NOT NULL
                  AND b.ExpectedTime IS NOT NULL
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            now = datetime.now()

            for row in rows:
                boarding_id = row[0]
                pet_name = row[1]
                expected_date = row[2]
                expected_time = row[3]

                expected_datetime = datetime.combine(
                    expected_date,
                    expected_time
                )

                if (
                        now >= expected_datetime
                        and boarding_id not in self.notified_boardings
                ):
                    self.notified_boardings.add(boarding_id)

                    messagebox.showwarning(
                        "Nhắc giờ trả thú cưng",
                        "Thú cưng: " + str(pet_name)
                        + "\nMã lưu trú: " + str(boarding_id)
                        + "\nĐã đến hoặc quá giờ hẹn trả."
                        + "\nVui lòng kiểm tra và liên hệ khách hàng."
                    )

        except Exception as e:
            print("Lỗi kiểm tra giờ trả thú cưng:", e)

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

        self.parent.after(
            60000,
            self.check_boarding_reminder
        )

    # KIỂM TRA NGÀY

    def validate_dates(self):

        checkin_date = self.txt_checkin_date.get().strip()
        expected_date = self.txt_expected_date.get().strip()

        if checkin_date == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập ngày gửi."
            )
            return False

        if expected_date == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập ngày nhận dự kiến."
            )
            return False

        try:
            datetime.datetime.strptime(checkin_date, "%Y-%m-%d")
            datetime.datetime.strptime(expected_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning(
                "Thông báo",
                "Ngày phải có định dạng YYYY-MM-DD."
            )
            return False

        if expected_date < checkin_date:
            messagebox.showwarning(
                "Thông báo",
                "Ngày nhận dự kiến không được trước ngày gửi."
            )
            return False

        return True

    # THÊM

    def add_boarding(self):

        pet_id = self.get_pet_id()
        customer_id = self.get_customer_id()

        checkin_date = self.txt_checkin_date.get().strip()
        checkin_time = self.txt_checkin_time.get().strip()

        expected_date = self.txt_expected_date.get().strip()
        expected_time = self.txt_expected_time.get().strip()

        area = self.txt_area.get().strip()
        status = self.cbo_status.get().strip()
        note = self.txt_note.get().strip()

        if pet_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thú cưng."
            )

            return

        if customer_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng."
            )

            return

        if self.validate_dates() is False:
            return

        if checkin_time == "":
            checkin_time = None

        if expected_time == "":
            expected_time = None

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                INSERT INTO tbPetBoarding
                (
                    PetID,
                    CustomerID,
                    CheckInDate,
                    CheckInTime,
                    ExpectedDate,
                    ExpectedTime,
                    Area,
                    Status,
                    Note
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            cursor.execute(
                sql,
                (
                    pet_id,
                    customer_id,
                    checkin_date,
                    checkin_time,
                    expected_date,
                    expected_time,
                    area,
                    status,
                    note
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Thêm thông tin gửi thú cưng thành công."
            )

            self.clear_form()
            self.load_boarding()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể thêm thông tin gửi thú cưng.\n\n"
                + str(e)
            )

    # LOAD DANH SÁCH

    def load_boarding(self):

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT
                    b.BoardingID,
                    p.PetName,
                    c.name AS CustomerName,
                    b.CheckInDate,
                    b.CheckInTime,
                    b.ExpectedDate,
                    b.ExpectedTime,
                    b.Area,
                    b.Status,
                    b.Note
                FROM tbPetBoarding b
                INNER JOIN tbPet p
                    ON b.PetID = p.PetID
                LEFT JOIN tbCustomer c
                    ON b.CustomerID = c.id
                ORDER BY b.BoardingID DESC
            """

            cursor.execute(sql)

            rows = cursor.fetchall()

            for item in self.tree.get_children():

                self.tree.delete(item)

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
                "Không thể tải danh sách gửi thú cưng.\n\n"
                + str(e)
            )

    # CHỌN DỮ LIỆU

    def select_boarding(self, event):

        selected = self.tree.selection()

        if len(selected) == 0:

            return

        item = self.tree.item(
            selected[0]
        )

        values = item["values"]

        self.selected_id = values[0]

        self.lbl_id.configure(
            text=str(self.selected_id)
        )

        # =========================
        # THÚ CƯNG
        # =========================

        pet_name = values[1]

        for pet in self.pet_data:

            if str(pet["name"]) == str(pet_name):

                self.cbo_pet.set(
                    pet["display"]
                )

                break

        # =========================
        # KHÁCH HÀNG
        # =========================

        customer_name = values[2]

        for customer in self.customer_data:

            if str(customer["name"]) == str(customer_name):

                self.cbo_customer.set(
                    customer["display"]
                )

                break

        # =========================
        # NGÀY GỬI
        # =========================

        self.txt_checkin_date.delete(
            0,
            "end"
        )

        if values[3] is not None:

            self.txt_checkin_date.insert(
                0,
                str(values[3])
            )

        # =========================
        # GIỜ GỬI
        # =========================

        self.txt_checkin_time.delete(
            0,
            "end"
        )

        if values[4] is not None:

            self.txt_checkin_time.insert(
                0,
                str(values[4])
            )

        # =========================
        # NGÀY NHẬN
        # =========================

        self.txt_expected_date.delete(
            0,
            "end"
        )

        if values[5] is not None:

            self.txt_expected_date.insert(
                0,
                str(values[5])
            )

        # =========================
        # GIỜ NHẬN
        # =========================

        self.txt_expected_time.delete(
            0,
            "end"
        )

        if values[6] is not None:

            self.txt_expected_time.insert(
                0,
                str(values[6])
            )

        # =========================
        # KHU VỰC
        # =========================

        self.txt_area.delete(
            0,
            "end"
        )

        if values[7] is not None:

            self.txt_area.insert(
                0,
                str(values[7])
            )

        # =========================
        # TRẠNG THÁI
        # =========================

        if values[8] is not None:

            self.cbo_status.set(
                str(values[8])
            )

        # =========================
        # GHI CHÚ
        # =========================

        self.txt_note.delete(
            0,
            "end"
        )

        if values[9] is not None:

            self.txt_note.insert(
                0,
                str(values[9])
            )

    # SỬA

    def update_boarding(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thông tin cần sửa."
            )

            return

        pet_id = self.get_pet_id()
        customer_id = self.get_customer_id()

        checkin_date = self.txt_checkin_date.get().strip()
        checkin_time = self.txt_checkin_time.get().strip()

        expected_date = self.txt_expected_date.get().strip()
        expected_time = self.txt_expected_time.get().strip()

        area = self.txt_area.get().strip()
        status = self.cbo_status.get().strip()
        note = self.txt_note.get().strip()

        if pet_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thú cưng."
            )

            return

        if customer_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn khách hàng."
            )

            return

        if self.validate_dates() is False:
            return

        if checkin_time == "":
            checkin_time = None

        if expected_time == "":
            expected_time = None

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                UPDATE tbPetBoarding
                SET PetID = ?,
                    CustomerID = ?,
                    CheckInDate = ?,
                    CheckInTime = ?,
                    ExpectedDate = ?,
                    ExpectedTime = ?,
                    Area = ?,
                    Status = ?,
                    Note = ?
                WHERE BoardingID = ?
            """

            cursor.execute(
                sql,
                (
                    pet_id,
                    customer_id,
                    checkin_date,
                    checkin_time,
                    expected_date,
                    expected_time,
                    area,
                    status,
                    note,
                    self.selected_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật thông tin thành công."
            )

            self.clear_form()
            self.load_boarding()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật thông tin.\n\n"
                + str(e)
            )

    # XÓA

    def delete_boarding(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thông tin cần xóa."
            )

            return

        answer = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa thông tin này không?"
        )

        if answer is False:
            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                DELETE FROM tbPetBoarding
                WHERE BoardingID = ?
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
                "Xóa thông tin thành công."
            )

            self.clear_form()
            self.load_boarding()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa thông tin.\n\n"
                + str(e)
            )

    # TÌM KIẾM

    def search_boarding(self):

        keyword = self.txt_search.get().strip()

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT
                    b.BoardingID,
                    p.PetName,
                    c.name AS CustomerName,
                    b.CheckInDate,
                    b.CheckInTime,
                    b.ExpectedDate,
                    b.ExpectedTime,
                    b.Area,
                    b.Status,
                    b.Note
                FROM tbPetBoarding b
                INNER JOIN tbPet p
                    ON b.PetID = p.PetID
                LEFT JOIN tbCustomer c
                    ON b.CustomerID = c.id
                WHERE p.PetName LIKE ?
                   OR c.name LIKE ?
                   OR b.Status LIKE ?
                   OR b.Area LIKE ?
                ORDER BY b.BoardingID DESC
            """

            search_value = "%" + keyword + "%"

            cursor.execute(
                sql,
                (
                    search_value,
                    search_value,
                    search_value,
                    search_value
                )
            )

            rows = cursor.fetchall()

            for item in self.tree.get_children():

                self.tree.delete(item)

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
                "Không thể tìm kiếm.\n\n"
                + str(e)
            )

    # LÀM MỚI

    def clear_form(self):

        self.selected_id = 0

        self.lbl_id.configure(
            text="Tự động"
        )

        self.txt_checkin_date.delete(
            0,
            "end"
        )

        self.txt_checkin_time.delete(
            0,
            "end"
        )

        self.txt_expected_date.delete(
            0,
            "end"
        )

        self.txt_expected_time.delete(
            0,
            "end"
        )

        self.txt_area.delete(
            0,
            "end"
        )

        self.txt_note.delete(
            0,
            "end"
        )

        self.txt_search.delete(
            0,
            "end"
        )

        self.cbo_status.set(
            "Đang gửi"
        )

        if len(self.pet_data) > 0:

            self.cbo_pet.set(
                self.pet_data[0]["display"]
            )

        if len(self.customer_data) > 0:

            self.cbo_customer.set(
                self.customer_data[0]["display"]
            )

        for item in self.tree.selection():

            self.tree.selection_remove(item)

        self.load_boarding()