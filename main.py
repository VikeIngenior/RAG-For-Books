import uvicorn

def main():
    uvicorn.run(
        app='wsgi:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )

    if __name__ == '__main__':
        main()