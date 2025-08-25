#!/bin/bash

source .venv/bin/activate

export OLLAMA_HOST=http://localhost:11434

echo "Starting MCP server in stdio mode..."
cd /Users/priyalaruna/Src/Demos/MCP/Local-MCP
exec python server.py 