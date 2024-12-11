import matplotlib.pyplot as plt
import numpy as np


def _draw_unit_circle(ax: plt.Axes, **plot_kwargs):
    # Generate theta values (angle) for the unit circle
    theta = np.linspace(0, 2 * np.pi, 1000)

    # Parametric equations for the unit circle
    x = np.cos(theta)
    y = np.sin(theta)

    plt.plot(x, y, **plot_kwargs)


def _draw_eigenvalues(matrix: np.array, ax=None):
    ew = np.linalg.eig(matrix).eigenvalues
    x = np.real(ew)
    y = np.imag(ew)

    if ax is None:
        ax = plt.gca()
    
    ax.scatter(x, y, marker='x', s=3)


def plot_eigenvalues(matrix: np.array, ax=None):
    if ax is None:
        ax = plt.gca()
    ax.set_aspect('equal')

    ax.grid(alpha=0.1)

    _draw_unit_circle(ax, alpha=0.3, color='black', linewidth=0.5)
    _draw_eigenvalues(matrix)






# def draw_column_vectors(matrix: np.array):
#     if np.iscomplexobj(matrix):
#         # don't try to visualize complex column vectors
#         raise ValueError("Should be called on real matrices only")
#     # TODO EDF
#     pass


def plot_matrix(matrix, ax=None, cmap='viridis', grid_color='black', grid_linewidth=1, colorbar=True, **kwargs):
    """
    Plots a matrix using matshow with grid lines around each cell.

    Parameters:
        matrix (2D array-like): The data to display as a matrix.
        cmap (str): Colormap for the matrix.
        grid_color (str): Color of the grid lines.
        grid_linewidth (float): Line width of the grid lines.
        colorbar (bool): Whether to include a colorbar.
        **kwargs: Additional keyword arguments to pass to `matshow`.

    Returns:
        matplotlib.figure.Figure, matplotlib.axes.Axes: The figure and axes objects for further customization.
    """
    if ax is None:
        ax = plt.gca()
    
    # Create the plot
    cax = ax.matshow(matrix, cmap=cmap, **kwargs)

    # Enable grid lines
    ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)
    ax.grid(which='minor', color=grid_color, linestyle='-', linewidth=grid_linewidth)
    ax.tick_params(which='minor', size=0)  # Remove minor tick marks
   