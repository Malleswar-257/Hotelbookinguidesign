# Hotelbookinguidesign

Backend generation request for repo https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign

## Tech Stack

- **Backend**: FastAPI + SQLAlchemy
- **Frontend**: Provided via GitHub repo (https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign)

## Project Structure

```
Hotelbookinguidesign/
├── frontend/           # Frontend (cloned from provided repo)
├── backend/            # Backend API
├── README.md           # This file
└── docker-compose.yml  # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)
- Node.js 18+ (for frontend from repo)

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
python -m venv .venv
source .venv/bin/activate  # or .venv\Scriptsctivate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup (from provided repo)

```bash
cd frontend
npm install
npm run dev
```

## Features

- User registration and login
- Hotel search based on location and date
- Viewing hotel details
- Room booking

## API Endpoints

- `POST /api/register` - Endpoint for user registration
- `POST /api/login` - Endpoint for user login
- `GET /api/hotels/search` - Endpoint to search hotels based on location and date
- `GET /api/hotels/{hotel_id}` - Endpoint to view details of a hotel
- `POST /api/bookings` - Endpoint to book a hotel room

## License

MIT
