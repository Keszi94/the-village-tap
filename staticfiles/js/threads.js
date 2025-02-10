// Handle delete thread button click
document.querySelector('.delete-thread-btn').addEventListener('click', function (e) {
    e.preventDefault();

    // Get the thread slug (can be passed via a data attribute)
    const threadSlug = document.getElementById("threadSlug").value;

    // Set the form's action to the delete thread URL
    const deleteForm = document.getElementById('deleteThreadForm');
    deleteForm.action = `/forum/delete_thread/${threadSlug}/`;  // Adjust this URL pattern according to your Django URL structure

    // Show the delete modal
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteThreadModal"));
    deleteModal.show();
});
