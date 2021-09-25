from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/shows/{show_id}/edit')
    else:
        update_show = Show.objects.get(id=show_id)
        update_show.title = request.POST['title']
        update_show.network = request.POST['network']
        update_show.release_date = request.POST['release_date']
        update_show.description = request.POST['description']
        update_show.save()
        messages.success(request, "Show successfully updated")
    return redirect(f'/shows/{show_id}')


def index(request):

    return render(request, 'index.html')  # Create your views here.


def create(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')
    else:
        new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"],
        release_date=request.POST["release_date"], 
        description=request.POST["description"])
    return redirect(f'/shows/{new_show.id}')

# def update(request, show_id):
    update_show = Show.objects.get(id=show_id)

    if request.POST["title"] != "":
        update_show.title = request.POST["title"]
        update_show.save()

    if request.POST["network"] != "":
        update_show.network = request.POST["network"]
        update_show.save()

    if request.POST["release_date"] != "":
        update_show.release_date = request.POST["release_date"]
        update_show.save()

    if request.POST["description"] != "":
        update_show.description = request.POST["description"]
        update_show.save()

    return redirect(f'/shows/{show_id}')


def all_shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'all_shows.html', context)


def edit(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        "one_show": this_show
    }
    return render(request, 'edit.html', context)


def profile(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        "one_show": this_show
    }
    return render(request, 'profile.html', context)


def delete(request, show_id):
    delete_this_show = Show.objects.get(id=show_id)
    delete_this_show.delete()
    return redirect('/shows/deleted')


def deleted(request):

    return render(request, 'deleted.html')
