from matplotlib import pyplot as plt

class betplot:

    def _shAnnotate(xyScatter, xyAnnotate, text, marker='.', sCol='red', sDepth=2,
                    linestyles='dotted', hDepth=1):
        ''' 
        helper function for "history" to combine 'scatter, hlines, and annotate' in a single function.
        
        <scatter part>
        xyScatter: (x, y) tuple of xy-coordinate for point to be scattered.
        marker: marker type for the point. Default value is '.'.
        sCol: color of the marker. Default value is 'red'.
        sDepth: zorder of the marker Default value is 2.

        <hlines part>
        linestyles: linestyles for the hlines (horizontal lines). Default value is 'dotted'.
        hDepth: zorder of the hlines. Default value is 1.

        <annotate part>
        xyAnnotate: (x, y) tuple of xy-coordinate for the position of annotation.
        text: string to be annotated on the plot. ({text}: {xyScatter[1]}).
        '''
        plt.scatter(xyScatter[0], xyScatter[1], marker=marker, c=sCol, zorder=sDepth)
        plt.hlines(y=xyScatter[1], xmin=0, xmax=xyScatter[0], linestyles=linestyles, zorder=hDepth)
        plt.annotate(f'{text}: {xyScatter[1]}', xy=xyAnnotate)
        
    def history(bet_result, save=False, dpi=None, path=None, show=False):
        '''
        function for plotting bet history through n_trial bets.

        bet_result: (asset_history, max_consecutive_lose) tuple.
                    asset_history is a list of asset values at each bettting, and
                    max_consecutive_lose is the maximum number of consecutive lose in n_trial bets.
        save: bool. checks whether you want to save the image.
        dpi: int. dpi for the image.
        path: str. path where you want the image to be saved.
        show: bool. checks whether you want to see the image.
        '''
        asset_history, max_consecutive_lose = bet_result
        
        # find the minimum asset during the bettings
        min_asset = min(asset_history)
        min_pos = asset_history.index(min_asset)

        # find the maximum asset during the bettings
        max_asset = max(asset_history)
        max_pos = asset_history.index(max_asset)

        # plot piecewise linear curve with resulting points in dots.
        plt.figure()
        trials = len(asset_history)
        plt.plot(range(trials), asset_history, linestyle='-', zorder=1)

        # scatter and annotate the minimum point
        betplot._shAnnotate(xyScatter=(min_pos, min_asset),
                            xyAnnotate=(0, min_asset+0.5), text='min')

        # scatter and annotate the maximum point
        betplot._shAnnotate(xyScatter=(max_pos, max_asset),
                            xyAnnotate=(0, max_asset+0.5), text='max')

        # scatter and annotate the last point
        betplot._shAnnotate(xyScatter=(trials-1, asset_history[-1]),
                            linestyles='dashed',
                            xyAnnotate=(trials, asset_history[-1]+1), text='final')

        # give title with max_consecutive_lose
        plt.title(label=f'{max_consecutive_lose} consecutive loses at the maximum')
        
        if save:
            plt.savefig(fname=path, dpi=dpi)
        if show:
            plt.show()
        plt.close()

    def barChart(x, y, width=0.4, save=False, dpi=None, path=None, show=True):
        '''
        function for plotting bar chart, especially designed to plot the distribution
        of max_consecutive_lose.

        x: x-coordinate value(s) (e.g. numbers fo max_consecutive_lose)
        y: y-coordinate value(s) (e.g. occurrence of each max_consecutive_lose)
        width: width of the bar. Default value is 0.4.
        save: bool. checks whether you want to save the image.
        dpi: int. dpi for the image.
        path: str. path where you want the image to be saved.
        show: bool. checks whether you want to see the image.
        '''
        plt.bar(x, y, width=width)
        if save:
            plt.savefig(fname=path, dpi=dpi)
        if show:
            plt.show()
        plt.close()