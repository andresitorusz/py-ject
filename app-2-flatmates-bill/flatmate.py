class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_apart):
        self.name = name
        self.days_in_apart = days_in_apart

    def pays(self, bill, co_flatmate):
        weight = self.days_in_apart / (self.days_in_apart + co_flatmate.days_in_apart)
        bill = bill.amount * weight
        return bill
