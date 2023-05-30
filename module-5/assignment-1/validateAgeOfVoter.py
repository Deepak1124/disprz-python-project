# Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less than 18 should not be allowed to vote.

class VoterAgeException(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate_voter_age(age):
    if age < 18:
        raise VoterAgeException("Voter's age must be at least 18.")


def main():
    age = int(input("Enter the voter's age: "))

    try:
        validate_voter_age(age)
        print("Voter is eligible to vote.")
    except VoterAgeException as e:
        print(e)


if __name__ == "__main__":
    main()
