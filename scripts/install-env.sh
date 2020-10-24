#!/bin/sh

python -m venv env

if [ ! -f .env ]; then
  cp .env.example .env
fi
