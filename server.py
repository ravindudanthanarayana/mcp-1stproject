import asyncio
from dotenv import load_dotenv
from linkup import LinkupClient
from rag import RAGWorkflow
from mcp.server.fastmcp import FastMCP
import sys
import os

load_dotenv()

mcp = FastMCP('linkup-server')
client = LinkupClient()
rag_workflow = RAGWorkflow()


@mcp.tool()
async def rag(query: str) -> str:
    """Use a simple RAG workflow to answer queries using documents from data directory"""
    response = await rag_workflow.query(query)
    return str(response)

async def setup():
    """Initialize the RAG workflow by ingesting documents"""
    await rag_workflow.ingest_documents("data")
    print("✅ Documents ingested successfully")

if __name__ == "__main__":
    transport = "stdio"
    port = 8000

    if len(sys.argv) > 1 and sys.argv[1] == "--http":
        transport = "http"
        # Get port if specified
        if len(sys.argv) > 2:
            try:
                port = int(sys.argv[2])
            except ValueError:
                print(f"Invalid port number: {sys.argv[2]}, using default port {port}")
    
    asyncio.run(setup())
    
    if transport == "http":
        print(f"Starting MCP server with HTTP transport on port {port}")
        mcp.run(transport="http", port=port)
    else:
        print("Starting MCP server with stdio transport")
        mcp.run(transport="stdio")










