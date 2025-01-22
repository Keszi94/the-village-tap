from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Thread, Comment
from .forms import ThreadCreationForm, CommentForm



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
    
    # Fetch all the comments for the thread
    comments = thread.comment.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # Associates the comment with the thread it's left on
            comment.thread = thread
            # Sets the logged in user as the author
            comment.author = request.user
            comment.save()
            return redirect('thread_detail', slug=slug)

    else:
        form = CommentForm()        
    
    return render(request, 'forum/thread_detail.html', {
        'thread': thread,
        'comments': comments,
        'form': form,
        })


def edit_thread(request, slug):
    """
    View to edit threads
    """
    thread = get_object_or_404(Thread, slug=slug, author=request.user)

    if request.method == 'POST':
        thread.title = request.POST.get('title')
        thread.description = request.POST.get('description')
        thread.related_article_url = request.POST.get('related_article_url')
        thread.save()
        return redirect('thread_detail', slug=slug)

    return redirect('thread_detail', slug=slug)


def delete_thread(request, slug):
    """
    View to delete threads
    """
    if request.method == 'POST':
        thread = get_object_or_404(Thread, slug=slug, author=request.user)

        thread.delete()
        messages.success(request, 'Thread has been deleted successfully!')

        return redirect('threads_page')

    else:
        return HttpResponseRedirect('/')    
    

