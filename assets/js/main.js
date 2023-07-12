// @ts-check

(function ($) {
  var $window = $(window),
    $body = $("body"),
    $header = $("#header"),
    $footer = $("#footer"),
    $main = $("#main");

  // Breakpoints.
  breakpoints({
    xlarge: ["1281px", "1800px"],
    large: ["981px", "1280px"],
    medium: ["737px", "980px"],
    small: ["481px", "736px"],
    xsmall: [null, "480px"],
  });

  // Play initial animations on page load.
  $window.on("load", function () {
    window.setTimeout(function () {
      $body.removeClass("is-preload");
    }, 100);
  });

  // Touch?
  if (browser.mobile) {
    // Turn on touch mode.
    $body.addClass("is-touch");

    // Height fix (mostly for iOS).
    window.setTimeout(function () {
      $window.scrollTop($window.scrollTop() + 1);
    }, 0);
  }

  // Footer.
  breakpoints.on("<=medium", function () {
    $footer.insertAfter($main);
  });

  breakpoints.on(">medium", function () {
    $footer.appendTo($header);
  });
})(jQuery);
