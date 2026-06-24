import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class ThreatLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class SaaSApp:
    name: str
    vulnerabilities: List[str]

class SaasVisibilityGuard:
    def __init__(self):
        self.saaas_apps = {}

    def add_saaas_app(self, name: str, vulnerabilities: List[str]):
        self.saaas_apps[name] = SaaSApp(name, vulnerabilities)

    def detect_vulnerabilities(self, saaas_app_name: str) -> Dict[str, ThreatLevel]:
        saaas_app = self.saaas_apps.get(saaas_app_name)
        if saaas_app is None:
            return {}

        vulnerabilities = saaas_app.vulnerabilities
        threat_levels = {}

        for vulnerability in vulnerabilities:
            if "SQL Injection" in vulnerability:
                threat_levels[vulnerability] = ThreatLevel.HIGH
            elif "Cross-Site Scripting" in vulnerability:
                threat_levels[vulnerability] = ThreatLevel.MEDIUM
            else:
                threat_levels[vulnerability] = ThreatLevel.LOW

        return threat_levels

    def generate_report(self, saaas_app_name: str) -> str:
        saaas_app = self.saaas_apps.get(saaas_app_name)
        if saaas_app is None:
            return ""

        report = f"SaaS App: {saaas_app.name}\n"
        report += "Vulnerabilities:\n"
        for vulnerability in saaas_app.vulnerabilities:
            report += f"- {vulnerability}\n"

        return report
