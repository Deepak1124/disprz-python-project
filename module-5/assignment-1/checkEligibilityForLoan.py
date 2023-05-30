# Create a program to check eligibility of the person for loan  with the help of oops concepts 
# and exception handling. Person whose salary is less than 10K/ Month will not be eligible for the loan.

class LoanEligibility:
    def __init__(self, salary):
        self.salary = salary

    def is_eligible(self):
        if self.salary >= 10000:
            return True
        else:
            raise LoanNotEligibleException("Person's salary is less than 10K/ Month")


class LoanNotEligibleException(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    salary = int(input("Enter the person's salary: "))

    try:
        loan_eligibility = LoanEligibility(salary)
        if loan_eligibility.is_eligible():
            print("Person is eligible for loan.")
        else:
            print("Person is not eligible for loan.")
    except LoanNotEligibleException as e:
        print(e)


if __name__ == "__main__":
    main()
