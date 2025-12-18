const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || process.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const apiService = {
  async create_(data) {
    const response = await fetch(`${API_BASE_URL}-`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Failed to create _');
    return response.json();
  },
  async get_() {
    const response = await fetch(`${API_BASE_URL}-`);
    if (!response.ok) throw new Error('Failed to fetch _');
    return response.json();
  },
};

export default apiService;
