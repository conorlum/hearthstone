import json


def full_entity_creation_parser(file):
	entities = {}
	creating = False
	creatingId = ""
	for line in file:
		if "FULL_ENTITY - Creating" in line:
			ID = line.split("Creating ID=")[1].split(" ")[0]
			entities[ID] = {}
			creating = True
			creatingId = ID
		if creating and "GameState.DebugPrintPower() -         tag=" in line:
			tag = line.split("tag=")[1].split(" ")[0]
			value = line.split("value=")[1].strip("\n")
			entities[creatingId][tag] = value

	print(json.dumps(entities, indent=4, sort_keys=True))


if __name__ == "__main__":
	file = open("Power.log", "r")
	full_entity_creation_parser(file)
