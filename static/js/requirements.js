document.addEventListener("DOMContentLoaded", function () {                         //Waits for the html page to load

    const addButton = document.getElementById("add-requirement");
    const container = document.getElementById("requirements-container");
    const totalForms = document.getElementById("id_requirements-TOTAL_FORMS");
    const emptyForm = document.getElementById("empty-form");

    // Safety check (prevents JS errors on pages without this form)
    if (!addButton || !container || !totalForms || !emptyForm) {
        return;
    }

    addButton.addEventListener("click", function () {
        let formCount = parseInt(totalForms.value);                                 //Gets the current number of forms
        let newFormHtml = emptyForm.innerHTML.replace(/__prefix__/g, formCount);    //Replaces the "__prefix__" that was created by DJango with the current form number

        container.insertAdjacentHTML("beforeend", newFormHtml);                     //Add the new form to the page
        totalForms.value = formCount + 1;                                           //Increases the form count by 1
    });

});