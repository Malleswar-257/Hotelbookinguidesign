// Rooms API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const RoomsService = {
  // Create new rooms
  async create(data) {
    return apiClient.post('/rooms', data);
  }

  // Get rooms by ID
  async getById(id) {
    return apiClient.get('/rooms'.replace('{id}', id));
  }
};

export default RoomsService;
