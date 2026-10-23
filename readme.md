# StyleMatch AI : AI-Powered Outfit Recommendation System

StyleMatch AI is a lightweight, content-based outfit recommendation prototype designed to suggest matching clothing items based on a user's selected top, occasion, and preferred style.
The project explores how AI-driven personalization could complement **Urban Wardrobe**, Cynbit's AR virtual try-on experience, by helping users discover coordinated outfits before trying them on virtually.

> **Project type:** AI/ML Proof of Concept  
> **Core techniques:** TF-IDF Vectorization and Cosine Similarity  
> **Interface:** Streamlit

## Features

- **Personalized outfit recommendations:** Suggests suitable bottoms and shoes based on user selections.
- **Content-based filtering:** Compares clothing attributes using TF-IDF vectorization and cosine similarity.
- **Occasion-aware filtering:** Filters candidate clothing items according to the selected occasion.
- **Style matching:** Uses catalog attributes such as style, color, and occasion to rank recommendations.
- **Interactive interface:** Provides an easy-to-use web application built with Streamlit.
- **Custom clothing catalog:** Uses a structured CSV dataset that can be extended with additional products.

## Problem Statement

Online fashion shoppers may struggle to identify clothing combinations that suit their preferred style and intended occasion. A virtual try-on experience helps users visualize clothing, but complementary outfit recommendations could further simplify their shopping decisions.
StyleMatch AI explores a potential solution by recommending coordinated clothing items from a catalog using content-based similarity.

## Proposed Business Opportunity

As a proposed extension to Cynbit's Urban Wardrobe AR experience, StyleMatch AI could:
- Help shoppers discover complementary clothing items.
- Support personalized shopping experiences.
- Encourage exploration of related products.
- Provide outfit suggestions before users proceed to virtual try-on.

These are potential benefits to investigate, not measured outcomes or existing Cynbit product features.

## Technology Stack

| Technology | Purpose |
-------------------------------
| Python | Core application logic |
| Pandas | Clothing catalog loading and processing |
| Scikit-learn | TF-IDF vectorization and cosine similarity |
| Streamlit | Interactive web interface |
| Pytest | Automated testing |

## How It Works

1. **Input:** The user selects a top, occasion, and preferred style.
2. **Catalog loading:** The application reads clothing information from `data/clothing_catalog.csv`.
3. **Feature preparation:** Relevant text attributes are combined into a textual representation.
4. **Vectorization:** TF-IDF converts the clothing descriptions into numerical feature vectors.
5. **Similarity calculation:** Cosine similarity compares the selected item's attributes with candidate items.
6. **Filtering and ranking:** Candidates are filtered by category and occasion, then ranked by similarity.
7. **Output:** The interface displays recommended bottoms and shoes with their similarity scores.

**Important:** Similarity scores measure textual attribute similarity. They are not probabilities, verified fashion compatibility scores, or evidence of customer preference.

## Project Structure

```text
stylematch-ai/
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── data/
│   └── clothing_catalog.csv
```

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by the listed dependencies
- pip
- Git (optional, for GitHub publishing)

### 1. Clone the repository

```bash
git clone https://github.com/kratika1428/cynbit-stylematch-ai.git
cd stylematch-ai
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can interact with the application.

## Dataset

The prototype uses `data/clothing_catalog.csv`, a structured clothing catalog containing product attributes used by the recommendation pipeline.

The recommender relies on catalog text rather than historical user interactions. The dataset should not be interpreted as Cynbit's real product inventory or customer data.

## Current Limitations

- Uses a small demonstration catalog rather than a live retail inventory.
- Does not learn from real customer purchases, clicks, ratings, or feedback.
- Does not implement AR rendering or virtual try-on.
- Does not predict clothing size or fit.
- Does not use a trained deep-learning model or a large language model.
- Recommendations depend on the quality and coverage of catalog attributes.
- Business impact has not been measured in a production environment.

## Future Enhancements

- Integrate outfit recommendations with an AR virtual try-on workflow.
- Expand the catalog with product images, brands, prices, and availability.
- Collect user feedback to improve recommendation quality.
- Evaluate recommendations using precision@K, recall@K, and user feedback.
- Explore hybrid recommendations combining product content and user interaction data.
- Add product-level filtering for budget, color preferences, and availability.

## Evaluation Approach

A production-oriented evaluation could measure:

- **Recommendation relevance:** Whether users find suggested items suitable.
- **Click-through rate:** How often recommended products are opened.
- **Add-to-cart rate:** Whether recommendations encourage shopping actions.
- **Conversion rate:** Whether recommendations contribute to purchases.
- **Return rate:** Whether coordinated outfit suggestions affect returns.

These metrics would require an appropriately designed experiment and real usage data. No improvement in these metrics is claimed by this prototype.

## Reference

Cynbit — Urban Wardrobe AR Integration:  
https://www.cynbit.in/case-studies/urban-wardrobe-ar-integration

StyleMatch AI is an independent proof-of-concept project developed to explore a potential personalization extension. It is not an official Cynbit product and is not affiliated with or endorsed by Cynbit.

## Author
Kratika Singhal
(Developed as an AI/ML engineering proof of concept to demonstrate content-based recommendation, Python development, and practical application design.)