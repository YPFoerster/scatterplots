"""
Matplotlib wrapper to make nicer scatterplots
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import cycle


__all__=[
'scatter','errorbar','make_marker_iterable','make_color_iterable'
]

class scatter():
    """
    Scatter y_data over x_data. args and kwargs are passed to plt.scatter
    """
    def __init__(self,figure=None,axis=None,*args,**kwargs):
        if figure is None:
            self.figure = plt.figure()
        else:
            self.figure = figure
        if axis is None:
            self.axis = self.figure.gca()
        else:
            self.axis = axis
        self.args=args
        self.kwargs=kwargs
        self.markers=make_marker_iterable()
        self.colors=make_color_iterable()

    def scatter(self,x_data,y_data,**further_kwargs):
        self.axis.scatter(x_data,y_data,*self.args,facecolors='none',edgecolors=next(self.colors),marker=next(self.markers),**self.kwargs,**further_kwargs)
        return self.figure,self.axis

class errorbar(scatter):

    def scatter(self,x_data,y_data,**errbar_kwargs):
        color=next(self.colors)
        self.axis.errorbar(x_data,y_data,*self.args, marker=next(self.markers),mfc='none',mec=color,ecolor=color,**self.kwargs,**errbar_kwargs)

def make_marker_iterable():
    return cycle(('o','^','<','>','p','s','8'))

def make_color_iterable():
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = cycle(prop_cycle.by_key()['color'])
    return colors


if __name__ == '__main__':
    import numpy as np
    x_data=np.random.randn(1000)
    y1_data=np.random.randn(1000)
    y2_data=np.random.randn(1000)*2

    scatterer=scatter()
    fig,axis=scatterer.figure,scatterer.axis
    scatterer.scatter(x_data,y1_data,label=r'$\sigma = 1$')
    scatterer.scatter(x_data,y2_data,label=r'$\sigma = 2$')
    axis.legend(loc='best')
    plt.show()
