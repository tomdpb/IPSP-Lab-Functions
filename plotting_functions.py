from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})


def fit(x_values, data, function, xlabel="X", ylabel="Y", title="Title",
        guesses=None, save_plot=False):
    """Curve fit parameters
    - takes your data
    - fits it to a function of your choice
    - gives you a plot of your data as scatter points and a curve fit line

    Parameters:
        x_values:   array, your x values
        data:       array, your y values
        function:   a self defined function of possibly multiple parameters
                    in the form f(x,a1,a2,...an) with n = number of parameters
        title:      str, the title of your plot
        xlabel:	    str, the label of the x axis of your plot
        ylabel:	    str, the label of the y axis of your plot
        guesses:    array, guesses for your initial values
                    when in doubt put an array of ones of size n
                    watch out with putting 0 --> 1/0 = problem
                    depending on n you might have to be very good at guessing
        save_plot:	bool, optional, determines whether or not to save your plot
                    as a .png file

    Returns:
        parameters of your function. The plot can also be visualised in a plot
        window if your IDE supports it.

    """
    pars, pcov = curve_fit(f=function, xdata=x_values, ydata=data, p0=guesses)
    #                    bounds=(data[0], data[-1]))
    fig, ax = plt.subplots(dpi=200, tight_layout=True)
    ax.plot(x_values, data, ".", label="Data")
    ax.plot(x_values, function(x_values, *pars), label="Curve Fit")
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.legend()
    ax.grid(True)

    if save_plot:
        file_name = str(title) + ".png"
        fig.savefig(file_name)

    return pars
