'''quat calculation demo
'''
import numpy as np
from scipy.spatial.transform import Rotation as R

# Extract rotation matrix from ego_pose
ego_pose = np.array([
    [0.002592007862403989, 0.9999966621398926, 0.0, 990.8573608398438],
    [-0.9999966621398926, 0.002592007862403989, 0.0, 350.5302429199219],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
])

rotation_matrix = ego_pose[:3, :3]

# Convert to quaternion
r = R.from_matrix(rotation_matrix)
quat = r.as_quat()  # Returns [x, y, z, w]

print("Quaternion:", quat)
# Convert to Euler angles

r = R.from_quat(quat)
euler_angles = r.as_euler('xyz', degrees=False)  # Roll, Pitch, Yaw

# Zero out Roll and Pitch
euler_angles[0] = 0  # Roll
euler_angles[1] = 0  # Pitch

# Convert back to Quaternion
adjusted_quat = R.from_euler('xyz', euler_angles).as_quat()
print("Adjusted Quaternion:", adjusted_quat)