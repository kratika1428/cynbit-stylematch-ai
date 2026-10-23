import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CATALOG_PATH = Path(__file__).parent / "data" / "clothing_catalog.csv"
VALID_STYLES = ["Classic", "Minimal", "Trendy"]

def load_catalog():
    catalog = pd.read_csv(CATALOG_PATH)

    required = {"item", "category", "color", "style", "occasion"}
    if not required.issubset(catalog.columns):
        raise ValueError("The clothing catalog is missing required columns.")

    return catalog.fillna("")

def get_available_tops():
    catalog = load_catalog()
    return catalog[catalog["category"] == "Top"]["item"].tolist()

def get_available_occasions(top):
    catalog = load_catalog()
    matching = catalog[catalog["item"] == top]

    if matching.empty or matching.iloc[0]["category"] != "Top":
        raise ValueError("Please select a valid top.")

    return matching.iloc[0]["occasion"].split("|")

def build_feature_text(catalog):
    return (
        catalog["style"].str.replace("|", " ", regex=False)
        + " "
        + catalog["occasion"].str.replace("|", " ", regex=False)
        + " "
        + catalog["color"]
    ).str.lower()

def rank_items(catalog, category, occasion, style, top_color):
    candidates = catalog[
        (catalog["category"] == category)
        & catalog["occasion"].apply(
            lambda value: occasion in value.split("|")
        )
    ].copy()

    if candidates.empty:
        raise ValueError(
            f"No {category.lower()} items are available for {occasion}."
        )

    # Query emphasizes the selected occasion and style.
    query = f"{style} {style} {occasion} {occasion}"
    feature_text = build_feature_text(candidates)
    documents = feature_text.tolist() + [query]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        matrix[-1],
        matrix[:-1]
    ).flatten()
    candidates["similarity_score"] = scores

    # Prefer style-compatible items if their scores are equal.
    candidates["style_match"] = candidates["style"].apply(
        lambda value: int(style in value.split("|"))
    )

    candidates = candidates.sort_values(
        by=["similarity_score", "style_match", "item"],
        ascending=[False, False, True]
    )

    return candidates.iloc[0].to_dict()

def recommend_outfit(top, occasion, style):
    catalog = load_catalog()

    if style not in VALID_STYLES:
        raise ValueError("Please select a supported style.")

    top_rows = catalog[
        (catalog["item"] == top)
        & (catalog["category"] == "Top")
    ]

    if top_rows.empty:
        raise ValueError("Please select a supported top.")

    selected_top = top_rows.iloc[0].to_dict()
    available_occasions = selected_top["occasion"].split("|")

    if occasion not in available_occasions:
        raise ValueError(
            f"{top} is not listed for the {occasion} occasion."
        )

    bottom = rank_items(
        catalog,
        "Bottom",
        occasion,
        style,
        selected_top["color"]
    )
    shoes = rank_items(
        catalog,
        "Shoes",
        occasion,
        style,
        selected_top["color"]
    )
    explanation = (
        f"The {bottom['item'].lower()} and "
        f"{shoes['item'].lower()} were selected because "
        f"their catalog attributes match your "
        f"{occasion.lower()} occasion and "
        f"{style.lower()} style preference."
    )
    products = [
        selected_top,
        bottom,
        shoes
    ]

    return {
        "top": top,
        "bottom": bottom["item"],
        "shoes": shoes["item"],
        "occasion": occasion,
        "style": style,
        "explanation": explanation,
        "products": products,
        "bottom_score": round(float(bottom["similarity_score"]), 3),
        "shoes_score": round(float(shoes["similarity_score"]), 3),
        "method": "Content-based TF-IDF and cosine similarity",
    }