from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
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
                # sets the author as the user logged in
                thread.author = request.user 
                # automatically approve threads created by a superuser
                if request.user.is_superuser: 
                    thread.status = Thread.APPROVED
                else:
                        thread.status = Thread.PENDING
                thread.save()
                # redirects the user to the same page after submission
                return redirect('threads_page') 
        else:
            # if user is not logged in, redirect to login page
            return redirect('login') 
    else:
        form = ThreadCreationForm()

    return render(request, 'forum/threads_page.html', {
        'threads': threads,
        'form': form,
    })


def thread_detail(request, slug):
    thread = Thread.objects.get(slug=slug)
    return render(request, 'forum/thread_detail.html', {'thread': thread})


def edit_thread(request, slug):
    thread = get_object_or_404(Thread, slug=slug, author=request.user)

    if request.method == 'POST':
        thread.title = request.POST.get('title')
        thrread.description = request.POST.get('description')
        thread.save()
        return redirect('thread_detail', slug=slug)

    return redirect('thread_detail', slug=slug)        
    
