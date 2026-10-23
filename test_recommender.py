from recommender import recommend_outfit

result = recommend_outfit(
    "White shirt",
    "Casual",
    "Trendy"
)

print(result)
print("\nRecommended outfit")
print("Top:", result["top"])
print("Bottom:", result["bottom"])
print("Shoes:", result["shoes"])
print("Explanation:", result["explanation"])