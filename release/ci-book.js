//@ts-check
"use strict";

const { execSync } = require("child_process");

function $(cmd) {
  console.log(`$ ${cmd}`);
  execSync(cmd, { stdio: "inherit" });
}

function main() {
  $("npm run build");

  if (process.env.CI_BUILD_REF_NAME) {
    $(`gsutil -m cp -r -a public-read _book/* gs://docs.itch.ovh/itch/${process.env.CI_BUILD_REF_NAME}/`);
  } else {
    console.warn("Skipping uploading book, no CI_BUILD_REF_NAME environment variable set");
  }
}

main();
