from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Thread, Comment
from .forms import ThreadCreationForm


# Create your views here.
def threads_page(request):
    threads = Thread.objects.filter(status=Thread.APPROVED).order_by('-created_on')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ThreadCreationForm(request.POST)
            if form.is_valid():
                thread = form.save(commit=False)
                thread.author = request.user # sets the author as the user logged in
                thread.save()
                return redirect('threads_page') # redirects the user to the same page after submission
        else:
            return redirect('login') # if user is not logged in, redirect to login page
    else:
        form = ThreadCreationForm()

    return render(request, 'forum/threads_page.html', {
        'threads': threads,
        'form': form,
    })
