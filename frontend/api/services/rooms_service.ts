// Rooms API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const RoomsService = {
  // Create new rooms
  async create(data) {
    return apiClient.post('/rooms', data);
  }
};

export default RoomsService;
