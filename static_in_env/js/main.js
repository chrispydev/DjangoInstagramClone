// Declaring variables
const submit = document.querySelector("#submit");

// setting functions
function form_submit() {
  submit.submit();
}

function wait() {
  setTimeout(form_submit, 6000);
}

// hooking functions
submit.addEventListener("change", wait);
