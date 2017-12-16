# Please add write your phrase_repeater program in this file.

inputPhrase = input( 'Input your phrase: ' )
PhraseCount = int(input( 'How many times should it be repeated: ' ))

for count in range(PhraseCount):
    print(str(count) + " " + inputPhrase)