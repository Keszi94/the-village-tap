from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Thread, Comment
from .forms import ThreadCreationForm, CommentForm, ThreadEditForm


# Create your views here.
def threads_page(request):
    """
    Display a list of approved :model:`forum.Thread` and
    handle thread creation.

    **Context**
    ``threads``
        A queryset of approved :model:`forum.Thread` objects.
    ``form``
        An instance of :form:`forum.ThreadCreationForm`.

    **Template**
    :template:`forum/threads_page.html`
    """
    threads_list = Thread.objects.filter(
        status=Thread.APPROVED).order_by('-created_on')

    # Add Pagination
    paginator = Paginator(threads_list, 4)
    page_numer = request.GET.get('page')
    page_obj = paginator.get_page(page_numer)

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
                    messages.success(request, "Your thread has been posted"
                                     "successfully!")
                else:
                    thread.status = Thread.PENDING
                    messages.warning(request, "Your thread has been submitted"
                                     " and is pending approval.")
                thread.save()
                # redirects the user to the same page after submission
                return redirect('threads_page')
        else:
            # if user is not logged in, redirect to login page
            return redirect('login')
    else:
        form = ThreadCreationForm()

    return render(request, 'forum/threads_page.html', {
        'threads': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'form': form,
    })


def thread_detail(request, slug):
    """
    Display an individual :model:`forum.Thread` and its associated comments.

    **Context**

    ``thread``
        An instance of :model:`forum.Thread`.
    ``comments``
        A queryset of :model:`forum.Comment` associated with the thread.
    ``form``
        An instance of :form:`forum.CommentForm` for adding a new comment.

    **Template**
    :template:`forum/thread_detail.html`
    """
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in or register to view threads.")
        return redirect('threads_page')

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


@login_required
def edit_thread(request, slug):
    """
    Edit an existing :model:`forum.Thread` by the logged-in user.

    **Permissions**
    Only the thread author can edit it.

    **Parameters**
    ``slug``
        The unique identifier (slug) of the thread to edit.

    **Template**
    Renders :template:`forum/edit_thread.html`.

    **Behavior**
    Sets `related_article_url` to an empty string if `None`.
    Handles both GET (display form) and POST (save changes).
    """

    thread = get_object_or_404(Thread, slug=slug)

    if thread.author != request.user:
        messages.error(request, "You are not allowed to edit this thread!")
        return redirect('threads_page')

    if thread.related_article_url is None:
        thread.related_article_url = ""

    if request.method == 'POST':
        form = ThreadEditForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your thread has been successfully updated!"
                )
            return redirect('thread_detail', slug=thread.slug)
    else:
        form = ThreadEditForm(instance=thread)

    return render(request, 'forum/edit_thread.html', {
        'form': form,
        'thread': thread
        })


@login_required
def delete_thread(request, slug):
    """
    Delete a :model:`forum.Thread` created by the logged-in user.

    **Permissions**
    Only accessible by the thread author.

    **Parameters**
    ``slug``
        Unique identifier for the thread.

    Deletes the thread on POST and redirects to the threads page.

    **Template**
    Redirects to :template:`forum/threads_page.html`.
    """

    thread = get_object_or_404(Thread, slug=slug)

    if thread.author != request.user and not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorized to delete this thread!'
            )
        return redirect('thread_detail', slug=slug)

    if request.method == 'POST':
        thread.delete()
        messages.success(request, 'Thread has been deleted successfully!')
        return redirect('threads_page')
    else:
        messages.error(request, 'Invalid request!')
        return redirect('thread_detail', slug=slug)


@login_required
def comment_edit(request, slug, comment_id):
    """
    Edit a :model:`forum.Comment` on a :model:`forum.Thread`.

    **Permissions**
    Only the comment's author or a superuser can edit the comment.

    **Parameters**
    ``slug``
        Unique identifier for the thread.
    ``comment_id``
        The ID of the comment being edited.

    **Context**
    ``thread``
        The :model:`forum.Thread` the comment belongs to.
    ``comments``
        A queryset of all comments for the thread.
    ``form``
        An instance of :form:`forum.CommentForm` for editing the comment.
    ``edit_comment``
        The comment being edited.

    Handles comment updates on POST and redirects back to
    the thread detail page.

    **Template**
    :template:`forum/thread_detail.html`
    """
    # Get the thread and comment objects
    thread = get_object_or_404(Thread, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author:
        messages.error(request, 'You are not authorized to edit this comment!')
        return redirect('thread_detail', slug=slug)

    # Handles the form submission
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your comment has been updated successfully!')
            # After saving the form, redirect back to the thread_detail page
            return redirect('thread_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    # If the form is not submitted or is invalid,
    # render the thread_detail page with the form
    return render(request, 'forum/thread_detail.html', {
        'thread': thread,
        'comments': thread.comments.all(),
        'form': form,
        'edit_comment': comment,  # Passes the comment being edited
    })


@login_required
def delete_comment(request, slug, comment_id):
    """
    Delete a :model:`forum.Comment` from a :model:`forum.Thread`.

    **Permissions**
    Only the comment's author or a superuser can delete the comment.

    **Parameters**
    ``slug``
        The unique identifier of the thread.
    ``comment_id``
        The ID of the comment to be deleted.
    """
    # Get the comment by its ID
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is authorized to delete this comment (owner or admin)
    if request.user == comment.author or request.user.is_superuser:
        # Delete the comment
        comment.delete()
        messages.success(request, "The comment was deleted successfully.")
    else:
        # Unauthorized user trying to delete
        messages.error(
            request, "You are not authorized to delete this comment.")

    # After deletion, redirect to the thread detail page
    return redirect('thread_detail', slug=slug)
