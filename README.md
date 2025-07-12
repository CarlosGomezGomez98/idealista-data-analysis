# Barcelona Real Estate Price Predictor
<div align="center">
<!-- GitHub Stats -->
<a href="https://github.com/CarlosGomezGomez98/idealista-data-analysis">
    <img src="https://img.shields.io/github/stars/CarlosGomezGomez98/idealista-data-analysis?style=flat-square" alt="GitHub stars">
</a>
<a href="https://github.com/CarlosGomezGomez98/idealista-data-analysis/fork">
    <img src="https://img.shields.io/github/forks/CarlosGomezGomez98/idealista-data-analysis?style=flat-square" alt="GitHub forks">
</a>
<a href="https://github.com/CarlosGomezGomez98/idealista-data-analysis/issues">
    <img src="https://img.shields.io/github/issues/CarlosGomezGomez98/idealista-data-analysis?style=flat-square" alt="GitHub issues">
</a>
<a href="https://github.com/CarlosGomezGomez98/idealista-data-analysis/blob/main/LICENSE.txt">
     <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</a>
    
</div>

<div align="center">
<!-- Technologies -->
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
<img src="https://img.shields.io/badge/Numpy-013243?style=flat-square&logo=numpy&logoColor=white" alt="Numpy">
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white" alt="Selenium">

</div>
An end-to-end data science project that scrapes real estate data, performs market segmentation using clustering, and predicts housing prices in Barcelona using regression models.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#key-results">Key Results</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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
---
##  Usage

The primary deliverable of this project is the interactive web application. To launch it, run the following command from the root directory of the project:

```sh
streamlit run app.py
```


## Roadmap

Future enhancements for this project could include:

* [ ] **Expand the Dataset:** Incorporate socioeconomic data, historical transaction records, and proximity to amenities (e.g., public transport, schools) to enrich the model.
* [ ] **Longitudinal Analysis:** Study how price trends evolve over time by collecting data periodically to capture market shifts.
* [ ] **Advanced Modeling:** Experiment with more complex neural network architectures or other machine learning algorithms to improve predictive accuracy.

See the [open issues](https://github.com/CarlosGomezGomez98/idealista-data-analysis/issues) for a full list of proposed features (and known issues).

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

*(Note: You'll need to create a file named `LICENSE.txt` in your repository with the MIT License text).*


---

## Contact


* Email: [carlosgomezgomez1998@gmail.com](mailto:carlosgomezgomez1998@gmail.com)
* Likedin: [carlos-gómez-gómez](https://www.linkedin.com/in/carlos-gómez-gómez-a91961185/)
* Project Link: [https://github.com/CarlosGomezGomez98/idealista-data-analysis](https://github.com/CarlosGomezGomez98/idealista-data-analysis)


---

## Acknowledgments

A few acknowledgments for this project:

* My thesis advisor, **Jorge Crespo Álvarez**, for the guidance and support.
* The open-source community for creating amazing tools like `scikit-learn`, `pandas`, and `Streamlit`.

