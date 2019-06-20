$(document).ready(() => {
  $("#deploy").click(() => {
    $.ajax({
      url: '/scripts/php/deploy.php',
      success: () => {
      }
    });
  });
  $("#provision").click(() => {
    $.ajax({
      url: '/scripts/php/provision.php',
      success: () => {
      }
    });
  });
  $('#ppinstall').click(() => {
    $.ajax({
      url: '/scripts/php/ppinstall.php',
      success: () => {
      }
    });
  });
  $('#down').click(() => {
    $.ajax({
      url: '/scripts/php/down.php',
      success: () => {
      }
    });
  });
});
