from django.urls import path
from . import views

urlpatterns = [
    # ------------------ STATIC PAGES ------------------
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

  #--------------------------Admin Routes ------------------------------------------------

    path('admin/login_form/', views.admin_login_form_view, name="admin_login_form"),
    path('admin/dashboard/', views.admin_dashboard_view, name="admin_dashboard"),
    path('admin/logout/', views.admin_logout_view, name="admin_logout"),
    path('admin/delete_bird/<int:bird_id>/', views.admin_delete_bird_view, name="admin_delete_bird"),
    path('admin/edit_bird/<int:bird_id>/', views.admin_edit_bird_view, name='admin_edit_bird'),
    path('admin/add_bird/', views.admin_add_bird_view, name='admin_add_bird'),  


  # CRUD for Customer
    path('admin/customer/add/', views.admin_add_customer_view, name='admin_add_customer'),
    path('admin/customer/edit/<int:customer_id>/', views.admin_edit_customer_view, name='admin_edit_customer'),
    path('admin/customer/delete/<int:customer_id>/', views.admin_delete_customer_view, name='admin_delete_customer'),

    # CRUD for Vendor
    path('admin/vendor/add/', views.admin_add_vendor_view, name='admin_add_vendor'),
    path('admin/vendor/edit/<int:vendor_id>/', views.admin_edit_vendor_view, name='admin_edit_vendor'),
    path('admin/vendor/delete/<int:vendor_id>/', views.admin_delete_vendor_view, name='admin_delete_vendor'),



    # ------------------ CUSTOMER ROUTES ------------------
    path('customer/signup_form/', views.customer_signup_form_view, name="customer_signup_form"),
    path('customer/login_form/', views.customer_login_form_view, name="customer_login_form"),
    path('customer/check_login/', views.customer_login_user_view, name='customer_check_login'),
    path('customer/products/', views.customer_product_list_view, name='customer_product_list'),
    path('customer/logout/', views.customer_logout_view, name='customer_logout'),

    # ------------------ VENDOR ROUTES ------------------
    path('vendor/signup_form/', views.vendor_signup_form_view, name="vendor_signup_form"),
    path('vendor/login_form/', views.vendor_login_form_view, name="vendor_login_form"),
    path('vendor/check_login/', views.check_vendor_login_form_view, name="check_vendor_login_form"),
    path('vendor/page/', views.vendor_page_view, name="vendor_page"),
    path('vendor/upload/', views.vendor_upload_bird_view, name='vendor_upload'),
    path('vendor_products/', views.vendor_product_list_view, name='vendor_product_list'),
    path('vendor/dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'),
    path('vendor/logout/', views.vendor_logout_view, name='vendor_logout'),
]
