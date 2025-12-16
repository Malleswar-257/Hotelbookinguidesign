// Base API Client for React (TypeScript)
import axios, { AxiosError, AxiosResponse } from 'axios';

export interface ApiResponse<T = any> {
  data: T;
  status: number;
  message?: string;
}

export interface ApiError {
  status: number;
  message: string;
  data?: any;
}

const API_BASE_URL =
  (import.meta as any)?.env?.VITE_API_BASE_URL ||
  process.env.REACT_APP_API_BASE_URL ||
  process.env.API_BASE_URL ||
  'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,
  timeout: 15000,
});

const normalizeResponse = <T>(response: AxiosResponse<T>): ApiResponse<T> => ({
  data: response?.data,
  status: response?.status ?? 200,
  message: (response?.data as any)?.message || response?.statusText || '',
});

const normalizeError = (error: AxiosError): ApiError => ({
  status: error?.response?.status ?? 0,
  message: (error?.response?.data as any)?.message || error?.message || 'Request failed',
  data: error?.response?.data,
});

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers = config.headers || {};
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(normalizeError(error))
);

apiClient.interceptors.response.use(
  (response) => normalizeResponse(response),
  (error) => Promise.reject(normalizeError(error))
);

export default apiClient;
