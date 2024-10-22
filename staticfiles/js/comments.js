const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/** 
 * This is effectively DRY code for the comment edit buttons, from the Codestar
 * blog. Attribution to the tutorial, however, there is original JS elsewhere.
 * 
 */

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
      // Get the comment ID from the button attribute
      let commentId = e.target.getAttribute("comment_id");
      // Gets the comment body content
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      // Navigates to the parent element of the comment body
      let commentDiv = document.getElementById(`comment${commentId}`).parentElement;
      // Gets the comment title
      let commentTitle = commentDiv.previousElementSibling.innerText;
      // A clumsy way of getting the comment review, by going down two divs
      let reviewParagraph = commentDiv.nextElementSibling.nextElementSibling;
      let commentReview = reviewParagraph.innerText;
      // Populates the form fields with the retrieved values
      commentText.value = commentContent;
      commentTitleInput.value = commentTitle;
      commentReviewInput.value = commentReview;
      // Updates the submit button text to "Update"
      submitButton.innerText = "Update";
      // Sets the form action to the appropriate edit URL
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}


/**
* This shows a delete modal. The modal will ask and confirm if the user wants to delete.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

/**
 * Some simple event listeners to make some things more frilly
 */

editButtons.addEventListener("mouseover", darkenBackground);
deleteButtons.addEventListener("mouseover", darkenBackground);

function darkenBackground(e) {
  e.currentTarget.style.backgroundColor = "#7eadff";
}