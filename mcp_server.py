import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from onedrive import OneDriveClient
from summarize import Summmarization

load_dotenv()

mcp = FastMCP(
    name="OneDrive doc summarize",
    host="0.0.0.0",
    port=8050,
)

@mcp.tool()
def get_file_summary(access_token: str, file_id: str):
    """
    get the file from oneDrive and then summarize it using llm.
    """
    onedrive_client = OneDriveClient(access_token=access_token)
    file_text = onedrive_client.get_file(file_id=file_id)
    summarizer = Summmarization()
    summary = summarizer.summarize_text(file_text)
    return summary

if __name__ == "__main__":
    mcp.run(transport="sse")

