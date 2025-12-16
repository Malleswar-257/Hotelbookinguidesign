# Hotel Booking Application
## Setup Instructions
1. Install dependencies:
    ```bash
devcontainer run --workspace-folder $(pwd)
    ````2. Set environment variables:
    ```bash
cp .env.example .env
    ```3. Run the application:
    ```bash
uvicorn app.main:app --reload
    ```