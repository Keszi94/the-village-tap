// Get all edit buttons and the edit form elements
const editButtons = document.getElementsByClassName("btn-edit");
const editForm = document.getElementById("editForm");
const submitButton = document.getElementById("submitButton");

// Get modal and delete buttons
const deleteModal = new bootstrap.Modal(document.getElementById("deleteThreadModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", function (e) {
        // Retrieve the data attributes
        let threadTitle = e.target.getAttribute("data-title");
        let threadDescription = e.target.getAttribute("data-description");
        let threadRelatedArticle = e.target.getAttribute("data-related");

        // Populate the edit form fields with the thread data
        document.getElementById("id_title").value = threadTitle;
        document.getElementById("id_description").value = threadDescription;
        document.getElementById("id_related_article").value = threadRelatedArticle;

        // Toggle the visibility of the edit form
        if (editForm.style.display === "none") {
            editForm.style.display = "block";  // Show the form
            submitButton.textContent = "Update Thread";  // Update button text to "Update"
        } else {
            editForm.style.display = "none";  // Hide the form if it was already shown
        }
    });
}

/**
 * Adds event listeners to each delete button.
 * When a delete button is clicked, the associated thread slug is set
 * and the modal is shown to confirm the deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const threadSlug = e.target.getAttribute("data-slug");
        document.getElementById("deleteSlug").value = threadSlug;  // Set the thread slug to the form input for delete confirmation
        deleteModal.show();  // Show the modal for confirmation
    });
}