from saas_visibility_guard import SaaSVisibilityGuard, User, PricingTier
import json
import pytest

def test_get_active_user_count():
    guard = SaaSVisibilityGuard()
    guard.add_user(User(1, True))
    guard.add_user(User(2, False))
    assert guard.get_active_user_count() == 1

def test_calculate_charge():
    guard = SaaSVisibilityGuard()
    guard.add_user(User(1, True))
    guard.add_user(User(2, True))
    assert guard.calculate_charge() == 20.0

def test_edit_pricing_tier():
    guard = SaaSVisibilityGuard()
    guard.edit_pricing_tier(20.0)
    assert guard.pricing_tier.price_per_user == 20.0

def test_create_recurring_invoice():
    guard = SaaSVisibilityGuard()
    guard.add_user(User(1, True))
    invoice = guard.create_recurring_invoice()
    assert invoice["charge"] == 10.0
    assert invoice["users"] == 1

def test_generate_invoice_pdf():
    guard = SaaSVisibilityGuard()
    guard.add_user(User(1, True))
    invoice = guard.create_recurring_invoice()
    pdf = guard.generate_invoice_pdf(invoice)
    assert json.loads(pdf) == invoice

def test_edge_case_no_users():
    guard = SaaSVisibilityGuard()
    assert guard.get_active_user_count() == 0
    assert guard.calculate_charge() == 0.0
