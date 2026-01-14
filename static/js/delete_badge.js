const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    const badgeId = button.dataset.badgeId;
    console.log("Badge ID:", badgeId);                     // Logging the badge ID to console to see if the badge id is being retrieved.
    deleteConfirm.href = `/badges/delete/${badgeId}/`;
    deleteModal.show();
  });
}
