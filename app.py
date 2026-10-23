import streamlit as st

from recommender import *

st.set_page_config(
    page_title="StyleMatch AI",
    layout="centered"
)
st.title("StyleMatch AI")
st.subheader("Smart Outfit Recommendation System")
st.write("Discover clothing combinations based on your preferred style and occasion.")
st.divider()

catalog = load_catalog()

top = st.selectbox(
    "Choose your top",
    get_available_tops()
)
occasion = st.selectbox(
    "Choose the occasion",
    get_available_occasions(top)
)
style = st.selectbox(
    "Choose your preferred style",
    ["Classic", "Minimal", "Trendy"]
)

if st.button("Recommend My Outfit", type="primary"):
    try:
        result = recommend_outfit(
            top,
            occasion,
            style
        )
        st.success("Your outfit recommendation is ready!")

        st.markdown("### Recommended Outfit")
        col1, col2, col3 = st.columns(3)
        col1.metric("Top", result["top"])
        col2.metric("Bottom", result["bottom"])
        col3.metric("Shoes", result["shoes"])

        st.markdown("### Recommendation Explanation")
        st.write(result["explanation"])

        st.markdown("### Recommended Product Details")

        st.dataframe(
            result["products"],
            hide_index=True,
            use_container_width=True
        )

    except ValueError as error:
        st.error(str(error))

st.divider()

with st.expander("View Complete Clothing Catalog"):
    st.dataframe(
        catalog,
        hide_index=True,
        use_container_width=True
    )

st.caption(
    "StyleMatch AI uses content-based similarity. "
    "It does not currently provide AR virtual try-on "
    "or trained personalized recommendations."
)