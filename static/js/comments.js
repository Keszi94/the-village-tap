document.addEventListener("DOMContentLoaded", function() {
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

                // Display the form 
                commentEditForm.style.display = "block";
            } else {
                console.error("Form or textarea not found for comment ID:", commentId);
            }
        });
    }
});
