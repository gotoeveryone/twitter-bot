# Twitter Bot

![Build Status](https://github.com/gotoeveryone/twitter-bot/workflows/Build/badge.svg)

## Requirements

- Python 3.9
- pipenv
- AWS account (use to DynamoDB, Lambda and Secrets Manager)
- Twitter Account

## Setup

```console
$ pipenv install # When with dev-package add `-d` option.
$ cp .env.example .env # Please edit the value.
```

## Run (Local)

```console
$ pipenv run execute
```

## Code check and format (with pycodestyle and autopep8)

```console
$ # Code check
$ pipenv run code_check
$ # Format
$ pipenv run code_format
```

## Create infra resources (use [Pulumi](https://www.pulumi.com/))

```console
$ cd infra
$ pulumi preview
$ pulumi up
```

## Deploy

```console
$ cp .chalice/config.json.example .chalice/config.json # Please edit the value.
$ pipenv run deploy
```
