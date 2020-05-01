# TEMPORARY FILE FOR REPO SET UP:
# Run the following script to get Travis CI set up for this repo.

set -e

echo
echo "Let's set up Slack..."
read -p "Enter Slack Workspace: "  SLACK_SPACE
echo "Go to https://$SLACK_SPACE.slack.com/services/B012T3NE5EX, grab the token, and enter it below."
read -p "Enter Your Slack Secret Token (this gets encrypted): "  SLACK_TOKEN

echo "Now let's set up Git..."
read -p "Enter Git Username: "  GIT_USERNAME
read -p "Enter Name of the Git Repo: "  GIT_REPO
echo "Go to https://github.com/settings/tokens, generate a new token, and paste it below."
read -p "Enter Your Github secret token (this gets encrypted): "  GIT_TOKEN

travis login --github-token $GIT_TOKEN --com
travis encrypt "$SLACK_SPACE:$SLACK_TOKEN" --add notifications.slack --com
travis encrypt "GITHUB_USERNAME=$GIT_USERNAME" --add
travis encrypt "GITHUB_TOKEN=$GIT_TOKEN" --add
travis encrypt "GITHUB_REPO=$GIT_REPO" --add

echo "Travis CI is good to go!"
