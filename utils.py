def plot_image_grid(images, nrow=8, title="Grid of Images"):
    """
    Plots a grid of images 
    """

    # Create a grid of images
    #images, _ = next(iter(dataloader))
    grid = make_grid(images, nrow=nrow, padding=2)
    np_grid = grid.numpy()
    np_grid = np.transpose(np_grid, (1, 2, 0))

    # Plot the grid
    plt.figure(figsize=(10, 10))
    plt.imshow(np_grid)
    plt.axis('off')
    plt.title()
    plt.show()

