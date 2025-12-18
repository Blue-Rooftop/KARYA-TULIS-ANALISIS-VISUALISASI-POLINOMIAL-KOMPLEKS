import plotly.graph_objects as go

def visualizeY(resultNewX,resultY):
    realX = [c.real for c in resultNewX]
    imagX = [c.imag for c in resultNewX]
    realY = [c.real for c in resultY]
    imagY = [c.imag for c in resultY]
    x = realX
    y = realY
    z = imagY

    fig = go.Figure(data=go.Scatter3d(
    x=x, y=y, z=z, mode='lines'
))
    
    fig.update_layout(
        scene=dict(
            xaxis_title="x",
            yaxis_title="y",
            zaxis_title="Imag Y"
        )
    )

    return fig.to_html(full_html=False)

def visualizeX(resultNewX,resultY):
    realX = [c.real for c in resultNewX]
    imagX = [c.imag for c in resultNewX]
    realY = [c.real for c in resultY]
    imagY = [c.imag for c in resultY]
    x = realX
    y = realY
    z = imagX

    fig = go.Figure(data=go.Scatter3d(
    x=x, y=y, z=z, mode='lines'
))
    
    fig.update_layout(
        scene=dict(
            xaxis_title="x",
            yaxis_title="y",
            zaxis_title="Imag X"
        )
    )

    return fig.to_html(full_html=False)
    