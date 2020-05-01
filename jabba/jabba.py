"""
Jabba is a simple, no-nonsense way to CRUD secrets in the cloud.
"""

import base64
import boto3

from google.cloud import secretmanager

# Functions for fetching existing secrets.


# AWS
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


# GCP
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


# Functions for putting new secrets.

# AWS
def put_aws_secrets_manager_secret(
    secret_name, secret_value, region="us-east-1", **create_secret_args
):
    """
    Put a secret into AWS Secrets Manager. You can pass arbitraty creation
    args to this, see:
    https://boto3.amazonaws.com/v1/documentation/api/1.9.46/reference/services/secretsmanager.html#SecretsManager.Client.create_secret

    :param str secret_name: Name of the secret.
    :param str secret_value: Value of the secret.
    :param str region: AWS Region.
    """
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region)
    client.create_secret(
        Name=secret_name, SecretString=secret_value, **create_secret_args,
    )


# GCP
def create_gcp_secret_manager_secret(secret_name, secret_value, project):
    """
    Create a secret in GCP Secret Manager. See:
    https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create_a_secret

    :param str secret_name: The name of the secret to put.
    :param str secret_value: The value of the secret to put.
    :param str project: The name of the project the secret belongs to.
    """
    client = secretmanager.SecretManagerServiceClient()
    project_parent = client.project_path(project)
    response = client.create_secret(project_parent, secret_name, {
        'replication': {
            'automatic': {},
        },
    })
    secret_parent = client.secret_path(project, secret_name)
    secret_bytes = secret_value.encode('UTF-8')
    client.add_secret_version(secret_parent, {'data': secret_bytes})



SECRET_PUT_DISPATCHER = {
    "aws-secretsmanager": put_aws_secrets_manager_secret,
    "gcp-secretmanager": create_gcp_secret_manager_secret,
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
            f"{', '.join(list(SECRET_PUT_DISPATCHER.keys()))}"
        )

    secret = fetch_function(*args, **kwargs)

    return secret


# Functions for dropping existing secrets.

# AWS
def drop_aws_secrets_manager_secret(
    secret_name, region="us-east-1", **drop_secret_args
):
    """
    Drop a secret from AWS Secrets Manager. You can pass arbitrary arguments
    to this as well, see:
    https://boto3.amazonaws.com/v1/documentation/api/1.9.46/reference/services/secretsmanager.html#SecretsManager.Client.delete_secret

    :param str secret_name: Name of the secret.
    :param str region: AWS Region.
    """
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region)
    client.delete_secret(
        SecretId=secret_name, **drop_secret_args,
    )


SECRET_DROP_DISPATCHER = {
    "aws-secretsmanager": drop_aws_secrets_manager_secret,
}


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
    fetch_function = SECRET_DROP_DISPATCHER.get(provider_service)

    if not fetch_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for fetching secrets are: "
            f"{', '.join(list(SECRET_DROP_DISPATCHER.keys()))}"
        )

    secret = fetch_function(*args, **kwargs)

    return secret


# Functions for updating existing secrets.

# AWS
def update_aws_secrets_manager_secret(
    secret_name, secret_value, region="us-east-1", **update_secret_args
):
    """
    Update a secret in AWS Secrets Manager. You can pass in arbitrary options
    as well, see:
    https://boto3.amazonaws.com/v1/documentation/api/1.9.46/reference/services/secretsmanager.html#SecretsManager.Client.update_secret

    :param str secret_name: Name of the secret.
    :param str region: AWS Region.
    """
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region)
    client.update_secret(
        SecretId=secret_name, SecretString=secret_value, **update_secret_args,
    )


SECRET_UPDATE_DISPATCHER = {
    "aws-secretsmanager": update_aws_secrets_manager_secret,
}


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
    fetch_function = SECRET_UPDATE_DISPATCHER.get(provider_service)

    if not fetch_function:
        raise NotImplementedError(
            f"Provider-Service combination: '{provider_service}' is not "
            "supported! Currently supported for fetching secrets are: "
            f"{', '.join(list(SECRET_UPDATE_DISPATCHER.keys()))}"
        )

    secret = fetch_function(*args, **kwargs)

    return secret
