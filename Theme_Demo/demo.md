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



## Slide Center Alignment <!-- .slide: class="center" -->

To vertically align a single slide to the center of the page, add `.slide: class="center" ` to a comment next to the the slide header element in the markdown of this page. 

You can also use this method to apply a class to any element by adding `.element class="whatever-class-you-want"` in a comment directly to the right of the element in question.

<pre>
	<code>
## Slide Top Alignment <!-- Add the above code here INSIDE the comment-->
	</code>
</pre>



## Slide Center Alignment
If you wish to center *all* the slides vertically, change `center: false` to `center: true` in the `Reveal.initialize({})` function in `_layouts/slides.html`.

<pre>
	<code>
Reveal.initialize({
    dependencies: [
      { src: "{{site.baseurl}}/reveal.js/plugin/markdown/marked.js" },
    ],
    center: true
});
	</code>
</pre>



## Paragraph Alignment

This is regular paragraph text to which no default has been applied. The default is center.

<p class="align-left">This is a left 👈 aligned paragraph.</p>
<p class="align-right">This is a right 👉 aligned paragraph.</p>

<pre>
	<code>
<p class="align-left">This is a left 👈 aligned paragraph.</p>
<p class="align-right">This is a right 👉 aligned paragraph.</p> 
	</code>
</pre>