# server.py
import sys
import traceback
from mcp.server.fastmcp import FastMCP

# Create an MCP server
try:
    print("Creating MCP server...", file=sys.stderr)
    mcp = FastMCP("MCPDemo")
except Exception as e:
    print(f"Error creating server: {e}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    try:
        print(f'Adding numbers: a={a}, b={b}', file=sys.stderr)
        result = a + b
        print(f'Result: {result}', file=sys.stderr)
        return result
    except Exception as e:
        print(f"Error in add function: {e}", file=sys.stderr)
        raise

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    try:
        print(f'Generating greeting for name: {name}', file=sys.stderr)
        return f"Hello, {name}!"
    except Exception as e:
        print(f"Error in greeting function: {e}", file=sys.stderr)
        raise

# Start the server
if __name__ == "__main__":
    try:
        print("Starting MCP server...", file=sys.stderr)
        mcp.run()
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)