#!/usr/bin/env python
import sys
import logging
import nest_asyncio
from server import mcp, rag_workflow

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("mcp-server")

if __name__ == "__main__":
    try:
        logger.info("Starting MCP server...")
        
        # Run the MCP server with stdio transport
        logger.info("MCP server running. Waiting for requests...")
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Error running MCP server: {e}")
        raise 