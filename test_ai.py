from ai.generator import generate_test_cases

response = generate_test_cases(
    "User should be able to login using username and password."
)

print(response)