import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='kwseow', api_key='fq3CCwbwjJPwNH2AA2xi')

data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

py.plot(data, filename='basic-bar')