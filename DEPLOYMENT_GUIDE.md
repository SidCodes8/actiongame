# How to Deploy Falling & Catch to Render.com (Manual Setup)

This guide will help you deploy your Django game to the web for free using Render.com.

## Prerequisites
1.  **GitHub Account**: You need a GitHub account to host your code.
2.  **Render Account**: Sign up at [render.com](https://render.com).

## Step 1: Push Code to GitHub

1.  Create a new repository on GitHub (e.g., named `falling-catch-game`).
2.  Push your local code to this repository.

## Step 2: Deploy on Render

1.  Log in to your Render Dashboard.
2.  Click **"New +"** and select **"Web Service"**.
3.  Connect your GitHub account if you haven't already.
4.  Select your `falling-catch-game` repository from the list.
5.  **Configure the Service**:
    *   **Name**: Choose a unique name (e.g., `my-falling-catch-game`).
    *   **Region**: Choose the one closest to you.
    *   **Branch**: `main` (or whatever branch you pushed to).
    *   **Root Directory**: Leave blank (defaults to root).
    *   **Runtime**: `Python 3`.
    *   **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
    *   **Start Command**: `gunicorn config.wsgi:application`
6.  **Free Tier**: Select "Free" plan type.
7.  **Environment Variables**:
    You **must** add these in the "Environment" section (or "Advanced"):
    *   Key: `PYTHON_VERSION` Value: `3.12.0`
    *   Key: `SECRET_KEY` Value: (Generate a random string of characters here)
    *   Key: `DEBUG` Value: `False`
8.  Click **"Create Web Service"**.

## Step 3: Wait & Play!

Render will take a few minutes to build your app. You can watch the logs in the dashboard.
Once it says "Live", click the URL provided (e.g., `https://my-falling-catch-game.onrender.com`).

**Note on Free Tier**: The server will "spin down" (sleep) if no one visits it for a while. The first request after sleeping might take 30-50 seconds to load. This is normal!
