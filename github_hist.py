import sys
import subprocess


print('\n \n \n GENERATE POSE RELATIONSHIPS HISTOGRAMS \n \n \n')
path = '/Volumes/Elements/B-SOID/output3/'
fig_format = 'png'
outpath = '/Volumes/Elements/Manuscripts/B-SOiD/bsoid_natcomm/figure_panels/pose_relationships/'
print('\n DATA FROM {} \n'.format(path))
print('-' * 50)


# HISTOGRAMS
print('\n' * 1)
print('Preparing pose relationships histograms as xxx.{} found on GitHub...'.format(fig_format))
print('\n' * 1)
name = 'openfield_60min_N6'
order = str([-1, 4, 5, 7, 0, 3, 2, 1, 6, 8, 9, 10])

p = subprocess.Popen([sys.executable, './subroutines/pose_relationships_hist.py',
                      '-p', path, '-f', name,
                      '-r', order, '-m', fig_format, '-o', outpath])
p.communicate()
p.kill()


