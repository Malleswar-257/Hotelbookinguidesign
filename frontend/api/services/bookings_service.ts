// Bookings API Service (TypeScript)
import apiClient, { ApiResponse, ApiError } from '../client';

export const BookingsService = {
  // Create new bookings
  async create(data) {
    return apiClient.post('/bookings', data);
  }

  // Get bookings by ID
  async getById(id) {
    return apiClient.get('/bookings'.replace('{id}', id));
  }
};

export default BookingsService;
