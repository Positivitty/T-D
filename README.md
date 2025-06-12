# T@D Rolloff Container Tracker

A modern web application for managing roll-off containers, tracking their locations, and maintaining customer records.

## Features

- Container Management
  - Track container status and location
  - Assign containers to customers
  - View container history

- Customer Management
  - Store customer information
  - Track customer's container usage
  - Search customers by name

- Activity Logging
  - Record container pickups and deliveries
  - Maintain history of container movements
  - Track maintenance activities

## Tech Stack

- Backend:
  - FastAPI (Python)
  - PostgreSQL
  - SQLAlchemy ORM
  - Pydantic for data validation

- Frontend:
  - React with TypeScript
  - Mantine UI components
  - React Router for navigation
  - Axios for API calls

## Setup

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL
- Git

### Backend Setup

1. Create and activate a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE tad_rolloff;
   ```

4. Create a `.env` file in the backend directory with the following content:
   ```
   POSTGRES_SERVER=localhost
   POSTGRES_USER=your_postgres_username
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_DB=tad_rolloff
   SECRET_KEY=your-secret-key-here  # Generate a secure random key
   ```

5. Run the application:
   ```bash
   python run.py
   ```

   The API will be available at http://localhost:8000

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

   The application will be available at http://localhost:3000

## API Documentation

Once the backend is running, visit http://localhost:8000/docs for the interactive API documentation.

## Project Structure

```
tad-rolloff/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   ├── core/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── models/
│   │   └── schemas/
│   ├── requirements.txt
│   └── run.py
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── containers/
    │   │   ├── customers/
    │   │   └── log-entries/
    │   ├── api/
    │   ├── types/
    │   ├── App.tsx
    │   └── main.tsx
    ├── package.json
    └── vite.config.ts
```

## Development

### Backend Development

- The backend uses FastAPI for the REST API
- SQLAlchemy for database ORM
- Pydantic for data validation and serialization
- PostgreSQL for the database

### Frontend Development

- React with TypeScript for type safety
- Mantine UI components for a modern look
- React Router for client-side routing
- Axios for API communication

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 