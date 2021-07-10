from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from numpy import inf, sqrt, diag
from uncertainties.unumpy import uarray


def fit(x_values, y_values, function, y_errors=None, guesses=None, ax=False,
        title=None, x_label=None, y_label=None, pnt_size=3, line_size=3,
        log_scale=None, scientific_notation=None, dpi=200, save_plot=False,
        show_plot=True):
    """Curve fit function
    - takes data and fits it to a given function.
    - gives you a plot of your data as scatter points and a curve fit line
      (possibly to be used in a multiplot)
    - returns your curve fit parameters

    Parameters:
        x_values:       array; your x values.
        y_values:       array; your y values.
        function:       a self defined function of possibly multiple parameters
                        in the form f(x, a1, a2, ..., an) with n = number of
                        parameters.
        y_errors:       opt, array; errors in the y_values.
        guesses:        opt, array; guesses for your parameters.
        ax:             opt, matplotlib.axes._subplots.AxesSubplot
                        to be used in a figure enviroment
                            pars2 = fit
                            ex: Fig, (ax1, ax2) = plt.subplots(2, 1)
                            pars1 = fit(x, y, linear, "cool", ax = ax1)
                            pars2 = fit(x, y2, exponential, "nice", ax = ax2)
        title:          opt, str; the title of your plot.
        x_label:        opt, str; the label of the x axis of your plot.
        y_label:        opt, str; the label of the y axis of your plot.
        pnt_size:       opt, float; marker size of your data points.
        line_size:      opt, float; marker size of the fit line.
        log_scale:      opt, str; allows you to choose which axis to have a
                        logarithmic scale. Leaving it blank will plot it with
                        a linear axis.
        scientific_notation:
                        opt, str; allows you to choose which axis should be
                        plotted with the scientific notation.
        dpi:
                        opt, int; if given, determines the pixel density of the
                        plot, and therefore its quality.
        save_plot:      opt, bool; if given, saves the figure using the name
                        given by the 'title' variable.
        show_plot:      opt, bool; if given, shows the plot. Note that if this
                        function isn't assigned to a variable, some
                        environments might show the plot regardless.

    Returns:
        array of parameters with standard error
        CAUTION! calculations like np.sin may not be performed on this
        for further documentation look up the uncertainties package

    """

    pars, cov = curve_fit(f=function, xdata=x_values, ydata=y_values,
                          p0=guesses, sigma=y_errors, bounds=(-inf, inf))

    std = sqrt(diag(cov))
    parameters = uarray(pars, std)

    if show_plot or save_plot:
        if not ax:
            plt.figure(tight_layout=True, dpi=dpi)
            ax = plt.axes()
        # TODO allow using functions such as np.sin instead of having to first define them
        ax.plot(x_values, y_values, ".", ms=pnt_size, label="Data")
        ax.plot(x_values, function(x_values, *pars), ms=line_size, label="Fit")
        ax.set(title=title, xlabel=x_label, ylabel=y_label)

        if log_scale:
            if log_scale == "x":
                plt.xscale("log")

            elif log_scale == "y":
                plt.yscale("log")

            elif log_scale == "both":
                plt.xscale("log")
                plt.yscale("log")
            else:
                raise ValueError(f"log_scale={log_scale} is not a valid argument")

        if scientific_notation:
            if scientific_notation == "x":
                ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))

            elif scientific_notation == "y":
                ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

            elif scientific_notation == "both":
                ax.ticklabel_format(style="sci", axis="both", scilimits=(0, 0))
            else:
                raise ValueError(f"scientific_notation={scientific_notation} is "
                                 "not a valid argument")

        

        if show_plot:
        	ax.grid(True)
        	ax.legend()
            plt.show()

        if save_plot:
            file_name = str(title) + ".png"
            plt.savefig(file_name)


    return parameters



def linear(x, a, b):
	return a*x + b


def exponential(x, a, b, c):
    return a*exp(x*b + c)


def parabola(x, a, b, c):
    return a*x**2 + b*x + c

