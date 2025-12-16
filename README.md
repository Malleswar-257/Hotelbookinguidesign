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

- hotel search
- room booking
- booking management
- user authentication

## API Endpoints

- `GET /api/hotels` - Retrieve a list of hotels based on search criteria (location, date range).
- `GET /api/rooms/{hotel_id}` - Retrieve available rooms for a specific hotel.
- `POST /api/bookings` - Book a room for a specific date range.
- `DELETE /api/bookings/{booking_id}` - Cancel a booked room.
- `POST /api/auth/register` - Register a new user account.
- `POST /api/auth/login` - Login to an existing user account.

## License

MIT
