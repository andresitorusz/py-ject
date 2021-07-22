from colorama import Fore

from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport


def main():
    print(Fore.GREEN + "Hello there! Welcome to flatmates bill counter application. \nPlease fill the form below, "
                       "so we can count your and your flatmate bill.")
    amount, period, flatmate_name, co_flatmate_name, flatmate_days_in_apart, co_flatmate_days_in_apart = fill_the_form()

    bill = Bill(amount=amount, period=period)
    flatmate = Flatmate(name=flatmate_name, days_in_apart=flatmate_days_in_apart)
    co_flatmate = Flatmate(name=co_flatmate_name, days_in_apart=co_flatmate_days_in_apart)

    print(f"{flatmate.name} pays: ${flatmate.pays(bill, co_flatmate)}")
    print(f"{co_flatmate.name} pays: ${co_flatmate.pays(bill, flatmate)}")

    pdf_report = PdfReport(filename=f"{period}.pdf")
    pdf_report.generate(flatmate, co_flatmate, bill)


def fill_the_form():
    flatmate_name = input(Fore.RESET + "What is your name? ")
    amount = float(input(f"Hi {flatmate_name}, enter the total bill amount: $"))
    period = input("What is the bill period? (e.g. July 2021): ")
    co_flatmate_name = input("What is the name of the other flatmate? ")
    flatmate_days_in_apart = int(input("How many days did you stay in the house during the bill period? "))
    co_flatmate_days_in_apart = int(input(
        f"How many days did {co_flatmate_name} stay in the apart during the bill period? "
    ))

    return amount, period, flatmate_name, co_flatmate_name, flatmate_days_in_apart, co_flatmate_days_in_apart


if __name__ == '__main__':
    main()
