// frontend/src/config.js

// Base URL for your FastAPI backend hosted on Azure App Service
export const API_BASE_URL =
  process.env.REACT_APP_API_URL ||
  "https://ticketing-tool-fkgggvcafjb2bnan.centralindia-01.azurewebsites.net";
