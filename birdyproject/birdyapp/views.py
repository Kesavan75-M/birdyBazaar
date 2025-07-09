from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer, Vendor, BirdProduct

# --------------------- STATIC PAGES ---------------------
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            user_type=user_type,
            message=message
        )
        return render(request, 'contact.html', {'success': True})
    
    return render(request, 'contact.html')


from django.shortcuts import render, redirect
from .models import Admin
from django.contrib import messages

# Home login logic - from your earlier code
def login_view(request):
    if request.method == "POST":
        action = request.POST.get("action")
        user_type = request.POST.get("user_type")

        if user_type == "customer":
            return redirect('customer_signup_form' if action == "signup" else "customer_login_form")
        elif user_type == "vendor":
            return redirect('vendor_signup_form' if action == "signup" else "vendor_login_form")
        elif user_type == "admin":
            if action == "login":
                return redirect("admin_login_form")  
            else:
                messages.error(request, " Admin cannot sign up.")
        else:
            messages.error(request, " Please select a valid user type.")

    return render(request, 'login.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer, Vendor, BirdProduct, Contact, Admin

# --------------------- STATIC PAGES ---------------------
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            user_type=user_type,
            message=message
        )
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')

# --------------------- LOGIN ---------------------
def login_view(request):
    if request.method == "POST":
        action = request.POST.get("action")
        user_type = request.POST.get("user_type")

        if user_type == "customer":
            return redirect('customer_signup_form' if action == "signup" else "customer_login_form")
        elif user_type == "vendor":
            return redirect('vendor_signup_form' if action == "signup" else "vendor_login_form")
        elif user_type == "admin":
            if action == "login":
                return redirect("admin_login_form")
            else:
                messages.error(request, "Admin cannot sign up.")
        else:
            messages.error(request, "Please select a valid user type.")

    return render(request, 'login.html')

# --------------------- ADMIN ---------------------
def admin_login_form_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(username=username, password=password)
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')
        except Admin.DoesNotExist:
            return render(request, 'admin/admin_login_form.html', {'error': 'Invalid credentials'})

    return render(request, 'admin/admin_login_form.html')

def admin_dashboard_view(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login_form')

    context = {
        'customers': Customer.objects.all(),
        'vendors': Vendor.objects.all(),
        'birds': BirdProduct.objects.all()
    }
    return render(request, 'admin/dashboard.html', context)

def admin_logout_view(request):
    request.session.flush()
    return redirect('admin_login_form')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vendor, BirdProduct

def admin_add_bird_view(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login_form')

    if request.method == "POST":
        bird_type = request.POST.get("bird_type")
        niram = request.POST.get("niram")
        weight = request.POST.get("weight")
        age = request.POST.get("age")
        price = request.POST.get("price")
        vendor_id = request.POST.get("vendor_id")

        print("Vendor ID from form:", vendor_id)

        # Check if vendor_id is missing or invalid
        if not vendor_id or not vendor_id.isdigit():
            messages.error(request, "Invalid or missing vendor ID.")
            return redirect("admin_add_bird")

        # Fetch vendor safely
        vendor = get_object_or_404(Vendor, id=int(vendor_id))

        # Create and save BirdProduct
        BirdProduct.objects.create(
            vendor=vendor,
            bird_type=bird_type,
            niram=niram,
            weight=weight,
            age=age,
            price=price,
            image=request.FILES.get("image"),
            video=request.FILES.get("video"),
            father_image=request.FILES.get("father_image"),
            father_video=request.FILES.get("father_video")
        )

        messages.success(request, "Bird added successfully!")
        return redirect("admin_dashboard")

    # For GET requests, show the add bird form with vendors
    vendors = Vendor.objects.all()
    return render(request, "admin/add_bird.html", {"vendors": vendors})



def admin_edit_bird_view(request, bird_id):
    bird = get_object_or_404(BirdProduct, id=bird_id)
    if request.method == "POST":
        bird.bird_type = request.POST.get('bird_type')
        bird.niram = request.POST.get('niram')
        bird.weight = request.POST.get('weight')
        bird.age = request.POST.get('age')
        bird.price = request.POST.get('price')
        if 'image' in request.FILES: bird.image = request.FILES['image']
        if 'video' in request.FILES: bird.video = request.FILES['video']
        if 'father_image' in request.FILES: bird.father_image = request.FILES['father_image']
        if 'father_video' in request.FILES: bird.father_video = request.FILES['father_video']
        bird.save()
        return redirect('admin_dashboard')
    return render(request, 'admin/edit_bird.html', {'bird': bird})

def admin_delete_bird_view(request, bird_id):
    get_object_or_404(BirdProduct, id=bird_id).delete()
    return redirect('admin_dashboard')

# Customer CRUD
def admin_add_customer_view(request):
    if request.method == 'POST':
        Customer.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password']
        )
        return redirect('admin_dashboard')
    return render(request, 'admin/add_customer.html')

def admin_edit_customer_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.username = request.POST['username']
        customer.email = request.POST['email']
        customer.phone = request.POST['phone']
        customer.password = request.POST['password']
        customer.save()
        return redirect('admin_dashboard')
    return render(request, 'admin/edit_customer.html', {'customer': customer})

def admin_delete_customer_view(request, customer_id):
    get_object_or_404(Customer, id=customer_id).delete()
    return redirect('admin_dashboard')

# Vendor CRUD
def admin_add_vendor_view(request):
    if request.method == 'POST':
        Vendor.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password']
        )
        return redirect('admin_dashboard')
    return render(request, 'admin/add_vendor.html')

