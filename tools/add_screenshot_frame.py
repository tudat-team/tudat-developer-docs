from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont


class ScreenshotConfig:
    def __init__(self):
        self.frame_thickness_horizontal = 10
        self.frame_thickness_vertical = 50
        self.frame_color = (255, 255, 255, 0)
        self.title_bar_height = 40
        self.button_radius = 8
        self.button_spacing = 20
        self.colors = [
            (244, 67, 54, 255),
            (255, 193, 7, 255),
            (76, 175, 80, 255)
        ]
        self.screenshot_radius = 5

    def shadow_command(self, input_image, output_image):
        cmd = [
            'convert', input_image,
            '(', '+clone', '-background', 'black',
            '-shadow', '55x10+0+2', ')',
            '+swap', '-background', 'none',
            '-layers', 'merge', '+repage', output_image
        ]
        return cmd
    # Other configuration methods can be added here


# def calculate_frame_dimensions(screenshot, config):
#     frame_width = screenshot.width + config.frame_thickness_horizontal
#     frame_height = screenshot.height + config.frame_thickness_vertical
#     radius = 13
#     return frame_width, frame_height, radius


def calculate_frame_dimensions(screenshot):
    """
    Calculate dimensions for a frame to be added around a screenshot.

    Args:
    screenshot (Image): The original screenshot image.

    Returns:
    tuple: Contains frame width, frame height, and corner radius.
    """
    frame_thickness_horizontal = 10
    frame_thickness_vertical = frame_thickness_horizontal + 40
    frame_width = screenshot.width + frame_thickness_horizontal
    frame_height = screenshot.height + frame_thickness_vertical
    radius = 13
    return frame_width, frame_height, radius


def create_frame(frame_width, frame_height, radius):
    """
    Create a frame image with rounded corners.

    Args:
    frame_width (int): The width of the frame.
    frame_height (int): The height of the frame.
    radius (int): The radius of the rounded corners.

    Returns:
    Image: The created frame image.
    """
    frame_color = (255, 255, 255, 0)
    frame = Image.new("RGBA", (frame_width, frame_height), frame_color)
    draw = ImageDraw.Draw(frame)
    rectangle_fill = (128, 128, 128, 70)
    rectangle_outline = (128, 128, 128, 255)
    draw.rounded_rectangle((0, 0, frame_width, frame_height), radius,
                           fill=rectangle_fill, outline=rectangle_outline,
                           width=0)
    return frame


def draw_title_bar_and_buttons(frame, frame_width,
                               title_bar_height=40,
                               button_radius=8,
                               button_spacing=20):
    """
    Draw a title bar and control buttons on the frame.

    Args:
    frame (Image): The frame on which to draw the title bar and buttons.
    frame_width (int): The width of the frame.
    title_bar_height (int): The height of the title bar.
    button_radius (int): The radius of the control buttons.
    button_spacing (int): The spacing between control buttons.
    """
    button_center_y = int(title_bar_height / 2) + 3
    button_center_x = (button_radius * 3 + button_spacing * 2) - 40
    colors = [(244, 67, 54, 255), (255, 193, 7, 255), (76, 175, 80, 255)]
    for color in colors:
        draw = ImageDraw.Draw(frame)
        draw.ellipse((button_center_x, button_center_y - button_radius,
                      button_center_x + button_radius * 2,
                      button_center_y + button_radius), fill=color, width=2)
        button_center_x += button_radius + button_spacing


def add_rounded_corners_to_screenshot(screenshot):
    """
    Add rounded corners to the screenshot image.

    Args:
    screenshot (Image): The original screenshot image.

    Returns:
    Image: The screenshot with rounded corners.
    """
    screenshot_radius = 5
    screenshot_mask = Image.new("L", screenshot.size, 0)
    screenshot_draw = ImageDraw.Draw(screenshot_mask)
    screenshot_draw.rounded_rectangle(
        (0, 0, screenshot.width, screenshot.height), screenshot_radius,
        fill=255)
    screenshot.putalpha(screenshot_mask)
    return screenshot


def overlay_screenshot_on_frame(screenshot, frame, frame_width):
    """
    Overlay the screenshot on the frame.

    Args:
    screenshot (Image): The screenshot with rounded corners.
    frame (Image): The frame to overlay the screenshot on.
    frame_width (int): The width of the frame.
    """
    frame_thickness_horizontal = 10
    title_bar_height = 40
    frame.paste(screenshot, (frame_thickness_horizontal // 2,
                             title_bar_height + frame_thickness_horizontal // 2))


def add_frame_to_image(input_image, output_image):
    """
    Add a custom frame and rounded corners to an image.

    Args:
    input_image (str): The file path of the input image.
    output_image (str): The file path for the output image.
    """
    try:
        screenshot = Image.open(input_image)
        frame_width, frame_height, radius = calculate_frame_dimensions(
            screenshot)
        frame = create_frame(frame_width, frame_height, radius)
        draw_title_bar_and_buttons(frame, frame_width)
        screenshot = add_rounded_corners_to_screenshot(screenshot)
        overlay_screenshot_on_frame(screenshot, frame, frame_width)
        frame.save(output_image)
    except IOError as e:
        print(f"Error processing {input_image}: {e}")


def add_shadow_to_image(input_image, output_image):
    """
    Add a shadow effect to an image using ImageMagick.

    Args:
    input_image (str): The file path of the input image.
    output_image (str): The file path for the output image.
    """
    cmd = [
        'convert', input_image,
        '(', '+clone', '-background', 'black',
        '-shadow', '55x10+0+2', ')',
        '+swap', '-background', 'none',
        '-layers', 'merge', '+repage', output_image
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error adding shadow to image: {e}")


if __name__ == "__main__":
    screenshot_dir = Path("./test")
    prefix = "framed_"
    for filename in screenshot_dir.glob("*.jpeg"):
        output_filepath = filename.with_name(prefix + filename.name)
        output_filepath = output_filepath.with_suffix(".png")
        add_frame_to_image(str(filename), str(output_filepath))
        add_shadow_to_image(str(output_filepath), str(output_filepath))
