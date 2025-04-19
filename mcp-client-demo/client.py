import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Executable
    args=[
        "run",
        "--with",
        "mcp[cli]",
        "--with-editable",
        r"D:\projects\AI\achievement",
        "mcp",
        "run",
        r"D:\projects\AI\achievement\\server.py"
    ],  # Optional command line arguments
    env=None  # Optional environment variables
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Tools:", tools)

            # call a tool
            score = await session.call_tool(name="get_score_by_name", arguments={"name": "张三"})
            print("score: ", score)


if __name__ == "__main__":
    asyncio.run(run())
