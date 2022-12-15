textarea = document.querySelector('#textarea');
buttons_container = document.querySelector('#buttons-container');
buttons_container.classList.add("visible-flex");

header_button = document.querySelector('#header');
italics_button = document.querySelector('#italics');
underline_button = document.querySelector('#underline');
bold_button = document.querySelector('#bold');

const getUserSelection = () => {
  const text = textarea.value;
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  return text.substring(start, end);
}

const replaceInTextarea = (replacement) => {
  const text = textarea.value;
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  return text.slice(0, start) + replacement + text.slice(end);
}

const wrapSelectionWith = (tag) => {
  const selection = getUserSelection();
  const newText = replaceInTextarea(`<${tag}>${selection}</${tag}>`);
  textarea.value = newText;
}

//prevent default is required, because otherwise the form would be sent for some reason.
header_button.addEventListener('click', event => {
  event.preventDefault();
  wrapSelectionWith('h2');
})

italics_button.addEventListener('click', event => {
  event.preventDefault();
  wrapSelectionWith('i');
})

underline_button.addEventListener('click', event => {
  event.preventDefault();
  wrapSelectionWith('u');
})

bold_button.addEventListener('click', event => {
  event.preventDefault();
  wrapSelectionWith('b');
})

console.log(textarea)
