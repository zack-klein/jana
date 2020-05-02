import boto3
import base64


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
