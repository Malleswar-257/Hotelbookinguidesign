import { clsx, type ClassValue } from "clsx";
import { apiService } from '../services/api';

import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
