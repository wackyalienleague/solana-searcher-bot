# jito_client.py

class JitoClient:
    def __init__(self, pubkey):
        self.pubkey = pubkey

    def simulate_bundle(self, bundle):
        print(f"[Simulate] Simulating bundle with {len(bundle.transactions)} txs")
        return {"success": True, "expected_tip": bundle.tip}

    def send_bundle(self, bundle):
        print(f"[Send] Submitting bundle (tip={bundle.tip}) with {len(bundle.transactions)} txs")
        return {"status": "submitted"}
