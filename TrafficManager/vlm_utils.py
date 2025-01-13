import base64
import io
from PIL import Image, ImageDraw
import math
# def plot_traj(traj):
#     # Create a blank image (1000x1000 pixels) with white background
#     img_size = 1000
#     blank_img = Image.new("RGB", (img_size, img_size), "white")

#     # Decode base64 blank image (if provided as base64 string)
#     # Here we mock the base64 image creation for example purposes
#     buffer = io.BytesIO()
#     blank_img.save(buffer, format="JPEG")
#     pred_bev_base64 = base64.b64encode(buffer.getvalue()).decode()

#     # Decode the base64 image and prepare for drawing
#     pred_bev_img = base64.b64decode(pred_bev_base64)
#     pred_bev_img = Image.open(io.BytesIO(pred_bev_img))
#     pred_bev_img = pred_bev_img.convert("RGB")

#     # Draw the trajectory
#     draw = ImageDraw.Draw(pred_bev_img)
#     center_x, center_y = img_size // 2, img_size // 2  # Center of the BEV image
#     trajectory_color = "red"  # Color of the trajectory
#     line_width = 5  # Thickness of the trajectory line

#     # Draw the ego car as a blue rectangle
#     ego_width, ego_height = 20, 40  # Size of the ego car rectangle
#     ego_top_left = (center_x - ego_width // 2, center_y - ego_height // 2)
#     ego_bottom_right = (center_x + ego_width // 2, center_y + ego_height // 2)
#     draw.rectangle([ego_top_left, ego_bottom_right], fill="blue")

#     # Convert BEV trajectory points to image coordinates and draw
#     trajectory_points = [(center_x + x * 20, center_y - y * 20) for x, y in traj]
#     draw.line(trajectory_points, fill=trajectory_color, width=line_width)

#     # Save the image
#     return pred_bev_img
# def add_traj(draw, img_size, traj):
#     """
#     Draws a trajectory in the middle of the original image.
#     Parameters:
#     - draw: ImageDraw.Draw object to draw on the image.
#     - img_size: Size of the image (assumes square image).
#     - traj: List of (x, y) points representing the trajectory in BEV space.

#     Returns:
#     - None (modifies the image in place).
#     """
#     center_x, center_y = img_size // 2, img_size // 2  # Center of the image
#     trajectory_color = "red"  # Color of the trajectory
#     line_width = 5  # Thickness of the trajectory line

#     # Convert BEV trajectory points to image coordinates
#     trajectory_points = [(center_x + x * 20, center_y - y * 20) for x, y in traj]
#     draw.line(trajectory_points, fill=trajectory_color, width=line_width)

#     # Draw the ego car as a blue rectangle
#     # ego_width, ego_height = 40, 20  # Size of the ego car rectangle
#     # ego_top_left = (center_x - ego_width // 2, center_y - ego_height // 2)
#     # ego_bottom_right = (center_x + ego_width // 2, center_y + ego_height // 2)
#     # draw.rectangle([ego_top_left, ego_bottom_right], fill="blue")
def world_to_ego(world_points, ego_vehicle):
    """
    Converts a list of points from world coordinates to ego vehicle coordinates.
    
    Args:
    - world_points: List of (x, y) points in world frame.
    - ego_vehicle: Dictionary containing the ego vehicle's state, with keys 'xQ', 'yQ', and 'yawQ'.
    
    Returns:
    - List of (x, y) points in ego vehicle frame.
    """
    world_points = [list(world_points[0]), list(world_points[1])]
    ego_x, ego_y, ego_yaw = (
        ego_vehicle["xQ"][-1],  # Current position in x (world frame)
        ego_vehicle["yQ"][-1],  # Current position in y (world frame)
        ego_vehicle["yawQ"][-1],  # Current orientation (yaw in radians)
    )
    
    # Convert world points to ego coordinates
    ego_points = []
    for i in range(len(world_points[0])):
        x_w, y_w = world_points[0][i], world_points[1][i]
        # Perform the reverse transformation
        x_e = (x_w - ego_x) * math.cos(ego_yaw) + (y_w - ego_y) * math.sin(ego_yaw)
        y_e = -(x_w - ego_x) * math.sin(ego_yaw) + (y_w - ego_y) * math.cos(ego_yaw)
        ego_points.append((x_e, y_e))
    ego_points = [[-round(point[1],2),round(point[0],2)] for point in ego_points]
    if len(ego_points)<7:
        ego_points = []
    return ego_points[:6]

def add_interpolate_traj(draw, img_size,traj,ego_past_traj=[]):
    """ draw traj
    """
    center_x, center_y = img_size // 2+60, img_size // 2-15 # Center of the image
    trajectory_color = "yellow"  # Color of the interpolated trajectory
    line_width = 10  # Thickness of the trajectory line
    # Debug the trajectory points
    # Convert interpolated trajectory states to image coordinates
    trajectory_points = [(center_x + x * 20, center_y - y * 20) for x, y in traj]
    #print('Center location',center_x,center_y)
    # Draw the trajectory as a line
    print("Trajectory Points (Pixel Coordinates):", trajectory_points)
    draw.line(trajectory_points, fill=trajectory_color, width=line_width)

    # Optional: Highlight each interpolated point
    point_radius = 10
    for x, y in trajectory_points:
        draw.ellipse(
            (x - point_radius, y - point_radius, x + point_radius, y + point_radius),
            fill="blue",
            outline="blue",
        )
    if ego_past_traj !=[]:
        trajectory_color = (150,150,150)
        ego_past_traj = [(center_x + x * 20, center_y - y * 20) for x, y in ego_past_traj]
        print("Trajectory Points (Pixel Coordinates):", trajectory_points)
        draw.line(ego_past_traj, fill=trajectory_color, width=line_width)

        # Optional: Highlight each interpolated point
        point_radius = 10
        for x, y in ego_past_traj:
            draw.ellipse(
                (x - point_radius, y - point_radius, x + point_radius, y + point_radius),
                fill=(35,35,35),
                outline=(35,35,35),
            )
def custom_interpolate_traj(ego_vehicle, path_points, Ti_path=0.5):
    '''ego coords to world coords
    '''
    ego_x, ego_y, ego_yaw = (
        ego_vehicle["xQ"][-1],
        ego_vehicle["yQ"][-1],
        ego_vehicle["yawQ"][-1],
    )
    ego_x, ego_y = 0,0
    global_points = [
        (
            ego_x
            + px * math.cos(ego_yaw - math.pi / 2)
            - py * math.sin(ego_yaw - math.pi / 2),
            ego_y
            + px * math.sin(ego_yaw - math.pi / 2)
            + py * math.cos(ego_yaw - math.pi / 2),
        )
        for px, py in path_points
    ]
    return global_points