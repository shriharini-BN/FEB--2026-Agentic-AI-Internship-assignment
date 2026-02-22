def duplicate_accounts(usernames):
    if len(usernames) != len(set(usernames)):
      print("Duplicate Accounts Found: Yes")
    else:
        print("Duplicate Accounts Found: No")
duplicate_accounts(["ram", "sam", "ram", "john"])