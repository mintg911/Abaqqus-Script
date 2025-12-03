import numpy as np
import matplotlib.pyplot as plt

def curved_plate_coordinates_aligned(L, t, R, num_points=100):
    """
    计算弯曲板材的中心线、内表面和外表面的 x 和 y 坐标，并对齐起始点。
    参数：
        L: 板材的原始长度。
        t: 板材的厚度。
        R: 中心线的曲率半径。
        num_points: 用于计算坐标的点数。
    返回值：
        一个包含中心线、内表面和外表面的 x 和 y 坐标的字典。
    """

    R_inner = R - t/2.0
    R_outer = R + t/2.0
    theta = L/R

    # 中心线坐标
    theta_values = np.linspace(0, theta, num_points)
    x_center = R * np.sin(theta_values)
    y_center = R * (1 - np.cos(theta_values))

    # 内表面坐标
    x_inner =  R*np.sin(theta_values)
    y_inner =  R*(1 - np.cos(theta_values)) + t/2.0

    # 外表面坐标
    x_outer =  R*np.sin(theta_values)
    y_outer =  R*(1 - np.cos(theta_values)) - t/2.0

    return{
        "Center": (x_center, y_center),
        "Inner": (x_inner, y_inner),
        "Outer": (x_outer, y_outer), }

# 示例用法
L = 30  # 板材长度
t = 0.13   # 板材厚度
R = 10  # 中心线曲率半径

coordinates = curved_plate_coordinates_aligned(L, t, R)

x_center, y_center = coordinates["Center"]
x_inner , y_inner  = coordinates["Inner"]
x_outer , y_outer  = coordinates["Outer"]

# 可视化结果
plt.plot(x_center, y_center, label="Center Line")
plt.plot(x_inner, y_inner, label="Inner Surface")
plt.plot(x_outer, y_outer, label="Outer Surface")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Curved Plate with Aligned Start Points")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
