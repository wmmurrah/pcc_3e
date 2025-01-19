# check_usernames

current_users = ["wmm0017", "Kwm0082", "rlm0018", "Tlw0055", "mmw0055"]

new_users = ["dtm0085", "amp0033", "Fre0078", "Wmm0017", "Rlm0018"]

current_users_lower = [current_user.lower() for current_user in current_users]
new_users_lower = [new_user.lower() for new_user in new_users]

# TODO fix below. not functionsl
for new_user in new_users_lower:
    if new_user in current_users_lower:
        print(
            f"Username {new_user} is not available. "
            "Please choose another username."
        )
    else:
        print(f"Username {new_user} is available.")
