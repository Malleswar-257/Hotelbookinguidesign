// Users API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const UsersService = {
  // Create new users
  async create(data) {
    return apiClient.post('/users', data);
  }

  // Get users by ID
  async getById(id) {
    return apiClient.get('/users'.replace('{id}', id));
  }
};

export default UsersService;
