# MCP Server

## Overview

The **MCP Server** is a lightweight, Dockerized Python server that integrates with OneDrive to fetch PDF files using an access token and file ID. It uses OpenAI's `gpt-4o-mini` language model to generate a summary of the document using the **Stuff** method.

## Features

- 🔐 Fetch PDF files from OneDrive using access token and file ID  
- 🧠 Generate summaries using OpenAI's `gpt-4o-mini`  
- 🧪 Includes an MCP Inspector tool for development and inspection  

---

## 🔧 Dockerized Build & Run

### Build the Docker Image

```bash
docker build -t mcp-server .
```
### Run the Docker Container

```bash
docker run -p 8050:8050 mcp-server
```