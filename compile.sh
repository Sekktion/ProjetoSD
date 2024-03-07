#!/bin/bash
pipenv install

pipenv run python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I./proto proto/pa.proto
pipenv run python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I./proto proto/pm.proto
