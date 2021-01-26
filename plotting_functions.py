from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from numpy import inf, sqrt, diag
from uncertainties.unumpy import uarray


def fit(x_values, y_values, function, y_errors=None, title=None, ax=False,
        save_plot=False, guesses=None, x_label=None, y_label=None,
        pnt_size=3, line_size=3, log_scale=None, scientific_notation=None):
    """Curve fit function
    - takes your data
    - fits it to a function of your choice
    - gives you a plot of your data as scatter points and a curve fit line
      (possibly to be used in a multiplot)
    - returns your curve fit parameters

    Parameters:
        x_values:       array, your x values.
        y_values:       array, your y values.
        function:       a self defined function of possibly multiple parameters
                        in the form f(x,a1,a2,...an) with n = number of
                        parameters.
        y_errors:       array, errors in the y_values.
        title:          string, the title of your plot.
        ax:             opt, matplotlib.axes._subplots.AxesSubplot
                        to be used in a figure enviroment
                            pars2 = fit
                            ex: FunFig, (ax1, ax2) = plt.subplots(2, 1)
                            pars1 = fit(x, y, linear, "cool", ax = ax1)
                            pars2 = fit(x, y2, exponential, "nice", ax = ax2)
        save_plot:      bool, if given, saves the figure using the name given
                        by the 'title' variable.
        guesses:        array , guesses for your initial values.
        x_label:	    str, the label of the x axis of your plot.
        y_label:	    str, the label of the y axis of your plot.
        pnt_size:       float, marker size of your data points.
        line_size:      float, marker size of the fit line.
        log_scale:      str, allows you to choose which axis to have a
                        logarithmic scale. Leaving it blank will plot it with
                        a linear axis.
        scientific_notation:
                        str, allows you to choose which axis should be plotted
                        with the scientific notation.

    Returns:
        array of parameters with standard error
        CAUTION! calculations like np.sin may not be performed on this
        for further documentation look up the uncertainies package

    """

    pars, cov = curve_fit(f=function, xdata=x_values, ydata=y_values,
                          p0=guesses, sigma=y_errors, bounds=(-inf, inf))

    if not ax:
        fig = plt.figure(tight_layout=True, dpi=200)
        ax = plt.axes()

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

    ax.grid(True)
    ax.legend()

    std = sqrt(diag(cov))
    parameters = uarray(pars, std)

    if save_plot:
        file_name = str(title) + ".png"
        fig.savefig(file_name)

    return parameters
