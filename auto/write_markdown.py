from os import listdir

nSamples = 50
directory = "../images/samples"
fileNames = sorted([fileName.lower() for fileName in listdir(directory) if fileName.lower().endswith(".png")])[:nSamples]

output = f"# {nSamples} common nouns\nIn an effort to show lack of bias, I have taken the top {nSamples} nouns from [this list](https://www.espressoenglish.net/100-common-nouns-in-english/).\n\nI may increase this number at some point, but only in the order as listed on that page."

for fileName in fileNames:
	word = fileName[:-4].split("_")[1]
	output += f"\n\n### {word}\n![{word}](images/samples/{fileName})"

with open("output.md", "w", encoding="utf-8") as outFile:
	outFile.write(output)