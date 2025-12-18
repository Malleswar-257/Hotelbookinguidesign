// Items API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const ItemsService = {
  // Get items by ID
  async getById(id) {
    return apiClient.get('/items'.replace('{id}', id));
  }
};

export default ItemsService;
