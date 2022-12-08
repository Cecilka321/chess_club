from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members


def index(request):
    return render(request, 'index.html')


def academy(request):
    return render(request, 'academy.html')


def contacts(request):
    return render(request, 'contacts.html')


def gallery(request):
    return render(request, 'gallery.html')


def history(request):
    return render(request, 'history.html')


def members(request):
    members_list = Members.objects.all()
    return render(request, 'members.html', {'members_list': members_list})


def detail(request, pk):
    member_by_id = Members.objects.get(pk=pk)
    return render(request, 'detail.html', {'member_by_id': member_by_id})


def news(request):
    return render(request, 'news.html')


def tournaments(request):
    return render(request, 'tournaments.html')


def attribution(request):
    return render(request, 'attribution.html')





#   def member_view(request):
#       club_member = Members.objects.all().values()
#       output = ""
#       context = {'club_members': club_member}
#       for x in club_member:
#           output += x["firstname"]
#       return render(request, 'members.html', context)

# funkce render() má první argument REQUEST OBJECT (požadovaný objekt) druhý argument TEMPLATE NAME a třetí argumentem
# je optional DICTATIONARY (slovník jako třetí volitelný arument)
# dávám tam dohodu že dictationary pojmenuji kontext





