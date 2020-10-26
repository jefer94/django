#!/bin/sh

build() {
  echo ======================= $1 =======================
  docker build ./$1 \
    -f ./Dockerfile \
    -t breathecode/$1
    # --rm=false \
}

if [ $1 ]; then
  build "$1"
else
  build projects
fi
