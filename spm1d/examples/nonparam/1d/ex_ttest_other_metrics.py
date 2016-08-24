
import numpy as np
from matplotlib import pyplot
import spm1d




#(0) Load dataset:
# dataset    = spm1d.data.uv1d.t1.Random()
# dataset    = spm1d.data.uv1d.t1.SimulatedPataky2015a()
dataset    = spm1d.data.uv1d.t1.SimulatedPataky2015b()
y,mu       = dataset.get_data()
# y *= -1


metrics    = 'MaxClusterIntegral', 'MaxClusterExtent', 'MaxClusterHeight'
metric     = metrics[1]


#(1) Conduct non-parametric test:
np.random.seed(0)
alpha      = 0.05
two_tailed = False
snpm       = spm1d.stats.nonparam.ttest(y, mu)
snpmi      = snpm.inference(alpha, two_tailed=two_tailed, iterations=-1, cluster_metric=metric)
print( snpmi )
print( snpmi ).clusters



#(2) Compare with parametric result:
spm        = spm1d.stats.ttest(y, mu)
spmi       = spm.inference(alpha, two_tailed=two_tailed)
print( spmi )
print( spmi ).clusters



#(3) Plot
pyplot.close('all')
pyplot.figure(figsize=(12,4))
pyplot.get_current_fig_manager().window.move(0, 0)
ax0 = pyplot.subplot(121)
ax1 = pyplot.subplot(122)
labels = 'Parametric', 'Non-parametric'
for ax,zi,label in zip([ax0,ax1], [spmi,snpmi], labels):
	zi.plot(ax=ax)
	zi.plot_threshold_label(ax=ax, fontsize=8)
	zi.plot_p_values(ax=ax, size=10)
	ax.set_title( label )
pyplot.show()


