import matplotlib.pyplot as plt


def configure(grid=True):
    #plt.style.use('seaborn-paper')
    plt.rcParams.update({
        'text.usetex': True,
        'font.family': 'serif',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.grid': grid,
        'grid.linewidth': 0.7,
        'legend.fontsize': 14,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'figure.figsize': (4.774, 2.950)
    })


def default_colors(color):
    color_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown',
                  'magenta', 'grey', 'yellow', 'cyan']
    if color in color_list:
        color_idx = color_list.index(color)
        hex_col = plt.rcParams['axes.prop_cycle'].by_key()['color'][color_idx]
    return hex_col
