#!/bin/sh

build() {
  echo ======================= $1 =======================
  docker build ./ \
    -t breathecode/$1
    # --rm=false \
}

if [ $1 ]; then
  build "$1"
else
  build example
fi
