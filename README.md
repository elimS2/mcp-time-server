# MCP Time Server

A simple Model Context Protocol (MCP) server that provides current UTC time functionality. This server can be integrated globally with Cursor IDE to provide time-related capabilities across all projects.

## Features

- Get current UTC time in multiple formats
- Simple MCP protocol implementation
- Global Cursor IDE integration
- Lightweight and fast

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install from source

1. Clone or download this repository
2. Navigate to the project directory
3. Install the package:

```bash
pip install -e .
```

### Install dependencies only

```bash
pip install -r requirements.txt
```

## Usage

### Running the server

```bash
# Run directly
python -m mcp_time_server.server

# Or use the installed script
mcp-time-server
```

### Available Tools

#### get_current_time_utc

Get the current UTC time in various formats.

**Parameters:**
- `format` (optional): Output format
  - `"iso"` (default): ISO 8601 format (2025-01-15T10:30:45Z)
  - `"datetime"`: Human-readable format (2025-01-15 10:30:45)
  - `"timestamp"`: Unix timestamp (1736939445)

**Example response:**
```
Current UTC time: 2025-01-15T10:30:45.123456Z
Format: iso
Full ISO: 2025-01-15T10:30:45.123456Z
```

## Cursor IDE Integration

### Global Configuration (Recommended)

**For permanent integration across all projects:**

1. Create the global MCP configuration file:
   - **Windows**: `C:\Users\[USERNAME]\.cursor\mcp.json`
   - **macOS/Linux**: `~/.cursor/mcp.json`

2. Add the following configuration:

```json
{
  "mcpServers": {
    "time-server": {
      "command": "python",
      "args": ["-m", "mcp_time_server.server"],
      "cwd": "/full/path/to/mcp-time-server/src",
      "env": {
        "PYTHONPATH": "/full/path/to/mcp-time-server/src"
      }
    }
  }
}
```

3. Restart Cursor IDE
4. Check `Tools & Integrations` > `MCP` to verify the server is enabled

**The server will now automatically start with Cursor IDE and work across all projects!**

### Project-Specific Configuration

For project-only usage, create `.cursor/mcp.json` in your project directory with the same structure.

## Development

### Development Setup

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/
isort src/

# Type checking
mypy src/
```

### Project Structure

```
mcp-time-server/
├── src/
│   └── mcp_time_server/
│       ├── __init__.py
│       └── server.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── mcp_config.json
└── PROJECT_PLAN.md
```

## Testing

Test the server functionality:

```python
from mcp_time_server.server import get_current_time_utc

# Test different formats
print(get_current_time_utc("iso"))
print(get_current_time_utc("datetime"))
print(get_current_time_utc("timestamp"))
```

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure the package is installed with `pip install -e .`
2. **MCP connection issues**: Verify the server path in your MCP configuration
3. **Permission errors**: Ensure Python has necessary permissions to run the server
4. **Server not appearing**: Check that the `.cursor` directory exists and `mcp.json` is properly formatted

### Windows PowerShell

If you encounter issues with `&&` operator in PowerShell, use:

```powershell
cd src; python -m mcp_time_server.server
```

### Verifying Server Status

**Check if server is running:**
```powershell
# Windows
tasklist | findstr python
wmic process where "name='python.exe'" get ProcessId,CommandLine /format:list

# macOS/Linux  
ps aux | grep mcp_time_server
```

**Test connection in Cursor:**
Ask the AI assistant to get current time - it should use the MCP Time Server automatically.

### Manual Server Management

**Start server manually:**
```bash
cd src && python -m mcp_time_server.server
```

**Stop server:**
```powershell
# Windows (replace PID with actual process ID)
taskkill /PID [PID] /F
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Changelog

### v0.1.0
- Initial release
- Basic UTC time functionality
- MCP protocol compliance
- FastMCP integration for simplified server management
- Global Cursor IDE configuration support
- Multiple time formats (ISO, datetime, timestamp)
- Comprehensive testing and documentation
- Process management and troubleshooting tools
- GitHub repository with MIT license
- Live testing confirmed across restart cycles 