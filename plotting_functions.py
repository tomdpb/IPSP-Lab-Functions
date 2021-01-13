def fit(x_values, data, function, title, ax="fig", imgname="jk", guesses=[1,1], 
        xLabel= "x (unit of x)", yLabel="y (unit of y)", ms=3):
    """Curve fit function
    - takes your data 
    - fits it to a function of your choice 
    - gives you a plot of your data as scatter points and a curve fit line
      (possibly to be used in a multiplot)
    - spits out your curve fit parameters
    
    Parameters:
        x_values:   array , your x values
        data:       array , your y values
        function:   a self defined function of possibly multiple parameters
                    in the form f(x,a1,a2,...an) with n = number of parameters
        Title:      string , the title of your plot 
        ax:         (if changed) matplotlib.axes._subplots.AxesSubplot
                    to be used in a figure enviroment 
                        pars2 = fit
                    ex: FunFig, (ax1, ax2) = plt.subplots(2,1)
                        pars1 = fit(x, y, linear, "cool", ax = ax1)
                        pars2 = fit(x, y2, exponential, "nice", ax = ax2)
        imgname:    str, if changed this is the name of the saved image .png
        guesses:    array , guesses for your initial values 
                    when in doubt put an array of ones of size n
                    watch out with putting 0 --> 1/0 = problem
                    depending on n you might have to be very good at guessing
        x_label:	str, the label of the x axis of your plot
        y_label:	str, the label of the y axis of your plot  
        ms:         float, markersize of your data points
    
    Returns: 
        array of parameters with standart error
        CAUTION! calculations like np.sin may not be performed on this 
        for further documentation look up the uncertainies package
    
    """
    pars, cov = curve_fit(f=function, xdata=x_values, ydata=data, p0=guesses, 
                          bounds=(-np.inf, np.inf))
    if ax == "fig":
        fig = plt.figure(tight_layout=True ,dpi=200)
        ax  = plt.axes()
    ax.plot(x_values,data ,".", ms=ms, label="data")
    ax.plot(x_values,function(x_values,*pars),label="curve fit")
    ax.set(title=title, xlabel=xLabel, ylabel=yLabel) 
    ax.legend()
    if ax == "fig":
        if imgname != "jk" :
            filename = imgname + ".png"
            fig.savefig(filename)
    std = np.sqrt(np.diag(cov))
    parameters = unp.uarray(pars, std)
    
    return parameters
