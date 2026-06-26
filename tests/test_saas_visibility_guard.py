from saas_visibility_guard import SaaSVisibilityGuard, PolicyRule

def test_create_policy_rule():
    guard = SaaSVisibilityGuard()
    rule = guard.create_policy_rule("category1", "domain1", True)
    assert rule.id == 1
    assert rule.saas_category == "category1"
    assert rule.domain == "domain1"
    assert rule.allowed

def test_edit_policy_rule():
    guard = SaaSVisibilityGuard()
    rule = guard.create_policy_rule("category1", "domain1", True)
    edited_rule = guard.edit_policy_rule(rule.id, saas_category="category2")
    assert edited_rule.saas_category == "category2"

def test_delete_policy_rule():
    guard = SaaSVisibilityGuard()
    rule = guard.create_policy_rule("category1", "domain1", True)
    guard.delete_policy_rule(rule.id)
    assert len(guard.policy_rules) == 0

def test_detect_violations():
    guard = SaaSVisibilityGuard()
    rule = guard.create_policy_rule("category1", "domain1", False)
    saas_applications = [{"name": "app1", "saas_category": "category1", "domain": "domain1"}]
    guard.detect_violations(saas_applications)
    assert len(guard.violations) == 1

def test_send_email_notification():
    guard = SaaSVisibilityGuard()
    rule = guard.create_policy_rule("category1", "domain1", False)
    saas_applications = [{"name": "app1", "saas_category": "category1", "domain": "domain1"}]
    guard.detect_violations(saas_applications)
    # Simulate sending an email notification
    print("Email notification sent")

def test_get_policy_violations():
    guard = SaaSVisibilityGuard()
    rule = guard.create_policy_rule("category1", "domain1", False)
    saas_applications = [{"name": "app1", "saas_category": "category1", "domain": "domain1"}]
    guard.detect_violations(saas_applications)
    violations = guard.get_policy_violations()
    assert len(violations) == 1
