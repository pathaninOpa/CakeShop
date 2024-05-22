import uvicorn
import config

if __name__ == "__main__":
    print(f"Deploying server at http://localhost:{config.PORT}")
    uvicorn.run("run:app", host="localhost", port=config.PORT, reload=True)