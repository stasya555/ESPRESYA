from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Drink, Poster
from .forms import DrinkForm, PosterForm

ADMIN_PASSWORD = "mysecretpassword"

def admin_login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('admin_panel')
        else:
            return render(request, 'admin_login.html', {'error': 'Неверный пароль'})
    return render(request, 'admin_login.html')

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('is_admin'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_required
def admin_panel(request):
    drinks = Drink.objects.all()
    posters = Poster.objects.all()

    if request.method == 'POST':
        if 'add_drink' in request.POST:
            drink_form = DrinkForm(request.POST, request.FILES)
            if drink_form.is_valid():
                drink_form.save()
                return redirect('admin_panel')
        elif 'add_poster' in request.POST:
            poster_form = PosterForm(request.POST, request.FILES)
            if poster_form.is_valid():
                poster_form.save()
                return redirect('admin_panel')
    else:
        drink_form = DrinkForm()
        poster_form = PosterForm()

    return render(request, 'admin_panel.html', {
        'drink_form': drink_form,
        'poster_form': poster_form,
        'drinks': drinks,
        'posters': posters,
    })

@admin_required
def edit_drink(request, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = DrinkForm(instance=drink)
    return render(request, 'edit_drink.html', {'form': form, 'drink': drink})

@admin_required
def delete_drink(request, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)
    if request.method == 'POST':
        drink.delete()
        return redirect('admin_panel')
    return render(request, 'confirm_delete.html', {'object': drink, 'type': 'напиток'})

@admin_required
def edit_poster(request, poster_id):
    poster = get_object_or_404(Poster, id=poster_id)
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES, instance=poster)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = PosterForm(instance=poster)
    return render(request, 'edit_poster.html', {'form': form, 'poster': poster})

@admin_required
def delete_poster(request, poster_id):
    poster = get_object_or_404(Poster, id=poster_id)
    if request.method == 'POST':
        poster.delete()
        return redirect('admin_panel')
    return render(request, 'confirm_delete.html', {'object': poster, 'type': 'постер'})

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'our-story.html')


# def afisha(request):
#     return render(request, 'afisha.html')


def afisha(request):
    posters = Poster.objects.all()
    return render(request, 'afisha.html', {'posters':posters})


# def menu(request):
#     return render(request, 'menu.html')
def menu(request):
    category = request.GET.get('category', 'all')

    if category == 'all':
        drinks = Drink.objects.all()
    else:
        drinks = Drink.objects.filter(category=category)

    return render(request, 'menu.html', {
        'drinks': drinks,
        'active_category': category,
    })

def location(request):
    return render(request, 'location.html')


def admin_panel(request):
    drinks = Drink.objects.all()
    posters = Poster.objects.all()

    if request.method == 'POST':
        if 'add_drink' in request.POST:
            drink_form = DrinkForm(request.POST, request.FILES)
            if drink_form.is_valid():
                drink_form.save()
                return redirect('admin_panel')
        elif 'add_poster' in request.POST:
            poster_form = PosterForm(request.POST, request.FILES)
            if poster_form.is_valid():
                poster_form.save()
                return redirect('admin_panel')
    else:
        drink_form = DrinkForm()
        poster_form = PosterForm()

    return render(request, 'admin_panel.html', {
        'drink_form': drink_form,
        'poster_form': poster_form,
        'drinks': drinks,
        'posters': posters,
    })

def contact(request):
    return render(request, 'contact.html')




from django.core.mail import send_mail
from django.shortcuts import render

def location(request):
    message_sent = False

    if request.method == 'POST':
        print('POST запрос получен')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') or 'не указан'
        message = request.POST.get('message')

        subject = f'Новое сообщение от {name}'
        full_message = (
            f'Имя: {name}\n'
            f'Email: {email}\n'
            f'Телефон: {phone}\n\n'
            f'Сообщение:\n{message}'
        )

        print('Готовлюсь отправлять письмо...')
        print(full_message)  # ← 3

        try:
            send_mail(
                subject,
                full_message,
                'dorozkinaanastasia05@gmail.com',
                ['dorozkinaanastasia05@gmail.com'],
                fail_silently=False,
            )
            print('Письмо отправлено!')
        except Exception as e:
            print('Ошибка при отправке письма:', e)

        message_sent = True

    return render(request, 'location.html', {'message_sent': message_sent})