import requests
import json 

sample_test = {
	"playerBoard": {
		"player": { "tavernTier": 2, "hpLeft": 40, "cardId": "BG20_HERO_301", "heroPowerId": "BG20_HERO_301p", "heroPowerUsed": False },
		"board": [
			{
				"cardId": "EX1_556",
				"attack": 2,
				"divineShield": False,
				"enchantments": [],
				"entityId": 694,
				"health": 3,
				"poisonous": False,
				"reborn": False,
				"taunt": False,
				"windfury": False,
				"megaWindfury": False,
				"friendly": True,
				"frenzyApplied": False
			}
		],
		"secrets": []
	},
	"opponentBoard": {
		"player": {
			"tavernTier": 2,
			"hpLeft": 37,
			"cardId": "TB_BaconShop_HERO_11",
			"heroPowerId": "TB_BaconShop_HP_087",
			"heroPowerUsed": False
		},
		"board": [
			{
				"cardId": "BG20_102",
				"attack": 4,
				"divineShield": False,
				"enchantments": [],
				"entityId": 822,
				"health": 3,
				"poisonous": False,
				"reborn": False,
				"taunt": False,
				"windfury": False,
				"megaWindfury": False,
				"friendly": True,
				"frenzyApplied": False
			}
		],
		"secrets": []
	},
	"options": None
}

print(json.dumps(sample_test))

data = json.dumps(sample_test)
BGS_BATTLE_SIMULATION_ENDPOINT = 'https://o5gz4ktmfl.execute-api.us-west-2.amazonaws.com/Prod/{proxy+}'
header = {'Content-Type': 'application/json'}
response = requests.post(BGS_BATTLE_SIMULATION_ENDPOINT, headers = header, data = data)
print(response.json())

# curl --header "Content-Type: application/json" --request POST --data "{\"playerBoard\": {\"player\": { \"tavernTier\": 2, \"hpLeft\": 40, \"cardId\": \"BG20_HERO_301\", \"heroPowerId\": \"BG20_HERO_301p\", \"heroPowerUsed\": False },\"board\": [{\"cardId\": \"EX1_556\",\"attack\": 2,\"divineShield\": False,\"enchantments\": [],\"entityId\": 694,\"health\": 3,\"poisonous\": False,\"reborn\": False,\"taunt\": False,\"windfury\": False,\"megaWindfury\": False,\"friendly\": True,\"frenzyApplied\": False}],\"secrets\": []},\"opponentBoard\": {\"player\": {\"tavernTier\": 2,\"hpLeft\": 37,\"cardId\": \"TB_BaconShop_HERO_11\",\"heroPowerId\": \"TB_BaconShop_HP_087\",\"heroPowerUsed\": False},\"board\": [{\"cardId\": \"BG20_102\",\"attack\": 4,\"divineShield\": False,\"enchantments\": [],\"entityId\": 822,\"health\": 3,\"poisonous\": False,\"reborn\": False,\"taunt\": False,\"windfury\": False,\"megaWindfury\": False,\"friendly\": True,\"frenzyApplied\": False}],\"secrets\": []},\"options\": None}" https://o5gz4ktmfl.execute-api.us-west-2.amazonaws.com/Prod/{proxy+}