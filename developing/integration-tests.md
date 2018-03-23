# Integration tests

Whereas unit tests are small, fast, and test code directly \(trying not to hit slow things like the filesystem, the network, etc.\), **integration tests** are the opposite.

They make sure that all of the code, together, makes meaningful interactions happen.

> Speaking of: if you haven't read the [Unit tests](unit-tests.md) section already, go do that first.

The app is tested as a whole using a homegrown golang runner that speaks webdriver to the app.

### Running integration tests

It looks deceptively simple:

```bash
npm run integration-tests
```

But it'll error out pretty soon if you don't have the right environment variables set.

If you're an itch.io employee, poke Amos about it to get set up. If you're not, well consider this page "light reading" - open-source contributors are expected to run \(and write!\) unit tests, not integration tests.

We'll take care of that part!

### Writing an integration test

Scenarios live in `integration-tests`, along with some support code that makes it all tick. They're also explicitly listed in `integration-tests/main.go`.

These resources can be useful:

* The [webdriver API docs](http://webdriver.io/api.html)
* Existing tests!



