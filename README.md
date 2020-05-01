# Jabba

An easy way to use secrets in (several of) the cloud(s).

# Installation

TODO

# Usage
```python
>> import jabba
>> secret_string = jabba.fetch_string(
...    "aws-secretsmanager",
...    "my-secret-name",
...)
>> print(secret_string)
You'll never guess me!
```

# Development

Development starts by running (or something similar):
```bash
docker-compose run --rm jabba
```

# CI

TODO
