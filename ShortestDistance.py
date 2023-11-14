
def preprocess_file(file_path): #function that takes in the file path
    word_positions = {} #initialize Dictionary
    with open(file_path, 'r') as file:#read file
        #iterate over each word in the file separated by new line
        for i, word in enumerate(file.read().split('\n')):
            #check if the word is already a key
            if word not in word_positions:
                #initializes an empty list for that word.
                word_positions[word] = []
            # if already exist append the position of the word to its list in the dictionary.
            word_positions[word].append(i)
    #return the dictionary mapping words to their positions.
    return word_positions

def find_shortest_distance(preprocessed_data, word1, word2):
    #If either word is missing, the function returns None.
    if word1 not in preprocessed_data or word2 not in preprocessed_data:
        return None

    positions1 = preprocessed_data[word1] #retrieves list of positions
    positions2 = preprocessed_data[word2]

    i, j = 0, 0 #initializes two pointers for iterating through the lists of positions
    min_distance = float('inf') #initializes the minimum distance as infinity.
    while i < len(positions1) and j < len(positions2): #iterate through both lists of positions.
        #update the minimum distance if a smaller distance is found.
        min_distance = min(min_distance, abs(positions1[i] - positions2[j]))
        # block increments the pointer (i or j) pointing to the smaller current position.
        if positions1[i] < positions2[j]:
            i += 1
        else:
            j += 1

    return min_distance# returns the shortest distance found or infinity if no such distance exists.

# Preprocess the file
file_path = 'C:\\Users\\izere\\Downloads\\newWord.txt'
#file_path = 'C:\\Users\\izere\\Downloads\\words.txt'
preprocessed_data = preprocess_file(file_path)

# Example usage
word1 = 'yang'
word2 = 'yields'
print(find_shortest_distance(preprocessed_data, word1, word2))
