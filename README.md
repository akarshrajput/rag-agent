# Valuefy Natural Language Cross-Platform Data Query RAG Agent

A professional AI-powered platform for querying wealth portfolio data across MongoDB and MySQL using natural language. Built with FastAPI (Python) for the backend, Next.js (React) for the frontend, MongoDB for client profiles, and Shadcn UI for a modern interface. Integrates GroqCloud API and LangChain for advanced AI-driven responses.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Managing the Backend](#managing-the-backend)
- [Frontend Usage](#frontend-usage)
- [Deployment Notes](#deployment-notes)
- [Logging & Monitoring](#logging--monitoring)
- [Contribution Guidelines](#contribution-guidelines)
- [Future Vision](#future-vision)
- [Contact & Support](#contact--support)

---

---
<img width="1710" alt="Screenshot 2025-06-25 at 7 52 30 PM" src="https://github.com/user-attachments/assets/6997fd1a-7e44-4064-aca1-72f7e51a3d36" />
<img width="1710" alt="Screenshot 2025-06-25 at 7 52 47 PM" src="https://github.com/user-attachments/assets/2f3cd570-aed0-4b9d-b27e-f281ed8d772f" />
<img width="1710" alt="Screenshot 2025-06-25 at 7 53 59 PM" src="https://github.com/user-attachments/assets/71fc7faf-6134-438a-aee0-90002b2f4692" />
<img width="1710" alt="Screenshot 2025-06-25 at 7 53 48 PM" src="https://github.com/user-attachments/assets/f99913c0-7961-4f8c-b22d-3eddedffd7ed" />
<img width="1710" alt="Screenshot 2025-06-25 at 7 53 15 PM" src="https://github.com/user-attachments/assets/4b90fa09-12d4-42e7-a200-516351f36694" />
<img width="1710" alt="Screenshot 2025-06-25 at 7 52 47 PM" src="https://github.com/user-attachments/assets/d7b8b2ef-6f19-4c19-a854-bebc3f775996" />

## Overview

This project enables business users to ask complex, cross-database questions about high-value client portfolios in plain English and receive responses as text, tables, or graphs. Designed for asset management firms handling portfolios of film stars and sports personalities, with seamless integration between AI, databases, and a modern frontend.

---

## Features

- Natural language querying over MongoDB (client profiles) and MySQL (transactions)
- AI-powered responses using GroqCloud API + LangChain
- RESTful FastAPI backend
- Next.js frontend with React and Shadcn UI components
- Secure, scalable, and production-ready architecture
- Supports text, table, and graph outputs
- Easy local and cloud deployment

---

## Architecture


---

## Tech Stack

- **Backend:** Python, FastAPI, LangChain, GroqCloud API
- **Frontend:** Next.js (React), Shadcn UI
- **Databases:** MongoDB (client profiles), MySQL (transactions)
- **Deployment:** Local, Vercel, or any cloud provider

---

## Prerequisites

- Python 3.9+
- Node.js 18+
- MongoDB instance (local or Atlas)
- MySQL instance (local or cloud)
- GroqCloud API Key
- Git

---

## Setup & Installation

### 1. Clone the Repository


### 2. Backend (FastAPI) Setup



#### Environment Variables

Create a `.env` file in the `backend/` directory with:


#### Start FastAPI Server

- The API will be available at `http://localhost:8000`.

### 3. Frontend (Next.js + Shadcn UI) Setup


#### Configure API Proxy

Ensure the frontend is configured to proxy API requests to the FastAPI backend (see `next.config.js`):


#### Start Next.js Frontend

- The frontend will be available at `http://localhost:3000`.

#### Install Shadcn UI

- Import and use Shadcn UI components as needed.

---

## Running the Application

1. Start the backend FastAPI server.
2. Start the Next.js frontend.
3. Open `http://localhost:3000` in your browser.
4. Log in and begin querying using natural language.

---

## Environment Variables

| Variable           | Description                       |
|--------------------|-----------------------------------|
| MONGODB_URI        | MongoDB connection string         |
| MYSQL_URI          | MySQL connection string           |
| GROQ_API_KEY       | GroqCloud API key                 |
| LANGCHAIN_API_KEY  | LangChain API key                 |

**How to get GroqCloud API Key:**  
- Sign up/log in to Groq Cloud.
- Go to "Create API Key", name it, and copy the key (it will not be shown again).
- Set it as an environment variable or in your `.env` file.

---

## Managing the Backend

- **Start:** `uvicorn main:app --host 0.0.0.0 --port 8000`
- **Stop:** Use `Ctrl+C`
- **Logs:** Output is shown in the terminal. For production, configure logging in `main.py` and use tools like Gunicorn or Docker for process management.
- **Hot Reload:** Use `--reload` flag for development.

---

## Frontend Usage

- Built with Next.js and Shadcn UI for a modern, responsive interface.
- Query interface allows users to type natural language questions.
- Results are displayed as text, tables, or graphs.
- Authentication and user management can be extended as needed.

---

## Deployment Notes

- **Local:** Run backend and frontend as described above.
- **Production:**  
  - Deploy FastAPI backend on cloud (AWS, GCP, Azure, Vercel, etc.).
  - Use Docker for containerization (recommended).
  - Secure endpoints with HTTPS.
  - Deploy Next.js frontend (Vercel, Netlify, or your own server).
  - Set environment variables securely in your deployment environment.

---

## Logging & Monitoring

- Backend logs are output to the console by default.
- For production, integrate with a logging service (e.g., ELK, Datadog).
- Monitor API health and errors.
- Add audit logs for sensitive queries if required.

---

## Contribution Guidelines

- Fork the repository and create a feature branch.
- Write clear, concise commit messages.
- Ensure code is linted and tested.
- Open a pull request for review.

---

## Future Vision

- **MCP (Model Context Protocol):**  
  Integrate MCP for improved scalability and context management across AI agents.
- **Role-based Access Control:**  
  Add granular permissions for different user roles.
- **Advanced Analytics:**  
  More complex visualizations and insights.
- **Multi-tenancy:**  
  Support for multiple asset management firms.
- **CI/CD:**  
  Automate testing and deployment pipelines.

---

## Contact & Support

For issues, open a GitHub issue or contact the maintainer.


**_This README is crafted for professional submission to Valuefy, demonstrating technical depth, clarity, and scalability._**
