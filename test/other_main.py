import pandas as pd
import pygame
import math

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D-Like Question Game")

# Font setup
font = pygame.font.Font(None, 36)

# Camera angles in 3D space
camera_angle_x = 0  # Up/Down rotation (around the X-axis)
camera_angle_y = 0  # Left/Right rotation (around the Y-axis)

# Rotation speed (in degrees per key press)
rotation_speed = 30

# Function to rotate a point in 3D space and project it onto 2D screen
def rotate_3d(x, y, z, angle_x, angle_y):
    # Convert angles to radians
    rad_x = math.radians(angle_x)
    rad_y = math.radians(angle_y)

    # Rotate around the X-axis (up/down)
    y_rot = y * math.cos(rad_x) - z * math.sin(rad_x)
    z_rot = y * math.sin(rad_x) + z * math.cos(rad_x)

    # Rotate around the Y-axis (left/right)
    x_rot = x * math.cos(rad_y) + z_rot * math.sin(rad_y)
    z_rot = -x * math.sin(rad_y) + z_rot * math.cos(rad_y)

    # Avoid division by zero by adding a small epsilon to z_rot
    epsilon = 0.1  # Small value to prevent z_rot from becoming zero
    if abs(z_rot) < epsilon:
        print("Warning: z_rot is too small, setting z_rot to epsilon.")
        z_rot = epsilon  # Prevent z_rot from being too close to zero

    # Project the 3D point onto 2D space
    fov = 500  # Field of view (adjust for zoom level)
    distance = 5  # Camera distance from the object
    try:
        x_projected = int((x_rot * fov) / (z_rot + distance) + screen_width // 2)
        y_projected = int((y_rot * fov) / (z_rot + distance) + screen_height // 2)
    except ZeroDivisionError:
        print(f"Error: z_rot is zero, skipping projection.")
        return screen_width // 2, screen_height // 2  # Return a default position if error occurs

    return x_projected, y_projected

def jumpscare():
    print("Jumpscare!")

def exit_game():
    print("Exiting the game...")
    pygame.quit()
    exit()

def question():
    global camera_angle_x, camera_angle_y

    try:
        question_csv = pd.read_csv('test/questions.csv')
    except Exception as e:
        print(f"Error loading CSV: {e}")
        pygame.time.wait(3000)
        return

    for index, row in question_csv.iterrows():
        question_text = str(row['question'])
        correct_answer = str(row['answer']).strip().lower()
        user_input = ""
        answered = False

        # Fixed position for the question in 3D space
        question_x = 0
        question_y = 0
        question_z = 10  # Increase distance from the camera to avoid z_rot being too small

        while not answered:
            screen.fill((0, 0, 0))

            # Rotate the question and project its position onto the 2D screen
            projected_x, projected_y = rotate_3d(question_x, question_y, question_z, camera_angle_x, camera_angle_y)

            # Render the question at the rotated position
            question_surface = font.render(question_text, True, (255, 255, 255))
            question_rect = question_surface.get_rect(center=(projected_x, projected_y))
            screen.blit(question_surface, question_rect)

            # Render user input
            input_surface = font.render(user_input, True, (255, 255, 255))
            input_rect = input_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
            screen.blit(input_surface, input_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        camera_angle_y += rotation_speed  # Rotate clockwise (left arrow)
                    elif event.key == pygame.K_RIGHT:
                        camera_angle_y -= rotation_speed  # Rotate counterclockwise (right arrow)
                    elif event.key == pygame.K_UP:
                        camera_angle_x -= rotation_speed  # Rotate up (up arrow)
                    elif event.key == pygame.K_DOWN:
                        camera_angle_x += rotation_speed  # Rotate down (down arrow)

                    # Ensure camera_angle_y wraps around at 360 degrees to avoid overflow
                    camera_angle_y = camera_angle_y % 360

                    # Limit camera_angle_x to prevent upside-down rotation
                    if camera_angle_x > 45:  # Limit the vertical rotation to 45 degrees
                        camera_angle_x = 45
                    elif camera_angle_x < -45:  # Limit the vertical rotation to -45 degrees
                        camera_angle_x = -45

                    # Handle user input for answering the question
                    elif event.key == pygame.K_RETURN:
                        if user_input.strip().lower() == correct_answer:
                            response_surface = font.render("Correct!", True, (0, 255, 0))
                            response_rect = response_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
                            screen.blit(response_surface, response_rect)
                            pygame.display.update()
                            pygame.time.wait(1000)

                            # Check for flags (like jumpscare and exit)
                            if str(row.get('exit', False)).lower() == 'true':
                                exit_game()
                            elif str(row.get('jumpscare', False)).lower() == 'true':
                                jumpscare()

                            answered = True
                        else:
                            user_input = ""

                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

# 🟢 Start the game
question()
