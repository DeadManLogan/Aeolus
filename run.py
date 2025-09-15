from src.app import create_app
from config import Settings

settings = Settings()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
