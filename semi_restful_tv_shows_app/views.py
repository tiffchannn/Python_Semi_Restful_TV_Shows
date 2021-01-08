from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show

  # update -> redirect(f"/shows/{{show_id}}") OR redirect('/shows' + request.POST['show_id'])

def index(request):

  context = {
    'all_shows': Show.objects.all()
  }

  return render(request, 'index.html', context)

def display_shows(request):
  # will display all tv shows
  print('*'*80)
  print('This is coming from display shows function! ----')

  context = {
    'all_shows': Show.objects.all()
  }

  return render(request, 'all_shows.html', context)

#method should return a template containing the form for adding a new TV show
def get_shows_new(request):
  print('*'*80)
  print('This is from add a new show! ---- ')

  return render(request, 'add_new_show.html') # will redirect to added show's info page

def post_new(request):
  print('New show was created! ----- ')

  # if request.method == 'POST':
  errors = Show.objects.getErrors(request.POST)

  if len(errors) > 0:
    print('There are errors!! --- ')
    for key, value in errors.items():
        messages.error(request, value, tags=key)
    return redirect(f'/shows/new')
  else:
    form_title = request.POST['title']
    form_network = request.POST['network']
    form_release_date = request.POST['release_date']
    form_description = request.POST['description']

    new_show = Show.objects.create(
        title=form_title,
        network=form_network,
        release_date=form_release_date,
        description=form_description
        )

    print('New Show:', new_show)

  return redirect(f"/shows/{new_show.id}")


def show_info(request, show_id):
  print('*'*80)
  print('This is from show info ----')

  context = {
    'this_show': Show.objects.get(id=show_id)
  }
  return render(request, 'show_info.html', context)

def edit_show(request, show_id):
  print('*'*80)
  print('This is from edit show ----')

  context = {
    'this_show': Show.objects.get(id=show_id)
  }

  print('Show was updated!', request.POST)
  return render(request, 'edit_show.html', context)

def update(request):
  show_id = int(request.POST['show_id'])

  if request.method == 'POST':
    errors = Show.objects.getErrors(request.POST)

  if len(errors) > 0:
    for key, value in errors.items():
        messages.error(request, value)
    return redirect(f'/shows/{show_id}/edit')
  else:
    show_to_update = Show.objects.get(id=show_id)

    show_to_update.title = request.POST['title']
    show_to_update.network = request.POST['network']
    show_to_update.release_date = request.POST['release_date'] # must be in YYYY-MM-DD format."
    show_to_update.description = request.POST['description']

    show_to_update.save()

    print('!'*80)
    print('Show was updated!', request.POST)
    return redirect(f'/shows/{show_id}')


def delete_show(request, show_id):
  print('This is from delete show')

  this_show = Show.objects.get(id=show_id)
  this_show.delete()

  return redirect('/shows')