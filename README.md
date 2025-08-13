# Stock_Sentimental_Analysis

# AI-Powered Stock Market Sentiment Analysis

This project provides real-time sentiment analysis for publicly traded stocks by scraping and interpreting data from financial news and social media platforms. It leverages Natural Language Processing (NLP) to generate predictive insights, assisting users in making informed trading decisions through an interactive web dashboard.

## Description

In today's volatile financial markets, understanding public sentiment is crucial. This application provides a powerful tool for traders and investors by automating the process of data collection and sentiment analysis. Users can enter any valid stock symbol, and the system dynamically scrapes the latest news from Yahoo Finance and discussions from Twitter. This data is then processed through a pipeline of NLP models to calculate sentiment scores, which are stored and visualized historically. The result is a powerful, real-time snapshot of market sentiment for any given stock.

## Key Features

- **Dynamic Web Scraping:** Uses Playwright and BeautifulSoup to extract real-time headlines and social media posts from Yahoo Finance and Twitter for any user-provided stock symbol.
- **NLP Sentiment Analysis:** Employs NLTK, VADER, and TextBlob to process textual data, extracting polarity and subjectivity scores to assess sentiment.
- **RESTful API:** A backend built with **FastAPI** provides endpoints to trigger the scraping and analysis pipeline on-demand.
- **Data Persistence:** Integrates with a **PostgreSQL** database to store historical sentiment data for trend analysis.
- **Interactive Dashboard:** A modern frontend built with **React** and **Material-UI** allows users to input stock symbols and view dynamic charts (using Chart.js) that visualize sentiment trends over time.
- **Cloud-Native Deployment:** The application is fully deployed, with the frontend hosted on Netlify and the backend API on AWS for scalability and high availability.

## Technologies Used

- **Backend:** Python, FastAPI, Playwright, BeautifulSoup, NLTK, TextBlob, VADER
- **Frontend:** React.js, Chart.js, Material-UI
- **Database:** PostgreSQL
- **Deployment:** AWS, Netlify, Git

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.9+
- Node.js and npm
- PostgreSQL server

### Installation

1.  **Clone the new repo** (after you push the code):
    ```sh
    git clone <your-new-repo-url>
    ```
2.  **Setup Backend** (from the project's root directory):
    ```sh
    # Navigate to your Python environment and install dependencies
    pip install -r requirements.txt
    # Set up your .env file with database credentials
    ```
3.  **Setup Frontend** (from the project's root directory):
    ```sh
    # Navigate to your frontend folder
    cd frontend
    # Install npm packages
    npm install
    ```
