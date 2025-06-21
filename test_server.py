"""
Simple test script for MCP Time Server functionality.
"""

import sys
import os

# Add src directory to Python path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mcp_time_server.server import get_current_time_utc


def test_time_formats():
    """Test different time formats."""
    print("Testing MCP Time Server functionality...\n")
    
    # Test ISO format (default)
    print("1. ISO format (default):")
    result_iso = get_current_time_utc()
    print(f"   Result: {result_iso}")
    print(f"   Formatted: {result_iso['formatted_time']}\n")
    
    # Test datetime format
    print("2. Datetime format:")
    result_datetime = get_current_time_utc("datetime")
    print(f"   Result: {result_datetime}")
    print(f"   Formatted: {result_datetime['formatted_time']}\n")
    
    # Test timestamp format
    print("3. Timestamp format:")
    result_timestamp = get_current_time_utc("timestamp")
    print(f"   Result: {result_timestamp}")
    print(f"   Formatted: {result_timestamp['formatted_time']}\n")
    
    # Test invalid format (should default to ISO)
    print("4. Invalid format (should default to ISO):")
    result_invalid = get_current_time_utc("invalid")
    print(f"   Result: {result_invalid}")
    print(f"   Formatted: {result_invalid['formatted_time']}\n")
    
    print("✅ All tests completed successfully!")


if __name__ == "__main__":
    test_time_formats() 