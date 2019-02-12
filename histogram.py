import numpy as np
import matplotlib.pyplot as plt
def bin_mean_and_std(to_bin, to_calc, bmin=0, bmax=15, nbins=50, return_arrays=True):
    """
    return statistics for equaly spaced histogram bins between bmin and bmax.
    Then calculate means, standard deviations, and counts for each bin.
    
    The subroutine is set up so that you can bin by variable a (tobin)
    and do stats on variable B (to_calc). I guess they could be the
    same though.
    
    ! WARNING. np.arrange may behave weirdly with reals according to
    the documentation but it worked fine for me. You could r
    
    param: to_bin: np vector with N samples
    param: to_calc: np vector with N samples
    param: bmin real
    param: bmax real
    param: nbins real
    return: bins: np vector with nbins+1 entries
    return: means: np vector with nbins+1 entries
    return: stds: np vector with nbins+1 entries
    return counts: np vector with nbins+1 entries
    """
    bins = np.linspace(bmin, bmax, nbins + 1)
    inds = np.digitize(to_bin, bins)
    means = [to_calc[inds == i].mean() for i in range(0, len(bins))]
    stds = [np.std(to_calc[inds == i]) for i in range(0, len(bins))]
    counts = [to_calc[inds == i].size for i in range(0, len(bins))]
    if return_arrays:
        return np.asarray(bins),np.asarray(means),np.asarray(stds),np.asarray(counts)
    else:
        return bins, means, stds, counts

size = 5000
x = np.random.uniform(0, 1, size)
y = np.random.randn(size)

bins, means, stds, counts = bin_mean_and_std(x, y, 0, 1, 50)
print(bins.shape, means.shape, stds.shape, counts.shape)
start=1
stop=-1
# We graph 
plt.errorbar(bins[start:stop], means[start:stop], yerr=stds[start:stop],  capsize=1, elinewidth=0.5, c='b', markeredgewidth=1)
plt.show()
