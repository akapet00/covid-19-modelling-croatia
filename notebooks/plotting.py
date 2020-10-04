import matplotlib.pyplot as plt


def configure():
    plt.style.use('seaborn-whitegrid')
    plt.rcParams.update({
        'pgf.texsystem': 'pdflatex',
        'text.usetex': True,
        'font.family': 'serif',
        'font.size': 12,
        'axes.labelsize': 12,
        'axes.grid': True,
        'grid.linewidth': 0.7,
        'legend.fontsize': 10,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.figsize': (4.774*2, 2.950*2)
    })
    

def default_colors(color):
    b, o, g, r = plt.rcParams['axes.prop_cycle'].by_key()['color'][:4]
    if color in ['blue', 'b']:
        return b
    elif color in ['orange', 'o']:
        return o
    elif color in ['green', 'g']:
        return g
    elif color in ['red', 'r']:
        return r