"""Demonstrating dictionary capabilities."""

# declaring type
schools: dict[str, int]

# initializing an empty dict
schools = dict()

# setting key-value pairing
schools["UNC"] = 19400  # cant use commas for large nums
schools["Duke"] = 6717

# printing dict literal example
print(schools)

# accessing a value
print(schools["UNC"])

# removing a key-value pair
schools.pop("Duke")

# test for existance of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present {is_duke_present}")

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")