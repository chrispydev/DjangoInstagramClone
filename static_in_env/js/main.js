// Declearing variables
const submit = document.querySelector("#submit");

// setting functions
function form_submit() {
  submit.submit();
}
function wait()

// hooking functions
submit.addEventListener("change", form_submit);
