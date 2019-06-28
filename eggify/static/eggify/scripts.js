function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'centuryEgg');
	localStorage.setItem('theme', 'centuryEgg');
    }
    else {
        document.documentElement.setAttribute('data-theme', 'yellowEgg');
	localStorage.setItem('theme', 'yellowEgg');
    }    
}

document.addEventListener('DOMContentLoaded', function () {
  const currentTheme = localStorage.getItem('theme') || null;
  const toggleSwitch = document.querySelector('#theme-label input[type="checkbox"]');
  toggleSwitch.addEventListener('change', switchTheme, false);
  if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'centuryEgg') {
      toggleSwitch.checked = true;
    }
  }
});

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
