import pytest
from saas_visibility_guard import SaaSUsage, SaaSVisibilityGuard, UserRole
from datetime import date

def test_export_csv_compliance_officer():
    saas_usage_data = [
        SaaSUsage("app1", "domain1", 10, 0.5, date(2024, 9, 1)),
        SaaSUsage("app2", "domain2", 20, 0.8, date(2024, 9, 15)),
    ]

    guard = SaaSVisibilityGuard(saas_usage_data)

    csv_string = guard.export_csv(date(2024, 9, 1), date(2024, 9, 30), UserRole.COMPLIANCE_OFFICER)

    assert "app1" in csv_string
    assert "app2" in csv_string

def test_export_csv_non_compliance_officer():
    saas_usage_data = [
        SaaSUsage("app1", "domain1", 10, 0.5, date(2024, 9, 1)),
    ]

    guard = SaaSVisibilityGuard(saas_usage_data)

    with pytest.raises(PermissionError):
        guard.export_csv(date(2024, 9, 1), date(2024, 9, 30), UserRole.ADMIN)

def test_get_saas_usage_compliance_officer():
    saas_usage_data = [
        SaaSUsage("app1", "domain1", 10, 0.5, date(2024, 9, 1)),
        SaaSUsage("app2", "domain2", 20, 0.8, date(2024, 9, 15)),
    ]

    guard = SaaSVisibilityGuard(saas_usage_data)

    usage = guard.get_saas_usage(date(2024, 9, 1), date(2024, 9, 30), UserRole.COMPLIANCE_OFFICER)

    assert len(usage) == 2

def test_get_saas_usage_non_compliance_officer():
    saas_usage_data = [
        SaaSUsage("app1", "domain1", 10, 0.5, date(2024, 9, 1)),
    ]

    guard = SaaSVisibilityGuard(saas_usage_data)

    with pytest.raises(PermissionError):
        guard.get_saas_usage(date(2024, 9, 1), date(2024, 9, 30), UserRole.ADMIN)
