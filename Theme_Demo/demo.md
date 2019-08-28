# Flatiron Theme Demo

Reveal.js enables you to create beautiful interactive slide decks using HTML. This presentation demos the _*Flatiron Theme*_



## Spacer

This paragraph text is <div class="spacer"></div> separated by a spacer.

The spacer is 20px high, you can layer a few of them together.

<pre>
	<code>
<div class="spacer"></div>
	</code>
</pre>



## Slide Top Alignment

To vertically align all slides to the top of the page, add the `align-top` class to the `<section>` element in slides.html. Remove this class to revert to the default vertical centering.

<pre>
<code>
<section
  data-markdown="{{ page.markdown }}"
  data-separator="^\n\n\n"
  data-separator-vertical="^\n\n"
  data-separator-notes="^#note:"
  class="align-top"
></section>
</code>
</pre>



## Paragraph Left Alignment

This is regular paragraph text to which no default has been applied. The default is center.

<p class="align-left">This is a left 👈 aligned paragraph.</p>
<p class="align-right">This is a right 👉 aligned paragraph.</p>

<pre>
	<code>
<p class="align-left">This is a left 👈 aligned paragraph.</p>
<p class="align-right">This is a right 👉 aligned paragraph.</p> 
	</code>
</pre>


