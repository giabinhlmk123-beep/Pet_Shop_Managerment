import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from database.database import connect_database


class ProductForm:

    def __init__(self, parent):

        self.parent = parent

        self.create_interface()

        self.load_products()

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
        # STYLE BẢNG DỮ LIỆU
        # =========================

        style = ttk.Style()

        style.configure(
            "Product.Treeview",
            background=card_color,
            foreground=text_color,
            fieldbackground=card_color,
            rowheight=34,
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "Product.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=(8, 10)
        )

        style.map(
            "Product.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        style.map(
            "Product.Treeview.Heading",
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
            text="QUẢN LÝ SẢN PHẨM",
            font=("Arial", 25, "bold"),
            text_color=text_color
        )

        title.pack(
            side="left",
            padx=5
        )

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Quản lý thông tin, số lượng và giá sản phẩm",
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

        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # TIÊU ĐỀ KHUNG

        ctk.CTkLabel(
            input_frame,
            text="Thông tin sản phẩm",
            font=("Arial", 16, "bold"),
            text_color=text_color
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=(15, 5),
            sticky="w"
        )

        # =========================
        # TÊN SẢN PHẨM
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Tên sản phẩm:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.name_entry = ctk.CTkEntry(
            input_frame,
            width=220,
            height=35,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            placeholder_text="Nhập tên sản phẩm"
        )

        self.name_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # LOẠI SẢN PHẨM
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Loại:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.type_entry = ctk.CTkEntry(
            input_frame,
            width=180,
            height=35,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            placeholder_text="Nhập loại sản phẩm"
        )

        self.type_entry.grid(
            row=1,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # =========================
        # DANH MỤC
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Danh mục:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.category_entry = ctk.CTkComboBox(
            input_frame,
            width=220,
            height=35,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            button_color=primary_color,
            button_hover_color=hover_color,
            dropdown_fg_color=card_color,
            dropdown_text_color=text_color,
            values=[
                "Thức ăn",
                "Đồ chơi",
                "Phụ kiện",
                "Vệ sinh",
                "Thú cưng",
                "Khác"
            ],
            state="normal"
        )

        self.category_entry.grid(
            row=2,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # SỐ LƯỢNG
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Số lượng:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.quantity_entry = ctk.CTkEntry(
            input_frame,
            width=180,
            height=35,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            placeholder_text="Nhập số lượng"
        )

        self.quantity_entry.grid(
            row=2,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="ew"
        )

        # =========================
        # GIÁ SẢN PHẨM
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Giá (VNĐ):",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=3,
            column=0,
            padx=(20, 10),
            pady=8,
            sticky="w"
        )

        self.price_entry = ctk.CTkEntry(
            input_frame,
            width=220,
            height=35,
            corner_radius=8,
            border_color=border_color,
            fg_color="#FAFAFC",
            text_color=text_color,
            placeholder_text="Nhập giá sản phẩm"
        )

        self.price_entry.grid(
            row=3,
            column=1,
            padx=10,
            pady=8,
            sticky="ew"
        )

        # =========================
        # MÃ SẢN PHẨM
        # =========================

        ctk.CTkLabel(
            input_frame,
            text="Mã sản phẩm:",
            font=("Arial", 12),
            text_color=text_color
        ).grid(
            row=3,
            column=2,
            padx=10,
            pady=8,
            sticky="w"
        )

        self.code_label = ctk.CTkLabel(
            input_frame,
            text="Tự động",
            width=180,
            height=35,
            font=("Arial", 13, "bold"),
            text_color=primary_color,
            anchor="w"
        )

        self.code_label.grid(
            row=3,
            column=3,
            padx=(10, 20),
            pady=8,
            sticky="w"
        )

        # KHOẢNG ĐỆM CUỐI KHUNG

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
            self.parent,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=25,
            pady=(5, 10)
        )

        # NÚT THÊM

        add_button = ctk.CTkButton(
            button_frame,
            text="＋  Thêm",
            width=110,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            font=("Arial", 12, "bold"),
            command=self.add_product
        )

        add_button.pack(
            side="left",
            padx=(0, 8)
        )

        # NÚT SỬA

        update_button = ctk.CTkButton(
            button_frame,
            text="✎  Sửa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color=primary_color,
            font=("Arial", 12, "bold"),
            command=self.update_product
        )

        update_button.pack(
            side="left",
            padx=8
        )

        # NÚT XÓA

        delete_button = ctk.CTkButton(
            button_frame,
            text="✕  Xóa",
            width=110,
            height=36,
            corner_radius=8,
            fg_color=danger_color,
            hover_color=danger_hover,
            text_color="#FFFFFF",
            font=("Arial", 12, "bold"),
            command=self.delete_product
        )

        delete_button.pack(
            side="left",
            padx=8
        )

        # NÚT LÀM MỚI

        clear_button = ctk.CTkButton(
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

        clear_button.pack(
            side="left",
            padx=8
        )

        # =========================
        # TÌM KIẾM SẢN PHẨM
        # =========================

        ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Arial", 12, "bold"),
            text_color=text_color
        ).pack(
            side="left",
            padx=(20, 8)
        )

        self.search_entry = ctk.CTkEntry(
            button_frame,
            width=210,
            height=36,
            corner_radius=8,
            border_color=border_color,
            fg_color=card_color,
            text_color=text_color,
            placeholder_text="Nhập tên sản phẩm"
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        search_button = ctk.CTkButton(
            button_frame,
            text="Tìm",
            width=75,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            font=("Arial", 12, "bold"),
            command=self.search_product
        )

        search_button.pack(
            side="left",
            padx=5
        )

        # =========================
        # KHUNG BẢNG SẢN PHẨM
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
            text="Danh sách sản phẩm",
            font=("Arial", 16, "bold"),
            text_color=text_color
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            table_title_frame,
            text="Thông tin hàng hóa trong cửa hàng",
            font=("Arial", 11),
            text_color=muted_color
        ).pack(
            side="right"
        )

        # =========================
        # CÁC CỘT DỮ LIỆU
        # =========================

        columns = (
            "pcode",
            "pname",
            "ptype",
            "pcategory",
            "pqty",
            "pprice"
        )

        self.product_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Product.Treeview"
        )

        self.product_table.heading(
            "pcode",
            text="Mã SP"
        )

        self.product_table.heading(
            "pname",
            text="Tên sản phẩm"
        )

        self.product_table.heading(
            "ptype",
            text="Loại"
        )

        self.product_table.heading(
            "pcategory",
            text="Danh mục"
        )

        self.product_table.heading(
            "pqty",
            text="Số lượng"
        )

        self.product_table.heading(
            "pprice",
            text="Giá (VNĐ)"
        )

        # ĐỘ RỘNG CỘT

        self.product_table.column(
            "pcode",
            width=75,
            minwidth=60,
            anchor="center",
            stretch=False
        )

        self.product_table.column(
            "pname",
            width=250,
            minwidth=150,
            anchor="w"
        )

        self.product_table.column(
            "ptype",
            width=130,
            minwidth=90,
            anchor="w"
        )

        self.product_table.column(
            "pcategory",
            width=170,
            minwidth=110,
            anchor="w"
        )

        self.product_table.column(
            "pqty",
            width=100,
            minwidth=75,
            anchor="center",
            stretch=False
        )

        self.product_table.column(
            "pprice",
            width=160,
            minwidth=120,
            anchor="e"
        )

        # =========================
        # THANH CUỘN
        # =========================

        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.product_table.yview
        )

        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.product_table.xview
        )

        self.product_table.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        self.product_table.pack(
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
        # SỰ KIỆN CHỌN SẢN PHẨM
        # =========================

        self.product_table.bind(
            "<ButtonRelease-1>",
            self.select_product
        )

    # LOAD PRODUCT

    def load_products(self):

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT
                    pcode,
                    pname,
                    ptype,
                    pcategory,
                    pqty,
                    pprice
                FROM tbProduct
                ORDER BY pcode
            """

            cursor.execute(sql)

            rows = cursor.fetchall()

            cursor.close()
            connection.close()

            for item in self.product_table.get_children():

                self.product_table.delete(item)

            for row in rows:

                price = "{:,.0f}".format(float(row[5]))

                self.product_table.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        price
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải danh sách sản phẩm!\n\n" + str(e)
            )

    # CHỌN SẢN PHẨM

    def select_product(self, event=None):

        selected = self.product_table.selection()

        if len(selected) == 0:

            return

        item = self.product_table.item(
            selected[0]
        )

        values = item["values"]

        if len(values) == 0:

            return

        self.code_label.configure(
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

        self.type_entry.delete(
            0,
            "end"
        )

        self.type_entry.insert(
            0,
            values[2]
        )

        self.category_entry.set(values[3])

        self.quantity_entry.delete(
            0,
            "end"
        )

        self.quantity_entry.insert(
            0,
            values[4]
        )

        self.price_entry.delete(
            0,
            "end"
        )

        self.price_entry.insert(
            0,
            str(values[5]).replace(",", "")
        )

    # THÊM PRODUCT

    def add_product(self):

        name = self.name_entry.get().strip()
        product_type = self.type_entry.get().strip()
        category = self.category_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        price = self.price_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên sản phẩm!"
            )

            return

        if product_type == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập loại sản phẩm!"
            )

            return

        if category == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập danh mục!"
            )

            return

        if quantity == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập số lượng!"
            )

            return

        if price == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập giá!"
            )

            return

        try:

            quantity_value = int(quantity)
            price_value = float(price)

        except ValueError:

            messagebox.showerror(
                "Lỗi",
                "Số lượng phải là số nguyên và giá phải là số!"
            )

            return

        if quantity_value < 0:

            messagebox.showwarning(
                "Thông báo",
                "Số lượng không được nhỏ hơn 0!"
            )

            return

        if price_value < 0:

            messagebox.showwarning(
                "Thông báo",
                "Giá không được nhỏ hơn 0!"
            )

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                INSERT INTO tbProduct
                (
                    pname,
                    ptype,
                    pcategory,
                    pqty,
                    pprice
                )
                VALUES (?, ?, ?, ?, ?)
            """

            cursor.execute(
                sql,
                (
                    name,
                    product_type,
                    category,
                    quantity_value,
                    price_value
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Thêm sản phẩm thành công!"
            )

            self.clear_form()
            self.load_products()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể thêm sản phẩm!\n\n" + str(e)
            )

    # SỬA PRODUCT

    def update_product(self):

        product_code = self.code_label.cget("text")

        if product_code == "Tự động":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn sản phẩm cần sửa!"
            )

            return

        name = self.name_entry.get().strip()
        product_type = self.type_entry.get().strip()
        category = self.category_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        price = self.price_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên sản phẩm!"
            )

            return

        if quantity == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập số lượng!"
            )

            return

        if price == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập giá!"
            )

            return

        try:

            quantity_value = int(quantity)
            price_value = float(price)

        except ValueError:

            messagebox.showerror(
                "Lỗi",
                "Số lượng phải là số nguyên và giá phải là số!"
            )

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                UPDATE tbProduct
                SET
                    pname = ?,
                    ptype = ?,
                    pcategory = ?,
                    pqty = ?,
                    pprice = ?
                WHERE pcode = ?
            """

            cursor.execute(
                sql,
                (
                    name,
                    product_type,
                    category,
                    quantity_value,
                    price_value,
                    product_code
                )
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Cập nhật sản phẩm thành công!"
            )

            self.clear_form()
            self.load_products()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể cập nhật sản phẩm!\n\n" + str(e)
            )

    # XÓA PRODUCT

    def delete_product(self):

        product_code = self.code_label.cget("text")

        if product_code == "Tự động":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn sản phẩm cần xóa!"
            )

            return

        result = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa sản phẩm này không?"
        )

        if not result:

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                DELETE FROM tbProduct
                WHERE pcode = ?
            """

            cursor.execute(
                sql,
                (product_code,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Thông báo",
                "Xóa sản phẩm thành công!"
            )

            self.clear_form()
            self.load_products()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa sản phẩm!\n\n" + str(e)
            )

    # TÌM KIẾM PRODUCT

    def search_product(self):

        keyword = self.search_entry.get().strip()

        if keyword == "":

            self.load_products()

            return

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT
                    pcode,
                    pname,
                    ptype,
                    pcategory,
                    pqty,
                    pprice
                FROM tbProduct
                WHERE pname LIKE ?
                OR ptype LIKE ?
                OR pcategory LIKE ?
                ORDER BY pcode
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

            cursor.close()
            connection.close()

            for item in self.product_table.get_children():

                self.product_table.delete(item)

            for row in rows:

                price = "{:,.0f}".format(float(row[5]))

                self.product_table.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        price
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tìm kiếm sản phẩm!\n\n" + str(e)
            )

    # LÀM MỚI

    def clear_form(self):

        self.code_label.configure(
            text="Tự động"
        )

        self.name_entry.delete(
            0,
            "end"
        )

        self.type_entry.delete(
            0,
            "end"
        )

        self.category_entry.set("")

        self.quantity_entry.delete(
            0,
            "end"
        )

        self.price_entry.delete(
            0,
            "end"
        )

        self.search_entry.delete(
            0,
            "end"
        )

        selected = self.product_table.selection()

        for item in selected:

            self.product_table.selection_remove(item)

        self.load_products()