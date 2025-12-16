// Hotels API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const HotelsService = {
  // Get hotels by ID
  async getById(id) {
    return apiClient.get('/hotels'.replace('{id}', id));
  }
};

export default HotelsService;
