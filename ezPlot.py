from matplotlib import pyplot

def ezScatter(x, y, x_start, y_start, x_end, y_end):
    """
    x - x values to scatter
    y - y values to scatter
    x_start - x lower limit
    x_end - x upper limit
    y_start - y lower limit
    y_end - y upper limit
    """
    
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)
    pyplot.scatter(x, y)
    return None

def ezPlot(x, y, x_start, y_start, x_end, y_end):
    """
    x - x values to plot
    y - y values to plot
    x_start - x lower limit
    x_end - x upper limit
    y_start - y lower limit
    y_end - y upper limit
    """
    
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)
    pyplot.plot(x, y)
    return None
    
def ezContourf(x, y, cont, contLevel, x_start, y_start, x_end, y_end):
    """
    x - x values to contour
    y - y values to contour
    cont - contour variable
    contLevel - number of contour lines
    x_start - x lower limit
    x_end - x upper limit
    y_start - y lower limit
    y_end - y upper limit
    """
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)
    pyplot.contourf(x, y, cont, contLevel)
    return None

def ezStreamline(x, y, U, V, x_start, y_start, x_end, y_end):
    """
    x - x values to scatter
    y - y values to scatter
    U - x velocity
    V - y velocity
    x_start - x lower limit
    x_end - x upper limit
    y_start - y lower limit
    y_end - y upper limit
    """
    width = 10
    height = (y_end - y_start) / (x_end - x_start) * width
    pyplot.figure(figsize=(width, height))
    pyplot.xlabel('x', fontsize=16)
    pyplot.ylabel('y', fontsize=16)
    pyplot.xlim(x_start, x_end)
    pyplot.ylim(y_start, y_end)
    pyplot.streamplot(x, y, U, V, density=2, linewidth=1, arrowsize=1, arrowstyle='->')
    return None