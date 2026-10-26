import customtkinter as ctk
from tkinter import ttk, messagebox
from models.session import Session

from database.database import connect_database


class PetCareForm:

    def __init__(self, parent):

        self.parent = parent

        # =========================
        # KHỞI TẠO BIẾN
        # =========================

        self.selected_id = 0
        self.service_selected_id = 0

        self.pet_data = []
        self.service_data = []
        self.staff_data = []

        # =========================
        # CẤU HÌNH MÀU SẮC
        # =========================

        self.bg_color = "#F1F2F7"
        self.card_color = "#FFFFFF"
        self.primary_color = "#6500F5"
        self.hover_color = "#4D00C4"
        self.text_color = "#202044"
        self.muted_color = "#85859B"
        self.border_color = "#E5E7F0"

        self.parent.configure(
            fg_color=self.bg_color
        )

        # =========================
        # TIÊU ĐỀ CHÍNH
        # =========================

        header_frame = ctk.CTkFrame(
            self.parent,
            fg_color=self.bg_color,
            corner_radius=0
        )

        header_frame.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        title = ctk.CTkLabel(
            header_frame,
            text="QUẢN LÝ CHĂM SÓC THÚ CƯNG",
            font=("Arial", 25, "bold"),
            text_color=self.text_color
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Theo dõi lịch sử chăm sóc và quản lý dịch vụ dành cho thú cưng",
            font=("Arial", 12),
            text_color=self.muted_color
        )

        subtitle.pack(
            anchor="w",
            pady=(5, 0)
        )

        # =========================
        # KHUNG CHỌN CHỨC NĂNG
        # =========================

        tab_frame = ctk.CTkFrame(
            self.parent,
            fg_color=self.card_color,
            corner_radius=12,
            border_width=1,
            border_color=self.border_color
        )

        tab_frame.pack(
            fill="x",
            padx=20,
            pady=(5, 12)
        )

        # Nút lịch sử chăm sóc
        self.btn_history = ctk.CTkButton(
            tab_frame,
            text="Lịch sử chăm sóc",
            width=180,
            height=40,
            corner_radius=8,
            fg_color=self.primary_color,
            hover_color=self.hover_color,
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.show_history
        )

        self.btn_history.pack(
            side="left",
            padx=(12, 6),
            pady=10
        )

        # Nút quản lý dịch vụ
        self.btn_service = ctk.CTkButton(
            tab_frame,
            text="Quản lý dịch vụ",
            width=180,
            height=40,
            corner_radius=8,
            fg_color=self.primary_color,
            hover_color="#F0EBFF",
            text_color=self.text_color,
            border_width=1,
            border_color=self.border_color,
            font=("Arial", 12, "bold"),
            command=self.show_service
        )

        self.btn_service.pack(
            side="left",
            padx=6,
            pady=10
        )

        # =========================
        # TẠO HAI GIAO DIỆN
        # =========================

        self.create_history_frame()

        self.create_service_frame()

        # =========================
        # HIỂN THỊ MẶC ĐỊNH
        # =========================

        self.service_frame.pack_forget()

        # Đánh dấu tab đang được chọn
        self.btn_history.configure(
            fg_color=self.primary_color,
            hover_color=self.hover_color,
            text_color="#FFFFFF",
            border_width=0
        )

        self.btn_service.configure(
            fg_color="#FFFFFF",
            hover_color="#F0EBFF",
            text_color=self.text_color,
            border_width=1,
            border_color=self.border_color
        )

        # =========================
        # TẢI DỮ LIỆU
        # =========================

        self.load_pets()
        self.load_services()
        self.load_staff()
        self.load_history()

    # FRAME LỊCH SỬ CHĂM SÓC

    def create_history_frame(self):

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

        self.history_frame = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color,
            corner_radius=0
        )

        self.history_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # =========================
        # TIÊU ĐỀ
        # =========================

        header_frame = ctk.CTkFrame(
            self.history_frame,
            fg_color=bg_color,
            corner_radius=0
        )

        header_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        ctk.CTkLabel(
            header_frame,
            text="LỊCH SỬ CHĂM SÓC THÚ CƯNG",
            font=("Arial", 24, "bold"),
            text_color=text_color
        ).pack(anchor="w")

        ctk.CTkLabel(
            header_frame,
            text="Theo dõi các dịch vụ đã thực hiện cho thú cưng",
            font=("Arial", 12),
            text_color=muted_color
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # =========================
        # KHUNG NHẬP THÔNG TIN
        # =========================

        input_frame = ctk.CTkFrame(
            self.history_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        input_frame.pack(
            fill="x",
            pady=(0, 12)
        )

        ctk.CTkLabel(
            input_frame,
            text="THÔNG TIN LỊCH SỬ CHĂM SÓC",
            font=("Arial", 15, "bold"),
            text_color=text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(16, 10),
            sticky="w"
        )

        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # Thú cưng
        ctk.CTkLabel(
            input_frame,
            text="Thú cưng:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.cbo_pet = ctk.CTkComboBox(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color
        )

        self.cbo_pet.grid(
            row=1,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Dịch vụ
        ctk.CTkLabel(
            input_frame,
            text="Dịch vụ:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.cbo_service = ctk.CTkComboBox(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color
        )

        self.cbo_service.grid(
            row=1,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Ngày thực hiện
        ctk.CTkLabel(
            input_frame,
            text="Ngày thực hiện:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_date = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="YYYY-MM-DD"
        )

        self.txt_date.grid(
            row=2,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Nhân viên
        ctk.CTkLabel(
            input_frame,
            text="Nhân viên:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.txt_employee = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="Nhập tên nhân viên"
        )

        self.txt_employee.grid(
            row=2,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Ghi chú
        ctk.CTkLabel(
            input_frame,
            text="Ghi chú:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_history_note = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="Nhập ghi chú"
        )

        self.txt_history_note.grid(
            row=3,
            column=1,
            columnspan=3,
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
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.lbl_history_id = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            font=("Arial", 13, "bold"),
            text_color=primary_color
        )

        self.lbl_history_id.grid(
            row=4,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

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
            self.history_frame,
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
        self.btn_add_history = ctk.CTkButton(
            action_frame,
            text="＋ Thêm",
            width=100,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.add_history
        )

        self.btn_add_history.pack(
            side="left",
            padx=4
        )

        # NÚT SỬA
        self.btn_update_history = ctk.CTkButton(
            action_frame,
            text="✎ Sửa",
            width=100,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color=primary_color,
            font=("Arial", 12, "bold"),
            command=self.update_history
        )

        self.btn_update_history.pack(
            side="left",
            padx=4
        )

        # NÚT XÓA
        self.btn_delete_history = ctk.CTkButton(
            action_frame,
            text="✕ Xóa",
            width=100,
            height=36,
            corner_radius=8,
            fg_color="#E5484D",
            hover_color="#C92A32",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_history
        )

        self.btn_delete_history.pack(
            side="left",
            padx=4
        )

        # NÚT LÀM MỚI
        self.btn_clear_history = ctk.CTkButton(
            action_frame,
            text="↻ Làm mới",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E9ECF3",
            hover_color="#DDE1EB",
            text_color=text_color,
            font=("Arial", 12, "bold"),
            command=self.clear_history
        )

        self.btn_clear_history.pack(
            side="left",
            padx=4
        )

        # ĐƯỜNG PHÂN CÁCH
        ctk.CTkFrame(
            action_frame,
            width=1,
            height=30,
            fg_color=border_color
        ).pack(
            side="left",
            padx=10
        )

        # NHÃN TÌM KIẾM
        ctk.CTkLabel(
            action_frame,
            text="Tìm kiếm:",
            font=("Arial", 12, "bold"),
            text_color=text_color
        ).pack(
            side="left",
            padx=(0, 6)
        )

        # Ô TÌM KIẾM
        self.txt_history_search = ctk.CTkEntry(
            action_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="Tên thú cưng..."
        )

        self.txt_history_search.pack(
            side="left",
            fill="x",
            expand=True,
            padx=4
        )

        # NÚT TÌM
        self.btn_history_search = ctk.CTkButton(
            action_frame,
            text="Tìm",
            width=70,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.search_history
        )

        self.btn_history_search.pack(
            side="left",
            padx=4
        )

        # =========================
        # KHUNG BẢNG DỮ LIỆU
        # =========================

        table_frame = ctk.CTkFrame(
            self.history_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

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
            text="DANH SÁCH LỊCH SỬ CHĂM SÓC",
            font=("Arial", 15, "bold"),
            text_color=text_color
        ).pack(side="left")

        ctk.CTkLabel(
            table_header,
            text="Chọn một dòng để xem hoặc chỉnh sửa",
            font=("Arial", 11),
            text_color=muted_color
        ).pack(side="right")

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

        # Style bảng
        style = ttk.Style()

        style.configure(
            "History.Treeview",
            background=card_color,
            foreground=text_color,
            fieldbackground=card_color,
            rowheight=34,
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "History.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            padding=(8, 10),
            relief="flat"
        )

        style.map(
            "History.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        columns = (
            "id",
            "pet",
            "service",
            "price",
            "date",
            "employee",
            "note"
        )

        self.history_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            style="History.Treeview"
        )

        self.history_tree.heading("id", text="ID")
        self.history_tree.heading("pet", text="Thú cưng")
        self.history_tree.heading("service", text="Dịch vụ")
        self.history_tree.heading("price", text="Giá")
        self.history_tree.heading("date", text="Ngày thực hiện")
        self.history_tree.heading("employee", text="Nhân viên")
        self.history_tree.heading("note", text="Ghi chú")

        self.history_tree.column(
            "id",
            width=55,
            minwidth=45,
            anchor="center",
            stretch=False
        )

        self.history_tree.column(
            "pet",
            width=150,
            minwidth=110
        )

        self.history_tree.column(
            "service",
            width=180,
            minwidth=130
        )

        self.history_tree.column(
            "price",
            width=120,
            minwidth=100,
            anchor="e"
        )

        self.history_tree.column(
            "date",
            width=130,
            minwidth=110,
            anchor="center"
        )

        self.history_tree.column(
            "employee",
            width=150,
            minwidth=110
        )

        self.history_tree.column(
            "note",
            width=250,
            minwidth=150
        )

        scrollbar_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.history_tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            tree_frame,
            orient="horizontal",
            command=self.history_tree.xview
        )

        self.history_tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.history_tree.grid(
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

        self.history_tree.bind(
            "<ButtonRelease-1>",
            self.select_history
        )

    # FRAME QUẢN LÝ DỊCH VỤ

    def create_service_frame(self):

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

        self.service_frame = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color,
            corner_radius=0
        )

        self.service_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # =========================
        # TIÊU ĐỀ
        # =========================

        header_frame = ctk.CTkFrame(
            self.service_frame,
            fg_color=bg_color,
            corner_radius=0
        )

        header_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        ctk.CTkLabel(
            header_frame,
            text="QUẢN LÝ DỊCH VỤ",
            font=("Arial", 24, "bold"),
            text_color=text_color
        ).pack(anchor="w")

        ctk.CTkLabel(
            header_frame,
            text="Quản lý danh sách dịch vụ chăm sóc và giá dịch vụ",
            font=("Arial", 12),
            text_color=muted_color
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # =========================
        # KHUNG NHẬP THÔNG TIN
        # =========================

        input_frame = ctk.CTkFrame(
            self.service_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        input_frame.pack(
            fill="x",
            pady=(0, 12)
        )

        ctk.CTkLabel(
            input_frame,
            text="THÔNG TIN DỊCH VỤ",
            font=("Arial", 15, "bold"),
            text_color=text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(16, 10),
            sticky="w"
        )

        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # Tên dịch vụ
        ctk.CTkLabel(
            input_frame,
            text="Tên dịch vụ:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_service_name = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="Nhập tên dịch vụ"
        )

        self.txt_service_name.grid(
            row=1,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Giá dịch vụ
        ctk.CTkLabel(
            input_frame,
            text="Giá dịch vụ:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=2,
            padx=(10, 10),
            pady=8,
            sticky="w"
        )

        self.txt_service_price = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="Nhập giá dịch vụ"
        )

        self.txt_service_price.grid(
            row=1,
            column=3,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        # Mô tả
        ctk.CTkLabel(
            input_frame,
            text="Mô tả:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.txt_service_description = ctk.CTkEntry(
            input_frame,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFD",
            text_color="#000000",
            placeholder_text="Nhập mô tả dịch vụ"
        )

        self.txt_service_description.grid(
            row=2,
            column=1,
            columnspan=3,
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
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.lbl_service_id = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            font=("Arial", 13, "bold"),
            text_color=primary_color
        )

        self.lbl_service_id.grid(
            row=3,
            column=1,
            padx=(0, 20),
            pady=8,
            sticky="ew"
        )

        ctk.CTkLabel(
            input_frame,
            text="",
            height=5
        ).grid(
            row=4,
            column=0,
            columnspan=4
        )

        # =========================
        # KHUNG NÚT CHỨC NĂNG
        # =========================

        button_frame = ctk.CTkFrame(
            self.service_frame,
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
        ctk.CTkButton(
            action_frame,
            text="＋ Thêm",
            width=110,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.add_service
        ).pack(
            side="left",
            padx=4
        )

        # NÚT SỬA
        ctk.CTkButton(
            action_frame,
            text="✎ Sửa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color=primary_color,
            font=("Arial", 12, "bold"),
            command=self.update_service
        ).pack(
            side="left",
            padx=4
        )

        # NÚT XÓA
        ctk.CTkButton(
            action_frame,
            text="✕ Xóa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E5484D",
            hover_color="#C92A32",
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_service
        ).pack(
            side="left",
            padx=4
        )

        # NÚT LÀM MỚI
        ctk.CTkButton(
            action_frame,
            text="↻ Làm mới",
            width=120,
            height=36,
            corner_radius=8,
            fg_color="#E9ECF3",
            hover_color="#DDE1EB",
            text_color=text_color,
            font=("Arial", 12, "bold"),
            command=self.clear_service
        ).pack(
            side="left",
            padx=4
        )

        # =========================
        # KHUNG BẢNG DỊCH VỤ
        # =========================

        table_frame = ctk.CTkFrame(
            self.service_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

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
            text="DANH SÁCH DỊCH VỤ",
            font=("Arial", 15, "bold"),
            text_color=text_color
        ).pack(side="left")

        ctk.CTkLabel(
            table_header,
            text="Chọn một dòng để xem hoặc chỉnh sửa",
            font=("Arial", 11),
            text_color=muted_color
        ).pack(side="right")

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

        # Style bảng
        style = ttk.Style()

        style.configure(
            "Service.Treeview",
            background=card_color,
            foreground=text_color,
            fieldbackground=card_color,
            rowheight=35,
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "Service.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            padding=(8, 10),
            relief="flat"
        )

        style.map(
            "Service.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        columns = (
            "id",
            "name",
            "price",
            "description"
        )

        self.service_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            style="Service.Treeview"
        )

        self.service_tree.heading("id", text="ID")
        self.service_tree.heading("name", text="Tên dịch vụ")
        self.service_tree.heading("price", text="Giá")
        self.service_tree.heading("description", text="Mô tả")

        self.service_tree.column(
            "id",
            width=60,
            minwidth=50,
            anchor="center",
            stretch=False
        )

        self.service_tree.column(
            "name",
            width=250,
            minwidth=160
        )

        self.service_tree.column(
            "price",
            width=150,
            minwidth=120,
            anchor="e"
        )

        self.service_tree.column(
            "description",
            width=500,
            minwidth=200
        )

        scrollbar_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.service_tree.yview
        )

        scrollbar_x = ttk.Scrollbar(
            tree_frame,
            orient="horizontal",
            command=self.service_tree.xview
        )

        self.service_tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.service_tree.grid(
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

        self.service_tree.bind(
            "<ButtonRelease-1>",
            self.select_service
        )

    # HIỂN THỊ LỊCH SỬ

    def show_history(self):

        self.service_frame.pack_forget()

        self.history_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.load_history()

    # HIỂN THỊ DỊCH VỤ

    def show_service(self):

        self.history_frame.pack_forget()

        self.service_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.load_services()

    # LOAD THÚ CƯNG

    def load_pets(self):

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT PetID, PetName, PetType
                FROM tbPet
                ORDER BY PetID
            """

            cursor.execute(sql)

            rows = cursor.fetchall()

            self.pet_data = []

            values = []

            for row in rows:

                display = (
                    str(row[0])
                    + " - "
                    + str(row[1])
                )

                self.pet_data.append(
                    {
                        "id": row[0],
                        "name": row[1],
                        "type": row[2],
                        "display": display
                    }
                )

                values.append(display)

            if len(values) > 0:

                self.cbo_pet.configure(
                    values=values
                )

                self.cbo_pet.set(
                    values[0]
                )

            else:

                self.cbo_pet.configure(
                    values=["Chưa có thú cưng"]
                )

                self.cbo_pet.set(
                    "Chưa có thú cưng"
                )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải thú cưng.\n"
                + str(e)
            )

    # LẤY PET ID

    def get_pet_id(self):

        selected = self.cbo_pet.get()

        for pet in self.pet_data:

            if pet["display"] == selected:

                return pet["id"]

        return None

    # LOAD DỊCH VỤ

    def load_services(self):
        connection = None
        cursor = None

        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT ServiceID, ServiceName, Price, Description
                FROM tbService
                ORDER BY ServiceID
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            # Xóa dữ liệu cũ
            self.service_data = []
            service_values = []

            for item in self.service_tree.get_children():
                self.service_tree.delete(item)

            # Đọc danh sách dịch vụ từ database
            for row in rows:
                service_id = row[0]
                service_name = row[1]
                price = row[2]
                description = row[3]

                display = str(service_id) + " - " + str(service_name)

                self.service_data.append({
                    "id": service_id,
                    "name": service_name,
                    "price": price,
                    "description": description,
                    "display": display
                })

                # Thêm tên dịch vụ vào danh sách ComboBox
                service_values.append(display)

                # Hiển thị dịch vụ trong bảng quản lý
                display_price = ""

                if price is not None:
                    display_price = "{:,.0f}".format(float(price))

                self.service_tree.insert(
                    "",
                    "end",
                    values=(
                        service_id,
                        service_name,
                        display_price,
                        description
                    )
                )

            # CẬP NHẬT COMBOBOX DỊCH VỤ
            if len(service_values) > 0:
                self.cbo_service.configure(values=service_values)

                # Chọn dịch vụ đầu tiên nếu chưa có lựa chọn hợp lệ
                if self.cbo_service.get() not in service_values:
                    self.cbo_service.set(service_values[0])
            else:
                self.cbo_service.configure(values=[])
                self.cbo_service.set("Chưa có dịch vụ")

            # Đóng kết nối
            cursor.close()
            connection.close()

        except Exception as e:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách dịch vụ.\n\n" + str(e)
            )

    # LẤY SERVICE ID

    def get_service_id(self):

        selected = self.cbo_service.get()

        for service in self.service_data:

            if service["display"] == selected:

                return service["id"]

        return None

    # LOAD NHÂN VIÊN

    def load_staff(self):

        self.staff_data = []

        # Lấy thông tin nhân viên đang đăng nhập
        if Session.user_id != 0 and Session.full_name != "":

            self.staff_data.append({
                "id": Session.user_id,
                "name": Session.full_name
            })

            # Hiển thị tên nhân viên đăng nhập
            self.txt_employee.configure(state="normal")
            self.txt_employee.delete(0, "end")
            self.txt_employee.insert(0, Session.full_name)

            # Không cho sửa tên nhân viên
            self.txt_employee.configure(state="disabled")

        else:
            self.txt_employee.configure(state="normal")
            self.txt_employee.delete(0, "end")

            messagebox.showwarning(
                "Thông báo",
                "Không tìm thấy thông tin nhân viên đang đăng nhập."
            )

    # LẤY STAFF ID THEO TÊN

    # LẤY ID NHÂN VIÊN ĐANG ĐĂNG NHẬP

    def get_staff_id(self):

        if Session.user_id != 0:
            return Session.user_id

        return None

    # LẤY TÊN NHÂN VIÊN THEO STAFF ID

    def get_staff_name(self, staff_id):

        if staff_id is None:

            return ""

        for staff in self.staff_data:

            if staff["id"] == staff_id:

                return staff["name"]

        return ""

    # LOAD LỊCH SỬ

    def load_history(self):
        connection = None
        cursor = None

        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT
                    ps.PetServiceID,
                    p.PetName,
                    s.ServiceName,
                    ps.Price,
                    ps.ServiceDate,
                    u.name AS EmployeeName,
                    ps.Note
                FROM tbPetService ps
                INNER JOIN tbPet p
                    ON ps.PetID = p.PetID
                INNER JOIN tbService s
                    ON ps.ServiceID = s.ServiceID
                LEFT JOIN tbUser u
                    ON ps.StaffID = u.id
                ORDER BY ps.PetServiceID DESC
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            for item in self.history_tree.get_children():
                self.history_tree.delete(item)

            for row in rows:
                price = ""

                if row[3] is not None:
                    price = "{:,.0f}".format(float(row[3]))

                self.history_tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        price,
                        row[4],
                        row[5],
                        row[6]
                    )
                )

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                "Không thể tải lịch sử chăm sóc.\n\n" + str(e)
            )

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

    # CHỌN LỊCH SỬ

    def select_history(self, event):

        selected = self.history_tree.selection()

        if len(selected) == 0:

            return

        item = self.history_tree.item(
            selected[0]
        )

        values = item["values"]

        self.selected_id = values[0]

        self.lbl_history_id.configure(
            text=str(self.selected_id)
        )

        # Chọn thú cưng
        pet_name = values[1]

        for pet in self.pet_data:

            if pet["name"] == pet_name:

                self.cbo_pet.set(
                    pet["display"]
                )

                break

        # Chọn dịch vụ
        service_name = values[2]

        for service in self.service_data:

            if service["name"] == service_name:

                self.cbo_service.set(
                    service["display"]
                )

                break

        # Ngày
        self.txt_date.delete(
            0,
            "end"
        )

        if values[4] is not None:

            self.txt_date.insert(
                0,
                str(values[4])
            )

        # Nhân viên
        self.txt_employee.delete(
            0,
            "end"
        )

        if values[5] is not None:

            self.txt_employee.insert(
                0,
                str(values[5])
            )

        # Ghi chú
        self.txt_history_note.delete(
            0,
            "end"
        )

        if values[6] is not None:

            self.txt_history_note.insert(
                0,
                str(values[6])
            )

    # THÊM LỊCH SỬ

    def add_history(self):
        pet_id = self.get_pet_id()
        service_id = self.get_service_id()
        staff_id = self.get_staff_id()

        service_date = self.txt_date.get().strip()
        note = self.txt_history_note.get().strip()

        if pet_id is None:
            messagebox.showwarning("Thông báo", "Vui lòng chọn thú cưng.")
            return

        if service_id is None:
            messagebox.showwarning("Thông báo", "Vui lòng chọn dịch vụ.")
            return

        if service_date == "":
            messagebox.showwarning("Thông báo", "Vui lòng nhập ngày thực hiện.")
            return

        if staff_id is None:
            messagebox.showwarning(
                "Thông báo",
                "Nhân viên không tồn tại trong hệ thống."
            )
            return

        connection = None
        cursor = None

        try:
            connection = connect_database()
            cursor = connection.cursor()

            cursor.execute(
                "SELECT Price FROM tbService WHERE ServiceID = ?",
                (service_id,)
            )

            price_row = cursor.fetchone()

            if price_row is None:
                messagebox.showwarning("Thông báo", "Dịch vụ không tồn tại.")
                return

            price = price_row[0]

            # Lưu dịch vụ mới vào lịch sử chăm sóc.
            # Cần bảo đảm tbPetService có cột Status.
            sql = """
                INSERT INTO tbPetService
                (
                    PetID,
                    ServiceID,
                    StaffID,
                    ServiceDate,
                    Price,
                    Note,
                    Status
                )
                VALUES (?, ?, ?, ?, ?, ?, N'Đã đặt')
            """

            cursor.execute(
                sql,
                (
                    pet_id,
                    service_id,
                    staff_id,
                    service_date,
                    price,
                    note
                )
            )

            connection.commit()

            messagebox.showinfo(
                "Thông báo",
                "Đặt dịch vụ thành công. Dịch vụ đã được lưu."
            )

            self.clear_history()
            self.load_history()

        except Exception as e:
            if connection is not None:
                connection.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể đặt dịch vụ.\n\n" + str(e)
            )

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()

    # SỬA LỊCH SỬ

    def update_history(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn lịch sử cần sửa."
            )

            return

        pet_id = self.get_pet_id()
        service_id = self.get_service_id()
        staff_id = self.get_staff_id()

        service_date = self.txt_date.get().strip()
        note = self.txt_history_note.get().strip()

        if pet_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn thú cưng."
            )

            return

        if service_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn dịch vụ."
            )

            return

        if service_date == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập ngày thực hiện."
            )

            return

        if staff_id is None:

            messagebox.showwarning(
                "Thông báo",
                "Nhân viên không tồn tại trong hệ thống."
            )

            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            # Lấy giá hiện tại của dịch vụ
            sql_price = """
                SELECT Price
                FROM tbService
                WHERE ServiceID = ?
            """

            cursor.execute(
                sql_price,
                (service_id,)
            )

            price_row = cursor.fetchone()

            price = None

            if price_row is not None:

                price = price_row[0]

            # Cập nhật lịch sử
            sql = """
                UPDATE tbPetService
                SET PetID = ?,
                    ServiceID = ?,
                    StaffID = ?,
                    ServiceDate = ?,
                    Price = ?,
                    Note = ?
                WHERE PetServiceID = ?
            """

            cursor.execute(
                sql,
                (
                    pet_id,
                    service_id,
                    staff_id,
                    service_date,
                    price,
                    note,
                    self.selected_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật lịch sử thành công."
            )

            self.clear_history()
            self.load_history()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật lịch sử.\n"
                + str(e)
            )

    # XÓA LỊCH SỬ

    def delete_history(self):

        if self.selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn lịch sử cần xóa."
            )

            return

        answer = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa lịch sử này không?"
        )

        if answer is False:

            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                DELETE FROM tbPetService
                WHERE PetServiceID = ?
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
                "Xóa lịch sử thành công."
            )

            self.clear_history()
            self.load_history()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa lịch sử.\n"
                + str(e)
            )

    # TÌM KIẾM LỊCH SỬ

    def search_history(self):

        keyword = self.txt_history_search.get().strip()

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT
                    ps.PetServiceID,
                    p.PetName,
                    s.ServiceName,
                    ps.Price,
                    ps.ServiceDate,
                    u.name AS EmployeeName,
                    ps.Note
                FROM tbPetService ps
                INNER JOIN tbPet p
                    ON ps.PetID = p.PetID
                INNER JOIN tbService s
                    ON ps.ServiceID = s.ServiceID
                LEFT JOIN tbUser u
                    ON ps.StaffID = u.id
                WHERE p.PetName LIKE ?
                   OR s.ServiceName LIKE ?
                   OR u.name LIKE ?
                ORDER BY ps.PetServiceID DESC
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

            for item in self.history_tree.get_children():

                self.history_tree.delete(item)

            for row in rows:

                price = row[3]

                if price is not None:

                    price = "{:,.0f}".format(
                        float(price)
                    )

                self.history_tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        price,
                        row[4],
                        row[5],
                        row[6]
                    )
                )

            cursor.close()
            connection.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tìm kiếm.\n"
                + str(e)
            )

    # LÀM MỚI LỊCH SỬ

    def clear_history(self):

        self.selected_id = 0

        self.lbl_history_id.configure(
            text="Tự động"
        )
        self.txt_date.delete(
            0,
            "end"
        )

        self.txt_employee.configure(state="normal")
        self.txt_employee.delete(0, "end")

        if Session.full_name != "":
            self.txt_employee.insert(0, Session.full_name)

        self.txt_employee.configure(state="disabled")

        self.txt_history_note.delete(
            0,
            "end"
        )

        self.txt_history_search.delete(
            0,
            "end"
        )

        if len(self.pet_data) > 0:

            self.cbo_pet.set(
                self.pet_data[0]["display"]
            )

        if len(self.service_data) > 0:

            self.cbo_service.set(
                self.service_data[0]["display"]
            )

        for item in self.history_tree.selection():

            self.history_tree.selection_remove(item)

        self.load_history()

    # THÊM DỊCH VỤ

    def add_service(self):

        name = self.txt_service_name.get().strip()
        price = self.txt_service_price.get().strip()
        description = self.txt_service_description.get().strip()

        if name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên dịch vụ."
            )

            return

        try:

            price_value = float(price)

            if price_value < 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Giá không được nhỏ hơn 0."
                )

                return

        except:

            messagebox.showwarning(
                "Thông báo",
                "Giá dịch vụ phải là số."
            )

            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                INSERT INTO tbService
                (
                    ServiceName,
                    Price,
                    Description
                )
                VALUES (?, ?, ?)
            """

            cursor.execute(
                sql,
                (
                    name,
                    price_value,
                    description
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Thêm dịch vụ thành công."
            )

            self.clear_service()
            self.load_services()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể thêm dịch vụ.\n"
                + str(e)
            )

    # CHỌN DỊCH VỤ

    def select_service(self, event):

        selected = self.service_tree.selection()

        if len(selected) == 0:

            return

        item = self.service_tree.item(
            selected[0]
        )

        values = item["values"]

        self.service_selected_id = values[0]

        self.lbl_service_id.configure(
            text=str(
                self.service_selected_id
            )
        )

        self.txt_service_name.delete(
            0,
            "end"
        )

        self.txt_service_name.insert(
            0,
            values[1]
        )

        self.txt_service_price.delete(
            0,
            "end"
        )

        self.txt_service_price.insert(
            0,
            str(values[2]).replace(",", "")
        )

        self.txt_service_description.delete(
            0,
            "end"
        )

        if values[3] is not None:

            self.txt_service_description.insert(
                0,
                values[3]
            )

    # SỬA DỊCH VỤ

    def update_service(self):

        if self.service_selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn dịch vụ cần sửa."
            )

            return

        name = self.txt_service_name.get().strip()
        price = self.txt_service_price.get().strip()
        description = self.txt_service_description.get().strip()

        if name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên dịch vụ."
            )

            return

        try:

            price_value = float(price)

            if price_value < 0:

                messagebox.showwarning(
                    "Thông báo",
                    "Giá không được nhỏ hơn 0."
                )

                return

        except:

            messagebox.showwarning(
                "Thông báo",
                "Giá dịch vụ phải là số."
            )

            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                UPDATE tbService
                SET ServiceName = ?,
                    Price = ?,
                    Description = ?
                WHERE ServiceID = ?
            """

            cursor.execute(
                sql,
                (
                    name,
                    price_value,
                    description,
                    self.service_selected_id
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật dịch vụ thành công."
            )

            self.clear_service()
            self.load_services()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật dịch vụ.\n"
                + str(e)
            )

    # XÓA DỊCH VỤ

    def delete_service(self):

        if self.service_selected_id == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn dịch vụ cần xóa."
            )

            return

        answer = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa dịch vụ này không?"
        )

        if answer is False:

            return

        try:

            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                DELETE FROM tbService
                WHERE ServiceID = ?
            """

            cursor.execute(
                sql,
                (self.service_selected_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Xóa dịch vụ thành công."
            )

            self.clear_service()
            self.load_services()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa dịch vụ.\n"
                "Có thể dịch vụ này đang được sử dụng trong lịch sử chăm sóc.\n\n"
                + str(e)
            )

    # LÀM MỚI DỊCH VỤ

    def clear_service(self):

        self.service_selected_id = 0

        self.lbl_service_id.configure(
            text="Tự động"
        )
        self.txt_service_name.delete(
            0,
            "end"
        )

        self.txt_service_price.delete(
            0,
            "end"
        )

        self.txt_service_description.delete(
            0,
            "end"
        )

        for item in self.service_tree.selection():

            self.service_tree.selection_remove(item)

        self.load_services()