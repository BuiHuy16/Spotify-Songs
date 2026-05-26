import os
import matplotlib.pyplot as plt

# Định nghĩa đường dẫn lưu trữ
FIGURE_PATH = '../reports/figures/'

# Hàm tự động lưu biểu đồ vào thư mục reports/figures/
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    if not os.path.exists(FIGURE_PATH):
        os.makedirs(FIGURE_PATH)
    
    path = os.path.join(FIGURE_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution, bbox_inches='tight')