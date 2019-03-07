import csv
import operator

letterFrequency = {}

with open('letter-frequency.txt', encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for language in row:
                letterFrequency[language] = {}
        for language in row:
            letterFrequency[language][row['Letter']] = row[language]
        line_count += 1

sample = open(input('Enter filename: '), "r", encoding='utf-8')

sampleTxt = ''.join(sample.read().splitlines()).lower()

sampleTxt = sampleTxt.replace(' ', '')

sampleLetterAddUp = {}

letter_count = 0
for letter in sampleTxt:
    if letterFrequency['Letter'].get(letter, False):
        if(sampleLetterAddUp.get(letter, False)):
            sampleLetterAddUp[letter] += 1
        else:
            sampleLetterAddUp[letter] = 1
        letter_count += 1


sampleLetterFrequency = {}

for letter in sampleLetterAddUp:
    sampleLetterFrequency[letter] = (
        sampleLetterAddUp[letter]/letter_count) * 100

sampleLanguageDifference = {}

for language in letterFrequency:
    if(language != 'Letter'):
        sampleLanguageDifference[language] = 0
        for letter in sampleLetterFrequency:
            sampleLanguageDifference[language] += abs(
                float(letterFrequency[language][letter]) - sampleLetterFrequency[letter])

sortedLanguageDifference = sorted(
    sampleLanguageDifference.items(), key=operator.itemgetter(1))

print('1. ' + sortedLanguageDifference[0][0])
print('2. ' + sortedLanguageDifference[1][0])
print('3. '+sortedLanguageDifference[2][0])
