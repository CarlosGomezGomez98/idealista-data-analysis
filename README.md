# Barcelona Real Estate Price Predictor


An end-to-end data science project that scrapes real estate data, performs market segmentation using clustering, and predicts housing prices in Barcelona using regression models.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#-key-results">Key Results</a></li>
    <li><a href="#-built-with">Built With</a></li>
    <li><a href="#-getting-started">Getting Started</a></li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#-roadmap">Roadmap</a></li>
    <li><a href="#-license">License</a></li>
    <li><a href="#-contact">Contact</a></li>
    <li><a href="#-acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

This project was developed as part of my Master's Thesis in Big Data Management and Analysis. It addresses the growing challenge of accessing affordable housing in Spain's major cities, with a special focus on the highly competitive Barcelona market.

The main goal was to engineer a machine learning tool capable of accurately estimating the sale price of a property in Barcelona based on its features. The project covers the full data science pipeline:

* **Automated Data Collection:** Scraped over 12,000 property listings from the Spanish real estate portal [Idealista](https://www.idealista.com) using a custom web scraper.
* **In-depth Data Analysis:** Performed extensive data cleaning, feature engineering, and exploratory data analysis (EDA) to understand the market dynamics.
* **Market Segmentation:** Applied K-Means clustering to segment the properties into four distinct market categories, from budget-friendly apartments to premium luxury homes.
* **Predictive Modeling:** Trained and evaluated seven different regression algorithms to find the most accurate price prediction model.
* **Interactive Application:** Deployed the final model into an intuitive and user-friendly web application using `Streamlit`.

---

## Key Results

After a rigorous process of hyperparameter tuning and cross-validation, the project yielded the following key results:

* The best-performing model was **Gradient Boosting** (trained on a dataset with outliers removed), which achieved a **Coefficient of Determination (R²) of 0.812**. This indicates that the model can explain over 81% of the price variability in the dataset.
* The K-Means clustering analysis ($k=4$) successfully identified four distinct property archetypes, providing valuable market insights.

---

## Built With

This project was built using the following technologies and libraries:

* **Core & Modeling:**
    * [Python](https://www.python.org)
    * [scikit-learn](https://scikit-learn.org/stable/)
    * [Pandas](https://pandas.pydata.org)
    * [Numpy](https://numpy.org)
    * [XGBoost](https://xgboost.readthedocs.io/en/stable/index.html#)
* **Web Scraping:**
    * [Selenium](https://www.selenium.dev)
    * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* **Web Application:**
    * [Streamlit](https://streamlit.io)

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3.8+ and `pip` installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/carlosgomez1998/Barcelona-Housing-Price-Prediction.git](https://github.com/carlosgomez1998/Barcelona-Housing-Price-Prediction.git)
    cd Barcelona-Housing-Price-Prediction
    ```
    *(Note: Remember to replace the URL with your actual repository URL)*

2.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
