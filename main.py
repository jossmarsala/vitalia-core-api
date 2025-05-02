from src.app import run_app
import uvicorn

if __name__ == '__main__':
    uvicorn.run("src.app:api_server", host="0.0.0.0")
    run_app()