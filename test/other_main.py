import pandas as pd
import pygame

# Initialize pygame
pygame.init()

# Set screen width and height
screen_width = 800
screen_height = 600

# Create display window with width and height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Question Game")

# Set font for rendering text
font = pygame.font.Font(None, 36)

# Define the jumpscare function (you can customize this)
def jumpscare():
    # You can define the jumpscare behavior, like playing a sound or showing an image
    print("Jumpscare!")

# Define the exit function (you can customize this)
def exit_game():
    print("Exiting the game...")
    pygame.quit()

# Define the question function
def question():
    # Set the question csv to pandas reading the csv from a file
    question_csv = pd.read_csv('questions.csv')
    
    # Seek to the first line in the question csv
    for index, row in question_csv.iterrows():
        # Go to the next line in the question csv
        question_text = row[4]  # Assuming the 5th column contains the question text
        
        # Loop forever for each question
        while True:
            user_input = ""  # Initialize user input
            
            # Display the 5th row (question_text) at the center of the screen
            text_surface = font.render(question_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.fill((0, 0, 0))  # Clear the screen with black background
            screen.blit(text_surface, text_rect)
            pygame.display.update()
            
            # Wait for user to type input
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            # Exit the inner loop if Enter is pressed
                            break
                        elif event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]  # Remove last character
                        else:
                            user_input += event.unicode  # Add typed character to input
                
                # Render the current user input in the center of the screen
                input_surface = font.render(user_input, True, (255, 255, 255))
                input_rect = input_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
                screen.fill((0, 0, 0))  # Clear screen again to update
                screen.blit(text_surface, text_rect)
                screen.blit(input_surface, input_rect)
                pygame.display.update()
            
            # Check if user input matches the 5th row on the line
            if user_input == row[4]:  # Comparing with the 5th column (question text)
                # Display the 6th row (correct answer) at the center of the screen
                answer_text = row[5]  # Assuming the 6th column is the answer
                answer_surface = font.render(answer_text, True, (255, 255, 255))
                answer_rect = answer_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
                screen.fill((0, 0, 0))  # Clear screen
                screen.blit(answer_surface, answer_rect)
                pygame.display.update()
                pygame.time.wait(1000)  # Wait for 1 second
                break  # End the while loop and move to next question
            else:
                # If user input is incorrect, continue to next question
                continue

            # If 7th row on the line is equal to True, run the exit function
            if row[6] == True:  # Assuming 7th column is a boolean flag
                exit_game()
                break  # Exit the question loop

            # Else, if 4th row on the line is equal to True, run the jumpscare function
            elif row[3] == True:  # Assuming 4th column is a boolean flag for jumpscare
                jumpscare()
                break  # Exit the question loop to continue

# Start the question function
question()
