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

### Global Configuration

1. Open Cursor IDE settings
2. Navigate to MCP settings
3. Add the following configuration:

```json
{
  "mcpServers": {
    "mcp-time-server": {
      "command": "python",
      "args": ["-m", "mcp_time_server.server"],
      "cwd": "/path/to/mcp-time-server"
    }
  }
}
```

### Alternative: Local mcp_config.json

Copy the provided `mcp_config.json` to your Cursor IDE configuration directory.

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

### Windows PowerShell

If you encounter issues with `&&` operator in PowerShell, use:

```powershell
cd src; python -m mcp_time_server.server
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
- Cursor IDE integration support 