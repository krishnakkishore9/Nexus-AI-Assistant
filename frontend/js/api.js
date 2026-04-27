// Set BACKEND_URL to your deployed Vercel backend URL for production.
// For local development this automatically falls back to localhost:8001.
const BASE_URL = (window.BACKEND_URL || "http://localhost:8001") + "/api";

const API = {
    async post(endpoint, data, token = null) {
        const headers = {
            "Content-Type": "application/json"
        };
        if (token) headers["Authorization"] = `Bearer ${token}`;

        try {
            const response = await fetch(`${BASE_URL}${endpoint}`, {
                method: "POST",
                headers: headers,
                body: JSON.stringify(data)
            });
            return await response.json();
        } catch (error) {
            console.error(`API Error on ${endpoint}:`, error);
            return { status: "error", detail: "Network connection failed" };
        }
    },

    async get(endpoint, token = null) {
        const headers = {};
        if (token) headers["Authorization"] = `Bearer ${token}`;

        try {
            const response = await fetch(`${BASE_URL}${endpoint}`, {
                method: "GET",
                headers: headers
            });
            return await response.json();
        } catch (error) {
            console.error(`API Error on ${endpoint}:`, error);
            return { status: "error", detail: "Network connection failed" };
        }
    }
};