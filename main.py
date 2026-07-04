import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent / "ABHISHEK"
sys.path.insert(0, str(project_root))

from main import client, main as bot_main

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(bot_main())
