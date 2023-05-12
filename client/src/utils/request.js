import axios from "axios";

export const request = axios.create({
  baseURL:
    process.env.NODE_ENV === "production"
      ? "http://141.26.157.102"
      : "http://localhost:8000",
});
