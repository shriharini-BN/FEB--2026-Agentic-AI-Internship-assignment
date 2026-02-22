def post_engagement(likes):
    total_likes = 0
    for like in likes:
        total_likes += like
    if total_likes >= 1000:
        status = "Viral Post"
    else:
        status = "Normal Engagement"
    print("Total Likes:", total_likes)
    print("Post Status:", status)
post_engagement([200, 300, 250, 300])