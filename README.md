# Twitter Bot

## Requirements

- Python 3.7
- pipenv

## Setup

```console
$ pipenv install # When with dev-package add `-d` option.
$ cp .env.example .env # Please edit the value.
$ cp event.json.example event.json # Please edit the value.
```

## Run (Local)

```console
$ pipenv run execute
```

## Deploy

```console
$ cp .chalice/config.json.example .chalice/config.json # Please edit the value.
$ pipenv run deploy
```
