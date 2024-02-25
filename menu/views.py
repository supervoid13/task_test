from django.shortcuts import render, redirect
from .models import Item


def index(request):
    return redirect("main")


def show_menus(request):
    menus = Item.objects.filter(parent__isnull=True)
    return render(request,
                  "index.html",
                  {
                      "menus": menus,
                  }
                  )


def pick_menu(request, path):
    tree = path.split("/")
    return render(request,
                  "pick_menu.html",
                  {
                      "tree": tree,
                      "max_level": len(tree) + 1,
                  })
