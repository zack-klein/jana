"""
Jabba is a simple, no-nonsense way to store and fetch secrets in the cloud.

Each different environment for storing secrets is considered a Secret Provider,
with all Secret Providers deriving from the BaseSecretProvider class.
"""

import base64
import boto3

from google.cloud import secretmanager


def fetch_aws_secrets_manager_secret(secret_name, region="us-east-1"):
    """
    Grab a secret from AWS Secrets Manager.

    :param str secret_name: Name of the secret in secrets manager.
    :return str: The secret string.
    """
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)

    if "SecretString" in response:
        secret = response["SecretString"]
    else:
        secret = base64.b64decode(response["SecretBinary"])

    return secret


def fetch_gcp_secret_manager_secret(secret_name, project, secret_version):
    """
    Fetch a secret from GCP Secret Manager.

    :param str secret_name: The name of the secret to fetch.
    :param str project: The name of the project the secret belongs to.
    :param str secret_version: The version of the secret.
    :return str: The secret string.
    """
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project, secret_name, secret_version)
    response = client.access_secret_version(name)
    secret = response.payload.data.decode("UTF-8")
    return secret


SECRET_FETCH_DISPATCHER = {
    "aws-secretsmanager": fetch_aws_secrets_manager_secret,
    "gcp-secretmanager": fetch_gcp_secret_manager_secret,
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


def put_aws_secrets_manager_secret(
    secret_name, secret_value, region="us-east-1", **create_secret_args
):
    """
    Put a secret into AWS Secrets Manager.

    :param str secret_name: Name of the secret.
    :param str secret_value: Value of the secret.
    :param str region: AWS Region.
    """
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region)
    client.create_secret(
        Name=secret_name, SecretString=secret_value, **create_secret_args,
    )


SECRET_PUT_DISPATCHER = {
    "aws-secretsmanager": put_aws_secrets_manager_secret,
}


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
    fetch_function = SECRET_PUT_DISPATCHER.get(provider_service)

    if not fetch_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for fetching secrets are: "
            f"{', '.join(list(SECRET_FETCH_DISPATCHER.keys()))}"
        )

    secret = fetch_function(*args, **kwargs)

    return secret
