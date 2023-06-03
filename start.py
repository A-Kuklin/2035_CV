import uvicorn
from dotenv import load_dotenv

from core.settings import settings


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        'src.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True
    )
