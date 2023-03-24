from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "23398820")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "95ad635217d1b6b193c9c9be0254cc2d")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5945051414:AAF5Vm4GRSkCfXE_Alq_IE4XaBwWh9AWNb8")
SESSION_NAME = getenv("SESSION_NAME", "AgB9aUllGcVx6iO9GBwH2u_XJKgNTisRnRvuZWXFMevm2p9pLbISoXk4CVsMWsst-AJuiTSmXJKbqeljeexBFB2VSoB47wGHnAUdpyE_ogdTbYQwIsq6p_Fp3FBzn53xc-aS9Vs3M7on7fsN5CUa-Ct2DoTGMokyy5SE6W5kk4u_jf5S8na1Utle5rjvpT9BQK32NarrzeDFljZDfD_4Fxx3xpf9GE9sQu4FqTN7qzU_1HnCdDNVsinJJFRpHPoh5CUderlOQB1MKBzbTfeZ-B1h_PxeyYR1VNxLwIxqH8lfB_DpadXjh2JMjKwNUums10CcTpY7_OMc-NR3L9yHY21TAAAAAVaEJhIA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "AT_MGF") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "music") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "MUC_KBOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "anime6o") # @ هنا ضغ يوزر كروبك بدو
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "anime6lf") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5746468370").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5746468370").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/f7d0b8bf1ede6e2c2dc9e.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/3bebe90db0c9399d82881.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5199a41d34f118f942699.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/584a7dbfa8d6d6b24b236.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/2412cf577e0f61f843e6f.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/51b3539289e6648c3b062.jpg")
