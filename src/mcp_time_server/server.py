"""
MCP Time Server - Main server implementation.

This module implements a simple MCP server that provides current UTC time functionality.
"""

import asyncio
import sys
from datetime import datetime, timezone
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

# Create FastMCP server instance
mcp = FastMCP("mcp-time-server")


def get_current_time_utc(format: str = "iso") -> Dict[str, Any]:
    """
    Get current UTC time in the specified format.
    
    Args:
        format: Output format - 'iso' (2025-06-21T11:30:45Z), 'datetime' (2025-06-21 11:30:45), 'timestamp' (unix timestamp)
    
    Returns:
        Dictionary with current time information
    """
    now_utc = datetime.now(timezone.utc)
    
    result = {
        "utc_time": now_utc.isoformat(),
        "format": format,
        "timezone": "UTC"
    }
    
    if format == "iso":
        result["formatted_time"] = now_utc.isoformat()
    elif format == "datetime":
        result["formatted_time"] = now_utc.strftime("%Y-%m-%d %H:%M:%S")
    elif format == "timestamp":
        result["formatted_time"] = int(now_utc.timestamp())
    else:
        result["formatted_time"] = now_utc.isoformat()  # Default to ISO format
    
    return result


@mcp.tool()
def get_current_time_utc_tool(format: str = "iso") -> Dict[str, Any]:
    """
    Get current UTC time in the specified format.
    
    Args:
        format: Output format - 'iso' (2025-06-21T11:30:45Z), 'datetime' (2025-06-21 11:30:45), 'timestamp' (unix timestamp)
    
    Returns:
        Dictionary with current time information
    """
    return get_current_time_utc(format)


def main():
    """
    Main function to run the MCP server.
    """
    mcp.run()


if __name__ == "__main__":
    main() 