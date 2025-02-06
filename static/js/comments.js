document.addEventListener("DOMContentLoaded", function() {
    // Handling Edit Button for Comments
    const editButtons = document.getElementsByClassName("comment-edit-btn");
    
    for (let button of editButtons) {
        button.addEventListener("click", function (e) {
            let commentId = e.target.getAttribute("data-id");
            let commentContent = e.target.getAttribute("data-content");

            // Get the form and textarea based on the comment ID with a unique identifier
            const commentEditForm = document.getElementById(`comment-edit-form-${commentId}`);
            const commentTextArea = document.getElementById(`comment-id_content-${commentId}`);

            // Ensure the form and textarea are found
            if (commentEditForm && commentTextArea) {
                // Set the comment content into the textarea for editing
                commentTextArea.value = commentContent;

                // Toggle visibility of the form
                if (commentEditForm.style.display === "block") {
                    commentEditForm.style.display = "none"; // Hide the form if it's currently visible
                } else {
                    commentEditForm.style.display = "block"; // Show the form if it's hidden
                }
            } else {
                console.error("Form or textarea not found for comment ID:", commentId);
            }
        });
    }

    // Handling Delete Button for Comments
    const deleteButtons = document.getElementsByClassName("comment-delete-btn");
    
    for (let button of deleteButtons) {
        button.addEventListener("click", function (e) {
            let commentId = e.target.getAttribute("data-id");

            // Gets the modal form and updates the action attribute
            const deleteCommentForm = document.getElementById("deleteCommentForm");
            if (deleteCommentForm) {
                const threadSlug = document.getElementById("threadSlug").value;
                deleteCommentForm.action = `/forum/delete_comment/${threadSlug}/${commentId}/`;
            } else {
                console.error("Delete form not found in the modal.");
            }

            // Show the delete modal 
            const deleteModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
            deleteModal.show();
        });
    }
});
