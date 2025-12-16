// Auth API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const AuthService = {
  // Create new auth
  async create(data) {
    return apiClient.post('/api/auth/register', data);
  }

  // Create new auth
  async create(data) {
    return apiClient.post('/api/auth/login', data);
  }
};

export default AuthService;
