import os

from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GOOGLE_MAPS_API_KEY is not set. "
        "COPY .env.example to .env and fill in your key:)"
    )

# BFS 最大節點數，避免跑太瘋
MAX_NODES = 100

# 是否下載圖片（True=下載到本地, False=只存URL）
SAVE_IMAGES = False
IMAGE_DIR = "images"

# 每一步距離（公尺）：越小越密集，呼叫次數越多
STEP_METERS = 100

# metadata 搜尋 radius（公尺）：給 Google 一點空間 snap 到最近 pano
SEARCH_RADIUS_METERS = 20

# 可選：限制爬蟲在某個經緯度範圍內（避免跑太遠）
# 不想限制就設為 None
LAT_MIN = None
LAT_MAX = None
LNG_MIN = None
LNG_MAX = None
