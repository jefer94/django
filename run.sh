#!/bin/sh

grey=$(tput setaf 0)
red=$(tput setaf 1)
green=$(tput setaf 2)
yelloc=$(tput setaf 3)
blue=$(tput setaf 4)
violet=$(tput setaf 5)
cyan=$(tput setaf 6)
white=$(tput setaf 7)
normal=$(tput sgr0)

if [ "$1" = "env:install" ]; then
  ./scripts/install-env.sh
elif [ "$1" = "docker:build" ]; then
  ./scripts/docker-build.sh
elif [ "$1" = "docker:push" ]; then
  ./scripts/docker-push.sh
else
  printf "\n"
  printf "Type ./run.sh <command>\n"
  printf "\n"

  printf '%0s\n' "${red}[env]${normal}"
  printf "    env:install\n"
  printf "\n"

  printf '%0s\n' "${red}[docker]${normal}"
  printf "    docker:build\n"
  printf "    docker:push\n"
  printf "\n"

  printf '%0s\n' "${red}[django]${normal}"
  printf "    docker:build\n"
  printf "    docker:push\n"
fi