import axios from "axios";

const api: any = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export default api;
