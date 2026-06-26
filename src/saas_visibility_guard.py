import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class PolicyRule:
    id: int
    saas_category: str
    domain: str
    allowed: bool

class SaaSVisibilityGuard:
    def __init__(self):
        self.policy_rules = []
        self.violations = []

    def create_policy_rule(self, saas_category: str, domain: str, allowed: bool):
        new_rule = PolicyRule(len(self.policy_rules) + 1, saas_category, domain, allowed)
        self.policy_rules.append(new_rule)
        return new_rule

    def edit_policy_rule(self, rule_id: int, saas_category: str = None, domain: str = None, allowed: bool = None):
        for rule in self.policy_rules:
            if rule.id == rule_id:
                if saas_category:
                    rule.saas_category = saas_category
                if domain:
                    rule.domain = domain
                if allowed is not None:
                    rule.allowed = allowed
                return rule
        raise ValueError("Policy rule not found")

    def delete_policy_rule(self, rule_id: int):
        self.policy_rules = [rule for rule in self.policy_rules if rule.id != rule_id]

    def detect_violations(self, saas_applications: List[dict]):
        for app in saas_applications:
            for rule in self.policy_rules:
                if app["saas_category"] == rule.saas_category and app["domain"] == rule.domain and not rule.allowed:
                    self.violations.append({"app": app, "rule": rule})
                    self.send_email_notification(app, rule)

    def send_email_notification(self, app: dict, rule: PolicyRule):
        # Simulate sending an email notification
        print(f"Email notification sent: {app['name']} is not allowed in {rule.saas_category}")

    def get_policy_violations(self):
        return self.violations
