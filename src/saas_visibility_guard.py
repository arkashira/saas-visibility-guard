import csv
import dataclasses
import datetime
from enum import Enum
from typing import List

class UserRole(Enum):
    COMPLIANCE_OFFICER = 1
    ADMIN = 2

@dataclasses.dataclass
class SaaSUsage:
    app_name: str
    domain: str
    users: int
    risk_score: float
    last_seen: datetime.date

class SaaSVisibilityGuard:
    def __init__(self, saas_usage_data: List[SaaSUsage]):
        self.saas_usage_data = saas_usage_data

    def export_csv(self, start_date: datetime.date, end_date: datetime.date, user_role: UserRole) -> str:
        if user_role != UserRole.COMPLIANCE_OFFICER:
            raise PermissionError("Only compliance officers can export CSV")

        filtered_data = [usage for usage in self.saas_usage_data if start_date <= usage.last_seen <= end_date]

        csv_data = [
            ["app_name", "domain", "users", "risk_score", "last_seen"],
            *[[usage.app_name, usage.domain, usage.users, usage.risk_score, usage.last_seen] for usage in filtered_data]
        ]

        csv_string = "\n".join([",".join(map(str, row)) for row in csv_data])

        return csv_string

    def get_saas_usage(self, start_date: datetime.date, end_date: datetime.date, user_role: UserRole) -> List[SaaSUsage]:
        if user_role != UserRole.COMPLIANCE_OFFICER:
            raise PermissionError("Only compliance officers can view SaaS usage")

        return [usage for usage in self.saas_usage_data if start_date <= usage.last_seen <= end_date]