def admin_edit_vendor_view(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    if request.method == 'POST':
        vendor.username = request.POST['username']
        vendor.email = request.POST['email']
        vendor.phone = request.POST['phone']
        vendor.password = request.POST['password']
        vendor.save()
        return redirect('admin_dashboard')
    return render(request, 'admin/edit_vendor.html', {'vendor': vendor})

def admin_delete_vendor_view(request, vendor_id):
    get_object_or_404(Vendor, id=vendor_id).delete()
    return redirect('admin_dashboard')





# --------------------- CUSTOMER ---------------------
def customer_signup_form_view(request):
    if request.method == "POST":
        Customer.objects.create(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            password=request.POST.get("password")
        )
        return redirect('login')
    return render(request, 'customer/signup_form.html')

def customer_login_form_view(request):
    return render(request, 'customer/login_form.html')

def customer_login_user_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email, password=password)
            request.session['customer_id'] = customer.id  # Save to session
            return redirect("customer_product_list")
        except Customer.DoesNotExist:
            return render(request, 'customer/login_form.html', {
                'error': 'Something Wrong Please Try Again !'
            })

def customer_product_list_view(request):
    bird_type = request.GET.get('bird_type')
    niram = request.GET.get('niram')
    weight = request.GET.get('weight')
    age = request.GET.get('age')

    products = BirdProduct.objects.all()

    if bird_type:
        products = products.filter(bird_type__iexact=bird_type)
    if niram:
        products = products.filter(niram__icontains=niram)
    if weight:
        products = products.filter(weight=weight)
    if age:
        products = products.filter(age=age)

    return render(request, 'customer/product_list.html', {'products': products})

def customer_logout_view(request):
    request.session.flush()
    return redirect('login')

# --------------------- VENDOR ---------------------
def vendor_signup_form_view(request):
    if request.method == "POST":
        Vendor.objects.create(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            password=request.POST.get("password")
        )
        return redirect('login')
    return render(request, 'vendor/signup_form.html')

def vendor_login_form_view(request):
    return render(request, 'vendor/login_form.html')

def check_vendor_login_form_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            vendor = Vendor.objects.get(email=email, password=password)
            request.session['vendor_id'] = vendor.id  # Save vendor ID to session
            return redirect("vendor_page")
        except Vendor.DoesNotExist:
            return render(request, 'vendor/login_form.html', {
                'error': 'Something Wrong Please Retry !'
            })

def vendor_page_view(request):
    return render(request, 'vendor/vendor_page.html')

def vendor_upload_bird_view(request):
    if request.method == "POST":
        bird_type = request.POST.get("bird_type")
        niram = request.POST.get("niram")
        weight = request.POST.get("weight")
        age = request.POST.get("age")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        video = request.FILES.get("video")
        father_image = request.FILES.get("father_image")
        father_video = request.FILES.get("father_video")

        # Field validations
        if not all([bird_type, niram, weight, age, price, image, father_image]):
            messages.error(request, "All required fields must be filled!")
            return redirect('vendor_upload')

        # Get vendor from session
        vendor_id = request.session.get('vendor_id')
        if not vendor_id:
            messages.error(request, "You must be logged in as a vendor.")
            return redirect('vendor_login_form')

        vendor = Vendor.objects.get(id=vendor_id)

        BirdProduct.objects.create(
            vendor=vendor,
            bird_type=bird_type,
            niram=niram,
            weight=weight,
            age=age,
            price=price,
            image=image,
            video=video,
            father_image=father_image,
            father_video=father_video,
        )
        messages.success(request, " Bird uploaded successfully!")
        return redirect('vendor_dashboard')

    return render(request, 'vendor/upload.html')

def vendor_dashboard_view(request):
    vendor_id = request.session.get('vendor_id')
    if not vendor_id:
        return redirect('vendor_login_form')
    vendor = Vendor.objects.get(id=vendor_id)
    products = BirdProduct.objects.filter(vendor=vendor)
    return render(request, 'vendor/dashboard.html', {'products': products})

def vendor_product_list_view(request):
    products = BirdProduct.objects.all()
    return render(request, 'vendor/vendor_product.html', {'products': products})

def vendor_logout_view(request):
    request.session.flush()
    return redirect('login')



