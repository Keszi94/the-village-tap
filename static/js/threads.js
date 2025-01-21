const editButtons = document.getElementsByClassName("btn-edit");
const editForm = document.getElementById("editForm");
const submitButton = document.getElementById("submitButton");

// Get modal and delete buttons
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 * For each button in the `editButtons` collection:
 * - Retrieves the associated thread's title and description upon click.
 * - Populates the `editForm` with the thread's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_thread/{slug}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", function (e) {
        let threadTitle = e.target.getAttribute("data-title");
        let threadDescription = e.target.getAttribute("data-description");
        let threadRelatedArticle = e.target.getAttribute("data-related");

        document.getElementById("id_title").value = threadTitle;
        document.getElementById("id_description").value = threadDescription;
        document.getElementById("id_related_article").value = threadRelatedArticle;

        // Toggle the visibility of the edit form
        if (editForm.style.display === "none") {
            editForm.style.display = "block";  // Show the form
        } else {
            editForm.style.display = "none";  // Hide the form again
        }
    });
}

// Add event listeners to delete buttons
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const threadSlug = e.target.getAttribute("data-slug");
        document.getElementById("deleteSlug").value = threadSlug;
        deleteModal.show();  // Show the modal for confirmation
    });
}