#!/bin/bash

set -e

echo "Starting Vault..."
cd "$(dirname "$0")/.."

docker compose up -d vault

echo "Waiting for Vault..."
sleep 3

echo "Vault status:"
curl -s http://localhost:8201/v1/sys/health | python3 -m json.tool
