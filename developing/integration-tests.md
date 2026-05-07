# Integration tests

Integration tests exercise user flows like login, navigation, and game install against a running build of the app. They use a homegrown Go runner that drives the app via ChromeDriver \(WebDriver\).

## Requirements

* **Go** to compile the test runner
* **A desktop environment**. On Linux CI, `xvfb` is used.
* **An itch.io API key** for the test account that integration tests authenticate as

The test runner downloads a specific ChromeDriver version that must match the Electron version used by the app. If you bump Electron in `package.json`, also update `integration-tests/versions.go`.

## Running integration tests

```bash
# API key for the test account
export ITCH_TEST_ACCOUNT_API_KEY="your-api-key"

# Run against a packaged build
npm run integration-tests

# Run against the dev version (faster, no packaging step)
node release/test.js --test-dev
```

To start fresh, clear the cached ChromeDriver and test artifacts:

```bash
rm -rf integration-tests/.chromedriver integration-tests/tmp integration-tests/screenshots
```

If you're an itch.io employee, ask the team about getting an API key for the test account. Open-source contributors aren't expected to run the integration suite locally; CI will run them on your PR.

## Writing an integration test

Scenarios live in `integration-tests/` alongside the runner support code. They're explicitly listed in `integration-tests/main.go`.

References:

* The [WebDriver API docs](https://webdriver.io/docs/api)
* Existing tests in the `integration-tests/` directory
