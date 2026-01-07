# How to Deploy Falling & Catch to Render.com (Automatic Blueprint)

This guide will help you deploy your Django game to the web for free using Render.com's "Blueprint" feature. This is the easiest and most robust method.

## Prerequisites
1.  **GitHub Account**: You need a GitHub account to host your code.
2.  **Render Account**: Sign up at [render.com](https://render.com).

## Step 1: Push Code to GitHub

1.  Create a new repository on GitHub (e.g., named `falling-catch-game`).
2.  Push your local code to this repository.

## Step 2: Deploy on Render

1.  Log in to your Render Dashboard.
2.  Click **"New +"** and select **"Blueprint"**.
3.  Connect your GitHub account if you haven't already.
4.  Select your `falling-catch-game` repository from the list.
5.  **Service Name**: Enter a name (e.g., `falling-catch-game`).
6.  **Apply**: Click **"Apply"**.

Render will automatically read the `render.yaml` file in your repository and set everything up for you (Build command, Start command, Environment variables, etc.).

## Step 3: Wait & Play!

Render will take a few minutes to build your app. You can watch the logs in the dashboard.
Once it says "Live", click the URL provided (e.g., `https://falling-catch-game.onrender.com`).

**Note on Free Tier**: The server will "spin down" (sleep) if no one visits it for a while. The first request after sleeping might take 30-50 seconds to load. This is normal!
