// @ts-check
/**
 * This is a Node.js script to generate the index.html page for the Sciware website.
 * It's a little messy, sorry. — Paul Murray, 2024-02-06
 */

import fs from "node:fs";
import { execSync } from "node:child_process";

const config = {
  title: "Sciware: a scientific software development learning community",
  header_text: ``,
};

const template = html`<!DOCTYPE html>
  <html>
    <head>
      <title>${config.title}</title>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
      <link rel="shortcut icon" href="/icons/favicon.ico" />
      <link rel="stylesheet" href="assets/css/main-v2.css" />
    </head>
    <body>
      <header>
        <a href="#" style="width: 6rem; border-bottom: none;"><img src="assets/sciware.png" alt="" /></a>
        <h1>
          <strong>Sciware</strong>, a scientific<br />
          software learning community <br />
          at the <a href="http://flatironinstitute.org">Flatiron Institute</a>.
        </h1>
      </header>
      <main>main</main>
      <footer>footer</footer>
    </body>
  </html> `;

fs.writeFileSync("index-v2.html", template);

execSync("npx prettier --write index.html", { stdio: "inherit" });

function html(strings, ...values) {
  let result = "";
  for (const [i, string] of strings.entries()) {
    result += string;
    if (i >= values.length) continue;
    let value = values[i];
    // Process arrays by recursively processing each element
    if (Array.isArray(value)) {
      value = value
        .map((element) => {
          if (Array.isArray(element) || typeof element === "function") {
            return html`${element}`;
          }
          return element;
        })
        .join("\n");
    } else if (value == null) {
      // Handle undefined and null values safely
      value = "";
    }
    result += value; // Append the processed value to the result
  }
  return result;
}
