import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from utils.load_data import load_mat
import sys, getopt
from ast import literal_eval


def plot_cdf(var, data, c, x_range, fig_size, fig_format, outpath):
    figure(num=None, figsize=fig_size, dpi=300, facecolor='w', edgecolor='k')
    ax = plt.axes()
    values1, base = np.histogram(data[0], bins=np.arange(0, x_range[1], 0.2),
                                 weights=np.ones(len(data[0])) / len(data[0]), density=False)
    values2, base = np.histogram(data[1], bins=np.arange(0, x_range[1], 0.2),
                                 weights=np.ones(len(data[1])) / len(data[1]), density=False)
    values1 = np.append(values1, 0)
    values2 = np.append(values2, 0)

    ax.plot(base, np.cumsum(values1) / np.cumsum(values1)[-1],
            color=c[0], marker='None', linestyle='-',
            label="A2A Ctrl.", linewidth=8)
    ax.plot(base, np.cumsum(values2) / np.cumsum(values2)[-1],
            color=c[1], marker='None', linestyle='-',
            label="A2A Casp.", linewidth=8)

    ax.set_xlim(x_range[0], x_range[1])
    ax.set_ylim(0, 1)
    ax.set_axisbelow(True)
    ax.grid(linestyle='-', linewidth=5, axis='both')
    ax.set_xticks(np.arange(x_range[0], x_range[1]+0.1, (x_range[1]-x_range[0])/4))
    ax.set_yticks(np.arange(0, 1.1, 0.2))
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(True)
    ax.spines['top'].set_linewidth(5)
    ax.spines['right'].set_visible(True)
    ax.spines['right'].set_linewidth(5)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_linewidth(5)
    ax.spines['left'].set_visible(True)
    ax.spines['left'].set_linewidth(5)
    ax.spines['top'].set_color('k')
    ax.spines['right'].set_color('k')
    ax.spines['bottom'].set_color('k')
    ax.spines['left'].set_color('k')
    ax.tick_params(length=25, width=5)
    plt.savefig(str.join('', (outpath, '{}_kinematics_cdf.'.format(var[0]), fig_format)),
                format=fig_format, transparent=True)


def main(argv):
    path = None
    var = None
    c = None
    x_range = None
    fig_format = None
    outpath = None
    options, args = getopt.getopt(
        argv[1:],
        'p:v:c:r:m:o:',
        ['path=', 'variables=', 'colors=', 'range=', 'format=', 'outpath='])

    for option_key, option_value in options:
        if option_key in ('-p', '--path'):
            path = option_value
        elif option_key in ('-v', '--variables'):
            var = option_value
        elif option_key in ('-c', '--colors'):
            c = option_value
        elif option_key in ('-r', '--range'):
            x_range = option_value
        elif option_key in ('-m', '--format'):
            fig_format = option_value
        elif option_key in ('-o', '--outpath'):
            outpath = option_value
    print('*' * 50)
    print('PATH   :', path)
    print('VARIABLES   :', var)
    print('COLOR   :', c)
    print('RANGE   :', x_range)
    print('FIG FORMAT   :', fig_format)
    print('OUT PATH   :', outpath)
    print('*' * 50)
    print('Plotting...')
    mat = load_mat(path)
    data = [mat[literal_eval(var)[0]][0], mat[literal_eval(var)[1]][0]]
    plot_cdf(literal_eval(var), data, literal_eval(c), literal_eval(x_range), (16, 12), fig_format, outpath)


if __name__ == '__main__':
    main(sys.argv)
