#!/bin/sh
set -ex

WHERE=$(cd $(dirname $0) && pwd)

cd "${WHERE}"

pipenv run $1
