# strategies/launch_snipe.py

def detect_launch(token_info):
    return token_info.get("source") in ["Pump.fun", "LetsBonk"]

def build_launch_bundle(token_info):
    txs = ["tx_buy1", "tx_buy2"]
    return txs
