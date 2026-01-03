# =========================
# TRADING MODE TOGGLE
# =========================
# OPTIONS: "SCALP" or "SWING"
MODE = "SCALP"

# =========================
# MODE-BASED SETTINGS
# =========================
if MODE == "SCALP":
    TIMEFRAME = "5m"          # Faster signals
    EMA_LENGTH = 50
    LIQ_LOOKBACK = 8
    RR_RATIO = 2.0
    SCAN_DELAY = 45           # seconds

elif MODE == "SWING":
    TIMEFRAME = "15m"         # Higher timeframe
    EMA_LENGTH = 100
    LIQ_LOOKBACK = 20
    RR_RATIO = 3.0
    SCAN_DELAY = 120          # seconds

# =========================
# PARTIAL TP SETTINGS
# =========================
TP_SPLITS = [0.3, 0.3, 0.4]

# =========================
# OKX USDT PERPETUAL SYMBOLS
# (Railway-safe, high liquidity)
# =========================
SYMBOLS = [
    "BTC-USDT-SWAP","ETH-USDT-SWAP","SOL-USDT-SWAP","XRP-USDT-SWAP",
    "ADA-USDT-SWAP","AVAX-USDT-SWAP","DOGE-USDT-SWAP","DOT-USDT-SWAP",
    "LINK-USDT-SWAP","TRX-USDT-SWAP","ATOM-USDT-SWAP","LTC-USDT-SWAP",
    "OP-USDT-SWAP","ARB-USDT-SWAP","INJ-USDT-SWAP","APT-USDT-SWAP",
    "NEAR-USDT-SWAP","FIL-USDT-SWAP","SUI-USDT-SWAP"
]
