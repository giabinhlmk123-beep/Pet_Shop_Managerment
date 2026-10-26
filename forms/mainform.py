import customtkinter as ctk
from tkinter import messagebox

from models.session import Session


class MainForm:

    # PHÂN QUYỀN CHỨC NĂNG
    PERMISSIONS = {
        "Cashier": [
            "Dashboard",
            "Customer",
            "Pet",
            "Pet Care",
            "Pet Boarding",
            "Product",
            "Cash",
            "Report"
        ],

        "Employee": [
            "Dashboard",
            "Customer",
            "Pet",
            "Pet Care",
            "Pet Boarding",
            "Product",
            "Cash",
            "Report"
        ],

        "Staff": [
            "Dashboard",
            "Pet",
            "Pet Care",
            "Pet Boarding"
        ],

        "Administrator": [
            "Dashboard",
            "Customer",
            "Pet",
            "Pet Care",
            "Pet Boarding",
            "Product",
            "Cash",
            "Report",
            "User"
        ]
    }

    def __init__(self, parent, login_form):

        self.parent = parent
        self.login_form = login_form

        # TẠO CỬA SỔ MAIN FORM
        self.window = ctk.CTkToplevel(parent)

        self.window.title("Pet Shop Management System")

        # Mở cửa sổ ở trạng thái tối đa
        self.window.state("zoomed")

        # Cho phép thay đổi kích thước
        self.window.resizable(True, True)

        self.window.protocol(
            "WM_DELETE_WINDOW",
            self.logout
        )

        self.create_interface()

    # KIỂM TRA QUYỀN
    def has_permission(self, feature):

        if Session.is_admin():
            role = "Administrator"

        elif Session.is_cashier():
            role = "Cashier"

        elif Session.is_employee():
            role = "Employee"

        elif Session.is_staff():
            role = "Staff"

        else:
            return False

        return feature in self.PERMISSIONS.get(role, [])

    # TẠO NÚT MENU NẾU CÓ QUYỀN
    def add_menu_button(self, text, command):

        if self.has_permission(text):

            button = ctk.CTkButton(
                self.menu_frame,
                text=text,
                width=180,
                command=command
            )

            button.pack(pady=5)

    def create_interface(self):

        # MENU BÊN TRÁI
        self.menu_frame = ctk.CTkFrame(
            self.window,
            width=220
        )

        self.menu_frame.pack(
            side="left",
            fill="y"
        )

        # Không cho menu bị thay đổi chiều rộng
        self.menu_frame.pack_propagate(False)

        # TIÊU ĐỀ
        title = ctk.CTkLabel(
            self.menu_frame,
            text="Pet Shop",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # THÔNG TIN USER
        name_label = ctk.CTkLabel(
            self.menu_frame,
            text=Session.full_name,
            font=("Arial", 14, "bold")
        )

        name_label.pack(pady=(0, 5))

        role_label = ctk.CTkLabel(
            self.menu_frame,
            text=Session.role,
            font=("Arial", 12)
        )

        role_label.pack(pady=(0, 15))

        # DASHBOARD
        self.add_menu_button(
            "Dashboard",
            self.show_dashboard
        )

        # CUSTOMER
        self.add_menu_button(
            "Customer",
            self.show_customer
        )

        # PET
        self.add_menu_button(
            "Pet",
            self.show_pet
        )

        # PET CARE
        self.add_menu_button(
            "Pet Care",
            self.show_petcare
        )

        # PET BOARDING
        self.add_menu_button(
            "Pet Boarding",
            self.show_boarding
        )

        # PRODUCT
        self.add_menu_button(
            "Product",
            self.show_product
        )

        # CASH
        self.add_menu_button(
            "Cash",
            self.show_cash
        )

        # REPORT
        self.add_menu_button(
            "Report",
            self.show_reports
        )

        # USER
        self.add_menu_button(
            "User",
            self.show_user
        )

        # LOGOUT
        logout_button = ctk.CTkButton(
            self.menu_frame,
            text="Logout",
            width=180,
            command=self.logout
        )

        logout_button.pack(
            side="bottom",
            pady=15
        )

        # KHU VỰC NỘI DUNG
        # CÓ THANH CUỘN
        self.content_frame = ctk.CTkScrollableFrame(
            self.window
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # HIỂN THỊ DASHBOARD ĐẦU TIÊN
        if self.has_permission("Dashboard"):
            self.show_dashboard()

    # DASHBOARD
    def show_dashboard(self):

        if not self.has_permission("Dashboard"):
            return

        self.clear_content()

        from forms.dashboard import DashboardForm

        dashboard = DashboardForm(
            self.content_frame
        )

    # CUSTOMER
    def show_customer(self):

        if not self.has_permission("Customer"):
            return

        self.clear_content()

        from forms.customer import CustomerForm

        customer_form = CustomerForm(
            self.content_frame
        )

    # PET
    def show_pet(self):

        if not self.has_permission("Pet"):
            return

        self.clear_content()

        from forms.pet import PetForm

        pet_form = PetForm(
            self.content_frame
        )

    # PET CARE
    def show_petcare(self):

        if not self.has_permission("Pet Care"):
            return

        self.clear_content()

        from forms.petcare import PetCareForm

        petcare_form = PetCareForm(
            self.content_frame
        )

    # PET BOARDING
    def show_boarding(self):

        if not self.has_permission("Pet Boarding"):
            return

        self.clear_content()

        from forms.boarding import BoardingForm

        boarding_form = BoardingForm(
            self.content_frame
        )

    # PRODUCT
    def show_product(self):

        if not self.has_permission("Product"):
            return

        self.clear_content()

        from forms.product import ProductForm

        product_form = ProductForm(
            self.content_frame
        )

    # CASH
    def show_cash(self):

        if not self.has_permission("Cash"):
            return

        self.clear_content()

        from forms.cash import CashForm

        cash_form = CashForm(
            self.content_frame
        )

    # REPORT
    def show_reports(self):

        if not self.has_permission("Report"):
            return

        self.clear_content()

        from forms.reports import ReportsForm

        reports_form = ReportsForm(
            self.content_frame
        )

    # USER
    def show_user(self):

        if not self.has_permission("User"):

            messagebox.showwarning(
                "Thông báo",
                "Bạn không có quyền truy cập chức năng này!"
            )

            return

        self.clear_content()

        from forms.users import UserForm

        user_form = UserForm(
            self.content_frame
        )

    # XÓA NỘI DUNG CŨ
    def clear_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # LOGOUT
    def logout(self):

        result = messagebox.askyesno(
            "Đăng xuất",
            "Bạn có chắc muốn đăng xuất không?"
        )

        if result:

            Session.logout()

            self.window.destroy()

            self.login_form.show_login()
