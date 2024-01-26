<h1 align="center">lunchable-splitlunch</h1>

<p align="center">
LunchMoney + Splitwise Integration
</p>

<p align="center">
  <a href="https://github.com/juftin/lunchable-splitlunch"><img src="https://img.shields.io/pypi/v/lunchable-splitlunch?color=blue&label=lunchable-splitlunch" alt="PyPI"></a>
  <a href="https://pypi.python.org/pypi/lunchable-splitlunch/"><img src="https://img.shields.io/pypi/pyversions/lunchable-splitlunch" alt="PyPI - Python Version"></a>
  <a href="https://juftin.github.io/lunchable-splitlunch/"><img src="https://img.shields.io/static/v1?message=docs&color=526CFE&logo=Material+for+MkDocs&logoColor=FFFFFF&label=" alt="docs"></a>
  <a href="https://github.com/pypa/hatch"><img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg" alt="Hatch project"></a>
  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-lightgreen?logo=pre-commit" alt="pre-commit"></a>
  <a href="https://github.com/semantic-release/semantic-release"><img src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg" alt="semantic-release"></a>
  <a href="https://gitmoji.dev"><img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg" alt="Gitmoji"></a>
</p>

<div align="center">
    <p float="center">
        <img src=https://assets.splitwise.com/assets/core/logo-square.svg
            width="35%" alt="lunchable">
        <img src=https://i.imgur.com/FyKDsG3.png
            width="60%" alt="lunchable">
    </p>
</div>

## Run via the Lunchable CLI

You can install lunchable with `pip` or
[pipx](https://pypa.github.io/pipx/). Make sure to use the
`lunchable[splitlunch]` extra to install the `SplitLunch` plugin.
You can also use the `lunchable[plugins]` extra to install all the
known plugins.

```shell
pipx install "lunchable[splitlunch]"
```

```shell
pip install "lunchable[splitlunch]"
```

## Integrations

This plugin supports different operations, and some of those operations have prerequisites:

### Auto Importer

It supports the auto-importing of Splitwise expenses into Lunch Money transactions. This requires
a manual asset exist in your Lunch Money account with "Splitwise" in the Name. Expenses that
have been deleted or which don't impact you (i.e. are only between other users in your group)
are skipped. By default, payments and expenses for which you are recorded as the payer are
skipped as well, but these can be overridden by the `--allow-payments` and `--allow-self-paid`
CLI flags, respectively.

#### Prerequisites

-   Accounts:
    -   Splitwise must be in the account name

### LunchMoney -> Splitwise

It supports the creation of Splitwise transactions directly from synced Lunch Money accounts. This syncing requires you create a tag called `SplitLunchImport`. Transactions with this tag will be created in Splitwise with your "financial partner". Once transactions are created in Splitwise they will be split in half in Lunch Money. Half of the split will be marked in the `Reimbursement` category which must be created.

#### Prerequisites

-   Financial Partners:
    -   If you only have one friend in Splitwise, this is your Financial Partner
    -   Financial Partners can be individual users or groups and transactions will be split accordingly
    -   Financial Partners must be specified by their Splitwise Group ID, Splitwise User ID, or Email Address
-   Tags:
    -   `SplitLunchImport`
-   Categories:
    -   `Reimbursement`

### SplitLunch

It supports a workflow where you mark transactions as split (identical to `Lunch Money -> Splitwise`) without importing them into Splitwise. This syncing requires you create a tag called `SplitLunch` and a category named `Reimbursement`

#### Prerequisites

-   Tags:
    -   `SplitLunch`
-   Categories:
    -   `Reimbursement`

### LunchMoney -> Splitwise (without splitting)

It supports the creation of Splitwise transactions directly from synced Lunch Money accounts. This syncing requires you create a tag called `SplitLunchDirectImport`. Transactions with this tag will be created in Splitwise with the total completely owed by your "financial partner". The entire transaction wil then be categorized as `Reimbursement` without being split.

#### Prerequisites

-   Financial Partners:
    -   If you only have one friend in Splitwise, this is your Financial Partner
    -   Financial Partners can be individual users or groups and transactions will be split accordingly
    -   Financial Partners must be specified by their Splitwise Group ID, Splitwise User ID, or Email Address
-   Tags:
    -   `SplitLunchDirectImport`
-   Categories:
    -   `Reimbursement`

> **Note:** Some of the above scenarios allow for tagging of a `Splitwise` tag on updated transactions. This tag must be created for this functionality to work.

## Installation

```shell
pip install lunchable[splitlunch]
```

## Run the SplitLunch plugin for the Lunchable CLI

```shell
lunchable plugins splitlunch --help
```

## Run the SplitLunch plugin for the Lunchable CLI via Docker

```shell
docker pull juftin/lunchable
```

```shell
docker run \
    --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
    --env SPLITWISE_CONSUMER_KEY=${SPLITWISE_CONSUMER_KEY} \
    --env SPLITWISE_CONSUMER_SECRET=${SPLITWISE_CONSUMER_SECRET} \
    --env SPLITWISE_API_KEY=${SPLITWISE_API_KEY} \
    juftin/lunchable:latest \
    lunchable plugins splitlunch --help
```
