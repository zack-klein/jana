def setup_gcp(func):
    """
    Decorator for ensuring the right extensions are installed.
    """

    def inner(*args, **kwargs):
        try:
            from google.cloud import secretmanager

            global secretmanager
            response = func(*args, **kwargs)
        except ImportError:
            raise ImportError(
                "You must install jana[gcp] to use this function!"
            )
        return response

    return inner


@setup_gcp
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


@setup_gcp
def put_gcp_secret_manager_secret(secret_name, secret_value, project):
    """
    Create a secret in GCP Secret Manager. See:
    https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create_a_secret

    :param str secret_name: The name of the secret to put.
    :param str secret_value: The value of the secret to put.
    :param str project: The name of the project the secret belongs to.
    """
    client = secretmanager.SecretManagerServiceClient()
    project_parent = client.project_path(project)
    client.create_secret(
        project_parent, secret_name, {"replication": {"automatic": {}}}
    )
    secret_parent = client.secret_path(project, secret_name)
    secret_bytes = secret_value.encode("UTF-8")
    client.add_secret_version(secret_parent, {"data": secret_bytes})


@setup_gcp
def drop_gcp_secret_manager_secret(secret_name, project):
    """
    Drop a secret from GCP Secret Manager.

    :param str secret_name: Name of the secret.
    :param str project: Name of the GCP project.
    """
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_path(project, secret_name)
    client.delete_secret(name)


@setup_gcp
def update_gcp_secret_manager_secret(secret_name, secret_value, project):
    """
    Update a secret in GCP Secret Manager.

    :param str secret_name: Name of the secret.
    :param str region: AWS Region.
    """
    client = secretmanager.SecretManagerServiceClient()
    parent = client.secret_path(project, secret_name)
    secret_bytes = secret_value.encode("UTF-8")
    client.add_secret_version(parent, {"data": secret_bytes})
