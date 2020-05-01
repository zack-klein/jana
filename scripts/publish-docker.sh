set -e

REGISTRY_URL=$1
DOCKER_REPO=$2
TAG=$3

# For private repositories...
# echo "Logging in..."
# eval $(aws ecr get-login --no-include-email)
# TODO: Add GCP login

echo "Publishing..."
docker build --no-cache -t "$DOCKER_REPO" .
docker tag snowbird-southface "$REGISTRY_URL/$DOCKER_REPO:$TAG"
docker push "$REGISTRY_URL/$DOCKER_REPO:$TAG"
