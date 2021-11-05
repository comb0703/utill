from datetime import datetime
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import glob
import os

# 현재 작업 경로 변경
os.chdir("./src")
print(os.getcwd())

# results = 결과 저장한 json 파일명  (dtype:str) , 
# results 내부 = ["image_id": 1,"category_id": 7, "bbox": [1330.0, 998.0, 175.0, 74.0],"score": 1.0] - 박스가 1개일 경우, 여러 개는 extend

# gts = gt json 파일명 (dtype:str)
# gts 내부 = {'info':{}, 'licenses':{}, 'categories':{}, 'images':{}, 'annotations':{}}


def cal_bbox_map(results, gts):
    coco_gt = COCO("./"+gts)
    coco_dt = coco_gt.loadRes("./" + results) 
    
    output_dir = './'
    iou_type = 'bbox'
   
    coco_eval = COCOeval(coco_gt, coco_dt, iou_type)
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    result_strings = []
    keys = ["AP", "AP50", "AP75", "APs", "APm", "APl"]
    # metrics 저장 dict,  {'AP': 0.00035360678925035346, 'AP50': 0.0003536067892503535, 'AP75': 0.0003536067892503535, 'APs': 0.0, 'APm': 0.0, 'APl': 0.00038080731150038065}
    metrics = {}
    for i, key in enumerate(keys):
        metrics[key] = coco_eval.stats[i]
        result_strings.append('{:<10}: {}'.format(key, round(coco_eval.stats[i], 3)))

    # 결과 txt파일로 저장
    result_path = os.path.join(output_dir, 'result_{}.txt'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
    with open(result_path, "w") as f:
        f.write('\n'.join(result_strings))

    return print(dict(metrics=metrics))

#results = 'bbox.json'
#gts = 'small object money_584.json'
#cal_bbox_map(results, gts)
    