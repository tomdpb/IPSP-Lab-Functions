from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})


def fit(x_values, data, function, x_label="X", y_label="Y", title="Title",
        save_plot=False):
    """Curve fit parameters
    - takes your data
    - fits it to a function of your choice
    - gives you a plot of your data as scatter points and a curve fit line

    Parameters:
        x_values:   array, your x values
        data:       array, your y values
        function:   a self defined function of possibly multiple parameters
                    in the form f(x,a1,a2,...an) with n = number of parameters
        ax:         the actual plot
                    limits, y and x labels adjustable in ax.set
                    names of lines adjustable
        title:     str, the title of your plot
        x_label:	str, the label of the x axis of your plot
        y_label:	str, the label of the y axis of your plot
        save:		bool, optional, determines whether or not to save your plot
                    as a .png file

    Returns:
        parameters of your function. The plot can also be visualised in a plot
        window if your IDE supports it.

    """
    pars, _ = curve_fit(f=function, xdata=x_values, ydata=data)
    #                    bounds=(data[0], data[-1]))
    fig, ax = plt.subplots(dpi=200)
    plt.tight_layout()
    ax.plot(x_values, data, ".", label="Data")
    ax.plot(x_values, function(x_values, *pars), label="Curve Fit")
    ax.set(title=title, xlabel=x_label, ylabel=y_label)
    ax.legend()
    plt.grid()

    if save_plot:
        file_name = str(title) + ".png"
        fig.savefig(file_name)

    return pars
