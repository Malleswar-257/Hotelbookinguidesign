// Login API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const LoginService = {
  // Create new login
  async create(data) {
    return apiClient.post('/login', data);
  }
};

export default LoginService;
