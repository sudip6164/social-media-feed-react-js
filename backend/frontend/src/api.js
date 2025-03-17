import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

export const getPosts = async () => {
    const response = await axios.get(`${API_URL}/posts/`);
    return response.data;
};
