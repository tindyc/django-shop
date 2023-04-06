import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AY383SAgbsMCoj4dbE2kSTArknY9k_6VtTDhWh_KpzIWCxuMGAR2chiwdC3J796qmJm9alViVmLBxiRY"
        self.client_secret = "EKHpteS6jWvbTROoljwXNmTMDxi7ESztKSFgYL-WMfgnM4BXrdWaEU-3-xtPR3CiXB6jU053FDBmXcRH"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
