// Hotels API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const HotelsService = {
  // Create new hotels
  async create(data) {
    return apiClient.post('/hotels', data);
  }

  // Get hotels by ID
  async getById(id) {
    return apiClient.get('/hotels'.replace('{id}', id));
  }
};

export default HotelsService;
