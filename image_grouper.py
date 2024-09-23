import sys
from grouping.group_images import Groupter
from utils.file_utils import get_images_name, copy_image

def main(input_dir, output_dir, action='group'):
    # Get the filenames from the input directory
    filenames = get_images_name(input_dir)
    
    # Initialize the Groupter object with the list of images
    groupter = Groupter(filenames)
    
    # Group the images based on the specified action
    groupter.group_images()
    
    # Perform the action based on user input
    if action == 'group':
        groupter.save_grouped_images(output_dir)
    elif action == 'remove':
        groupter.remove_duplicates(output_dir)

if __name__ == "__main__":
    # Interactive prompts for user input
    input_dir = input("Please enter the input directory containing images: ")
    output_dir = input("Please enter the output directory to save the grouped images: ")
    action = input("Would you like to 'group' similar images or 'remove' duplicates? (group/remove): ").lower()

    # Validate the action input
    if action not in ['group', 'remove']:
        print("Invalid action! Please enter 'group' or 'remove'.")
        sys.exit(1)
    
    # Run the main function with the user's input
    main(input_dir, output_dir, action)
