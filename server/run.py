import uvicorn

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host ="localhost", port=8000, reload = True)
    except Exception as e:
        print(f"An error occur during uvicorn start-up: {e}")
    
