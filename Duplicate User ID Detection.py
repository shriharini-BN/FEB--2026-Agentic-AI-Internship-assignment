user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]
count_ids = {}
for user in user_ids:
    count_ids[user] = count_ids.get(user, 0) + 1
for user, count in count_ids.items():
    if count > 1:
        print(f"{user} → {count} times")