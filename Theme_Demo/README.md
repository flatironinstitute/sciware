# Reveal.js

## Flatiron Theme

This folder contains a custom Sass theme for reveal.js called `flatiron.scss.` It is currently installed in this repo. Installation instructions for other projects can be found below.

- [theme demo](https://flatironinstitute.github.io/sciware/Theme_Demo/slides.html) ([source](demo.md))

## Installation

To install the Flatiron theme you will need to remove any existing custom themes (identifiable by `id="theme"`) and add the line below in index.html:

`<link rel="stylesheet" href="css/theme/flatiron.css" id="theme">`

### Basic Setup

Copy `flatiron.css` into `css/theme` and reload your browser.

### Full Setup

If you are running reveal.js from a local Node server, add `flatiron.scss` to `css/theme/source`. The theme will be automatically compiled by Grunt from Sass to CSS (see the Gruntfile) when you run `npm start.` You can force a rebuild of the Sass by running `npm run build -- css-themes`.

## Usage

This theme will add Flatiron colors and logo to your presentation. It also comes with a few utility classes.

### Generic Spacer

You can add additional space by inserting the HTML below into the markdown. The spacer is 20px high.

`<div class="spacer"></div>`

### Right/Left Alignment

Center is the default text alignment. You can alter this by adding HTML classes and element tags into the markdown.

`<p class="align-left">This is a left aligned paragraph.</p>`

`<p class="align-right">This is a right aligned paragraph.</p>`

### Top Alignment

To vertically align all slides to the top of the page, add class="align-top" to the `<section>` element in `slides.html`. Remove this property to revert to the default vertical centering.

## More Info

- [Reveal.js Theming](https://github.com/hakimel/reveal.js/blob/master/README.md#theming)
