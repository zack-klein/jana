# Jana

[![Build Status](https://travis-ci.com/zack-klein/jana.svg?branch=master)](https://travis-ci.com/zack-klein/snowbird) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![codecov](https://codecov.io/gh/zack-klein/jana/branch/master/graph/badge.svg)](https://codecov.io/gh/zack-klein/jana)


:warning: **WARNING:** I'm no longer actively maintaining this library, I ended up not needing it as much as I thought I would. You can still it install it from the test instance of PyPi:

```bash
pip install -i https://test.pypi.org/simple/ jana
```

[Named after the Roman goddess of secrets](https://en.wikipedia.org/wiki/Janus), Jana is a tool for secret management built for lazy people - it's an easy way to CRUD secrets across (several of) the cloud(s). The goal is to provide a consistent experience for using secrets, regardless of which "backend" cloud provider you're using.

# Supported Platforms:
- GCP (Google Cloud Platform Secret Manager)
- AWS (AWS Secrets Manager)

# Installation

```bash
pip install -i https://test.pypi.org/simple/ jana
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

Commit style follows [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
