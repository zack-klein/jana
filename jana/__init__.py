"""
Jana is a simple, no-nonsense way to CRUD secrets in the cloud.
"""

from .aws_secretsmanager import (  # noqa:F401
    fetch_aws_secrets_manager_secret,
    put_aws_secrets_manager_secret,
    drop_aws_secrets_manager_secret,
    update_aws_secrets_manager_secret,
)
from .gcp_secretmanager import (
    fetch_gcp_secret_manager_secret,
    put_gcp_secret_manager_secret,
    drop_gcp_secret_manager_secret,
    update_gcp_secret_manager_secret,
)


SECRET_FETCH_DISPATCHER = {
    "aws-secretsmanager": fetch_aws_secrets_manager_secret,
    "gcp-secretmanager": fetch_gcp_secret_manager_secret,
    "__unittest__": lambda: "fetch",
}

SECRET_PUT_DISPATCHER = {
    "aws-secretsmanager": put_aws_secrets_manager_secret,
    "gcp-secretmanager": put_gcp_secret_manager_secret,
    "__unittest__": lambda: "put",
}

SECRET_DROP_DISPATCHER = {
    "aws-secretsmanager": drop_aws_secrets_manager_secret,
    "gcp-secretmanager": drop_gcp_secret_manager_secret,
    "__unittest__": lambda: "drop",
}

SECRET_UPDATE_DISPATCHER = {
    "aws-secretsmanager": update_aws_secrets_manager_secret,
    "gcp-secretmanager": update_gcp_secret_manager_secret,
    "__unittest__": lambda: "update",
}


def fetch_secret(provider_service, *args, **kwargs):
    """
    Dispatch to a specific provider/service combination function.

    :param str provider_service: The combination of provider and service in the
        format <provider>-<service>. For example: aws-secrecretsmanager,
        gcp-secretmanager.
    :param args: Arbitrary positional args to pass to the dispatched function.
    :param kwargs: Arbitrary key-value args to pass to the dispatched function.
    :raise NotImplementedError: If a function for the provider_service is
        invalid, it raises this error.
    """
    fetch_function = SECRET_FETCH_DISPATCHER.get(provider_service)

    if not fetch_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for fetching secrets are: "
            f"{', '.join(list(SECRET_FETCH_DISPATCHER.keys()))}"
        )

    secret = fetch_function(*args, **kwargs)

    return secret


def put_secret(provider_service, *args, **kwargs):
    """
    Dispatch to a specific provider/service combination function for putting
    secrets.

    :param str provider_service: The combination of provider and service in the
        format <provider>-<service>. For example: aws-secrecretsmanager,
        gcp-secretmanager.
    :param args: Arbitrary positional args to pass to the dispatched function.
    :param kwargs: Arbitrary key-value args to pass to the dispatched function.
    :raise NotImplementedError: If a function for the provider_service is
        invalid, it raises this error.
    """
    put_function = SECRET_PUT_DISPATCHER.get(provider_service)

    if not put_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for putting secrets are: "
            f"{', '.join(list(SECRET_PUT_DISPATCHER.keys()))}"
        )

    response = put_function(*args, **kwargs)
    return response


def drop_secret(provider_service, *args, **kwargs):
    """
    Dispatch to a specific provider/service combination function for deleting
    secrets.

    :param str provider_service: The combination of provider and service in the
        format <provider>-<service>. For example: aws-secrecretsmanager,
        gcp-secretmanager.
    :param args: Arbitrary positional args to pass to the dispatched function.
    :param kwargs: Arbitrary key-value args to pass to the dispatched function.
    :raise NotImplementedError: If a function for the provider_service is
        invalid, it raises this error.
    """
    drop_function = SECRET_DROP_DISPATCHER.get(provider_service)

    if not drop_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for dropping secrets are: "
            f"{', '.join(list(SECRET_DROP_DISPATCHER.keys()))}"
        )

    response = drop_function(*args, **kwargs)
    return response


def update_secret(provider_service, *args, **kwargs):
    """
    Dispatch to a specific provider/service combination function for updating
    secrets.

    :param str provider_service: The combination of provider and service in the
        format <provider>-<service>. For example: aws-secrecretsmanager,
        gcp-secretmanager.
    :param args: Arbitrary positional args to pass to the dispatched function.
    :param kwargs: Arbitrary key-value args to pass to the dispatched function.
    :raise NotImplementedError: If a function for the provider_service is
        invalid, it raises this error.
    """
    update_function = SECRET_UPDATE_DISPATCHER.get(provider_service)

    if not update_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for updating secrets are: "
            f"{', '.join(list(SECRET_UPDATE_DISPATCHER.keys()))}"
        )

    response = update_function(*args, **kwargs)
    return response
