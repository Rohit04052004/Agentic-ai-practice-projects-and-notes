from mcp.server.fastmcp import FastMCP

# Create a FastMCP server instance for mathematical operations
math_server = FastMCP("Math")


@math_server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
    
    
    

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

          
@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


@mcp.tool()
def square_root(x: float) -> float:
    """Return the square root of x."""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

@mcp.tool()
def factorial(n: int) -> int:
    """Return factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)





if __name__ == "__main__":
    # Run the server with stdio transport
    math_server.run(transport="stdio")