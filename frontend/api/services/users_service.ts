// Users API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const UsersService = {
  // Get users by ID
  async getById(id) {
    return apiClient.get('/users'.replace('{id}', id));
  }
};

export default UsersService;
