from textblob import TextBlob


# Make a mistake!
text = 'I love progamming and machine learnig.'

blob = TextBlob(text)

# Check your spelling
corrected_text = blob.correct()

# Print the corrected text
print('Original Text:', text)
print('Corrected Text:', corrected_text)
