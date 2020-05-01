# Jabba

Jabba is a tool for secret management for lazy people - it's an easy way to CRUD secrets across (several of) the cloud(s).

# Installation

```bash
pip install jabba-secrets
```

# Usage

Jabba exposes the following high level functions for secret management:
  - `fetch_secret`
  - `put_secret`
  - `drop_secret`
  - `update_secret`

Fetching secrets:
```python
>>> import jabba
>>> secret_string_aws = jabba.fetch_secret(
...  "aws-secretsmanager",
...  "my-secret-name",
...)
>>> print(secret_string_aws)
You'll never guess me!
>>> secret_string_gcp = jabba.fetch_secret(
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
>>> import jabba
>>> jabba.put_secret(
...    "aws-secretsmanager",
...    "nuclear_codes",
...    "boo00oom",
...)
>>> jabba.put_secret(
...    "gcp-secretmanager",
...    "answer_to_life",
...    "42",
...    "my-gcp-project",
...    "secret-version-2",
...)
```

Dropping secrets:
```python
>>> import jabba
>>> jabba.drop_secret(
...  "aws-secretsmanager",
...  "my-secret-name",
...)
>>> jabba.drop_secret(
...  "gcp-secretmanager",
...  "my-secret-name",
...  "my-gcp-project",
...  "secret-version-1",
...)
```

Updating secrets:
```python
>>> import jabba
>>> jabba.update_secret(
...    "aws-secretsmanager",
...    "nuclear_codes",
...    "boo00oom2",
...)
>>> jabba.put_secret(
...    "gcp-secretmanager",
...    "answer_to_life",
...    "Who freakin' knows!",
...    "my-gcp-project",
...    "secret-version-2",
...)
```

# Development

Development starts by running:
```bash
docker-compose run --rm jabba
```

# CI

TODO
