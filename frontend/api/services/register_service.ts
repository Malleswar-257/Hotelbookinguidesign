// Register API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const RegisterService = {
  // Create new register
  async create(data) {
    return apiClient.post('/register', data);
  }
};

export default RegisterService;
