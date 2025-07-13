# main.py

import time
from config import SEARCHER_PUBKEY, TIP_AMOUNT
from jito_client import JitoClient
from models.bundle import Bundle
from strategies.launch_snipe import detect_launch, build_launch_bundle

def run_searcher():
    token_info = {"source": "Pump.fun", "volume": 1000}
    if detect_launch(token_info):
        txs = build_launch_bundle(token_info)
        bundle = Bundle(transactions=txs, tip=TIP_AMOUNT, strategy="launch_snipe")

        client = JitoClient(SEARCHER_PUBKEY)
        sim = client.simulate_bundle(bundle)
        if sim["success"]:
            client.send_bundle(bundle)

if __name__ == "__main__":
    while True:
        run_searcher()
        time.sleep(5)
