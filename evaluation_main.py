from evaluation import evaluation
from visualize_orig import visualize
from path import Path

case_num = input("Please enter a case number:\n")

data_path = "case_" + case_num.zfill(5)
image_path = "segm_case" + case_num

out_path = Path(image_path)
visualize(data_path, image_path)

evaluation(case_num)