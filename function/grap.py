import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Glowing Particle Rose")
clock = pygame.time.Clock()

def generate_rose_data():
    pts_list = []
    colors_list = []

    # 1. Rose Petals (Parametric 3D Rose)
    num_petals = 22000
    u = np.sqrt(np.random.uniform(0, 1, num_petals))
    theta = np.random.uniform(0, 2 * np.pi * 10, num_petals)

    x_val = 1 - (0.5 * ((1.25 * (1 - np.mod(3.6 * theta, 2 * np.pi) / np.pi) ** 2) - 0.25) ** 2)
    phi = (np.pi / 2) * np.exp(-theta / (8 * np.pi))
    y_val = 1.95653 * (u ** 2) * ((1.27689 * u - 1) ** 2) * np.sin(phi)

    r = x_val * (u * np.sin(phi) + y_val * np.cos(phi))
    h = x_val * (u * np.cos(phi) - y_val * np.sin(phi))

    scale = 175
    px = r * np.sin(theta) * scale
    py = -h * scale + 35
    pz = r * np.cos(theta) * scale

    pts_list.append(np.column_stack((px, py, pz)))

    edge_glow = np.clip(x_val * u, 0, 1)
    red = np.clip(95 + edge_glow * 155 + np.random.randint(0, 25, num_petals), 0, 255)
    green = np.clip((edge_glow ** 3) * 55, 0, 255)
    blue = np.clip((edge_glow ** 2) * 70, 0, 255)
    colors_list.append(np.column_stack((red, green, blue)))

    # 2. Calyx / Sepals (Connects bloom to stem with zero gap)
    num_sepal = 2200
    su = np.random.uniform(0, 1, num_sepal)
    stheta = np.random.uniform(0, 2 * np.pi, num_sepal)
    sepal_flare = 1 + 0.45 * np.cos(5 * stheta)
    sr = su * 36 * sepal_flare
    sx = sr * np.cos(stheta)
    sz = sr * np.sin(stheta)
    sy = 35 + (su ** 1.5) * 22

    pts_list.append(np.column_stack((sx, sy, sz)))
    colors_list.append(np.column_stack((
        np.random.randint(25, 65, num_sepal),
        np.random.randint(120, 220, num_sepal),
        np.random.randint(15, 45, num_sepal)
    )))

    # 3. Stem
    num_stem = 3500
    t_stem = np.random.uniform(0, 1, num_stem)
    angle_stem = np.random.uniform(0, 2 * np.pi, num_stem)
    rad_stem = np.random.uniform(1.5, 6.5, num_stem)

    sy = 35 + t_stem * 265
    curve_x = np.sin(t_stem * np.pi) * 16
    curve_z = np.cos(t_stem * np.pi * 0.5) * 6 - 6
    sx = curve_x + rad_stem * np.cos(angle_stem)
    sz = curve_z + rad_stem * np.sin(angle_stem)

    pts_list.append(np.column_stack((sx, sy, sz)))
    colors_list.append(np.column_stack((
        np.random.randint(20, 55, num_stem),
        np.random.randint(110, 220, num_stem),
        np.random.randint(15, 40, num_stem)
    )))

    # 4. Two Curved Leaves
    leaf_configs = [
        {"side": 1,  "t_attach": 0.36, "yaw": 0.25},
        {"side": -1, "t_attach": 0.52, "yaw": -0.35},
    ]
    for cfg in leaf_configs:
        num_leaf = 3200
        lu = np.random.uniform(0, 1, num_leaf)
        lv = np.random.uniform(-1, 1, num_leaf)

        t0 = cfg["t_attach"]
        attach_x = np.sin(t0 * np.pi) * 16
        attach_y = 35 + t0 * 265
        attach_z = np.cos(t0 * np.pi * 0.5) * 6 - 6

        serration = 1 + 0.08 * np.sin(lu * 28)
        length = lu * 125
        half_width = (np.sin(lu * np.pi) ** 0.75) * 42 * serration
        w = lv * half_width

        local_x = cfg["side"] * length
        local_y = -length * 0.32 + (lu ** 2) * 32 + np.abs(lv) * 6
        local_z = w

        cy, sy_ang = math.cos(cfg["yaw"]), math.sin(cfg["yaw"])
        lx = attach_x + (local_x * cy - local_z * sy_ang)
        ly = attach_y + local_y
        lz = attach_z + (local_x * sy_ang + local_z * cy)

        pts_list.append(np.column_stack((lx, ly, lz)))

        vein_highlight = np.exp(-np.abs(lv) * 6) * 70
        l_green = np.clip(120 + lu * 80 + vein_highlight + np.random.randint(0, 30, num_leaf), 0, 255)
        l_red = np.clip(25 + vein_highlight * 0.5, 0, 255)
        l_blue = np.clip(20 + vein_highlight * 0.3, 0, 255)
        colors_list.append(np.column_stack((l_red, l_green, l_blue)))

    # 5. Background Stardust
    num_stars = 220
    stars = np.random.uniform(-420, 420, (num_stars, 3))
    pts_list.append(stars)
    b = np.random.randint(80, 210, (num_stars, 1))
    colors_list.append(np.hstack((b, b, np.clip(b + 20, 0, 255))))

    return np.vstack(pts_list), np.vstack(colors_list).astype(np.uint16)

points, colors = generate_rose_data()

angle_y = 0.0
tilt_x = 0.28
cos_x, sin_x = math.cos(tilt_x), math.sin(tilt_x)

# Pre-allocate 16-bit frame buffer to prevent uint8 overflow
frame_buffer = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint16)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle_y += 0.015
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)

    # 3D Rotation
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    rx = x * cos_y - z * sin_y
    rz_temp = x * sin_y + z * cos_y
    ry = y * cos_x - rz_temp * sin_x
    rz = y * sin_x + rz_temp * cos_x

    # Perspective Projection
    fov = 560.0
    z_depth = rz + 600.0
    valid = z_depth > 20

    scale = fov / z_depth[valid]
    sx = (rx[valid] * scale + WIDTH * 0.5).astype(np.int32)
    sy = (ry[valid] * scale + HEIGHT * 0.52).astype(np.int32)
    c_valid = colors[valid]
    rz_valid = rz[valid]

    in_bounds = (sx >= 2) & (sx < WIDTH - 2) & (sy >= 2) & (sy < HEIGHT - 2)
    sx, sy, c_valid, rz_valid = sx[in_bounds], sy[in_bounds], c_valid[in_bounds], rz_valid[in_bounds]

    # Reset buffer to dark background
    frame_buffer[:, :] = (4, 4, 8)

    # Add core particle brightness safely in uint16
    np.add.at(frame_buffer, (sx, sy), (c_valid * 3) // 4)

    # Add soft glow cross around front-facing particles
    front = rz_valid < 60
    fx, fy, fc = sx[front], sy[front], c_valid[front] // 4
    np.add.at(frame_buffer, (fx + 1, fy), fc)
    np.add.at(frame_buffer, (fx - 1, fy), fc)
    np.add.at(frame_buffer, (fx, fy + 1), fc)
    np.add.at(frame_buffer, (fx, fy - 1), fc)

    # Clip safely to [0, 255] and blit directly to screen
    pygame.surfarray.blit_array(screen, np.clip(frame_buffer, 0, 255).astype(np.uint8))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()