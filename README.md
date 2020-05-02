# Jana

[![Build Status](https://travis-ci.com/zack-klein/jana.svg?branch=master)](https://travis-ci.com/zack-klein/snowbird) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)


[Named after the Roman goddess of secrets](https://en.wikipedia.org/wiki/Janus), Jana is a tool for secret management built for lazy people - it's an easy way to CRUD secrets across (several of) the cloud(s).

# Installation

```bash
pip install jana
```

# Usage

Jana exposes the following high level functions for secret management:
  - `fetch_secret`
  - `put_secret`
  - `drop_secret`
  - `update_secret`

Fetching secrets:
```python
>>> import jana
>>> secret_string_aws = jana.fetch_secret(
...  "aws-secretsmanager",
...  "my-secret-name",
...)
>>> print(secret_string_aws)
You'll never guess me!
>>> secret_string_gcp = jana.fetch_secret(
...  "gcp-secretmanager",
...  "my-secret-name",
...  "my-gcp-project",
...  "secret-version-1",
...)
>>> print(secret_string_gcp)
You'll never guess me too!
```

Putting secrets:
```python
>>> import jana
>>> jana.put_secret(
...    "aws-secretsmanager",
...    "nuclear_codes",
...    "boo00oom",
...)
>>> jana.put_secret(
...    "gcp-secretmanager",
...    "answer_to_life",
...    "42",
...    "my-gcp-project",
...    "secret-version-2",
...)
```

Dropping secrets:
```python
>>> import jana
>>> jana.drop_secret(
...  "aws-secretsmanager",
...  "my-secret-name",
...)
>>> jana.drop_secret(
...  "gcp-secretmanager",
...  "my-secret-name",
...  "my-gcp-project",
...  "secret-version-1",
...)
```

Updating secrets:
```python
>>> import jana
>>> jana.update_secret(
...    "aws-secretsmanager",
...    "nuclear_codes",
...    "boo00oom2",
...)
>>> jana.put_secret(
...    "gcp-secretmanager",
...    "answer_to_life",
...    "Who freakin' knows!",
...    "my-gcp-project",
...    "secret-version-2",
...)
```

# Development/Contributing

Contributions are welcome! This repository ships with a development environment that you can start by running:
```bash
docker-compose run --rm jana
```
