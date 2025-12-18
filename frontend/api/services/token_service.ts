// Token API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const TokenService = {
  // Create new token
  async create(data) {
    return apiClient.post('/token', data);
  }
};

export default TokenService;
