import asyncio
from application_tools import ToolsClient
import json

async def test_filelistnode():
    """Test File List using ToolsClient"""
    try:
        async with ToolsClient() as client:
            # Execute File List
            result = await client.run_node(
                "autotask_core.nodes.file.FileListNode",
                {
                    "directory": "",
                    "pattern": "",
                    "include_dirs": "true",
                    "recursive": "false"
                }
            )
            print("Execution result:", json.dumps(result, indent=2, ensure_ascii=False))
            return result
    except Exception as e:
        print("Execution failed:", str(e))
        raise

async def test_node_info():
    """Test getting node information"""
    try:
        async with ToolsClient() as client:
            # Get node information
            info = await client.get_node_info("autotask_core.nodes.file.FileListNode")
            print("Node information:", json.dumps(info, indent=2, ensure_ascii=False))
            return info
    except Exception as e:
        print("Failed to get node information:", str(e))
        raise

async def test_list_nodes():
    """Test listing all available nodes"""
    try:
        async with ToolsClient() as client:
            # List all nodes
            nodes = await client.list_nodes()
            print("Available nodes list:", json.dumps(nodes, indent=2, ensure_ascii=False))
            return nodes
    except Exception as e:
        print("Failed to get nodes list:", str(e))
        raise

async def test_run_workflow(workflow_uuid: str):
    """Test running a workflow"""
    try:
        async with ToolsClient() as client:
            # Execute workflow
            result = await client.run_workflow(workflow_uuid)
            print("Workflow execution result:", json.dumps(result, indent=2, ensure_ascii=False))
            return result
    except Exception as e:
        print("Workflow execution failed:", str(e))
        raise

async def test_run_assistant(assistant_id: str, message: str):
    """Test running an assistant"""
    try:
        async with ToolsClient() as client:
            # Execute assistant
            result = await client.run_assistant_sync(
                assistant_id=assistant_id,
                message=message,
                session_id="test_session"
            )
            print("Assistant execution result:", json.dumps(result, indent=2, ensure_ascii=False))
            return result
    except Exception as e:
        print("Assistant execution failed:", str(e))
        raise

def run_tests():
    """Run all tests"""
    loop = asyncio.get_event_loop()
    
    # Test getting node information
    print("\n=== Testing Get Node Information ===")
    loop.run_until_complete(test_node_info())
    
    # Test listing all nodes
    print("\n=== Testing List All Nodes ===")
    loop.run_until_complete(test_list_nodes())
    
    # Test file list
    print("\n=== Testing File List ===")
    loop.run_until_complete(test_filelistnode())

if __name__ == "__main__":
    run_tests()