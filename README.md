# onepage-aptesting

Experimental extension of the [activitypub-testsuite](https://github.com/steve-bate/activitypub-testsuite) for testing [onepage.pub](https://github.com/evanp/onepage.pub).

This repository contains onepage.pub-specific code and configuration.

## Install

### Requirements

* MacOS or Linux
* Python 3.11+
* Node.js 16+

The project is currently configured to expect the `activitypub-testsuite` repository in a sibling directory. In the future, this may be modified to include `activitypub-testsuite` as a git submodule in the `onepage-aptesting` testing repository.

### Set Up

1. Create a directory to hold the repositories, `testing`, for example, but the name doesn't matter.

2. Clone the `activitypub-testsuite` into that directory and install it.

```bash
git clone https://github.com/steve-bate/activitypub-testsuite.git
cd activitypub-testsuite/
poetry install
```

3. Clone the `onepage-aptesting` repository into the `testing` directory (a sibling of the previous repository). *Note the special submodule-related argument to clone.*

```bash
git clone --recurse-submodules http://nas.lan:3000/steve/onepage-aptesting.git
```

> [!NOTE]
> The onepage.pub submodule is currently a test-related branch of my `onepage.pub` fork. This branch contains several patches to fix issues and add some test-related endpoint (which are subject to change). This project will eventually be using the primary, authoritative repository.

At this point, the directory structure should look similar to the following one.

```
testing
  ├── activitypub-testsuite
  ├── onepage-aptesting
```

4. Change to the `onepage-aptesting` directory and install it. This will do the Python (Poetry) install and run `npm init` in the `onepage.pub` submodule (the code being tested).

```
cd onepage-aptesting
sh install.sh
```

## Usage

Run the tests from `onepage-aptesting` directory. The tests will run in a Python virtual environment created by Poetry. You will need to run them using

```bash
poetry run pytest
```
or
```bash
poetry shell  # creates a shell configured with the virtual environment
pytest
```

## License

[MIT License](LICENSE.txt)
