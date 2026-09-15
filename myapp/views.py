from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from myapp.models import ContactBook, Courses

def homepage_get(request):
    return render(request, 'home.html')

def addcontact_get(request):

    courses = Courses.objects.all()

    return render(request, 'addcontact.html', {'data':courses})

def addcontact_post(request):

    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    course = request.POST['course']

    a = ContactBook()

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path

    a.name = name
    a.phone = phone
    a.email = email
    a.COURSES_id = course
    a.save()

    return JsonResponse({'status':'ok'})

def contactbook_get(request):

    courses = Courses.objects.all()

    return render(request, 'viewcontactbook.html', {'courses':courses})

def contactbook_get2(request):

    search = request.GET.get('search', '')
    page = request.GET.get('page', 1)
    course = request.GET.get('course', '')

    contacts = ContactBook.objects.all().order_by('-id')

    if search:
        contacts = contacts.filter(name__icontains = search)

    if course:
        contacts = contacts.filter(COURSES_id = course)

    paginator = Paginator(contacts, 5)
    data = paginator.get_page(page)

    l = []
    for i in data:
        l.append(
            [
                i.id,
                i.name,
                i.phone,
                i.email,
                i.COURSES.course,
                i.photo,
            ]
        )

    return JsonResponse({'status':'ok', 'data':l, 'current_page':data.number, 'total_pages':paginator.num_pages})

def editcontact_get(request, id):

    data = ContactBook.objects.get(id = id)
    courses = Courses.objects.all()

    return render(request, 'editcontact.html', {'data':data, 'courses':courses})

def editcontact_post(request):

    id = request.POST['id']
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    course = request.POST['course']

    a = ContactBook.objects.get(id = id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        a.photo = path

    a.name = name
    a.phone = phone
    a.email = email
    a.COURSES_id = course
    a.save()

    return JsonResponse({'status':'ok'})

@csrf_exempt
def deletecontact_post(request, id):

    ContactBook.objects.get(id = id).delete()

    return JsonResponse({'status':'ok'})