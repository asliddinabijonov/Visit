from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

TurUser = get_user_model()

# === 1. RO‘YXATDAN O‘TISH (REGISTER) ===
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        user_type = request.POST.get('user_type', '')
        phone = request.POST.get('phone', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        avatar = request.FILES.get('avatar')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # === Tekshiruvlar ===
        if not all([username, email, user_type, phone, country, city, password1, password2]):
            messages.error(request, "⚠️ Barcha maydonlarni to‘ldiring.")
            return render(request, self.template_name)

        if username != username.lower():
            messages.error(request, "⚠️ Foydalanuvchi nomi faqat kichik harflarda bo‘lishi kerak.")
            return render(request, self.template_name)

        if password1 != password2:
            messages.error(request, "⚠️ Parollar bir-biriga mos emas.")
            return render(request, self.template_name)

        if TurUser.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Bu foydalanuvchi nomi allaqachon mavjud.")
            return render(request, self.template_name)

        if TurUser.objects.filter(email=email).exists():
            messages.error(request, "⚠️ Ushbu email allaqachon ro‘yxatdan o‘tgan.")
            return render(request, self.template_name)

        # === Yangi foydalanuvchi yaratish ===
        TurUser.objects.create_user(
            username=username,
            email=email,
            user_type=user_type,
            phone=phone,
            country=country,
            city=city,
            avatar=avatar,
            password=password1
        )

        messages.success(request, "✅ Muvaffaqiyatli ro‘yxatdan o‘tdingiz! Endi kirish sahifasiga o‘ting.")
        return redirect('login')


# === 2. LOGIN ===
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, "⚠️ Iltimos, foydalanuvchi nomi va parolni kiriting.")
            return render(request, self.template_name)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"👋 Xush kelibsiz, {user.username.title()}!")
            return redirect('home')  # O‘zingizning asosiy sahifangiz nomi bilan almashtiring
        else:
            messages.error(request, "❌ Noto‘g‘ri foydalanuvchi nomi yoki parol.")
            return render(request, self.template_name)


# === 3. LOGOUT ===
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "👋 Siz tizimdan chiqdingiz.")
        return redirect('/')
