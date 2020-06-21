import queue
import numpy as np

def region_growing_local(image, seed, bottom_threshold, upper_threshold, colour):
    x_shape = image.shape[0]
    y_shape = image.shape[1]
    pixel_queue = queue.Queue()
    visited = set()
    def get_neighbours(co):
        nbs = []
        if co[0]-1 >= 0:
            nbs.append((co[0]-1, co[1]))
            if co[1]-1 >= 0:
                nbs.append((co[0]-1, co[1]-1))
            if co[1]+1 < y_shape:
                nbs.append((co[0]-1, co[1]+1))
        if co[0]+1 < x_shape:
            nbs.append((co[0]+1, co[1]))
            if co[1]-1 >= 0:
                nbs.append((co[0]+1, co[1]-1))
            if co[1]+1 < y_shape:
                nbs.append((co[0]+1, co[1]+1))
        if co[1]-1 >= 0:
                nbs.append((co[0], co[1]-1))
        if co[1]+1 < y_shape:
                nbs.append((co[0], co[1]+1))
        return nbs
    segmentation_image = np.full(np.shape(image), False)
    for i in seed:
        pixel_queue.put(i)
        visited.add(i)
    while not pixel_queue.empty():
        current = pixel_queue.get()
        segmentation_image[current] = True
        nbs = get_neighbours(current)
        for point in nbs:
            diff = image[point] - colour
            if (diff <= upper_threshold) and (diff >= -bottom_threshold) and (point not in visited):
                pixel_queue.put(point)
                visited.add(point)
                
    return segmentation_image