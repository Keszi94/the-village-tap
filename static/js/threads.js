const editButtons = document.getElementsByClassName("btn-edit");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        const threadSlug = e.target.getAttribute("data-slug");
        const threadTitle = document.getElementById(`threadTitle-${threadSlug}`).innerText;
        const threadDescription = document.getElementById(`threadDescription-${threadSlug}`).innerText;

        // Populate the form fields
        document.getElementById("id_title").value = threadTitle;
        document.getElementById("id_description").value = threadDescription;

        // Set the form's action URL
        document.getElementById("editForm").setAttribute("action", `/forum/${threadSlug}/edit/`);
    });
}
