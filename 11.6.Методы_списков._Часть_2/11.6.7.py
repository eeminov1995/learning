s = input().lower().split()

print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")