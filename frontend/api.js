const API_URL = 'http://localhost:5000/api';

export const fetchResources = async () => {
    const response = await fetch(`${API_URL}/resources`);
    return await response.json();
};