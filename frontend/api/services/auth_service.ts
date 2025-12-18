// Auth API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const AuthService = {
  // Create new auth
  async create(data) {
    return apiClient.post('/auth/register', data);
  }

  // Create new auth
  async create(data) {
    return apiClient.post('/auth/login', data);
  }
};

export default AuthService;
