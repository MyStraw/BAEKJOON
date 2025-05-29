emoji = input()
length = len(emoji)
colon_count = emoji.count(':')
underscore_count = emoji.count('_')
difficulty = length + colon_count + underscore_count * 5
print(difficulty)
