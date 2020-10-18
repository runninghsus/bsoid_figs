import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from utils.load_data import load_mat

def plot_cdf(fig_size, data):
    figure(num=None, figsize=fig_size, dpi=300, facecolor='w', edgecolor='k')
    ax = plt.axes()
    values1, base = np.histogram(data[0], bins=np.arange(-3, 10, 0.01),
                                 weights=np.ones(len(data[0])).reshape(len(data[0]), 1) / len(data[0]), density=False)
    values2, base = np.histogram(data[1], bins=np.arange(-3, 10, 0.01),
                                 weights=np.ones(len(data[1])).reshape(len(data[1]), 1) / len(data[1]), density=False)
    values3, base = np.histogram(data[2], bins=np.arange(-3, 10, 0.01),
                                 weights=np.ones(len(data[2])).reshape(len(data[2]), 1) / len(data[2]), density=False)
    values4, base = np.histogram(data[3], bins=np.arange(-3, 10, 0.01),
                                 weights=np.ones(len(data[3])).reshape(len(data[3]), 1) / len(data[3]), density=False)
    values5, base = np.histogram(data[4], bins=np.arange(-3, 10, 0.01),
                                 weights=np.ones(len(data[4])).reshape(len(data[4]), 1) / len(data[4]), density=False)
    values6, base = np.histogram(data[5], bins=np.arange(-3, 10, 0.01),
                                 weights=np.ones(len(data[5])).reshape(len(data[5]), 1) / len(data[5]), density=False)
    axis_font = {'fontname': 'Helvetica', 'size': '30'}
    values1 = np.append(values1, 0)
    values2 = np.append(values2, 0)
    values3 = np.append(values3, 0)
    values4 = np.append(values4, 0)
    values5 = np.append(values5, 0)
    values6 = np.append(values6, 0)
    ax.plot(base, np.cumsum(values5) / np.cumsum(values5)[-1],
            color='black', marker='None', linestyle='-',
            label="Shuff. same", linewidth=9)
    ax.plot(base, np.cumsum(values6) / np.cumsum(values6)[-1],
            color='black', marker='None', linestyle='--',
            label="Shuff. diff.", linewidth=9)
    ax.plot(base, np.cumsum(values1) / np.cumsum(values1)[-1],
            color='violet', marker='None', linestyle='-',
            label="MM same", linewidth=6)
    ax.plot(base, np.cumsum(values2) / np.cumsum(values2)[-1],
            color='violet', marker='None', linestyle='--',
            label="MM diff.", linewidth=6)
    ax.plot(base, np.cumsum(values3) / np.cumsum(values3)[-1],
            color='deepskyblue', marker='None', linestyle='-',
            label="BSOiD same", linewidth=6)
    ax.plot(base, np.cumsum(values4) / np.cumsum(values4)[-1],
            color='deepskyblue', marker='None', linestyle='--',
            label="BSOiD diff.", linewidth=6)

    ax.set_xlim(-2, 4)
    ax.set_ylim(0, 1)
    ax.set_axisbelow(True)
    ax.grid(linestyle='-', linewidth=5, axis='both')
    ax.set_xticks(np.arange(-2, 4.1, 2))
    ax.set_yticks(np.arange(0, 1.1, 0.2))
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    lgnd = plt.legend(loc=0, prop={'family': 'Helvetica', 'size': 48})
    lgnd.legendHandles[0]._legmarker.set_markersize(2)
    lgnd.legendHandles[1]._legmarker.set_markersize(2)
    ax.spines['top'].set_visible(True)
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_visible(True)
    ax.spines['right'].set_linewidth(5)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_linewidth(5)
    ax.tick_params(length=20, width=5)
    plt.savefig(str.join('', (
    '/Users/ahsu/Manuscripts/B-SOiD/bsoid_natcomm/figure_panels/motion_energy/mse_cdfcomparisons_', '.png')),
                format='png', transparent=True)


def main(fig_size):
    mse_mat = load_mat('/Users/ahsu/Manuscripts/B-SOiD/bsoid_natcomm/workspace/MvsBvsS_zscore_mse.mat')
    data = [mse_mat['mm_within_vec2'], mse_mat['mm_between_vec2'],
            mse_mat['bsf_within_vec2'], mse_mat['bsf_between_vec2'],
            mse_mat['sbsf_within_vec2'], mse_mat['sbsf_between_vec2']]
    plot_cdf(fig_size, data)


if __name__ == '__main__':
    main((16, 12))
