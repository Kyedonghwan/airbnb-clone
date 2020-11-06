from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models

# Create your views here.


class HomeView(ListView):

    """ HombeView Defnition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        pass
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
    return render(request, "rooms/detail.html", context={"room": room})


"""
def all_rooms(request):
    page = request.GET.get("page",1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")



def all_rooms(request):
    
    page = request.GET.get("page", 1)

    
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    
    return render(
        request,
        "rooms/home.html",
        context={


            
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
            
        },
    )
"""