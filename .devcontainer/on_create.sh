#!/bin/bash

# Update the submodules
git submodule update --init --recursive

# Setups the gem5 source directory
pushd gem5

## We cleanup git's 'blame' feature by ignoring certain commits (typically
## commits that have reformatted files)
git config --global blame.ignoreRevsFile .git-blame-ignore-revs

./util/pre-commit-install.sh

popd # gem5

# Update path in gem5-config and gem5-resources
# replace instances of "/workspaces/gem5-assignment-template" with $BASE_PATH

# Update path in gem5-config
sed -i "s|/workspaces/gem5-assignment-template|$BASE_PATH|g" $BASE_PATH/gem5-config.json

# Update path in gem5-resources
sed -i "s|/workspaces/gem5-assignment-template|$BASE_PATH|g" $BASE_PATH/workloads/resources.json

git add $BASE_PATH/gem5-config.json
git add $BASE_PATH/workloads/resources.json
git commit -m "Update resource paths for this repository"
