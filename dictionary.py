
# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'): "
# menu_prompt = ("1. Add/modify student grade\n"
#                 "2. Delete student grade\n"
#                 "3. Print student grades\n"
#                 "4. Quit\n")

# while True:  # Exit when user enters no input
#     command = input(menu_prompt).lower().strip()
#     if command == '1':
#         name, grade = input(grade_prompt).split()
#         print(f'grade:{grade} {type(grade)} name:{name} {type(name)}')
#         student_grades[name] = grade

#     elif command == '2':
#         del student_grades[name].grade

#     elif command == '3':
#         print('Student grades --- ')
#         for student in student_grades:
#             print(f'   -- {student} {student_grades[student]}')
#         print()

#     elif command == '4':
#         break
    
#     else:
#         print('Unrecognized command.')

# --------------------------------------------------------
'''zyDE 8.3.1: Iterating over a dictionary example: Gradebook statistics.
Write a program that uses the keys(), values(), and/or items() dict methods to find statistics about the student_grades dictionary. Find the following:

[done] Print the name and grade percentage of the student with the highest total of points.
Find the average score of each assignment.
Find and apply a curve to each student's total score, such that the best student has 100% of the total points.'''

# student_grades contains scores (out of 100) for 5 assignments
# student_grades = {
#     'Andrew': [56, 79, 90, 22, 50],
#     'Nisreen': [88, 62, 68, 75, 78],
#     'Alan': [95, 88, 92, 85, 85],
#     'Chang': [76, 88, 85, 82, 90],
#     'Tricia': [99, 92, 95, 89, 99]
# }

# avg_obj = {}
# highest_points = {}
# hp = 0

# for student, grades in student_grades.items():
#     avg_obj[student] = int(sum(grades)/len(grades))

# for student in avg_obj:
#     if avg_obj[student] > 90:
#         hp = avg_obj[student] 
#         highest_points[student] = avg_obj[student]

# for student, percent in highest_points.items():
#     print(f'{student} with a wooping {percent}%')

# print(avg_obj)   
# print(highest_points)
# --------------------------------------------------------


# --------------------------------------------------------
# challenge activity
# 8.3.1: Report country population.

# Write a loop that prints each country's population in country_pop.

# Sample output with input:
# 'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800':
# China has 1365830000 people.
# India has 1247220000 people.
# United States has 318463000 people.
# Indonesia has 252164800 people.

# user_input = input()
# entries = user_input.split(',')
# country_pop = {}

# for pair in entries:
#     split_pair = pair.split(':')
#     country_pop[split_pair[0]] = split_pair[1]
#     # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }

# # added the for loop with .items()
# for country, pop in country_pop.items():
#     print(f'{country} has {pop} people.')

# --------------------------------------------------------

# --------------------------------------------------------
# Figure 8.4.2: Nested dictionaries example: Storing grades.
# grades = {
#     'John Ponting': {
#         'Homeworks': [79, 80, 74],
#         'Midterm': 85,
#         'Final': 92
#     },
#     'Jacques Kallis': {
#         'Homeworks': [90, 92, 65],
#         'Midterm': 87,
#         'Final': 75
#     },
#     'Ricky Bobby': {
#         'Homeworks': [50, 52, 78],
#         'Midterm': 40,
#         'Final': 65
#     },
# }

# user_input = input('Enter student name: ')

# while user_input != 'exit':
#     if user_input in grades:
#         # Get values from nested dict
#         homeworks = grades[user_input]['Homeworks']
#         midterm = grades[user_input]['Midterm']
#         final = grades[user_input]['Final']

#         # print info
#         for hw, score in enumerate(homeworks):
#             print('Homework {}: {}'.format(hw, score))

#         print('Midterm: {}'.format(midterm))
#         print('Final: {}'.format(final))

#         # Compute student total score
#         total_points = sum([i for i in homeworks]) + midterm + final
#         print('Final percentage: {:.1f}%'.format(100*(total_points / 500.0)))

#     user_input = input('Enter student name: ')

# --------------------------------------------------------


# --------------------------------------------------------
# zyDE 8.4.1: Nested dictionaries example: Music library.
# The following example demonstrates a program that uses 3 levels of nested dictionaries to create a simple music library.

# The following program uses nested dictionaries to store a small music library. Extend the program such that a user can add artists, 
# albums, and songs to the library. First, add a command that adds an artist name to the music dictionary. 
# Then add commands for adding albums and songs. Take care to check that an artist exists in the dictionary before adding an album, 
# and that an album exists before adding a song.

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

prompt = """
Menu ---
1) Add Artist
2) Add Album
3) Add Song
4) exit to quit
"""
add_artist_prompt = "\nArtist to add: "
add_album_prompt = "Album(s) to add: "
add_songs_prompt = "Song(s) to add: "

# Get user input
command = input(prompt).strip().lower()

while command != 'exit':
    artist_obj = {}

    # Add Artist
    if command == '1':
        artist = input(add_artist_prompt)
        if artist in music:
            print(f'{artist} is already in the database.')
            print(artist_obj[artist])
            artist = input(add_artist_prompt)

        prompt = """
        Artist menu ---
        1) Add songs
        2) Add year
        3) Did the album go platinum (yes/no)? 
        4) < go back Menu
        """

        # Add artist to music library
        artist_obj = artist
        choice = input(prompt)
        while choice != '4':
            
            if choice == '1':
                songs = input('Add songs (song1 song2 ...): ').split()
                
            elif choice == '2':
                y = input('The year the album was created: ')
                print(type(y))
                y = int(y)
                print(type(y))
                artist_obj[artist]['year'] = y
    
            elif choice == '3':
                 artist_obj[artist]['platinum'] = bool(input('yes or no?: '))

            choice = input(prompt)   

    # Get user input
    command = input(prompt).strip().lower()







#     ''' Type your code here. '''
# words = input().lower().split()
# word_frequency = {}

# for word in words:
#     if word in word_frequency:
#         word_frequency[word] += 1
#     else:
#         word_frequency[word] = 1
        
# for word, freq in word_frequency.items():
#     print(f'{word} {freq}')
