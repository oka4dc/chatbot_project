# FastAPI Chatbot with OpenAI API

This project is a chatbot application built using FastAPI and OpenAI's API. The chatbot is designed to receive user input, process it through OpenAI's GPT model, and return a response. A simple HTML interface allows users to interact with the chatbot, and Postman can be used for API testing.

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Running the Application](#running-the-application)
6. [Using the Chatbot UI](#using-the-chatbot-ui)
7. [Testing with Postman](#testing-with-postman)
8. [Future Improvements](#future-improvements)

## Features
- Chatbot endpoint using OpenAI's GPT model.
- Simple HTML interface for user interaction.
- API endpoint for easy testing and integration with other applications.

## Project Structure

chatbot_project/
├── app/
│   ├── __init__.py            # Marks the app folder as a Python package
│   ├── main.py                # Main FastAPI application
│   └── api/
│       └── routes.py          # FastAPI routes for chatbot endpoint
├── static/
│   └── index.html             # HTML file for the chatbot UI
├── .env                       # Environment variables (e.g., OpenAI API key)
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation


