def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available"


    positive_ratings = sum(1 for rating in ratings if rating in [4, 5])


    percentage = (positive_ratings / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.2f}%"


#
ratings_input = input(" ratings: ")
ratings = list(map(int, ratings_input.split(',')))


print(calculate_positive_feedback_percentage(ratings))
