from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Heatmap


plot([Heatmap(z=[[1, 2, 3, 4],[5,6,7,8]])])