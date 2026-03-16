import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def plot_traj(traj_path: Path):
   
    if not traj_path.exists():
        raise FileNotFoundError(traj_path)

    # t px py pz roll pitch yaw
    data = np.genfromtxt(traj_path, skip_header=1, invalid_raise=False)
    x, y, z = data[:, 1], data[:, 2], data[:, 3]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Subplot 1: XY (Top View)
    axes[0].plot(x, y, lw=1.0)
    axes[0].set_xlabel('X [m]')
    axes[0].set_ylabel('Y [m]')
    axes[0].set_title('XY Trajectory (Top View)')
    axes[0].grid(True)
    axes[0].set_aspect('equal', adjustable='box')

    # Subplot 2: YZ (Front View)
    axes[1].plot(y, z, lw=1.0, color='orange')
    axes[1].set_xlabel('Y [m]')
    axes[1].set_ylabel('Z [m]')
    axes[1].set_title('YZ Trajectory (Front View)')
    axes[1].grid(True)
    axes[1].set_aspect('equal', adjustable='box')

    # Subplot 3: XZ (Side View)
    axes[2].plot(x, z, lw=1.0, color='green')
    axes[2].set_xlabel('X [m]')
    axes[2].set_ylabel('Z [m]')
    axes[2].set_title('XZ Trajectory (Side View)')
    axes[2].grid(True)
    axes[2].set_aspect('equal', adjustable='box')

    plt.tight_layout()
    save_path = traj_path.parent / "trajectory_all_views.png"
    plt.savefig(save_path)
    print(f"[INFO] Multi-view trajectory plot saved to: {save_path}")
    # plt.show()
