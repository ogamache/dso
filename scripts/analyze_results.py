
import numpy as np
import matplotlib.pyplot as plt

def read_vtk_trajectory(filename):
    positions = []
    save_lines = 0
    with open(filename,'r') as file:
        for line in file:
            if "VERTICES" in line:
                save_lines = 0
            if save_lines:
                value_split = line.split()
                positions.append([float(i) for i in value_split])
            if "POINTS" in line:
                save_lines = 1
    return np.array(positions)

def read_txt_trajectory(filename):
    positions = []
    with open(filename,'r') as file:
        for line in file:
            positions.append([float(i) for i in line.split()[1:4]])
    return np.array(positions)

def plot_2D(pos_lidar, pos_dso, scale_dso):
    fig = plt.figure()
    ax_positions = fig.add_subplot()
    ax_positions.scatter(pos_lidar[:,0], pos_lidar[:,1], color="red", label="LibpointMatcher")
    ax_positions.scatter(pos_dso[:,2]*scale_dso, -pos_dso[:,0]*scale_dso, color="blue", label="DSO")
    ax_positions.legend()
    ax_positions.set_xlabel("X (m)")
    ax_positions.set_ylabel("Y (m)")
    ax_positions.set_aspect("equal")
    return

def plot_3D(pos_lidar, pos_dso, scale_dso):
    fig = plt.figure()
    ax_positions = fig.add_subplot(projection='3d')
    ax_positions.scatter(pos_lidar[:,0], pos_lidar[:,1], pos_lidar[:,2], color="red", label="LibpointMatcher")
    ax_positions.scatter(pos_dso[:,2]*scale_dso, -pos_dso[:,0]*scale_dso, -pos_dso[:,1]*scale_dso, color="blue", label="DSO")
    ax_positions.legend()
    ax_positions.set_xlabel("X (m)")
    ax_positions.set_ylabel("Y (m)")
    ax_positions.set_zlabel("Z (m)")
    return

def main(filename_lidar, filename_dso, scale_factor_dso):
    pos_lidar = read_vtk_trajectory(filename_lidar)
    pos_dso = read_txt_trajectory(filename_dso)

    plot_2D(pos_lidar, pos_dso, scale_factor_dso)
    plot_3D(pos_lidar, pos_dso, scale_factor_dso)
    plt.show()


if __name__== "__main__" :
    filename_lidar = "../results/trajectory_campus_auto_exp.vtk"
    filename_dso = "../results/trajectory_campus_auto_exp_dso_trapeze.txt"
    scale_factor_dso = 27

    main(filename_lidar, filename_dso, scale_factor_dso)
