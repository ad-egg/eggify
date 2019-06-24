function changeTheme () {
  let oppTheme = document.getElementById('theme');
  if (oppTheme.innerHTML === 'dark theme') {
    oppTheme.innerHTML = 'light theme';
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
  } else {
    oppTheme.innerHTML = 'dark theme';
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
  }
}

function copyEgg () {
  // gets the text box
  let copyText = document.getElementById('eggOutput');
  // selects the text field
  copyText.select();
  // copies text inside the text field
  document.execCommand('copy');
  // get the button
  let eggButton = document.getElementById('eggButton');
  let originalText = eggButton.innerHTML;
  eggButton.innerHTML = 'copied egg!';
  setTimeout(function () {
    eggButton.innerHTML = originalText;
  }, 2000);
}

function copyLink () {
  let copyText = document.getElementById('eggntLink');
  copyText.select();
  document.execCommand('copy');
  let linkButton = document.getElementById('linkButton');
  let originalText = linkButton.innerHTML;
  linkButton.innerHTML = 'link copied!';
  setTimeout(function () {
    linkButton.innerHTML = originalText;
  }, 2000);
}
