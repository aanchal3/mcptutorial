from mcp.server.fastmcp import FastMCP


mcp = FastMCP("math")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b