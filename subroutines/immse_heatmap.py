import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from utils.load_data import load_mat
from utils.discrete_cmap import discrete_cmap


def plot_heatmap(fig_size, algo, data, delim, c):
    figure(num=None, figsize=fig_size, dpi=300, facecolor='w', edgecolor='k')
    ax = plt.subplot()
    # cm = sns.diverging_palette(150, 20, center='dark', s=85, l=60, n=5)
    sns.heatmap(data, vmin=-2, vmax=6, cmap=discrete_cmap(5, 'PuOr_r'), center=0, cbar=True, ax=ax)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    for i in range(delim.shape[1]):
        plt.axvline(x=np.cumsum(delim)[i] - 1, linewidth=4, linestyle='--', color=c)
        plt.axhline(y=np.cumsum(delim)[i], linewidth=4, linestyle='--', color=c)
        # plt.axvline(x=np.cumsum(delim)[i] - 1, linewidth=4, color='gainsboro')
        # plt.axhline(y=np.cumsum(delim)[i], linewidth=4, color='gainsboro')


    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    cax = plt.gcf().axes[-1]
    cax.tick_params(length=20, width=5, color='k')
    plt.savefig(str.join('', (
        str.join('', ('/Users/ahsu/Manuscripts/B-SOiD/bsoid_natcomm/figure_panels/motion_energy/', algo, '_mse_mat')),
        '.png')), format='png', transparent=True)


def main(fig_size, algo):
    mse_mat = load_mat('/Users/ahsu/Manuscripts/B-SOiD/bsoid_natcomm/workspace/MvsBvsS_zscore_mse.mat')
    if algo == 'MotionMapper':
        data = mse_mat['mm_mat_norm2_']
        delim = mse_mat['mm_mse_counts']
        c = 'violet'
    elif algo == 'B-SOiD':
        data = mse_mat['bsf_mat_norm2_']
        delim = mse_mat['bsf_mse_counts']
        c = 'deepskyblue'
    plot_heatmap(fig_size, algo, data, delim, c)


if __name__ == '__main__':
    # main((16, 14), 'MotionMapper')
    main((16, 14), 'B-SOiD')