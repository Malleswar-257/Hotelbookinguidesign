# API Connection Documentation

## Overview
This document describes the API connections between frontend and backend.

## Backend Endpoints

Total endpoints: 1

### Endpoints List

- **POST** `/token`
  - Function: `login_for_access_token`
  - Operation: `CREATE`


## Frontend API Services

Total services: 2

### Available Services

- `token_service.ts` - Token API operations

## Usage Example

```javascript
import UserService from './api/services/user_service.js';

// Get all users
const users = await UserService.getAll();

// Get user by ID
const user = await UserService.getById(1);

// Create new user
const newUser = await UserService.create({ name: 'John', email: 'john@example.com' });

// Update user
const updated = await UserService.update(1, { name: 'Jane' });

// Delete user
await UserService.delete(1);
```

## Environment Variables

Make sure to set the following environment variables:

- `VITE_API_BASE_URL` (Vite projects)
- `NEXT_PUBLIC_API_BASE_URL` (Next.js projects)
- `REACT_APP_API_BASE_URL` (Create React App)

Default: `http://localhost:8000`
