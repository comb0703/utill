# 여러 파일명을 가지고 있는 하나의 txt 파일 생성
import pandas as pd

# read images info
images = pd.read_csv("total_imgs.csv", index_col=0)

# seperate train,eval
q1 = 'is_eval == True'
q2 = 'is_eval == False'
images_eval = images.query(q1)
images_train = images.query(q2)

train_path = 'train.txt'
eval_path = 'eval.txt'

img_train_dir = './images/train/'
img_eval_dir = './images/eval/'

with open(eval_path, 'w') as f:
  for i in images_eval['file_name'] :
    f.write(img_eval_dir+i+'\n')
    
with open(train_path, 'w') as f:
  for i in images_train['file_name'] :
    f.write(img_train_dir+i+'\n')
    
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 이미지 명마다 txt 파일 생성
import pandas as pd

# read images info, annotation
total_imgs = pd.read_csv('/content/total_imgs.csv')
total_anno = pd.read_csv('/content/nia_total.csv')

# dir
eval_label_dir = '/labels/eval/'
train_label_dir = '/labels/train/'

for idx, val in total_imgs.iterrows():
    # for eval
  if val['is_eval'] == True :
      txt_path = eval_label_dir+val['file_name'][:-3]+"txt"
      with open(txt_path, 'w') as f:
          tmp_idx = total_anno['train_img_idx'] == idx
          cur_frame = total_anno.loc[tmp_idx]
          
          for c_idx, c_val in cur_frame.iterrows():
              # real_cate,yolo_cx,yolo_cy,yolo_w,yolo_h
              ann = '{} {} {} {} {}\n'.format(
                  int(c_val['train_cls_idx']), 
                  round(c_val['yolo_cx'],5),round(c_val['yolo_cy'],5), round(c_val['yolo_w'],5), round(c_val['yolo_h'],5))
              f.write(ann)  # label format
    
    # for train
  else :
      txt_path = train_label_dir+val['file_name'][:-3]+"txt"
      with open(txt_path, 'w') as f:
          tmp_idx = total_anno['train_img_idx'] == idx
          cur_frame = total_anno.loc[tmp_idx]
          
          for c_idx, c_val in cur_frame.iterrows():
              # real_cate,yolo_cx,yolo_cy,yolo_w,yolo_h
              ann = '{} {} {} {} {}\n'.format(
                  int(c_val['train_cls_idx']), 
                  round(c_val['yolo_cx'],5),round(c_val['yolo_cy'],5), round(c_val['yolo_w'],5), round(c_val['yolo_h'],5))
