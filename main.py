from src.canny_algorithm import canny_edge_detector

golfer_image = "data/images/golfer_grayscale.jpg"
bear_image = "./data/images/bear_grayscale.jpg"
lions_image = "./data/images/lions_grayscale.jpg"

# canny_edge_detector(golfer_image, 3, 1)
# canny_edge_detector(bear_image, 3, 3)
canny_edge_detector(lions_image, 3, .5)



