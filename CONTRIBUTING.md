# Contributing to XYZ

In this guide you will get an overview of the the different ways to contribute and the contribution approval process.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[Getting Started](#getting-started)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Code Contribution](#code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [TODO LANG Styleguide](#javascript-styleguide)
  * [Documentation Styleguide](#documentation-styleguide)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## Code of Conduct

This project is governed by the [XYZ Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. 

## Getting Started

To get an overview of the project, read the [README](README.md).

## How Can I Contribute?

### Reporting Bugs

Create an issue explaining the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** 
* **Describe the exact steps which reproduce the problem** 
* **Can you reliably reproduce the issue?** 
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots**

### Suggesting Enhancements

Create an issue for the enhancement suggestion and provide the following information:

* **Use a clear and descriptive title** 
* **Provide a step-by-step description of the suggested enhancement** 
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Explain why this enhancement would be useful** 

### Code Contribution

Look through the listed issues for the repository. Issues that are not assigned to a developer and are not labeled 'blocked' are avaliable for contribution.

#### Make changes locally

1. Fork the repository.
2. .....

### Pull Requests

When you have completed your changes please create a pull request.

- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).
- Once you submit your PR, a team member will review your proposal.
- We may ask for changes to be made before a PR can be merged. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as resolved.


## Styleguides

### Git Commit Messages

* Clear and consice description.


### LANG Styleguide

All TODO LANG code is linted with [Prettier](https://prettier.io/).

* TODO
* Inline `export`s with expressions whenever possible
  ```TODO
  // Use this:
  export default class ClassName {

  }

  // Instead of:
  class ClassName {

  }
  export default ClassName
  ```

### Documentation Styleguide

* TODO

#### Example

```TODO
# Public: Disable the package with the given name.
#
# * `name`    The {String} name of the package to disable.
# * `options` (optional) The {Object} with disable options (default: {}):
#   * `trackTime`     A {Boolean}, `true` to track the amount of time taken.
#   * `ignoreErrors`  A {Boolean}, `true` to catch and ignore errors thrown.
# * `callback` The {Function} to call after the package has been disabled.
#
# Returns `undefined`.
disablePackage: (name, options, callback) ->
```

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

#### Type of Issue and Issue State

| Label name | Description |
| --- | --- |
| `enhancement` | Feature requests. |
| `bug` | Bugs. |
| `blocked` | Issues blocked on other issues. |


#### Topic Categories

| Label name | Description |
| --- | --- |
| `documentation` | Related to any type of documentation |
| `ui` | Related to visual design. |
| `api` | Related to XYZ's APIs. |

#### Pull Request Labels

| Label name | Description
| --- | --- |
| `work-in-progress` | Pull requests which are still being worked on, more changes will follow. |
| `needs-review` | Pull requests which need code review, and approval from the team. |
| `under-review` | Pull requests being reviewed by the team. |
| `requires-changes` | Pull requests which need to be updated based on review comments and then reviewed again. |

