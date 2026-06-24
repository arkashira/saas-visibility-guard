import pytest
from src.saas_visibility_guard import SaasVisibilityGuard, ThreatLevel, SaaSApp

def test_add_saaas_app():
    guard = SaasVisibilityGuard()
    guard.add_saaas_app("App1", ["SQL Injection", "Cross-Site Scripting"])
    assert len(guard.saaas_apps) == 1

def test_detect_vulnerabilities():
    guard = SaasVisibilityGuard()
    guard.add_saaas_app("App1", ["SQL Injection", "Cross-Site Scripting"])
    threat_levels = guard.detect_vulnerabilities("App1")
    assert len(threat_levels) == 2
    assert threat_levels["SQL Injection"] == ThreatLevel.HIGH
    assert threat_levels["Cross-Site Scripting"] == ThreatLevel.MEDIUM

def test_generate_report():
    guard = SaasVisibilityGuard()
    guard.add_saaas_app("App1", ["SQL Injection", "Cross-Site Scripting"])
    report = guard.generate_report("App1")
    assert report.startswith("SaaS App: App1")
    assert "Vulnerabilities:" in report
    assert "SQL Injection" in report
    assert "Cross-Site Scripting" in report
