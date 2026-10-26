import customtkinter as ctk
from tkinter import messagebox, ttk

from database.database import connect_database

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DashboardForm:

    def __init__(self, parent):

        self.parent = parent

        self.create_interface()

        self.load_dashboard()

    # TẠO GIAO DIỆN

    def create_interface(self):

        # MÀU SẮC GIAO DIỆN

        bg_color = "#F1F2F7"
        card_color = "#FFFFFF"
        text_color = "#202044"
        purple_color = "#6500F5"
        pink_color = "#FF3FA4"
        green_color = "#00DDB0"
        blue_color = "#4385F5"

        self.parent.configure(fg_color=bg_color)

        # TIÊU ĐỀ

        header_frame = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color
        )
        header_frame.pack(
            fill="x",
            padx=25,
            pady=(18, 8)
        )

        ctk.CTkLabel(
            header_frame,
            text="Tổng quan cửa hàng",
            font=("Arial", 27, "bold"),
            text_color=text_color
        ).pack(side="left")

        ctk.CTkLabel(
            header_frame,
            text="PET SHOP  /  DASHBOARD",
            font=("Arial", 12),
            text_color="#85859B"
        ).pack(side="right", padx=10)

        # THẺ THỐNG KÊ

        statistic_frame = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color
        )
        statistic_frame.pack(
            fill="x",
            padx=20,
            pady=8
        )

        for column in range(5):
            statistic_frame.grid_columnconfigure(
                column,
                weight=1,
                uniform="statistic"
            )

        card_info = [
            ("♥", "Nhân viên", "employee", purple_color),
            ("●", "Khách hàng", "customer", green_color),
            ("▣", "Sản phẩm", "product", pink_color),
            ("▰", "Hóa đơn", "invoice", purple_color),
            ("₫", "Doanh thu", "revenue", blue_color)
        ]

        self.statistic_values = {}

        for index, info in enumerate(card_info):
            icon_text = info[0]
            title_text = info[1]
            key = info[2]
            accent_color = info[3]

            card = ctk.CTkFrame(
                statistic_frame,
                fg_color=card_color,
                corner_radius=12,
                height=115
            )
            card.grid(
                row=0,
                column=index,
                padx=6,
                pady=5,
                sticky="nsew"
            )
            card.grid_propagate(False)

            icon_label = ctk.CTkLabel(
                card,
                text=icon_text,
                font=("Arial", 23, "bold"),
                text_color=accent_color,
                fg_color="#F2EAFE",
                corner_radius=20,
                width=42,
                height=42
            )
            icon_label.pack(
                anchor="w",
                padx=15,
                pady=(12, 3)
            )

            ctk.CTkLabel(
                card,
                text=title_text,
                font=("Arial", 12),
                text_color="#77778D"
            ).pack(
                anchor="w",
                padx=15
            )

            value_label = ctk.CTkLabel(
                card,
                text="0",
                font=("Arial", 19, "bold"),
                text_color=text_color
            )
            value_label.pack(
                anchor="w",
                padx=15,
                pady=(0, 10)
            )

            self.statistic_values[key] = value_label

        # Giữ lại các biến cũ để những hàm khác không bị lỗi
        self.lbl_employee = self.statistic_values["employee"]
        self.lbl_customer = self.statistic_values["customer"]
        self.lbl_product = self.statistic_values["product"]
        self.lbl_invoice = self.statistic_values["invoice"]
        self.lbl_revenue = self.statistic_values["revenue"]

        # NÚT LÀM MỚI

        toolbar = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color
        )
        toolbar.pack(
            fill="x",
            padx=25,
            pady=(0, 8)
        )

        ctk.CTkButton(
            toolbar,
            text="↻  Làm mới dữ liệu",
            width=155,
            height=32,
            corner_radius=8,
            fg_color=purple_color,
            hover_color="#4D00C4",
            command=self.load_dashboard
        ).pack(side="right")

        # KHU VỰC BIỂU ĐỒ

        chart_row = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color
        )
        chart_row.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        chart_row.grid_columnconfigure(0, weight=1)
        chart_row.grid_rowconfigure(0, weight=1)

        # BIỂU ĐỒ DOANH THU

        revenue_card = ctk.CTkFrame(
            chart_row,
            fg_color=card_color,
            corner_radius=12
        )
        revenue_card.grid(
            row=0,
            column=0,
            padx=6,
            pady=5,
            sticky="nsew"
        )

        ctk.CTkLabel(
            revenue_card,
            text="Doanh thu theo tháng",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 5)
        )

        self.chart_area = ctk.CTkFrame(
            revenue_card,
            fg_color=card_color
        )
        self.chart_area.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # BẢNG DỮ LIỆU PHÍA DƯỚI

        bottom_row = ctk.CTkFrame(
            self.parent,
            fg_color=bg_color
        )
        bottom_row.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 18)
        )

        bottom_row.grid_columnconfigure(0, weight=3)
        bottom_row.grid_columnconfigure(1, weight=2)
        bottom_row.grid_rowconfigure(0, weight=1)

        # HÓA ĐƠN GẦN ĐÂY

        invoice_card = ctk.CTkFrame(
            bottom_row,
            fg_color=card_color,
            corner_radius=12
        )
        invoice_card.grid(
            row=0,
            column=0,
            padx=6,
            pady=5,
            sticky="nsew"
        )

        ctk.CTkLabel(
            invoice_card,
            text="Hóa đơn gần đây",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 8)
        )

        invoice_table_frame = ctk.CTkFrame(
            invoice_card,
            fg_color=card_color
        )
        invoice_table_frame.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        invoice_columns = (
            "transno",
            "customer",
            "cashier",
            "total"
        )

        self.recent_invoice_tree = ttk.Treeview(
            invoice_table_frame,
            columns=invoice_columns,
            show="headings",
            height=6
        )

        self.recent_invoice_tree.heading(
            "transno",
            text="Mã hóa đơn"
        )
        self.recent_invoice_tree.heading(
            "customer",
            text="Khách hàng"
        )
        self.recent_invoice_tree.heading(
            "cashier",
            text="Nhân viên"
        )
        self.recent_invoice_tree.heading(
            "total",
            text="Tổng tiền"
        )

        self.recent_invoice_tree.column(
            "transno",
            width=100,
            anchor="center"
        )
        self.recent_invoice_tree.column(
            "customer",
            width=140
        )
        self.recent_invoice_tree.column(
            "cashier",
            width=120
        )
        self.recent_invoice_tree.column(
            "total",
            width=120,
            anchor="e"
        )

        invoice_scrollbar = ttk.Scrollbar(
            invoice_table_frame,
            orient="vertical",
            command=self.recent_invoice_tree.yview
        )

        self.recent_invoice_tree.configure(
            yscrollcommand=invoice_scrollbar.set
        )

        self.recent_invoice_tree.pack(
            side="left",
            fill="both",
            expand=True
        )
        invoice_scrollbar.pack(
            side="right",
            fill="y"
        )

        # SẢN PHẨM NỔI BẬT

        product_card = ctk.CTkFrame(
            bottom_row,
            fg_color=card_color,
            corner_radius=12
        )
        product_card.grid(
            row=0,
            column=1,
            padx=6,
            pady=5,
            sticky="nsew"
        )

        ctk.CTkLabel(
            product_card,
            text="Sản phẩm nổi bật",
            font=("Arial", 17, "bold"),
            text_color=text_color
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 8)
        )

        product_table_frame = ctk.CTkFrame(
            product_card,
            fg_color=card_color
        )
        product_table_frame.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        product_columns = (
            "name",
            "quantity",
            "price"
        )

        self.featured_product_tree = ttk.Treeview(
            product_table_frame,
            columns=product_columns,
            show="headings",
            height=6
        )

        self.featured_product_tree.heading(
            "name",
            text="Tên sản phẩm"
        )
        self.featured_product_tree.heading(
            "quantity",
            text="Tồn kho"
        )
        self.featured_product_tree.heading(
            "price",
            text="Giá bán"
        )

        self.featured_product_tree.column(
            "name",
            width=190
        )
        self.featured_product_tree.column(
            "quantity",
            width=75,
            anchor="center"
        )
        self.featured_product_tree.column(
            "price",
            width=110,
            anchor="e"
        )

        product_scrollbar = ttk.Scrollbar(
            product_table_frame,
            orient="vertical",
            command=self.featured_product_tree.yview
        )

        self.featured_product_tree.configure(
            yscrollcommand=product_scrollbar.set
        )

        self.featured_product_tree.pack(
            side="left",
            fill="both",
            expand=True
        )
        product_scrollbar.pack(
            side="right",
            fill="y"
        )

    # LOAD DASHBOARD

    def load_dashboard(self):

        try:

            connection = connect_database()

            cursor = connection.cursor()

            # TỔNG NHÂN VIÊN

            sql_employee = """
                SELECT COUNT(*)
                FROM tbUser
            """

            cursor.execute(
                sql_employee
            )

            employee_result = cursor.fetchone()

            employee_count = 0

            if employee_result:

                if employee_result[0] is not None:

                    employee_count = employee_result[0]

            # ======================================
            # TỔNG KHÁCH HÀNG
            # ======================================

            sql_customer = """
                SELECT COUNT(*)
                FROM tbCustomer
            """

            cursor.execute(
                sql_customer
            )

            customer_result = cursor.fetchone()

            customer_count = 0

            if customer_result:

                if customer_result[0] is not None:

                    customer_count = customer_result[0]

            # ======================================
            # TỔNG SẢN PHẨM
            # ======================================

            sql_product = """
                SELECT COUNT(*)
                FROM tbProduct
            """

            cursor.execute(
                sql_product
            )

            product_result = cursor.fetchone()

            product_count = 0

            if product_result:

                if product_result[0] is not None:

                    product_count = product_result[0]

            # ======================================
            # TỔNG HÓA ĐƠN
            # ======================================

            sql_invoice = """
                SELECT COUNT(DISTINCT transno)
                FROM tbCash
            """

            cursor.execute(
                sql_invoice
            )

            invoice_result = cursor.fetchone()

            invoice_count = 0

            if invoice_result:

                if invoice_result[0] is not None:

                    invoice_count = invoice_result[0]

            # TỔNG DOANH THU

            sql_revenue = """
                SELECT ISNULL(SUM(total), 0)
                FROM tbCash
            """

            cursor.execute(
                sql_revenue
            )

            revenue_result = cursor.fetchone()

            revenue = 0

            if revenue_result:

                if revenue_result[0] is not None:

                    revenue = float(
                        revenue_result[0]
                    )

            # HIỂN THỊ DỮ LIỆU

            self.lbl_employee.configure(
                text="Nhân viên\n{}".format(
                    employee_count
                )
            )

            self.lbl_customer.configure(
                text="Khách hàng\n{}".format(
                    customer_count
                )
            )

            self.lbl_product.configure(
                text="Sản phẩm\n{}".format(
                    product_count
                )
            )

            self.lbl_invoice.configure(
                text="Hóa đơn\n{}".format(
                    invoice_count
                )
            )

            self.lbl_revenue.configure(
                text="Doanh thu\n{:,.0f} VNĐ".format(
                    revenue
                )
            )

            # DỮ LIỆU BIỂU ĐỒ

            sql_category = """
                SELECT
                    pcategory,
                    SUM(pqty)
                FROM tbProduct
                GROUP BY pcategory
                ORDER BY pcategory
            """

            cursor.execute(
                sql_category
            )

            rows = cursor.fetchall()

            categories = []
            quantities = []

            for row in rows:

                category = row[0]
                quantity = row[1]

                categories.append(
                    str(category)
                )

                quantities.append(
                    int(quantity)
                )

            self.load_recent_invoices()
            self.load_featured_products()

            cursor.close()

            connection.close()

            # VẼ BIỂU ĐỒ

            self.draw_chart(
                categories,
                quantities
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải Dashboard!\n\n"
                + str(e)
            )

    # LOAD HÓA ĐƠN GẦN ĐÂY

    def load_recent_invoices(self):
        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT TOP 10
                    c.transno,
                    ISNULL(cust.name, N'Khách lẻ') AS CustomerName,
                    MAX(c.cashier) AS CashierName,
                    SUM(c.total) AS TotalMoney
                FROM tbCash c
                LEFT JOIN tbCustomer cust
                    ON c.cid = CAST(cust.id AS NVARCHAR(20))
                GROUP BY c.transno, cust.name
                ORDER BY MAX(c.cashid) DESC
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            for item in self.recent_invoice_tree.get_children():
                self.recent_invoice_tree.delete(item)

            for row in rows:
                total = float(row[3] or 0)

                self.recent_invoice_tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        "{:,.0f} VNĐ".format(total)
                    )
                )

            cursor.close()
            connection.close()

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                "Không thể tải hóa đơn gần đây:\n" + str(e)
            )

    # LOAD SẢN PHẨM NỔI BẬT

    def load_featured_products(self):
        try:
            connection = connect_database()
            cursor = connection.cursor()

            sql = """
                SELECT TOP 10
                    p.pname,
                    p.pqty,
                    p.pprice
                FROM tbProduct p
                ORDER BY
                    ISNULL(
                        (
                            SELECT SUM(c.qty)
                            FROM tbCash c
                            WHERE TRY_CONVERT(INT, c.pcode) = p.pcode
                        ),
                        0
                    ) DESC,
                    p.pname
            """

            cursor.execute(sql)
            rows = cursor.fetchall()

            for item in self.featured_product_tree.get_children():
                self.featured_product_tree.delete(item)

            for row in rows:
                stock = row[1] if row[1] is not None else 0
                price = float(row[2] or 0)

                self.featured_product_tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        stock,
                        "{:,.0f} VNĐ".format(price)
                    )
                )

            cursor.close()
            connection.close()

        except Exception as e:
            messagebox.showerror(
                "Lỗi",
                "Không thể tải sản phẩm nổi bật:\n" + str(e)
            )

    # VẼ BIỂU ĐỒ

    def draw_chart(
        self,
        categories,
        quantities
    ):

        # XÓA BIỂU ĐỒ CŨ

        for widget in self.chart_area.winfo_children():

            widget.destroy()

        # KIỂM TRA DỮ LIỆU

        if len(categories) == 0:

            label = ctk.CTkLabel(
                self.chart_area,
                text="Chưa có dữ liệu sản phẩm."
            )

            label.pack(
                expand=True
            )

            return

        # TẠO BIỂU ĐỒ

        figure = Figure(
            figsize=(10, 4),
            dpi=100
        )

        axes = figure.add_subplot(111)

        axes.bar(
            categories,
            quantities
        )

        axes.set_title(
            "Số lượng sản phẩm theo loại"
        )

        axes.set_xlabel(
            "Loại sản phẩm"
        )

        axes.set_ylabel(
            "Số lượng"
        )

        axes.tick_params(
            axis="x",
            rotation=30
        )

        figure.tight_layout()

        # ĐƯA BIỂU ĐỒ VÀO CUSTOMTKINTER

        canvas = FigureCanvasTkAgg(
            figure,
            master=self.chart_area
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )