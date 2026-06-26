import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    active: bool

@dataclass
class PricingTier:
    price_per_user: float

class SaaSVisibilityGuard:
    def __init__(self):
        self.users = []
        self.pricing_tier = PricingTier(10.0)

    def add_user(self, user):
        self.users.append(user)

    def get_active_user_count(self):
        return sum(1 for user in self.users if user.active)

    def calculate_charge(self):
        return self.get_active_user_count() * self.pricing_tier.price_per_user

    def edit_pricing_tier(self, new_price_per_user):
        self.pricing_tier = PricingTier(new_price_per_user)

    def create_recurring_invoice(self):
        invoice = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "charge": self.calculate_charge(),
            "users": self.get_active_user_count()
        }
        return invoice

    def generate_invoice_pdf(self, invoice):
        # Simulate generating a PDF
        return json.dumps(invoice)
