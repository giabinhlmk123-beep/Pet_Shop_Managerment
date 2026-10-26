import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from database.database import connect_database

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ReportsForm:

    def __init__(self, parent):

        self.parent = parent

        self.create_interface()

        self.load_report()

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

        self.parent.configure(fg_color=bg_color)

        # =========================
        # STYLE BẢNG DỮ LIỆU
        # =========================

        style = ttk.Style()

        style.configure(
            "Report.Treeview",
            background=card_color,
            foreground=text_color,
            fieldbackground=card_color,
            rowheight=34,
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "Report.Treeview.Heading",
            background="#F0EBFF",
            foreground=text_color,
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=(8, 10)
        )

        style.map(
            "Report.Treeview",
            background=[("selected", "#E4D6FF")],
            foreground=[("selected", text_color)]
        )

        style.map(
            "Report.Treeview.Heading",
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
            pady=(20, 12)
        )

        title = ctk.CTkLabel(
            header_frame,
            text="BÁO CÁO THỐNG KÊ",
            font=("Arial", 25, "bold"),
            text_color=text_color
        )

        title.pack(
            side="left",
            padx=5
        )

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Tổng quan hoạt động kinh doanh và doanh thu",
            font=("Arial", 12),
            text_color=muted_color
        )

        subtitle.pack(
            side="left",
            padx=(15, 0),
            pady=(8, 0)
        )

        # =========================
        # KHUNG 4 THẺ THỐNG KÊ
        # =========================

        statistic_frame = ctk.CTkFrame(
            self.parent,
            fg_color="transparent"
        )

        statistic_frame.pack(
            fill="x",
            padx=25,
            pady=(0, 12)
        )

        # Chia đều chiều rộng 4 thẻ

        for i in range(4):
            statistic_frame.grid_columnconfigure(
                i,
                weight=1,
                uniform="report_statistic"
            )

        # =========================
        # THẺ 1: TỔNG HÓA ĐƠN
        # =========================

        invoice_card = ctk.CTkFrame(
            statistic_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color,
            height=105
        )

        invoice_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8),
            pady=2
        )

        invoice_card.grid_propagate(False)

        ctk.CTkLabel(
            invoice_card,
            text="▤",
            font=("Arial", 28, "bold"),
            text_color=primary_color,
            fg_color="#F0EBFF",
            corner_radius=12,
            width=48,
            height=48
        ).pack(
            side="left",
            padx=(15, 12),
            pady=15
        )

        invoice_info = ctk.CTkFrame(
            invoice_card,
            fg_color="transparent"
        )

        invoice_info.pack(
            side="left",
            fill="both",
            expand=True,
            pady=15
        )

        ctk.CTkLabel(
            invoice_info,
            text="Tổng hóa đơn",
            font=("Arial", 12),
            text_color=muted_color
        ).pack(
            anchor="w",
            pady=(3, 2)
        )

        self.lbl_invoice = ctk.CTkLabel(
            invoice_info,
            text="0",
            font=("Arial", 22, "bold"),
            text_color=text_color
        )

        self.lbl_invoice.pack(
            anchor="w"
        )

        # =========================
        # THẺ 2: DOANH THU
        # =========================

        revenue_card = ctk.CTkFrame(
            statistic_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color,
            height=105
        )

        revenue_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8,
            pady=2
        )

        revenue_card.grid_propagate(False)

        ctk.CTkLabel(
            revenue_card,
            text="₫",
            font=("Arial", 26, "bold"),
            text_color="#16865C",
            fg_color="#E3F7ED",
            corner_radius=12,
            width=48,
            height=48
        ).pack(
            side="left",
            padx=(15, 12),
            pady=15
        )

        revenue_info = ctk.CTkFrame(
            revenue_card,
            fg_color="transparent"
        )

        revenue_info.pack(
            side="left",
            fill="both",
            expand=True,
            pady=15
        )

        ctk.CTkLabel(
            revenue_info,
            text="Doanh thu",
            font=("Arial", 12),
            text_color=muted_color
        ).pack(
            anchor="w",
            pady=(3, 2)
        )

        self.lbl_revenue = ctk.CTkLabel(
            revenue_info,
            text="0 VNĐ",
            font=("Arial", 20, "bold"),
            text_color=text_color
        )

        self.lbl_revenue.pack(
            anchor="w"
        )

        # =========================
        # THẺ 3: SẢN PHẨM ĐÃ BÁN
        # =========================

        product_card = ctk.CTkFrame(
            statistic_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color,
            height=105
        )

        product_card.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=8,
            pady=2
        )

        product_card.grid_propagate(False)

        ctk.CTkLabel(
            product_card,
            text="□",
            font=("Arial", 28, "bold"),
            text_color="#D97706",
            fg_color="#FFF2D9",
            corner_radius=12,
            width=48,
            height=48
        ).pack(
            side="left",
            padx=(15, 12),
            pady=15
        )

        product_info = ctk.CTkFrame(
            product_card,
            fg_color="transparent"
        )

        product_info.pack(
            side="left",
            fill="both",
            expand=True,
            pady=15
        )

        ctk.CTkLabel(
            product_info,
            text="Sản phẩm đã bán",
            font=("Arial", 12),
            text_color=muted_color
        ).pack(
            anchor="w",
            pady=(3, 2)
        )

        self.lbl_product = ctk.CTkLabel(
            product_info,
            text="0",
            font=("Arial", 22, "bold"),
            text_color=text_color
        )

        self.lbl_product.pack(
            anchor="w"
        )

        # =========================
        # THẺ 4: KHÁCH HÀNG
        # =========================

        customer_card = ctk.CTkFrame(
            statistic_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color,
            height=105
        )

        customer_card.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=(8, 0),
            pady=2
        )

        customer_card.grid_propagate(False)

        ctk.CTkLabel(
            customer_card,
            text="♟",
            font=("Arial", 27, "bold"),
            text_color="#0D83B6",
            fg_color="#E1F5FC",
            corner_radius=12,
            width=48,
            height=48
        ).pack(
            side="left",
            padx=(15, 12),
            pady=15
        )

        customer_info = ctk.CTkFrame(
            customer_card,
            fg_color="transparent"
        )

        customer_info.pack(
            side="left",
            fill="both",
            expand=True,
            pady=15
        )

        ctk.CTkLabel(
            customer_info,
            text="Khách hàng",
            font=("Arial", 12),
            text_color=muted_color
        ).pack(
            anchor="w",
            pady=(3, 2)
        )

        self.lbl_customer = ctk.CTkLabel(
            customer_info,
            text="0",
            font=("Arial", 22, "bold"),
            text_color=text_color
        )

        self.lbl_customer.pack(
            anchor="w"
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
            pady=(0, 12)
        )

        refresh_button = ctk.CTkButton(
            button_frame,
            text="↻  Làm mới báo cáo",
            width=165,
            height=36,
            corner_radius=8,
            fg_color=primary_color,
            hover_color=hover_color,
            font=("Arial", 12, "bold"),
            command=self.load_report
        )

        refresh_button.pack(
            side="left",
            padx=(0, 8)
        )

        detail_button = ctk.CTkButton(
            button_frame,
            text="▤  Xem chi tiết hóa đơn",
            width=190,
            height=36,
            corner_radius=8,
            fg_color="#E8E0FF",
            hover_color="#D8CAFF",
            text_color=primary_color,
            font=("Arial", 12, "bold"),
            command=self.view_invoice_detail
        )

        detail_button.pack(
            side="left",
            padx=8
        )

        # =========================
        # KHUNG BẢNG VÀ BIỂU ĐỒ
        # =========================

        content_frame = ctk.CTkFrame(
            self.parent,
            fg_color="transparent"
        )

        content_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 20)
        )

        content_frame.grid_columnconfigure(
            0,
            weight=3,
            uniform="report_content"
        )

        content_frame.grid_columnconfigure(
            1,
            weight=2,
            uniform="report_content"
        )

        content_frame.grid_rowconfigure(
            0,
            weight=1
        )

        # =========================
        # KHUNG DANH SÁCH HÓA ĐƠN
        # =========================

        table_frame = ctk.CTkFrame(
            content_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        table_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8),
            pady=2
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
            text="DANH SÁCH HÓA ĐƠN",
            font=("Arial", 16, "bold"),
            text_color=text_color
        ).pack(
            side="left"
        )

        # =========================
        # KHUNG TREEVIEW
        # =========================

        tree_frame = ctk.CTkFrame(
            table_frame,
            fg_color=card_color,
            corner_radius=8
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 12)
        )

        columns = (
            "transno",
            "customer",
            "cashier",
            "quantity",
            "total"
        )

        self.invoice_table = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            style="Report.Treeview"
        )

        self.invoice_table.heading(
            "transno",
            text="Mã hóa đơn"
        )

        self.invoice_table.heading(
            "customer",
            text="Khách hàng"
        )

        self.invoice_table.heading(
            "cashier",
            text="Nhân viên"
        )

        self.invoice_table.heading(
            "quantity",
            text="Số lượng SP"
        )

        self.invoice_table.heading(
            "total",
            text="Tổng tiền (VNĐ)"
        )

        # KÍCH THƯỚC CỘT

        self.invoice_table.column(
            "transno",
            width=110,
            minwidth=90,
            anchor="center"
        )

        self.invoice_table.column(
            "customer",
            width=150,
            minwidth=100,
            anchor="w"
        )

        self.invoice_table.column(
            "cashier",
            width=130,
            minwidth=100,
            anchor="w"
        )

        self.invoice_table.column(
            "quantity",
            width=100,
            minwidth=80,
            anchor="center"
        )

        self.invoice_table.column(
            "total",
            width=150,
            minwidth=110,
            anchor="e"
        )

        # THANH CUỘN DỌC

        scrollbar_y = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=self.invoice_table.yview
        )

        self.invoice_table.configure(
            yscrollcommand=scrollbar_y.set
        )

        self.invoice_table.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(5, 0),
            pady=5
        )

        scrollbar_y.pack(
            side="right",
            fill="y",
            pady=5
        )

        # =========================
        # KHUNG BIỂU ĐỒ
        # =========================

        chart_frame = ctk.CTkFrame(
            content_frame,
            fg_color=card_color,
            corner_radius=14,
            border_width=1,
            border_color=border_color
        )

        chart_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8, 0),
            pady=2
        )

        # TIÊU ĐỀ BIỂU ĐỒ

        chart_title = ctk.CTkLabel(
            chart_frame,
            text="DOANH THU THEO HÓA ĐƠN",
            font=("Arial", 16, "bold"),
            text_color=text_color
        )

        chart_title.pack(
            anchor="w",
            padx=15,
            pady=(15, 8)
        )

        # VÙNG HIỂN THỊ BIỂU ĐỒ
        # Giữ nguyên tên chart_area để code vẽ biểu đồ hiện tại sử dụng.

        self.chart_area = ctk.CTkFrame(
            chart_frame,
            fg_color=card_color,
            corner_radius=8
        )

        self.chart_area.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 12)
        )

    # LOAD BÁO CÁO

    def load_report(self):

        try:

            connection = connect_database()

            cursor = connection.cursor()

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

            result = cursor.fetchone()

            invoice_count = 0

            if result:

                if result[0] is not None:

                    invoice_count = result[0]

            # ======================================
            # TỔNG DOANH THU
            # ======================================

            sql_revenue = """
                SELECT ISNULL(SUM(total), 0)
                FROM tbCash
            """

            cursor.execute(
                sql_revenue
            )

            result = cursor.fetchone()

            revenue = 0

            if result:

                if result[0] is not None:

                    revenue = float(
                        result[0]
                    )

            # ======================================
            # TỔNG SẢN PHẨM ĐÃ BÁN
            # ======================================

            sql_product = """
                SELECT ISNULL(SUM(qty), 0)
                FROM tbCash
            """

            cursor.execute(
                sql_product
            )

            result = cursor.fetchone()

            product_count = 0

            if result:

                if result[0] is not None:

                    product_count = result[0]

            # ======================================
            # SỐ KHÁCH HÀNG ĐÃ MUA
            # ======================================

            sql_customer = """
                SELECT COUNT(DISTINCT cid)
                FROM tbCash
                WHERE cid IS NOT NULL
            """

            cursor.execute(
                sql_customer
            )

            result = cursor.fetchone()

            customer_count = 0

            if result:

                if result[0] is not None:

                    customer_count = result[0]

            # ======================================
            # HIỂN THỊ THỐNG KÊ
            # ======================================

            self.lbl_invoice.configure(
                text="Tổng hóa đơn\n{}".format(
                    invoice_count
                )
            )

            self.lbl_revenue.configure(
                text="Doanh thu\n{:,.0f} VNĐ".format(
                    revenue
                )
            )

            self.lbl_product.configure(
                text="Sản phẩm đã bán\n{}".format(
                    product_count
                )
            )

            self.lbl_customer.configure(
                text="Khách hàng\n{}".format(
                    customer_count
                )
            )

            # ======================================
            # XÓA DỮ LIỆU CŨ
            # ======================================

            for item in self.invoice_table.get_children():

                self.invoice_table.delete(
                    item
                )

            # ======================================
            # LẤY DANH SÁCH HÓA ĐƠN
            # ======================================

            sql_invoice_list = """
                SELECT
                    c.transno,
                    ISNULL(cust.name, N'Khách lẻ'),
                    c.cashier,
                    SUM(c.qty),
                    SUM(c.total)
                FROM tbCash c

                LEFT JOIN tbCustomer cust
                    ON c.cid = CAST(cust.id AS NVARCHAR(20))

                GROUP BY
                    c.transno,
                    cust.name,
                    c.cashier

                ORDER BY
                    c.transno DESC
            """

            cursor.execute(
                sql_invoice_list
            )

            rows = cursor.fetchall()

            invoice_list = []
            revenue_list = []

            # ======================================
            # HIỂN THỊ HÓA ĐƠN
            # ======================================

            for row in rows:

                transno = row[0]

                customer = row[1]

                cashier = row[2]

                quantity = row[3]

                total = float(
                    row[4]
                )

                self.invoice_table.insert(
                    "",
                    "end",
                    values=(
                        transno,
                        customer,
                        cashier,
                        quantity,
                        "{:,.0f}".format(
                            total
                        )
                    )
                )

                invoice_list.append(
                    str(transno)
                )

                revenue_list.append(
                    total
                )

            cursor.close()

            connection.close()

            # ======================================
            # VẼ BIỂU ĐỒ
            # ======================================

            self.draw_chart(
                invoice_list,
                revenue_list
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể tải báo cáo!\n\n"
                + str(e)
            )

    # VẼ BIỂU ĐỒ

    def draw_chart(
        self,
        invoice_list,
        revenue_list
    ):

        # XÓA BIỂU ĐỒ CŨ

        for widget in self.chart_area.winfo_children():

            widget.destroy()

        # KHÔNG CÓ DỮ LIỆU

        if len(invoice_list) == 0:

            label = ctk.CTkLabel(
                self.chart_area,
                text="Chưa có dữ liệu để hiển thị biểu đồ."
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

        axes = figure.add_subplot(
            111
        )

        axes.bar(
            invoice_list,
            revenue_list
        )

        axes.set_title(
            "Doanh thu theo hóa đơn"
        )

        axes.set_xlabel(
            "Mã hóa đơn"
        )

        axes.set_ylabel(
            "Doanh thu (VNĐ)"
        )

        axes.tick_params(
            axis="x",
            rotation=45
        )

        figure.tight_layout()

        # HIỂN THỊ BIỂU ĐỒ

        canvas = FigureCanvasTkAgg(
            figure,
            master=self.chart_area
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    # XEM CHI TIẾT HÓA ĐƠN

    def view_invoice_detail(self):

        selected = self.invoice_table.selection()

        if len(selected) == 0:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn một hóa đơn!"
            )

            return

        item = self.invoice_table.item(
            selected[0]
        )

        values = item["values"]

        if len(values) == 0:

            return

        transno = values[0]

        try:

            connection = connect_database()

            cursor = connection.cursor()

            sql = """
                SELECT
                    pname,
                    qty,
                    price,
                    total
                FROM tbCash
                WHERE transno = ?
                ORDER BY cashid
            """

            cursor.execute(
                sql,
                (transno,)
            )

            rows = cursor.fetchall()

            cursor.close()

            connection.close()

            if len(rows) == 0:

                messagebox.showinfo(
                    "Thông báo",
                    "Không tìm thấy chi tiết hóa đơn!"
                )

                return

            # ======================================
            # TẠO NỘI DUNG
            # ======================================

            detail = ""

            detail = detail + "HÓA ĐƠN: "
            detail = detail + str(
                transno
            )

            detail = detail + "\n"

            detail = detail + "=" * 55

            detail = detail + "\n"

            total_money = 0

            for row in rows:

                pname = row[0]

                quantity = row[1]

                price = float(
                    row[2]
                )

                total = float(
                    row[3]
                )

                detail = detail + str(
                    pname
                )

                detail = detail + "\n"

                detail = detail + "Số lượng: "

                detail = detail + str(
                    quantity
                )

                detail = detail + "\n"

                detail = detail + "Đơn giá: "

                detail = detail + "{:,.0f}".format(
                    price
                )

                detail = detail + " VNĐ"

                detail = detail + "\n"

                detail = detail + "Thành tiền: "

                detail = detail + "{:,.0f}".format(
                    total
                )

                detail = detail + " VNĐ"

                detail = detail + "\n"

                detail = detail + "-" * 55

                detail = detail + "\n"

                total_money = (
                    total_money
                    + total
                )

            detail = detail + "\nTỔNG TIỀN: "

            detail = detail + "{:,.0f}".format(
                total_money
            )

            detail = detail + " VNĐ"

            # ======================================
            # HIỂN THỊ
            # ======================================

            messagebox.showinfo(
                "Chi tiết hóa đơn",
                detail
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                "Không thể xem chi tiết hóa đơn!\n\n"
                + str(e)
            )