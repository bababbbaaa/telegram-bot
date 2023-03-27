from datetime import datetime
import pytz
local = pytz.timezone("Europe/London")
# VARIABLES

# AUTO TIMES HOURS
wptime = 1
twittertime = 6
airdroptime = 1

# AUTO MESSAGE
automessage = "**X7 Finance Twitter Raid**\n\nClick the link below and like and RT everything you see!"
automessagelink = "https://twitter.com/search?q=%23x7finance&src=typed_query"

# SPACES                Y   M   D   H   M  S
spacestime = datetime(2023, 3, 28, 20, 00, 00)
spaceslink = "https://twitter.com/i/spaces/1RDGlanOvMkJL?s=20"

# RAFFLE               Y   M   D   H   M  S
raffle = datetime(2023, 3, 28, 12, 00, 00)
raffleupdate = datetime(2023, 3, 27, 11, 00, 00)


# GIVEAWAY               Y   M   D   H   M  S
giveaway = datetime(2023, 3, 30, 20, 30, 00)
snapshot1 = datetime(2023, 3, 9, 20, 30, 00)
snapshot2 = datetime(2023, 3, 29, 20, 30, 00)
giveawayupdate = datetime(2023, 3, 29, 20, 30, 00)
snapshot1time = snapshot1.strftime("%A %B %d %Y %I:%M %p")
snapshot2time = snapshot2.strftime("%A %B %d %Y %I:%M %p")
giveawaytime = giveaway.strftime("%A %B %d %Y %I:%M %p")
giveawaytitle = "X7 Finance 20,000 X7R Giveaway!"
giveawayinfo = "For every 0.1 X7D minted,1 entry into the draw was generated!\n\n" \
               f"A Snapshot of minters was taken at {snapshot1time} (UTC) and a second will be at " \
               f"{snapshot2time} (UTC)\n\n" \
               f"The Diamond hands that have held for the entire duration are in the draw! The more minted," \
               " the better the chance!\n\n" \
               "Any withdrawals will be deducted from the entries at the second snapshot.\n\nTo view entries use " \
               "`/giveaway entries`\n\n" \
               f"The draw will be made on {giveawaytime} (UTC)\n\nCredit: Defi Dipper!"

# TWITTER
tweetid = 1625541579074158607
tweetlink = "https://twitter.com/X7_Finance/status/1625541579074158607?s=20&t=h25BT4ivN34G70MIZCrHVQ"

# COMMANDS
modsonly = "You do not have permission to do this. #trustnoone"

commands = '/about - Welcome to X7 Finance\n' \
           '/ecosystem - Token Overview\n' \
           '/links - Official Links\n' \
           '/dashboard - X7 Finance community dashboard\n' \
           '/twitter - Latest X7 Finance tweet\n' \
           '/swap - Xchange DEX Info\n' \
           '/roadmap - Whats coming next\n' \
           '/website - Official Website\n' \
           '/x7r - X7R Info\n' \
           '/x7dao - X7DAO Info\n' \
           '/x7d  - X7Deposit Info\n' \
           '/x7101 - X7101 Info\n' \
           '/x7102 - X7102 Info\n' \
           '/x7103 - X7103 Info\n' \
           '/x7104 - X7104 Info\n' \
           '/x7105 - X7105 \n' \
           '/constellations - X7 Constellation Info\n' \
           '/buyevenly - A Guide to buying constellation series evenly\n' \
           '/contract - Token Contract Addresses\n' \
           '/chart - Chart Links\n' \
           '/price - [anytoken]  CG Price Info\n' \
           '/buy - Buy Links\n' \
           '/wp - Whitepaper\n' \
           '/tax - Token Tax and Slippage Info\n' \
           '/mcap - Market Cap Info\n' \
           '/liquidity - Liquidity Info\n' \
           '/treasury - Treasury Details\n' \
           '/pool - Lending Pool Info\n' \
           '/loans - Loan Term Info\n' \
           '/burn - X7R Burn \n' \
           '/holders - Token Holder Info\n' \
           '/airdrop - Snapshot Info\n' \
           '/nft - NFT Details\n' \
           'opensea - Opensea Links\n' \
           '/pioneer -  [tokenid] Pioneer NFT Stats\n' \
           '/discount - discount committee NFT Info\n' \
           '/smart - Smart Contract Details\n' \
           '/deployer  - X7 Finance Deployer Info\n' \
           '/withdraw  - How to withdraw X7D\n' \
           '/giveaway - Giveaway Details\n' \
           '/spaces  - Twitter Space Info\n' \
           '/gas - Gas Info\n' \
           '/wei - amount convert to ETH\n' \
           '/fg - Market fg Info\n' \
           '/time - World Time Info\n' \
           '/search - [keyword] Search the web\n' \
           '/channels - List of X7 Finance Community TG Channels\n' \
           '/media - TG Stickers and Emojis\n' \
           '/bobby - Bobby BuyBot Channels\n' \
           '/alumni - X7 Finance Alumni\n'

admincommands = 'To be run in main chat\n\n' \
                '/settings - Open the setting menu\n' \
                '/setup - Setup the portal\n' \
                '/difficulty - Set the CAPTCHA difficulty\n' \
                '/antiflood - (Dis)Enable antiflood mode\n' \
                '/lock all - mutes chat\n' \
                '/unlock all - unmute chat\n' \
                '/start_auto [name_oneword] [time_in_minutes] [message] \n' \
                '/stop_auto [name]\n' \
                '/view_auto\n\n' \
                f'wp quote will trigger every {wptime} hour\n' \
                f'twitter "RT everything" message will trigger every {twittertime}'
